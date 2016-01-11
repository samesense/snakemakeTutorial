"""Three step,
   multi sample
snakefile"""

DATA = '../data/'
WORK = '../work/res2.1/'

rule align:
    input:  DATA + 'fastq/{sample}'
    output: WORK + 'aln/{sample}'
    shell:  'touch {output}'

rule call_variants:
    input:  WORK + 'aln/{sample}'
    output: WORK + 'vars/{sample}'
    shell:  'touch {output}'

rule summarize:
    input:  WORK + 'vars/{sample}'
    output: WORK + 'sum/{sample}'
    shell:  'touch {output}'

rule all:
    input: WORK + 'sum/s1', \
           WORK + 'sum/s2', \
           WORK + 'sum/s3'
