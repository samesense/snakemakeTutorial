# snakemakeTutorial

#### References
* [Snakemake wiki](https://bitbucket.org/snakemake/snakemake/wiki/Home)
* [Documentation](https://bitbucket.org/snakemake/snakemake/wiki/Documentation)

#### Goals
* Run snakemake on respublica and refosco
* Understand template snakemake scripts

#### Outline
* Snakemake install overview
* Python envs
* Refosco snakemake
* Respublica snakemake
* Respublica job scripts
* Snakemake cli usage
* Dependency demo
* Python syntax
* Tips

##### Snakemake installation
[See Jeremy's instructions](https://github.research.chop.edu/leipzigj/fastq_to_gvcf_for_noor_dawany)

##### Python envs
Python virtural environments allow users multiple private module libraries. No need for sudo for most installations (system dependencies are exceptions).
* Respublica env

    Add to your .bash_profile

        export PATH=/home/evansj/me/respublicaTools/anaconda3/bin:$PATH
        alias p3="source activate snakeenv"
        
    Source your .bash_profile to reload variables. Calling p3 will put you in the python3 env, which already has snakemake installed.
* Refosco env

    Add to your .bash_profile

##### Examples
* 3 steps, one sample [code/res1.py](code/res1.py)
* multi sample [code/res2.1.py](code/res2.1.py)
* expand [code/res2.2.py](code/res2.2.py)
* multi sample & chrom [code/res2.3.py](code/res2.3.py)
* temp files [code/res2.4.py](code/res2.4.py)
* named input files [code/res2.5.py](code/res2.5.py)
* referencing wildcards [code/res2.6.py](code/res2.6.py)
* functions as inputs [code/res2.7.py](code/res2.7.py)
* qsub [code/res3.1.py](code/res3.1.py), [code/run3.1.sh](code/run3.1.sh)
* jobscripts [code/res3.2.py](code/run.3.2.py), [code/code/res3.2.py](code/res3.2.py), [code/jobscript.sh](code/jobscript.sh)

##### Snakemake cli
* Touch to update
* --rerun-incomplete
* --dryrun

##### Dependencies demo
* Touch file
* Delete old files

##### Python syntax
* List comprehensions

        [row for row in matrix]
        [row for row in matrix if row[0] == 1]
    
* List management
 
	rule collapse_files:
	    input: expand(DATA + 'vars/{sample}.tab', sample=SAMPLES)
            output: DATA + 'summary'
	    run:
		firstFile = list(input)[0]
		shell('head -1 {fileFile} > {output}')
		shell('cat {input} | grep -v header >> {output}')

##### Tips
* Seperate downstream analysis and heavy memory/time scripts
    * Minimizes dependency checks
    * Decreases iteration time for plots/filters
    * Ex. sf1.py has variant calling/summarize and sf2.py has paper figures
    * Watch out for temp file clobbering (ex samtools sort needs a tmp prefix to avoid over-writting tmp files)
* Sentinel output

        rule unzip:
            input: '../file.tar.gz'
            output: '../log/DONE_unzip'
            run:
            	shell('tar -xvcf {input}')
            	shell('touch {output}')

        rule use_unzipped_file:
            input:  '../log/DONE_unzip'
            output: DATA + 'file1.processed'
            shell:  'process.sh ../file1'

* Threads
* Rerun tons of files
    * Use mv instead of rm

##### Summary
