# Import the required module
import matplotlib.pyplot as plt
from PDI.src.pdi_utils import show_image, load_page_image
from skimage import exposure, color

page_image = load_page_image()
# Show original page image and its histogram
show_image(page_image, 'Original page')

page_image_gray = color.rgb2gray(page_image)

plt.title('Histogram of image')
plt.hist(page_image_gray.ravel(), bins=256)
plt.show()

# Use histogram equalization to improve the contrast
page_image_gray_eq =  exposure.equalize_hist(page_image_gray)


# Show the resulting image
show_image(page_image_gray_eq, 'Resulting image')