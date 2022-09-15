# Import the required module
from skimage import exposure, color
from PDI.src.pdi_utils import show_image
from PDI.src.pdi_utils import load_lena
image_lena = load_lena()
image_gray = color.rgb2gray(image_lena)

# Use histogram equalization to improve the contrast
image_eq =  exposure.equalize_hist(image_gray)

# Show the original and resulting image
show_image(image_lena, 'Original')
show_image(image_eq, 'Resulting image')