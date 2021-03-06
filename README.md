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

#### Snakemake installation
[See Jeremy's instructions](https://github.research.chop.edu/leipzigj/fastq_to_gvcf_for_noor_dawany)

#### Python envs
Python virtual environments allow users multiple private module libraries. No need for sudo for most installations (system dependencies are exceptions).
[See Jeremy's instructions](https://github.research.chop.edu/leipzigj/fastq_to_gvcf_for_noor_dawany)

#### [Johannes Koster's slides](http://slides.com/johanneskoester/deck-1#/1)
* Read slides 1-10

#### Respublica examples
* Clone this repo and run examples.
* 3 steps, one sample [code/res1.py](code/res1.py)
    * List rules:
    
            snakemake -s res1.py -l
    * Dryrun:
    
            snakemake -s res1.py --dryrun summarize
    * Run:
            
        ```snakemake -s res1.py summarize```

* multi sample [code/res2.1.py](code/res2.1.py)
    * Run by rule:
    
        ```snakemake -s res2.1.py all```

    * Run by file:
    
        ```snakemake -s res2.1.py ../work/res2.1/sum/s3```
        
* expand [code/res2.2.py](code/res2.2.py)
* multi sample & chrom [code/res2.3.py](code/res2.3.py)
* temp files [code/res2.4.py](code/res2.4.py)
* named input files [code/res2.5.py](code/res2.5.py)
* referencing wildcards [code/res2.6.py](code/res2.6.py)
* functions as inputs [code/res2.7.py](code/res2.7.py)
* qsub and jobscripts [code/run3.1.sh](code/run3.1.sh)
* json config files [code/run3.2.sh](code/run3.2.sh)
    * [Check config file format](http://jsonlint.com/)

#### Snakemake cli
* -l: list rules
* -j #cores (ex. -j5 for 5 cores)
* --dryrun: see what will be executed
* --touch: Touch output files (mark them up to date without really changing them) instead of running their commands. This is used to pretend that the rules were executed, in order to fool future invocations of snakemake. Fails if a file does not yet exist.
* --rerun-incomplete: fix broken files
* -F: force execution of all rules

#### Dependencies demo
* Jobs execute if:
    * Output file does not exist
    * Output file needed by another executed job and does not exist
    * Input file newer than output file
    * Input file will be updated by other job
    * Execution is enforced
* Deletion of intermediate files might not trigger execution

#### Python syntax
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

* List files in directories
    ```` 
    import os, glob
    files = glob.glob('fastq/*')
    files = os.listdir('fastq/')
    ````
* Read files

    ```
    import csv
    with open('file.tab') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            sample = row['sample']
            id = row['sample_id']
    ```

#### Tips
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
* Unknown output files

        rule unzip:
            input: '../file.tar.gz'
            output: '../fileIWant', '../log/DONE_unzip'
            run:
            	shell('tar -zxvf {input}')
            	shell('touch {output}')

        rule use_unzipped_file:
            input:  fileToProcess='../fileIWant', done='../log/DONE_unzip'
            output: DATA + 'file.processed'
            shell:  'process.sh {input.fileToProcess} {output}'

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
        
* Log files

    When executing a large workflow, it is usually desirable to store the output of each job persistently in files instead of just printing it to default output and error files. For this purpose, Snakemake allows to specify log files for rules. Log files are defined via the log directive and handled similarly to output files, but they are not subject of rule matching and are not cleaned up when a job fails.
    ```
    rule bwa_map:
    input:
        "data/genome.fa",
        lambda wildcards: config["samples"][wildcards.sample]
    output:
        "mapped_reads/{sample}.bam"
    log:
        "logs/bwa_map/{sample}.log"
    threads: 8
    shell:
        "(bwa mem -t {threads} {input} | "
        "samtools view -Sb - > {output}) 2> {log}"
    ```
	
* Rerun tons of files: use mv instead of rm
* Nohup job out and error files appear in /home
