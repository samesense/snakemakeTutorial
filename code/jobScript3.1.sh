#!/bin/bash
# properties = {properties}
#$ -cwd
#$ -S /bin/bash
#$ -M samesense@gmail.com

source /home/evansj/.bashrc
source /home/evansj/.bash_profile
{exec_job}
exit 0
