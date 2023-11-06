# Image Compression with Watermarking


This project provides a Python script for compressing images and adding watermarks. It is designed to be easy to use and highly configurable. Whether you are a photographer looking to reduce image sizes or a content creator adding your watermark, this script can help you achieve your goals.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Contributing](#contributing)

## Installation

1. Clone this repository or download the script file directly.
2. Install the required Python packages using pip:

   ```
   pip install Pillow
   ```

## Usage

To compress images and add watermarks, use the `compress_image` function provided in the script. You can also customize the watermark opacity, size, and placement.

```python
from image_compression_with_watermark import compress_image

# Example usage:
input_image_path = "input.jpg"
output_image_path = "output.jpg"
watermark_image_path = "watermark.png"
max_size = 1024  # Maximum size in pixels
watermark_opacity = 0.92

compress_image(input_image_path, output_image_path, max_size, watermark_image_path, watermark_opacity)
```

Ensure you have the required image files in your working directory.

## Features

- **Image Compression**: Resize images to a maximum size while preserving the aspect ratio.
- **Watermarking**: Add watermarks to images with adjustable opacity and size.
- **File Compatibility**: The script works with popular image formats like JPEG, PNG, and GIF.

## Contributing

We welcome contributions to this project. If you have any ideas, bug fixes, or enhancements, feel free to open an issue or submit a pull request.