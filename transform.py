from torchvision import transforms
from PIL import Image
from utils import NonUniformScaling

class ThresholdTransform:
    def __init__(self, threshold=50):
        self.threshold = threshold

    def __call__(self, img):
        # Ensure img is a PIL Image
        if not isinstance(img, Image.Image):
            raise TypeError("Input should be a PIL Image")
        
        # Convert image to grayscale if it's not already
        if img.mode != 'L':
            img = img.convert('L')
        
        # Apply thresholding
        img = img.point(lambda p: 255 if p > self.threshold else 0)
        
        return img

def load_train_transform_img(config):
    return transforms.Compose(
        [
            transforms.Resize((config.img_size, config.img_size), interpolation=config.img_interpolation),
            transforms.RandomCrop(config.img_size, padding=32, fill=0, padding_mode='constant'),
            transforms.RandomHorizontalFlip(p=config.flip_p),
            transforms.RandomApply([
                NonUniformScaling(scale_x_range=config.scale_x, scale_y_range=config.scale_y),
                transforms.RandomAffine(
                    degrees=config.degrees,
                    translate=config.translate,
                    scale=config.scale,
                    shear=config.shear
                ),
            ], p=config.apply_p),
            transforms.ToTensor(),
            transforms.Normalize([0.5], [0.5]),
        ]
    )

def load_train_transform_contour(config):
    return transforms.Compose(
        [
            transforms.Resize((config.img_size, config.img_size), interpolation=config.contour_interpolation),
            transforms.RandomCrop(config.img_size, padding=32, fill=0, padding_mode='constant'),
            transforms.RandomHorizontalFlip(p=config.flip_p),
            transforms.RandomApply([
                NonUniformScaling(scale_x_range=config.scale_x, scale_y_range=config.scale_y),
                transforms.RandomAffine(
                    degrees=config.degrees,
                    translate=config.translate,
                    scale=config.scale,
                    shear=config.shear
                ),
            ], p=config.apply_p),
            ThresholdTransform(50),
            transforms.ToTensor(),
        ]
    )

def load_val_transform_img(config):
    return transforms.Compose(
        [
            transforms.Resize((config.img_size, config.img_size), interpolation=config.img_interpolation),
            transforms.ToTensor(),
            transforms.Normalize([0.5], [0.5]),
        ]
    )

def load_val_transform_contour(config):
    return transforms.Compose(
        [
            transforms.Resize((config.img_size, config.img_size), interpolation=config.contour_interpolation),
            ThresholdTransform(50),
            transforms.ToTensor(),
        ]
    )