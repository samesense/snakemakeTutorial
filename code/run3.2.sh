# qsub, jobscript, config
snakemake -s res3.2.py all \
--jobscript jobScript3.1.sh \
--configfile config3.2.json \
-j -c "qsub -l h_vmem=2G -l mem_free=2G"
