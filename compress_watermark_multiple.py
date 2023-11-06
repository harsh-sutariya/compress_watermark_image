import os
from PIL import Image

def compress_image(input_image_path, output_image_path, max_size, watermark_image_path=None, watermark_opacity=0.92):
    image = Image.open(input_image_path)
    image.thumbnail((max_size, max_size))

    # Create a new image with transparency for the watermark
    compressed_image = Image.new("RGB", image.size)
    compressed_image.paste(image, (0, 0))

    if watermark_image_path:
        watermark = Image.open(watermark_image_path)

        # Scale the watermark based on the compressed image size
        watermark_size = int(min(image.size) * 0.25)
        watermark.thumbnail((watermark_size, watermark_size))

        # Decrease the opacity of the watermark using blend
        watermark = watermark.convert("RGBA")
        blended_watermark = Image.blend(watermark, Image.new("RGBA", watermark.size), watermark_opacity)

        # Calculate the grid size and spacing
        grid_rows = 4
        grid_columns = 3
        grid_width = image.size[0] // grid_columns
        grid_height = image.size[1] // grid_rows

        # Paste the blended watermark onto the compressed image in the center of each grid
        for row in range(grid_rows):
            for col in range(grid_columns):
                # Calculate the watermark position in the center of the current grid
                watermark_x = col * grid_width + (grid_width - blended_watermark.width) // 2
                watermark_y = row * grid_height + (grid_height - blended_watermark.height) // 2

                # Paste the blended watermark onto the compressed image
                compressed_image.paste(blended_watermark, (watermark_x, watermark_y), mask=blended_watermark)

    compressed_image.save(output_image_path, "JPEG", optimize=True)


# Input folder containing the images
input_folder = "input_folder"

# Output folder for compressed images
output_folder = "output_folder"

# Watermark image path
watermark_image_path = "./logo.png"

# Maximum size in pixels
max_size = 1024

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over each file in the input folder
for filename in os.listdir(input_folder):
    # Generate input and output paths
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    # Check if the file is an image
    if os.path.isfile(input_path) and filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Compress the image and add the watermark grid
        compress_image(input_path, output_path, max_size, watermark_image_path)
