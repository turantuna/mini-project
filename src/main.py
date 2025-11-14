from PIL import Image
import numpy as np
from random_key import generate_key

file_path_1 = "img/pengu_enc.png"
file_path_2 = "img/brot_enc.png"
#random noise
key = generate_key(600,600)

# Pengu and Brot are opened
img1 = Image.open(file_path_1).convert("RGBA")
img2 = Image.open(file_path_2).convert("RGBA")


# Ensure images are the same size
if img1.size != img2.size:
    raise ValueError("Images must be the same size")

# Convert to NumPy arrays
arr1 = np.array(img1)
arr2 = np.array(img2)

# XOR RGB channels
result = np.empty_like(arr1)
result[:, :, :3] = np.bitwise_xor(arr1[:, :, :3], arr2[:, :, :3])

# Make fully opaque
result[:, :, 3] = 255

# Convert back to image
result_image = Image.fromarray(result, "RGBA")
result_image.save("img/failed_otp.png")


