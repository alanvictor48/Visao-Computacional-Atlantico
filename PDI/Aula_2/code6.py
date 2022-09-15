# Import the module and the rotate and rescale functions
from PDI.src.pdi_utils import show_image, load_lena
from PDI.src.pdi_utils import load_lena

image_lena = load_lena()
from skimage.transform import rotate, rescale

# Rotate the image 90 degrees clockwise
rotated_lena_image = rotate(image_lena, -90)

# Rescale with anti aliasing
rescaled_with_aa = rescale(rotated_lena_image, 1/4, order=1, anti_aliasing=True)

# Rescale without anti aliasing
rescaled_without_aa = rescale(rotated_lena_image, 1/4, order=1, anti_aliasing=False)

# Show the resulting images
show_image(rescaled_with_aa, "Transformed with anti aliasing")
show_image(rescaled_without_aa, "Transformed without anti aliasing")