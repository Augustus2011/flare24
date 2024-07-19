import SimpleITK as sitk
import batchgenerators
from batchgenerators.utilities.file_and_folder_operations import subdirs
import os

# file_path = "/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/nnUNet_raw/Dataset001_SPINE/labelsTr/SPINE_000.nii.gz"

# try:
#     image = sitk.ReadImage(file_path)
#     print("File read successfully.")
# except Exception as e:
#     print(f"Error reading file: {e}")
#print(subdirs("/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/nnUNet_raw_data_base/nnUNet_raw_data/Dataset500_FLARE"))



for i in os.environ.keys():
    print(i)
