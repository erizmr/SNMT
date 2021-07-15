#!/bin/bash
for i in $(seq 2 5)  
do  
echo $(expr $i);
python3 multitask/main_diff_phy.py --config_file cfg/sim_config_DiffPhy_with_actuation_robot$i.json --train
done

for i in $(seq 2 5)
do
echo $(expr $i);
python3 multitask/main_diff_phy.py --config_file cfg/sim_config_DiffPhy_with_actuation_robot${i}_half_lr.json --train
done

