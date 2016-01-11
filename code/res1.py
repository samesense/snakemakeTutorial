"""Three step,
   one sample
snakefile"""
WORK = '../work/res1/'

rule align:
    output: WORK + 'aln/s1'
    shell:  'touch {output}'

rule call_variants:
    input:  WORK + 'aln/s1'
    output: WORK + 'vars/s1'
    shell:  'touch {output}'

rule summarize:
    input:  WORK + 'vars/s1'
    output: WORK + 'sum/s1'
    shell:  'touch {output}'
