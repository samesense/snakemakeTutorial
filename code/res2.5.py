"""Three step,
   multi sample
   multi chrom
   w/ expand
   w/ tmp
   w/ named input
snakefile"""
SAMPLES = ('s1', 's2', 's3')
CHROMS = range(1,4)
WORK = '../work/res2.4/'

rule align:
    output: WORK + 'aln/{sample}.{chrom}'
    shell:  'touch {output}'

rule index:
    input:  WORK + 'aln/{sample}.{chrom}'
    output: WORK + 'aln/{sample}.{chrom}.idx'
    shell:  'touch {output}'
    
rule call_variants:
    input:  bam = WORK + 'aln/{sample}.{chrom}',
            idx = WORK + 'aln/{sample}.{chrom}.idx'
    output: temp(WORK + 'vars/{sample}.{chrom}')
    shell:  'cat {input.bam} > {output}'

rule summarize:
    input:  expand(WORK + 'vars/{{sample}}.{chrom}',
		   chrom = CHROMS)
    output: WORK + 'sum/{sample}'
    shell:  'touch {output}'

rule all:
    input: expand(WORK + 'sum/{sample}', \
		  sample = SAMPLES)

