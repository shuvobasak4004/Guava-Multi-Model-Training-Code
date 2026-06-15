# Dataset and Code Repository

## Overview

This repository contains the dataset, augmentation configuration, source code, trained models, and supplementary materials used in this study. The resources are provided to support transparency, reproducibility, and future research.

## Dataset Structure

```text
dataset/
├── train/
│   ├── algal_leaf_spot/
│   │   ├── images/
│   │   └── labels/
├── valid/
│   ├── algal_leaf_spot/
│   │   ├── images/
│   │   └── labels/
└── test/
    ├── algal_leaf_spot/
    │   ├── images/
    │   └── labels/
```

## Source Code

The repository includes source code for dataset preprocessing, image augmentation, model training, model evaluation, performance analysis, and result visualization. The augmentation settings are provided in `augmentation_config.py`.

## Data Augmentation

The following augmentation techniques were applied to increase dataset diversity and improve model generalization:

* Horizontal Flip
* Vertical Flip
* Rotation (90° and 180°)
* Affine Shear (0.30)
* Brightness Enhancement (1.50)
* Color Enhancement (1.50)
* Contrast Enhancement (1.50)
* Gamma Correction (γ = 0.70)
* Color Jitter
* Channel Shuffle
* Grayscale Conversion
* Gaussian Blur (radius = 2)
* Gaussian Noise (mean = 0, std = 20)
* Salt-and-Pepper Noise (probability = 0.02)


## Notes

All resources are provided for research and educational purposes. The repository contains the dataset, source code, augmentation configuration, and trained models required to reproduce the experiments presented in this study.

# Guava-Multi-Model-Training-Code
#More Details:: https://www.kaggle.com/datasets/shuvokumarbasak4004/guava-leaf-disease-dataset-gldd https://www.kaggle.com/datasets/shuvokumarbasak4004/guava-fruit-and-leaf-diseases-data-latest-and-updated https://www.kaggle.com/datasets/shuvokumarbasak2030/multi-source-guava-fruitleaf-yolo-cnn-labeled-data
MODEL:
https://www.kaggle.com/models/shuvokumarbasak4004/guava-multi-model-yolocnn
ALL CODE:
https://github.com/shuvobasak4004/Guava-Multi-Model-Training-Code
