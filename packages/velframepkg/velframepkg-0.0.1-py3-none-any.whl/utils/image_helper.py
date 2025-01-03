# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import test
import xml.etree.ElementTree as ET

import numpy
from PIL import Image


def find_template_in_image(image_path: str, template_path: str):
    """Search for a template in an image. Both images must have the same bits depth Both images have to exist and be
    accessible, it has to be checked by caller.

    Parameters
    ----------
    image_path: the image path in which search is done
    template_path: template path that will be search

    Returns
    ----------
    position of the find patter, else (-1, -1) if not found
    """

    image = Image.open(image_path)
    template = Image.open(template_path)
    image = numpy.atleast_3d(image)
    template = numpy.atleast_3d(template)
    image_height, image_width, image_depth = image.shape[:3]
    template_height, template_width, template_depth = template.shape[:3]
    assert (
        image_height >= template_height and image_width >= template_width
    ), "Template image size shall smaller than image size "
    f"{template_width}x{template_height} / {image_width}x{image_height}"
    assert (
        image_depth == template_depth
    ), f"Image and template does not have same bits depth {8*image_depth}bits / {8*template_depth}bits"
    # Integral image and template sum per channel
    sat = image.cumsum(1).cumsum(0)
    template_sum = numpy.array([template[:, :, index].sum() for index in range(image_depth)])

    # Calculate lookup table for all the possible windows
    lookup_upper_left, lookup_upper_right, lookup_lower_left, lookup_lower_right = (
        sat[:-template_height, :-template_width],
        sat[:-template_height, template_width:],
        sat[template_height:, :-template_width],
        sat[template_height:, template_width:],
    )
    lookup = lookup_lower_right - lookup_upper_right - lookup_lower_left + lookup_upper_left
    # Possible matches
    possible_match = numpy.where(
        numpy.logical_and.reduce([lookup[..., index] == template_sum[index] for index in range(image_depth)])
    )

    # Find exact match
    for y, x in zip(*possible_match):
        if numpy.all(image[y + 1 : y + template_height + 1, x + 1 : x + template_width + 1] == template):
            return (y + 1, x + 1)

    return (-1, -1)


def get_image_size(image_path: str):
    """Get image size (height and width)

    Parameters
    ----------
    image_path: the path to the image

    Returns
    ----------
    height, width of the provided image
    """

    image = Image.open(image_path)
    image = numpy.atleast_3d(image)
    height, width, _ = image.shape
    return height, width


def compare_image_files(file_path1: str, file_path2: str, max_channel_difference: int = 2) -> bool:
    """Compare two image files for equality with a maximum difference per RGB channel.

    This function takes two file paths and a maximum channel difference as input and
    compare the images located at those paths. It checks if
    the differences in each RGB channel are within the specified maximum.

    Parameters
    ----------
    file_path1, file_path2: file paths of the images to be compared
    max_channel_difference: the maximum allowed difference in each RGB channel (default is 2)

    Returns
    ----------
    If the images have the same dimensions and the differences in each RGB channel
    are within the specified maximum, the function returns True. Otherwise, it returns False.
    """

    try:
        with Image.open(file_path1) as image1, Image.open(file_path2) as image2:
            # Converting the images into numpy arrays (ensure the data type is int32)
            np_array1 = numpy.array(image1, dtype=numpy.int32)
            np_array2 = numpy.array(image2, dtype=numpy.int32)

            # Check if the arrays have the same shape (size)
            if np_array1.shape != np_array2.shape:
                raise ValueError("Images have different sizes")

            # Calculate the absolute differences in each RGB channel
            channel_differences = numpy.abs(np_array1 - np_array2)

            # Check if the differences in each RGB channel are within the specified maximum
            channel_comparison = numpy.all(channel_differences <= max_channel_difference)

            return channel_comparison

    except FileNotFoundError as e:
        raise ValueError(f"One or both image files not found: {e}")


def compare_svg_images(svg_file1: str, svg_file2: str) -> bool:
    """Compare two svg files for equality.

    This function takes two svg file paths as input and compares the width and height metadata in the svg.
    It also compares the image tag instead svg files for equality.

    Parameters
    ----------
    svg_file1, svg_file2: file paths of the images to be compared

    Returns
    ------
    If the images have the same width and height and value inside image tag is same,
    the function returns True. Otherwise, it returns False.
    """

    def extract_encoded_image(file_path):
        """Extracts the text inside <image> tag."""
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Height and width tag
        image_height, image_width = root.get("height"), root.get("width")
        # Find the image tag
        image_tag = root.find(".//{http://www.w3.org/2000/svg}image")

        # Extract the 'xlink:href' attribute value, which contains the base64 encoded image data
        image_data = image_tag.get("{http://www.w3.org/1999/xlink}href")
        return image_height, image_width, image_data

    height1, width1, image_tags1 = extract_encoded_image(svg_file1)
    height2, width2, image_tags2 = extract_encoded_image(svg_file2)

    if image_tags1 == image_tags2:
        if height1 == height2 and width1 == width2:
            return True
        else:
            test.log("Dimensions of the images are different")
            test.log(f"Reference Image Height: {height2}, Width: {width2}")
            test.log(f"Exported Image Height: {height1}, Width: {width1}")
            return False
    else:
        return False
