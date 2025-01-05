from yta_general_utils.image.parser import ImageParser
from yta_general_utils.programming.parameter_validator import NumberValidator
from PIL import Image

import numpy as np
import colorsys


class ImageEditor:
    """
    Class to simplify and encapsulate all the functionality
    related to image edition.
    """
    
    @staticmethod
    def modify_color_temperature(image: any, factor: int = 0):
        # TODO: Apply 'image' typing and add to return
        return change_image_color_temperature(image, factor)

    @staticmethod
    def modify_color_hue(image: any, factor: int = 0):
        # TODO: Apply 'image' typing and add to return
        return change_image_color_hue(image, factor)



COLOR_TEMPERATURE_CHANGE_LOWER_LIMIT = -50
COLOR_TEMPERATURE_CHANGE_UPPER_LIMIT = 50

def change_image_color_temperature(image: any, factor: int = 0) -> np.ndarray:
    """
    Change the 'image' color temperature by the
    provided 'factor', that must be a value between
    [-50, 50].

    The color change consist of updating the red and
    blue values, where red is calid and blue is cold.
    Increasing the temperature means increasing the
    red color, and decreasing it, decreasing the blue
    color.
    """
    if not NumberValidator.is_number_between(factor, COLOR_TEMPERATURE_CHANGE_LOWER_LIMIT, COLOR_TEMPERATURE_CHANGE_UPPER_LIMIT):
        raise Exception(f'The "factor" parameter provided is not a number between [{COLOR_TEMPERATURE_CHANGE_LOWER_LIMIT}, {COLOR_TEMPERATURE_CHANGE_UPPER_LIMIT}].')
    
    # The '.copy()' makes it writeable
    image = ImageParser.to_numpy(image).copy()

    if factor == 0:
        return image

    # We want the factor being actually a value between 0.50 and 1.50,
    # but multiplying by 1.5 is equal to divide by 0.75 so I need to
    # manually do this calculation to apply the formula correctly
    if factor < 0:
        factor = 1 - (0.25 - normalize(factor, COLOR_TEMPERATURE_CHANGE_LOWER_LIMIT, 0, 0, 0.25))
    elif factor > 0:
        factor = 1 + normalize(factor, 0, COLOR_TEMPERATURE_CHANGE_UPPER_LIMIT, 0, 0.5)
    
    r, b = image[:, :, 0], image[:, :, 2]
    
    # Min and max values are 0 and 255
    r = np.clip(r * factor, 0, 255)
    b = np.clip(b / factor, 0, 255)
    
    # Reconstruimos la imagen con los canales modificados
    image[:, :, 0] = r
    image[:, :, 2] = b

    return image


COLOR_HUE_CHANGE_LOWER_LIMIT = -50
COLOR_HUE_CHANGE_UPPER_LIMIT = 50
# These below are 2 functions to convert
# TODO: Please, move these functions to a method
# maybe in 'yta_general_utils' or in 'yta_multimedia'
rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

def change_image_color_hue(image: any, factor: int = 0) -> np.ndarray:
    """
    Change the 'image' color hue by the provided
    'factor', that must be a value between [-50, 50].

    Colorize PIL image `original` with the given
    `factor` (hue within 0-360); returns another PIL image.
    """
    if not NumberValidator.is_number_between(factor, COLOR_HUE_CHANGE_LOWER_LIMIT, COLOR_HUE_CHANGE_UPPER_LIMIT):
        raise Exception(f'The "factor" parameter provided is not a number between [{COLOR_HUE_CHANGE_LOWER_LIMIT}, {COLOR_HUE_CHANGE_UPPER_LIMIT}].')
    
    # The '.copy()' makes it writeable
    image = ImageParser.to_numpy(image).copy()
    
    factor = normalize(factor, COLOR_HUE_CHANGE_LOWER_LIMIT, COLOR_HUE_CHANGE_UPPER_LIMIT, 0, 360)
    
    # TODO: This code is not working well
    # TODO: This method is very very slow
    #arr = np.array(np.asarray(img).astype('float'))
    #r, g, b, a = np.rollaxis(image, axis = -1)
    print(image.size) # size is 6220800
    r, g, b = np.rollaxis(image, axis = -1)
    #r, g, b = np.moveaxis(image, -1, 0)
    h, s, v = rgb_to_hsv(r, g, b)
    h = factor / 360.0
    r, g, b = hsv_to_rgb(h, s, v)
    #arr = np.dstack((r, g, b, a))
    arr = np.dstack((r, g, b)).astype(np.uint8)
    print(arr.size) # size is 220800
    print(arr)

    # TODO: I don't like this line below
    return arr
    return Image.fromarray(arr.astype('uint8'), 'RGBA')


# TODO: Move this method to 'yta_general_utils' library
# and check how other normalize methods are working,
# maybe we can use this general method
def normalize(number: float, input_lower_limit: float, input_upper_limit: float, output_lower_limit: float = 0.0, output_upper_limit: float = 1.0):
    """
    Normalize the 'number' value to be between 'output_lower_limit'
    and 'output_upper_limit', according to the input provided, that
    is between the 'input_lower_limit' and 'input_upper_limit' 
    values.
    """
    if not NumberValidator.is_number(number) or not NumberValidator.is_number(input_lower_limit) or not NumberValidator.is_number(input_upper_limit) or not NumberValidator.is_number(output_lower_limit) or not NumberValidator.is_number(output_upper_limit):
        raise Exception('All the parameters must be numbers.')

    if not NumberValidator.is_number_between(number, input_lower_limit, input_upper_limit):
        raise Exception('The "number" parameter provided is not a number between the input limits provided.')
    
    if input_upper_limit <= input_lower_limit or output_upper_limit <= output_lower_limit:
        raise Exception('The upper limit must be greater than the lower limit.')
    
    return (number - input_lower_limit) / (input_upper_limit - input_lower_limit) * (output_upper_limit - output_lower_limit) + output_lower_limit