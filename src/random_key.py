from PIL import Image
import numpy as np
   

    
def generate_key(width, height):
    
    # Generate random RGB values (0-255)
    random_pixels = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

    # Add an alpha channel (fully opaque)
    alpha_channel = np.full((height, width, 1), 255, dtype=np.uint8)

    # Combine RGB + alpha
    rgba_pixels = np.concatenate((random_pixels, alpha_channel), axis=2)

    
    noise_image = Image.fromarray(rgba_pixels, "RGBA")

    
    return noise_image
