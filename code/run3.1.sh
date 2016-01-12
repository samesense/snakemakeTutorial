snakemake -s res3.1.py all \
--jobscript jobScript3.1.sh \
-j -c "qsub -l h_vmem=2G -l mem_free=2G"
