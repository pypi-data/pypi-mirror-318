# Copyright(c) 2021 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
from velox.widget_image_grabber import WidgetImageGrabber


class WidgetImageSeriesGrabber:
    def __init__(self):
        self.__images = []
        self.width = 0
        self.height = 0
        self.__content = None

    def __capture(self):
        img = WidgetImageGrabber()
        img.capture(self.__content)

        self.__images.append(img)
        self.width = img.width
        self.height = img.height

    def init(self, obj):
        self.__images = []
        self.width = 0
        self.height = 0
        self.__content = obj
        self.__capture()

    def compare_pixel_rgba(self, obj, x, y, color, nb_attempt):
        """
        TODO: function parameter obj is not used. But it is given when this function is called.
        """
        if len(self.__images) == 0:
            self.__capture()

        for attempt in range(nb_attempt):
            if attempt >= len(self.__images):
                self.__capture()

            image = self.__images[attempt]
            if image.compare_pixel_rgba(x, y, color):
                return True

        return False

    def control_color_on_vertical_profile(self, x, y_min, y_max, color, nb_attempt):
        if len(self.__images) == 0:
            self.__capture()

        for attempt in range(nb_attempt):
            if attempt >= len(self.__images):
                self.__capture()

            image = self.__images[attempt]

            while y_min < y_max:
                if image.compare_pixel_rgba(x, y_min, color):
                    return True
                y_min += 1

        return False
