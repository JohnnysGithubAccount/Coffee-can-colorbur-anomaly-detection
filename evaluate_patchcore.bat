@echo off
setlocal

set PYTHONPATH=src
set KMP_DUPLICATE_LIB_OK=TRUE

set gpu_id=0
set seed=0
set savefolder="D:\UsingSpace\HCMUTE\Pratical Machine Learning and Artificial Intelligence\patchcore-inspection-main\patchcore-inspection-main\my_images"



set datapath="D:\UsingSpace\HCMUTE\Pratical Machine Learning and Artificial Intelligence\patchcore-inspection-main\patchcore-inspection-main\my_dataset"

set model_flags=-p "D:\UsingSpace\HCMUTE\Pratical Machine Learning and Artificial Intelligence\patchcore-inspection-main\patchcore-inspection-main\results\MVTecAD_Results\IM224_WR50_L2-3_P01_D1024-1024_PS-3_AN-1_S0_17\models\mvtec_coffee"

:: Define dataset flags
set dataset_flags=-d coffee

:: Run the Python script
python bin/load_and_evaluate_patchcore.py --gpu %gpu_id% --seed %seed% %savefolder% ^
patch_core_loader %model_flags% ^
dataset --resize 256 --imagesize 224 %dataset_flags% mvtec %datapath%

endlocal
pause