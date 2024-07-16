import os
import shutil
import subprocess
import tempfile
import argparse
from pathlib import Path

from nnUNet.nnunetv2 import helloworld

def predict(base_output_dir):
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    try:
        path_info = {}
        for i, source_file in enumerate(
            Path(base_output_dir).rglob("Selected_axial view.png")
        ):
            destination_file = os.path.join(temp_dir, f"{i}_0000.png")
            path_info[destination_file] = source_file

            # Copy the source file to the temporary directory
            shutil.copy2(source_file, destination_file)

        # Set environment variables
        os.environ["nnUNet_raw"] = "/mnt/ai_neuro/tsaengja/nnUNet_folders/nnUNet_raw/"
        os.environ["nnUNet_preprocessed"] = (
            "/mnt/ai_neuro/tsaengja/nnUNet_folders/nnUNet_preprocessed/"
        )
        os.environ["nnUNet_results"] = (
            "/mnt/ai_neuro/tsaengja/nnUNet_folders/nnUNet_results/"
        )

        # Define the input and output directories
        input_dir = temp_dir
        output_dir = tempfile.mkdtemp()

        try:
            # Construct the nnUNet prediction command
            nnunet_command = [
                "nnUNetv2_predict",
                "-d",
                "Dataset012_sarcopenia_muscle_fats",
                "-i",
                input_dir,
                "-o",
                output_dir,
                "-f",
                "0",
                "1",
                "2",
                "3",
                "4",
                "-tr",
                "nnUNetTrainer",
                "-c",
                "2d",
                "-p",
                "nnUNetPlans",
            ]

            # Run the nnUNet prediction command
            subprocess.run(nnunet_command, check=True)

            print(f"nnUNet prediction completed. Results are in: {output_dir}")
            for destination_file, source_file in path_info.items():
                # Copy the output file to the base output directory
                shutil.copy2(
                    os.path.join(
                        output_dir,
                        os.path.basename(destination_file).replace("_0000", ""),
                    ),
                    Path(source_file).parent / "Label.png",
                )
        finally:
            # Remove the output directory
            shutil.rmtree(output_dir)
    finally:
        # Remove the temporary directory
        shutil.rmtree(temp_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Use nnUnetv2 to label")
    #parser.add_argument(
    #    "--base_output_dir",
    #    required=True,
    #    help="Base output directory path containing multiple results",
    #)

    args = parser.parse_args()
    helloworld.hi()

    #predict(args.base_output_dir)