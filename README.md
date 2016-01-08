# snakemakeTutorial

#### Goals
* Run snakemake on respublica and refosco
* Understand template snakemake scripts

#### Outline
* Snakemake install overview
* Python envs
* Refosco snakemake
* Respublica snakemake
* Snakemake cli usage
* Python syntax
* Wildcards
* Labeled inputs
* Unknown output files
* Functions as inputs
* Threads
* Tips

##### Snakemake installation
[See Jeremy's instructions](https://github.research.chop.edu/leipzigj/fastq_to_gvcf_for_noor_dawany)

##### Python envs
Python virtural environments allow users multiple private module libraries. No need for sudo for most installations (system dependencies are exceptions).
* Respublica env
    Add to your .bash_profile
        export PATH=/home/evansj/me/respublicaTools/anaconda3/bin:$PATH
        alias p3="source actiuvate snakeenv"
    Calling p3 will put you in the python3 env, which already has snakemake installed.
* Refosco env
    Add to your .bash_profile
