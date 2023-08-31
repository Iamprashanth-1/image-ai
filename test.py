# import cv2
# import numpy as np

# def generate_code(image):
#     # Convert the image to grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     # Threshold the grayscale image to create a mask of the foreground
#     _, mask = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)
    
#     # Create a white background image with the same dimensions as the input image
#     white_background = np.ones_like(image) * 255
    
#     # Copy the foreground pixels from the original image to the white background using the mask
#     result_image = cv2.bitwise_and(white_background, white_background, mask=~mask)
    
#     # Add the foreground pixels to the result image
#     result_image = cv2.add(result_image, image)
    
#     return result_image

# img= generate_code(cv2.imread('path_to_save_rotated_image.jpg'))
# cv2.imwrite('path_to_save_rotated_image1.jpg', img)

from utils import *
from promts import *

# dr = GPT4ALL()
# pt = IMAGE_AI_PROMT.format(question='rotate image by 90')
# _code = dr.call(pt)
_code = '''
import cv2

def generate_code(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("temp.jpg", gray)

    return gray

 '''
print(_code)
_IMAGE_PATH = 'path_to_save_rotated_image.jpg'
img = run_python_code(str(_code) ,{'_img' : _IMAGE_PATH})


#generate_code(cv2.imread('path_to_save_rotated_image.jpg'))
# cv2.imwrite("temp.jpg", img)
# _IMAGE_PATH = 'temp.jpg'

# The Python code as a string
# python_code = """
# def my_function(arg1, arg2):
#     return arg1 + arg2
# """

# # Create a dictionary with argument values
# args_dict = {'arg1': 5, 'arg2': 10}

# # Execute the code with the provided arguments
# exec(python_code, globals(), args_dict)

# # Call the function with the provided arguments
# result = args_dict['my_function'](args_dict['arg1'], args_dict['arg2']) 
# print("Result:", result)
