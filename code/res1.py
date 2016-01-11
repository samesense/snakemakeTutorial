"""Three step,
   one sample
snakefile"""

DATA = '../data/'
WORK = '../work/res1/'

rule align:
    input:  DATA + 'fastq/{sample}'
    output: WORK + 'aln/{sample}'
    shell:  'touch {output}'

rule call_variants:
    input:  WORK + 'aln/s1'
    output: WORK + 'vars/s1'
    shell:  'touch {output}'

rule summarize:
    input:  WORK + 'vars/s1'
    output: WORK + 'sum/s1'
    shell:  'touch {output}'
