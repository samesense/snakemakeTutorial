# snakemakeTutorial

#### References
* [Snakemake wiki](https://bitbucket.org/snakemake/snakemake/wiki/Home)
* [Documentation](https://bitbucket.org/snakemake/snakemake/wiki/Documentation)

#### Goals
* Run snakemake on respublica
* Understand template snakemake scripts

#### Outline
* Snakemake installation
* Python envs
* [Johannes Koster's slides](http://slides.com/johanneskoester/deck-1#/1)
* Respublica snakemake examples
* Snakemake cli usage
* Dependency demo
* Python syntax
* Tips

##### Snakemake installation
[See Jeremy's instructions](https://github.research.chop.edu/leipzigj/fastq_to_gvcf_for_noor_dawany)

##### Python envs
Python virtual environments allow users multiple private module libraries. No need for sudo for most installations (system dependencies are exceptions).
* Respublica env

    Add to your .bash_profile

        export PATH=/home/evansj/me/respublicaTools/anaconda3/bin:$PATH
        alias p3="source activate snakeenv"
        
    Source your .bash_profile to reload variables. Calling p3 will put you in the python3 env, which already has snakemake installed.

##### [Johannes Koster's slides](http://slides.com/johanneskoester/deck-1#/1)
* Read slides 1-10

##### Respublica examples
* Log into respublica
    * [Passwordless ssh](http://www.thegeekstuff.com/2008/11/3-steps-to-perform-ssh-login-without-password-using-ssh-keygen-ssh-copy-id/)
* 3 steps, one sample [code/res1.py](code/res1.py)
* multi sample [code/res2.1.py](code/res2.1.py)
* expand [code/res2.2.py](code/res2.2.py)
* multi sample & chrom [code/res2.3.py](code/res2.3.py)
* temp files [code/res2.4.py](code/res2.4.py)
* named input files [code/res2.5.py](code/res2.5.py)
* referencing wildcards [code/res2.6.py](code/res2.6.py)
* functions as inputs [code/res2.7.py](code/res2.7.py)
* qsub and jobscripts [code/run3.1.sh](code/run3.1.sh)
* json config files [code/run3.2.sh](code/run3.2.sh)
    * [Check config file format](http://jsonlint.com/)

##### Snakemake cli
* -j #cores
* --dryrun: see what will be executed
* --touch: Touch output files (mark them up to date without really changing them) instead of running their commands. This is used to pretend that the rules were executed, in order to fool future invocations of snakemake. Fails if a file does not yet exist.
* --rerun-incomplete: fix broken files
* -F: force execution of all rules

##### Dependencies demo
* Jobs execute if:
    * Output file does not exist
    * Output file needed by another executed job and does not exist
    * Input file newer than output file
    * Input file will be updated by other job
    * Execution is enforced
* Deletion of intermediate files might not trigger execution

##### Python syntax
* range

        chroms = list(range(1,23)) + ['X','Y']

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

* Read files
  
        import csv
        with open('file.tab') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                sample = row['sample']
                id = row['sample_id']


##### Tips
* Clean up
    * Add .snakemake/ to .gitignore
    * Add snakejob* to .gitigore
    * Use bash alias to clear qsub job output/errors
     
         alias clr='rm *~ snakejob.* nohup* Rplots.pdf *.aux *.log *.bbl *.dvi *.blg'

* Separate downstream analysis and heavy memory/time scripts
    * Minimizes dependency checks
    * Decreases iteration time for plots/filters
    * Ex. sf1.py has variant calling/summarize and sf2.py has paper figures
    * Watch out for temp file clobbering (ex samtools sort needs a tmp prefix to avoid over-writing tmp files)
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

        rule sort:
            input: "path/to/{dataset}.txt"
            output: "{dataset}.sorted.txt"
            threads: 4
            shell: "sort --parallel {threads} {input} > {output}"

    * Run three sort jobs at a time
    
        snakemake -s sf.py -j 12

    * Run one sort job at a time

        snakemake -s sf.py -j 4
	
* Rerun tons of files: use mv instead of rm
* Nohup job out and error files appear in /home
