from PIL import Image
import torch

file_path = r"E:\data\cm\dest\images\1.tif"
image = Image.open(file_path)
transform = transforms.ToTensor()
tensor_image = transform(image)
print("Tensor shape:", tensor_image.shape)
