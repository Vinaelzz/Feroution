# -*- coding: utf-8 -*-
"""face.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SYGsa_914iu7smyOANfEs9lVi36TxHld
"""

# Mount Google Drive
from google.colab import drive
drive.mount('/content/gdrive')

# Buat simbolik link (link pintasan)
!ln -s /content/gdrive/My\ Drive/ /mydrive
!ls /mydrive

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/ultralytics/yolov5  # clone
# %cd yolov5
# %pip install -qr requirements.txt  # install

import torch
from yolov5 import utils
display = utils.notebook_init()  # checks

# Copy data train dan test ke root direktori
!cp /mydrive/face/dataface.zip ../
!cp /mydrive/face/custom_dataface_jg.yaml ../yolov5/data/

!unzip ../dataface.zip -d ../

# Commented out IPython magic to ensure Python compatibility.
# Weights & Biases  (optional)
# %pip install -q wandb
import wandb
wandb.login()

# Train YOLOv5s on COCO128 for 3 epochs
!python train.py --img 640 --batch 8 --epochs 200 --data custom_dataface_jg.yaml --weights yolov5s.pt --cache --project face --name feroution