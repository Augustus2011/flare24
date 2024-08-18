#run preprocess contour diff beware transformers,PIL,torch,diffusers version


python preprocess.py --data_directory data --domain_img_folder domain_2/images --domain_contour_folder domain_2/contours --domain_meta_path meta

python preprocess.py --data_directory data --domain_img_folder domain_3/images --domain_contour_folder domain_3/contours --domain_meta_path meta_3


#run train contour diff


CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 train.py --input_domain CT --output_domain MR --data_directory /workspace/data --input_domain_img_folder domain_2/images --input_domain_contour_folder domain_2/contours --output_domain_img_folder domain_3/images --output_domain_contour_folder domain_3/contours --input_domain_meta_path /workspace/data/domain_2/meta --output_domain_meta_path  /workspace/data/domain_3/meta_3 --output_dir checkout --contour_guided



CUDA_VISIBLE_DEVICES=0,1,2,3,4 python3 train.py --input_domain CT --output_domain MR --data_directory /workspace/data --input_domain_img_folder domain_2/images --input_domain_contour_folder domain_2/contours --output_domain_img_folder domain_2/images --output_domain_contour_folder domain_2/contours --input_domain_meta_path /workspace/data/domain_2/meta --output_domain_meta_path  /workspace/data/domain_2/meta --output_dir checkout --contour_guided


CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 train.py --input_domain CT --output_domain MR --data_directory /workspace/data --input_domain_img_folder domain_2/images --input_domain_contour_folder domain_2/contours --output_domain_img_folder domain_3/images --output_domain_contour_folder domain_3/contours --input_domain_meta_path /workspace/data/domain_2/meta --output_domain_meta_path  /workspace/data/domain_3/meta_3 --output_dir checkout --contour_guided --img_size 512 --train_batch_size 16 --save_model_epochs 10



CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 train.py --input_domain MR --output_domain CT --data_directory /workspace/data --input_domain_img_folder domain_3/images --input_domain_contour_folder domain_3/contours --output_domain_img_folder domain_2/images --output_domain_contour_folder domain_2/contours --input_domain_meta_path /workspace/data/domain_3/meta_3 --output_domain_meta_path  /workspace/data/domain_2/meta --output_dir /workspace/checkout/mr_2_ct/ --contour_guided --img_size 512 --train_batch_size 16 --save_model_epochs 5 --check_point /workspace/checkout/mr_2_ct/model_epoch_35/unet/


translation
python translation.py \
  --input_domain CT \
  --output_domain MRI \
  --data_directory /workspace/data/ \
  --input_domain_contour_folder /domain_2/contours \
  --input_domain_meta_path /workspace/data/domain_2/meta \
  --num_copy 1 \
  --by_volume \
  --selected_epoch 10 \
  --translating_folder_name translated \
  --device "cuda" \
  --num_partition 1 \
  --partition 0


python translation.py   --input_domain CT   --output_domain MRI   --data_directory /workspace/data/   --input_domain_contour_folder /workspace/data/domain_2/contours  --input_domain_meta_path /workspace/data/domain_2/meta   --num_copy 1   --by_volume   --selected_epoch 80   --translating_folder_name translated   --device "cuda"   --num_partition 1   --partition 0 --workers 8 --eval_batch_size 32


python translation.py   --input_domain CT   --output_domain MRI   --data_directory /workspace/data/   --input_domain_contour_folder /workspace/data/domain_2/contours  --input_domain_meta_path /workspace/data/domain_2/meta   --num_copy 1   --by_volume   --selected_epoch 40   --translating_folder_name translated   --device "cuda"   --num_partition 10   --partition 10 --workers 16 --eval_batch_size 128


CUDA_VISIBLE_DEVICES=2 python translation.py   --input_domain MRI   --output_domain CT   --data_directory /workspace/data/   --input_domain_contour_folder /workspace/data/domain_3/contours  --input_domain_meta_path /workspace/data/domain_3/meta_3   --num_copy 1   --by_volume   --selected_epoch 40   --translating_folder_name /workspace/outputs/epoch_40   --device "cuda"   --num_partition 1   --partition 0 --workers 16 --eval_batch_size 128


python translation.py   --input_domain CT   --output_domain MRI   --data_directory /data/   --input_domain_contour_folder /mnt/ai_neuro/august_kun/miccai/ContourDiff/data/domain_2/contours  --input_domain_meta_path /mnt/ai_neuro/august_kun/miccai/ContourDiff/data/domain_2/meta   --num_copy 1   --by_volume   --selected_epoch 10   --translating_folder_name translated   --device "cuda"   --num_partition 1   --partition 0
