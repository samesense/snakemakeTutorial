"""Three step,
   multi sample
   multi chrom
   w/ expand
   w/ tmp
   w/ named input
   w/ shell wildcards
   w/ input functions
   w/ sentinel output
snakefile"""

SAMPLES = ('s1', 's2', 's3')
CHROMS = {'s1':(1,),
          's2':(2,3),
          's3':(3,),
          }

DATA = '../data/'
WORK = '../work/res3.1/'

rule align:
    input:  DATA + 'fastq/{sample}.{chrom}'
    output: temp(WORK + 'aln/{sample}.{chrom}')
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

def mk_chrom_input(wc):
    return CHROMS[wc.sample]
    
rule summarize:
    input:  mk_chrom_input
    output: WORK + 'sum/{sample}'
    shell:  'echo {wildcards.sample} > {output}'

rule all:
    input: expand(WORK + 'sum/{sample}', \
		  sample = SAMPLES)

