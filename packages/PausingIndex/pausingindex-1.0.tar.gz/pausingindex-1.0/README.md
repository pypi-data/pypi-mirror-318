# PausingIndex  

### PausingIndex can calculate Promoter Pausing Index from RNApolII ChIP-seq data using longest TSS and TES.  

the input file is bam format.  
the output file is pausing index result.  
#### usage:
``` 
    PausingIndex \
    --bam "RNApolII.bam" \
    --size 300 \
    --gtf "gencode.v38.annotation.gtf" \
    --output "PausingIndex"
```

### Installation 
#### requirement for installation  
python>=3.12  
numpy  
pandas  
argparse  
pysam  
pybedtools  

#### pip install PausingIndex==1.00
https://pypi.org/project/PausingIndex/1.00/
