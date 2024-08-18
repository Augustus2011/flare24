import setuptools

setuptools.setup(
    name="contour-diff",
    version="2.5",
    author="Fabian Isensee",
    author_email="f.isensee@dkfz-heidelberg.de",
    description="nnU-Net is a framework for out-of-the-box image segmentation.",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MIC-DKFZ/nnUNet",
    packages=setuptools.find_packages(
        where='.',  # Search in the current directory
        include=['*'],  # Include all packages
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "acvl-utils>=0.2,<0.3",
        "dynamic-network-architectures>=0.3.1,<0.4",
        "tqdm",
        "dicom2nifti",
        "scipy",
        "diffusers",
        "batchgenerators>=0.25",
        "numpy",
        "scikit-learn",
        "scikit-image>=0.19.3",
        "SimpleITK>=2.2.1",
        "pandas",
        "graphviz",
        "tifffile",
        "requests",
        "matplotlib",
        "seaborn",
        "imagecodecs",
        "yacs",
        "batchgeneratorsv2",
        "einops",
        "opencv-python",
    ],
    extras_require={
        "dev": ["black", "ruff", "pre-commit"],
    },
    include_package_data=True,
    license_files=("LICENSE",),
)
