# !/bin/bash -e

export nnUNet_preprocessed="/workspace/datasets/nnunet_data/nnUNet_preprocessed"
export nnUNet_results="/workspace/datasets/nnunet_data/nnUNet_results/"
export nnUNet_raw="/workspace/datasets/nnunet_data/nnUNet_raw"


export PYTORCH_JIT=0
export CUDA_VISIBLE_DEVICES=0  # Use only one GPU
#nnUNetv2_train Dataset100_FLARE -p nnUNetResEncUNetMPlans 3d_lowres 1 -num_gpus 1 --c


nnUNetv2_train Dataset100_FLARE -p nnUNetPlans 3d_lowres 1 -num_gpus 1
