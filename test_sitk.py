import SimpleITK as sitk

file_path = "/Users/kunkerdthaisong/intern_cariva/flare24/datasets/nnunet_data/nnUNet_raw/Dataset001_SPINE/labelsTr/SPINE_000.nii.gz"
#
try:
    image = sitk.ReadImage(file_path)
    print("File read successfully.")
except Exception as e:
    print(f"Error reading file: {e}")

    