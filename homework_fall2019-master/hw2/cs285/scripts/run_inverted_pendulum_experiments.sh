#!/bin/bash

learning_rates=(0.001 0.0001 0.00001)
batch_sizes=(1000 5000 10000)

for lr in ${learning_rates}
do
  for b in ${batch_sizes}
  do
    python3 run_hw2_policy_gradient.py --env_name InvertedPendulum-v2 --ep_len 1000 --discount 0.9 -n 100 -l 2 -s 64 -b ${b} -lr ${lr} -rtg --exp_name ip_b${b}_r${lr}
  done
done