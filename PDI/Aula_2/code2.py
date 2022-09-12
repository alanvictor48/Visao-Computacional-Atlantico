# Import the color module
from skimage import color

# Import the filters module and sobel function
from skimage.filters import sobel

from PDI.src.pdi_utils import show_image
from atlantico_bootcamp.PDI.src.pdi_utils import load_page_image

page_image = load_page_image()

# Make the image grayscale
page_image_gray = color.rgb2gray(page_image)

# Apply edge detection filter
edge_sobel = sobel(page_image_gray)

# Show original and resulting image to compare
show_image(page_image, "Original")
show_image(edge_sobel, "Edges with Sobel")