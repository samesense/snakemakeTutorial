"""Three step,
   multi sample
   multi chrom
   w/ expand 
snakefile"""

SAMPLES = ('s1', 's2', 's3')
CHROMS = range(1,4)

DATA = '../data/'
WORK = '../work/res2.3/'

rule align:
    input:  DATA + 'fastq/{sample}.{chrom}'
    output: WORK + 'aln/{sample}.{chrom}'
    shell:  'touch {output}'

rule call_variants:
    input:  WORK + 'aln/{sample}.{chrom}'
    output: WORK + 'vars/{sample}.{chrom}'
    shell:  'touch {output}'

rule summarize:
    input:  expand(WORK + 'vars/{{sample}}.{chrom}', \
		   chrom = CHROMS)
    output: WORK + 'sum/{sample}'
    shell:  'touch {output}'

rule all:
    input: expand(WORK + 'sum/{sample}', \
		  sample = SAMPLES)

