#!/bin/bash
#SBATCH --account=vjgo8416-humat
#SBATCH --qos=turing
#SBATCH --gpus-per-task 1
#SBATCH --tasks-per-node 1
#SBATCH --nodes 1
#SBATCH --time 1:0:0

module purge
module load baskerville
module load bask-apps/live
module load jax

cd ~/pax
source .venv/bin/activate
python -m pax.experiment +experiment/ipd=shaper_v_ppo_mem