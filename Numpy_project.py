import numpy as np
from PIL import Image

# Loading the original image
image_path = r"C:\Users\PAIN\Desktop\shiba.jpg"
image = Image.open(image_path)

# Converting the original image to a NumPy array
image_array = np.array(image)

# Resizing the original image to match the width of other images
image_resized = image.resize((946, 946))

# Slicing the original image horizontally into 22 stripes
height, width, _ = np.array(image_resized).shape
num_stripes = 22
stripe_width = width // num_stripes
stripes = [np.array(image_resized)[:, i * stripe_width:(i + 1) * stripe_width] for i in range(num_stripes)]

# Creating images 1 and 2 from specific subsets of stripes
image1_indices = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # Stripes for image 1
image2_indices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]  # Stripes for image 2

image1_stripes = [stripes[i] for i in image1_indices]
image2_stripes = [stripes[i] for i in image2_indices]

# Concatenating the stripes to form images 1 and 2
image1 = np.concatenate(image1_stripes, axis=1)
image2 = np.concatenate(image2_stripes, axis=1)

# Resizing images 1 and 2 to match the height of other images
min_height = min(image1.shape[0], image2.shape[0])
image1_resized = Image.fromarray(image1[:min_height])
image2_resized = Image.fromarray(image2[:min_height])

# Slicing images 1 and 2 horizontally into 18 stripes each
num_stripes_new = 18
stripe_height1 = image1_resized.height // num_stripes_new
stripe_height2 = image2_resized.height // num_stripes_new
image1_stripes_new = [image1_resized.crop((0, i * stripe_height1, image1_resized.width, (i + 1) * stripe_height1)) for i in range(num_stripes_new)]
image2_stripes_new = [image2_resized.crop((0, i * stripe_height2, image2_resized.width, (i + 1) * stripe_height2)) for i in range(num_stripes_new)]

# Creating image 3 from specified stripes
image3_stripes = [image1_stripes_new[i] for i in range(num_stripes_new) if i % 2 == 0]
image3 = np.concatenate(image3_stripes, axis=0)

# Creating image 4 from specified stripes
image4_stripes = [image1_stripes_new[i] for i in range(num_stripes_new) if i % 2 != 0]
image4 = np.concatenate(image4_stripes, axis=0)

# Creating image 5 from specified stripes
image5_stripes = [image2_stripes_new[i] for i in range(num_stripes_new) if i % 2 == 0]
image5 = np.concatenate(image5_stripes, axis=0)

# Creating image 6 from specified stripes
image6_stripes = [image2_stripes_new[i] for i in range(num_stripes_new) if i % 2 != 0]
image6 = np.concatenate(image6_stripes, axis=0)

# Resizing images 3, 4, 5, 6 to fit in area
min_width = min(image3.shape[1], image4.shape[1], image5.shape[1], image6.shape[1])
min_height = min(image3.shape[0], image4.shape[0], image5.shape[0], image6.shape[0])

image3_resized = Image.fromarray(image3[:, :min_width])
image4_resized = Image.fromarray(image4[:, :min_width])
image5_resized = Image.fromarray(image5[:, :min_width])
image6_resized = Image.fromarray(image6[:, :min_width])

# Combining images into a collage
final_image = np.concatenate([
    np.array(image_resized),
    np.concatenate([np.array(image1_resized.resize((min_width, min_height))), np.array(image2_resized.resize((min_width, min_height)))], axis=1),
    np.concatenate([np.array(image3_resized.resize((min_width, min_height))), np.array(image4_resized.resize((min_width, min_height)))], axis=1),
    np.concatenate([np.array(image5_resized.resize((min_width, min_height))), np.array(image6_resized.resize((min_width, min_height)))], axis=1)
], axis=0)

# Saving image to the PyCharm project directory
final_image_path = "Shiba_inu_dog.jpg"
Image.fromarray(final_image).save(final_image_path)

print("Collage saved successfully.")
