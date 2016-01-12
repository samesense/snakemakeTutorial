snakemake -s res3.2.py all --jobscript jobScript3.2.sh -j -c "qsub -l h_vmem=2G -l mem_free=2G"
