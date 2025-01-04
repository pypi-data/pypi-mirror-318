#!/usr/bin/env python3
import os
import sys
import argparse
import pandas as pd
import numpy as np
import pysam
from pybedtools import BedTool

dir = os.path.dirname(os.path.abspath(__file__))
version_py = os.path.join(dir, "_version.py")
exec(open(version_py).read())

def load_gene_annotations_longest(gtf_file, promoter_size):
    genes = {}
    with open(gtf_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            fields = line.strip().split('\t')
            if len(fields) < 9:
                continue
            chrom, source, feature, start, end, score, strand, frame, attributes = fields
            if feature != 'gene':
                continue
            # Parse attributes to get gene_id and gene_name
            attr_dict = {}
            for attr in attributes.split(';'):
                attr = attr.strip()
                if attr == '':
                    continue
                if ' ' not in attr:
                    continue
                key, value = attr.split(' ', 1)
                attr_dict[key] = value.strip('"')
            gene_id = attr_dict.get('gene_id', None)
            gene_name = attr_dict.get('gene_name', gene_id)
            if not gene_id:
                continue
            # Initialize gene entry if not present
            if gene_id not in genes:
                genes[gene_id] = {
                    'chrom': chrom,
                    'strand': strand,
                    'tss': None,
                    'tes': None,
                    'gene_name': gene_name
                }
            # Determine TSS and TES based on strand
            try:
                start = int(start)
                end = int(end)
            except ValueError:
                continue  # Skip entries with invalid start/end positions
            if strand == '+':
                current_tss = start
                current_tes = end
                # Update TSS: smallest start
                if genes[gene_id]['tss'] is None or current_tss < genes[gene_id]['tss']:
                    genes[gene_id]['tss'] = current_tss
                # Update TES: largest end
                if genes[gene_id]['tes'] is None or current_tes > genes[gene_id]['tes']:
                    genes[gene_id]['tes'] = current_tes
            else:
                current_tss = end
                current_tes = start
                # Update TSS: largest end
                if genes[gene_id]['tss'] is None or current_tss > genes[gene_id]['tss']:
                    genes[gene_id]['tss'] = current_tss
                # Update TES: smallest start
                if genes[gene_id]['tes'] is None or current_tes < genes[gene_id]['tes']:
                    genes[gene_id]['tes'] = current_tes
    # Remove genes with length less than promoter_size
    genes_filtered = {}
    for gene_id, info in genes.items():
        tss = info['tss']
        tes = info['tes']
        gene_length = abs(tes - tss)
        if gene_length >= 3*promoter_size:
            genes_filtered[gene_id] = info
        else:
            print(f"Excluding gene {gene_id} due to insufficient length ({gene_length} bp).")
    del genes
    return genes_filtered

def promoter_region(genes, promoter_size):
    """
    Define promoter regions as ± promoter_size around the most upstream TSS for each gene.
    """
    promoters = []
    for gene_id, info in genes.items():
        chrom = info['chrom']
        strand = info['strand']
        tss = info['tss']
        gene_name = info['gene_name']
        if strand == '+':
            promoter_start = max(tss - promoter_size, 0)
            promoter_end = tss + promoter_size
        else:
            promoter_start = max(tss - promoter_size, 0)
            promoter_end = tss + promoter_size
        promoters.append((chrom, promoter_start, promoter_end, strand,gene_name,gene_id))
    promoters_bt = BedTool(promoters).to_dataframe(names=['chrom', 'start', 'end', 'strand','gene_name','gene_id'])
    del promoters
    return promoters_bt

def gene_body_region(genes, promoter_size):
    """
    Define gene body regions from the most upstream TSS to the most downstream TES, excluding the promoter region.
    """
    gene_bodies = []
    for gene_id, info in genes.items():
        chrom = info['chrom']
        strand = info['strand']
        tss = info['tss']
        tes = info['tes']
        gene_name = info['gene_name']
        if strand == '+':
            body_start = tss + promoter_size
            body_end = tes
        else:
            body_start = tes
            body_end = tss - promoter_size
        if body_end <= body_start:
            continue  # Skip if promoter overlaps entire gene
        gene_bodies.append((chrom, body_start, body_end, strand,gene_name,gene_id))
    gene_bodies_bt = BedTool(gene_bodies).to_dataframe(names=['chrom', 'start', 'end', 'strand','gene_name','gene_id'])
    del gene_bodies
    return gene_bodies_bt

def compute_coverage(bam_file, regions_bt, id_column='gene_id'):
    """
    Compute read counts in specified regions using pysam.
    Returns a dictionary with id_column as keys and read counts as values.
    """
    bam = pysam.AlignmentFile(bam_file, "rb")
    library_size = bam.mapped
    read_counts = {}
    for idx, row in regions_bt.iterrows():
        chrom = row['chrom']
        start = row['start']
        end = row['end']
        region_id = row[id_column]
        count = bam.count(contig=chrom, start=start, end=end)
        if region_id not in read_counts:
            read_counts[region_id] = 0
        read_counts[region_id] += count
    bam.close()
    read_counts = pd.DataFrame(list(read_counts.items()), columns=[id_column, 'read_count'])
    read_counts['CPM'] = (read_counts['read_count'] / library_size) * 1e6
    read_counts['CPM'] = np.round(read_counts['CPM'], decimals=4)
    read_counts = pd.merge(read_counts,regions_bt[['gene_name','gene_id']],on=['gene_id', 'gene_id'])
    return read_counts

def PausingIndex(input,gtf,size,output):
    genes = load_gene_annotations_longest(gtf,size)
    promoters = promoter_region(genes,size)
    genebodys = gene_body_region(genes,size)
    del genes
    TSScov = compute_coverage(input,promoters)
    del promoters
    bodycov = compute_coverage(input,genebodys)
    del genebodys
    result = pd.merge(TSScov[['gene_name','gene_id','CPM']],bodycov[['gene_name','gene_id','CPM']],
                              on=['gene_id', 'gene_name'],how='outer',suffixes=('_tss', '_body'))
    result = result[(result["CPM_tss"] != 0) | (result["CPM_body"] != 0)]
    result.loc[(result['CPM_tss'] == 0) | (result['CPM_body'] == 0), ['CPM_tss', 'CPM_body']] += 1e-4
    result['pasuingIndex'] = result['CPM_tss']/result['CPM_body']
    result.to_csv(output+'.bed', sep='\t', index=False)
    result.to_excel(output+'.xlsx', sep='\t', index=False)
    del result
def main():
    parser = argparse.ArgumentParser(description='Calculate Promoter Pausing Index from RNApolII ChIP-seq data using longest TSS and TES.')
    parser.add_argument('-b', '--bam', required=True, help='Path to RNApolII ChIP-seq BAM file.')
    parser.add_argument('-g', '--gtf', required=True, help='Path to gene annotation GTF/GFF file.')
    parser.add_argument('-o', '--output', required=True, help='Output file to save Pausing Index result.')
    parser.add_argument('-s', '--size', type=int, default=300, help='Size of promoter region around TSS (default: 300 bp).')
    parser.add_argument("-V", "--version", action="version",version="PausingIndex {}".format(__version__)\
                      ,help="Print version and exit")
    args = parser.parse_args()
    print('###Parameters:')
    print(args)
    print('###Parameters')
    PausingIndex(bamid=args.bam,gtfid=args.gtf,prosize=args.size,outid=args.output)
if __name__ == "__main__":
    main()

