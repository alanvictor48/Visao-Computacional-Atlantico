from skimage.color import rgb2gray
from PDI.src.pdi_utils import load_page_image,show_image
page_image = load_page_image()
page_image_gray = rgb2gray(page_image)

# Import Gaussian filter
from skimage.filters import gaussian

# Apply filter
gaussian_image = gaussian(page_image_gray)

# Show original and resulting image to compare
show_image(page_image, "Original")
show_image(gaussian_image, "Reduced sharpness Gaussian")