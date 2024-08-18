# !/bin/bash -e

export nnUNet_preprocessed="/workspace/datasets/nnunet_data/nnUNet_preprocessed"
export nnUNet_results="/workspace/datasets/nnunet_data/nnUNet_results/"
export nnUNet_raw="/workspace/datasets/nnunet_data/nnUNet_raw"

nnUNetv2_predict_from_modelfolder -i inputs/ -o outputs/ -m /workspace/datasets/nnunet_data/nnUNet_results/Dataset100_FLARE/nnUNetTrainer__nnUNetResEncUNetMPlans__3d_lowres  -f 1 -chk checkpoint_best.pth -device cuda -npp 1 -nps 1