

# augmentation_config.py
#all code https://github.com/shuvobasak4004/Guava-Multi-Model-Training-Code

AUGMENTATION_CONFIG = {
    "horizontal_flip": True,
    "vertical_flip": True,

    "rotation": {
        "angles": [90, 180]
    },

    "affine_shear": {
        "factor": 0.30
    },

    "brightness_adjustment": {
        "factor": 1.50
    },

    "color_enhancement": {
        "factor": 1.50
    },

    "contrast_enhancement": {
        "factor": 1.50
    },

    "gamma_correction": {
        "gamma": 0.70
    },

    "color_jitter": {
        "brightness_range": [0.7, 1.3],
        "contrast_range": [0.7, 1.3],
        "color_range": [0.7, 1.3]
    },

    "channel_shuffle": True,

    "grayscale_conversion": True,

    "gaussian_blur": {
        "radius": 2
    },

    "gaussian_noise": {
        "mean": 0,
        "std": 20
    },

    "salt_pepper_noise": {
        "probability": 0.02
    }
}