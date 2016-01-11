"""Three step,
   multi sample
   w/ expand
snakefile"""
SAMPLES = ('s1', 's2', 's3')
WORK = '../work/res2.2/'

rule align:
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
    input: expand(WORK + 'sum/{sample}', \
		  sample = SAMPLES)

