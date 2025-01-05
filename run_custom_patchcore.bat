@echo off
setlocal enabledelayedexpansion

set PYTHONPATH=src
set KMP_DUPLICATE_LIB_OK=TRUE

@REM set datapath="D:\UsingSpace\HCMUTE\Pratical Machine Learning and Artificial Intelligence\patchcore-inspection-main\patchcore-inspection-main\mvtec"
set datapath="D:\UsingSpace\HCMUTE\Pratical Machine Learning and Artificial Intelligence\patchcore-inspection-main\patchcore-inspection-main\my_dataset"
@REM set datasets=bottle cable capsule carpet grid hazelnut leather metal_nut pill screw tile toothbrush transistor wood zipper
set datasets=coffee
set dataset_flags=

rem Create dataset flags for command line
for %%d in (%datasets%) do (
    set dataset_flags=!dataset_flags! -d %%d
)

rem Baseline IM224
python bin\run_patchcore.py --gpu 0 --seed 0 --save_patchcore_model --log_group IM224_WR50_L2-3_P01_D1024-1024_PS-3_AN-1_S0 --log_project MVTecAD_Results results ^
patch_core -b wideresnet50 -le layer2 -le layer3 --pretrain_embed_dimension 1024 --target_embed_dimension 1024 --anomaly_scorer_num_nn 1 --patchsize 3 ^
sampler -p 0.1 approx_greedy_coreset dataset --resize 256 --imagesize 224 !dataset_flags! mvtec !datapath!


endlocal