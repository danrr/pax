#!/bin/bash
#SBATCH --account=vjgo8416-humat
#SBATCH --qos=turing
#SBATCH --gpus-per-task 1
#SBATCH --tasks-per-node 1
#SBATCH --nodes 1
#SBATCH --time 3:0:0

module purge
module load baskerville
module load bask-apps/live
module load Python/3.11.3-GCCcore-12.3.0
module load CUDA/12.1.1

cd ~/pax
source .venv/bin/activate
python3 -m pax.experiment +experiment/ipd=ppo_v_ppo num_iters=100