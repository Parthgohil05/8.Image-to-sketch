# Image to Sketch Conversion

This project converts an image to a sketch using Python. The script reads an image, converts it to grayscale, inverts the grayscale image, applies a Gaussian blur to the inverted image, and finally combines the blurred image with the grayscale image to produce a sketch effect.

## Requirements

- Python 3.x
- NumPy
- Imageio
- SciPy
- OpenCV

You can install the required libraries using pip:

```bash
pip install numpy imageio scipy opencv-python
```

## Usage

1. Place your image in the specified path in the script.
2. Run the script to generate a sketch from the image.

## Code Explanation

```python
import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "E:/Python Projects/8.Image to sketch/zuckerberg.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    # Converts RGB image to grayscale using the formula for luminosity

def dodge(front, back):
    final_sketch = front * 255 / (255 - back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch.astype('uint8')
    # Blends two images together to create a sketch effect

ss = imageio.imread(img)   # Read the input image
gray = rgb2gray(ss)  # Convert the image to grayscale

i = 255 - gray  # Invert the grayscale image

# Apply Gaussian blur to the inverted image
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)
# Combine the blurred image with the grayscale image to create the sketch
r = dodge(blur, gray)

# Save the resulting sketch
cv2.imwrite('new_sketch.png', r)
```

### Function Descriptions

- `rgb2gray(rgb)`: Converts an RGB image to a grayscale image using the luminosity method.
- `dodge(front, back)`: Blends two images to create a sketch effect. It uses a dodge blend which lightens the image.
  
### Steps in the Script

1. **Read Image**: The script reads the input image using `imageio.imread()`.
2. **Convert to Grayscale**: The image is converted to grayscale using the `rgb2gray` function.
3. **Invert Image**: The grayscale image is inverted by subtracting it from 255.
4. **Apply Gaussian Blur**: The inverted image is blurred using a Gaussian filter with a specified sigma value.
5. **Blend Images**: The blurred image and the grayscale image are blended together using the `dodge` function to create the sketch effect.
6. **Save Sketch**: The resulting sketch is saved as 'new_sketch.png' using `cv2.imwrite()`.

## Example

Before running the script, make sure to update the `img` variable with the path to your image. For example:

```python
img = "path/to/your/image.jpg"
```

After running the script, the sketch of the image will be saved as 'new_sketch.png' in the same directory.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Parth Gohil
