# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import math as m
import object

from velox.labels.colors import Colors
from velox.labels.display_settings import ImageSearchRegion


class WidgetImageGrabber:
    def __init__(self):
        self.obj = None
        self.__img = None
        self.width = 0
        self.height = 0

    @property
    def image(self):
        return self.__img

    def capture(self, obj, delay: int = 0):
        self.obj = obj
        self.__img = object.grabScreenshot(obj, {"delay": delay})
        self.width = self.__img.width
        self.height = self.__img.height

    def compare_pixel_rgba(self, x, y, other):
        pixel = self.__img.getPixelRGBA(x, y)
        for i in range(0, 4):
            if pixel[i] != other[i]:
                return False
        return True

    def get_pixel_rgba(self, x, y):
        return self.__img.getPixelRGBA(x, y)

    def get_pixel_rgb(self, x, y):
        rgba = self.__img.getPixelRGBA(x, y)
        return rgba[:3]

    def compare(self, other):
        return self.__img.equals(other.__img)

    def exists(self):
        return self.__img is not None

    def is_pixel_different_from_neighbours(self, x, y):
        reference_pixel = self.get_pixel_rgba(x, y)
        for x_offset in [-1, 0, 1]:
            for y_offset in [-1, 0, 1]:
                if x_offset != 0 or y_offset != 0:
                    if not self.compare_pixel_rgba(x + x_offset, y + y_offset, reference_pixel):
                        return True
        return False

    def check_color_exist_on_horizontal_line(self, x_min, x_max, y, color, tolerance: int = 0):
        while x_min < x_max:
            pixel_color = self.get_pixel_rgba(x_min, y)
            if (
                abs(list(pixel_color)[0] - color[0]) < tolerance
                and abs(list(pixel_color)[0] - color[0]) < tolerance
                and abs(list(pixel_color)[0] - color[0]) < tolerance
            ):
                return True
            x_min += 1
        return False

    def control_color_exist_in_area(self, color, search_width: int, search_area: ImageSearchRegion, tolerance: int = 1):
        # Define area of search
        # top left
        if search_area == ImageSearchRegion.TOP_LEFT:
            x_max = (self.__img.width // 2) - 1
            y_max = (self.__img.height // 2) - 1
            x = 0
            y = 0
        # top right
        elif search_area == ImageSearchRegion.TOP_RIGHT:
            x_max = self.__img.width
            y_max = (self.__img.height // 2) - 1
            x = self.__img.width // 2
            y = 0
        # bottom left
        elif search_area == ImageSearchRegion.BOTTOM_LEFT:
            x_max = (self.__img.width // 2) - 1
            y_max = self.__img.height
            x = 0
            y = self.__img.height // 2
        # bottom right
        elif search_area == ImageSearchRegion.BOTTOM_RIGHT:
            x_max = self.__img.width
            y_max = self.__img.height
            x = self.__img.width // 2
            y = self.__img.height // 2
        # center area
        elif search_area == ImageSearchRegion.CENTER:
            x_max = (self.__img.width // 4) + (self.__img.width // 2)
            y_max = (self.__img.height // 4) + (self.__img.height // 2)
            x = self.__img.width // 4
            y = self.__img.height // 4
        # full image
        elif search_area == ImageSearchRegion.FULL:
            x_max = self.__img.width
            y_max = self.__img.height
            x = 0
            y = 0

        nb_found = 0
        while y < y_max:
            while x < x_max:
                pixel_color = self.get_pixel_rgba(x, y)
                if (
                    abs(pixel_color[0] - color[0]) < tolerance
                    and abs(pixel_color[1] - color[1]) < tolerance
                    and abs(pixel_color[2] - color[2]) < tolerance
                ):
                    nb_found += 1
                    x += 1
                    if nb_found == search_width:
                        return True
                else:
                    nb_found = 0
                    x += 5
            y += 5
            x = 0
            nb_found = 0
        return False

    def get_pixel_intensity(self, angle: int, radius: int, image_center_x: int, image_center_y: int) -> float:
        """Calculate pixel color intensity as used in previous sikuli test.

        Parameters
        ----------
        angle: angle value used to get the pixel coordinate
        radius: distance of the pixel from the center
        image_center_x: x coordinate of the image center
        image_center_y: y coordinate of the image center

        Returns
        -------
        Float value of the pixel color intensity
        """
        x = int(round(radius * m.cos(m.radians(angle))))
        y = int(round(radius * m.sin(m.radians(angle))))
        color = self.get_pixel_rgba(image_center_x + x, image_center_y - y)
        return sum(color) / float(len(color))

    def crop(self, crop_start_x, crop_start_y, crop_width, crop_height):
        """Crops specific region of image."""
        self.__img = self.__img.copy(crop_start_x, crop_start_y, crop_width, crop_height)
        self.width = self.__img.width
        self.height = self.__img.height

    def check_all_pixels_in_image_are_color(self, color: Colors) -> bool:
        """Checks if all the pixels in the image are the given color.

        Parameters
        ----------
        color: the color to verify for each pixel in the given image
        """
        expected_colors = color.associated_RGBcolor()

        for x in range(self.width):
            for y in range(self.height):
                pixel_color = self.get_pixel_rgb(x, y)
                if not (list(pixel_color) in expected_colors):
                    return False
        return True

    def save_in_file(self, file_path: str):
        """Stores the image in an image file on the given path and file name.

        Parameters
        ----------
        file_path: Path to the file where the image should be saved
        """
        self.__img.save(file_path)
