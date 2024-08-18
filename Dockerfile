FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    vim \
    gcc \
    g++ \
    make \
    cmake \
    ninja-build \
    libgl1-mesa-glx \
    libglib2.0-0 \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && apt-get clean \
  && pip install --upgrade pip
  
COPY . /workspace/

RUN mkdir -p /workspace/inputs && mkdir -p /workspace/outputs \
  && cd /workspace/nnUNet \
