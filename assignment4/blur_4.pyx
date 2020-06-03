import cv2
import numpy
import sys
import time
from blur_2 import write_result_to_file


def calculate_average(image, row_counter, column_counter, channel_counter):
    """
    Takes in an image an calculates the average of 9 pixels. This is done by using the values around a certain pixel
    including the pixel itself.
    :param image: the image used to calculate pixel values from
    :param row_counter: can also be seen as height
    :param column_counter: can also be seen as width
    :param channel_counter: number of channels in image
    :return: returns the calculated average as float
    """
    return (image[row_counter][column_counter][channel_counter] + image[row_counter - 1][column_counter][
        channel_counter] + image[row_counter + 1][column_counter][channel_counter] +
            image[row_counter][column_counter - 1][channel_counter] + image[row_counter][column_counter + 1][
                channel_counter] +
            image[row_counter - 1][column_counter - 1][channel_counter - 1] +
            image[row_counter - 1][column_counter + 1][channel_counter] +
            image[row_counter + 1][column_counter - 1][channel_counter] + image[row_counter + 1][column_counter + 1][
                channel_counter]) / 9


def blur_entire_image(image):
    """
    Takes in an image an blures the entire image. This is done by calculating the average of 3x3 for every pixel
    and replacing the pixel value with the average. Added cython support.
    :param image: the image to blur
    :return: a blurred copy of the image. Original image remains the same.
    """

    image = image.astype("uint32")
    blurred_image = numpy.empty_like(image)
    cdef int height = blurred_image.shape[0]
    cdef int width = blurred_image.shape[1]
    cdef int channels = blurred_image.shape[2]
    padded_image = numpy.lib.pad(image, 1, "edge")[:, :, 1:4]
    cdef int y, x, z


    for y in range(0, height):
        for x in range(0, width):
            for z in range(channels):
                blurred_image[y, x, z] = calculate_average(padded_image, y + 1, x + 1, z)

    blurred_image = blurred_image.astype("uint8")
    return blurred_image

def run(image_name, blurred_name=""):
    """
    Runs the entire program
    :param image_name: name of the source image
    :param blurred_name: optional destination name for blurred image
    :return: numpay array representing the image
    """
    start = time.time()
    image = image_name
    src = cv2.imread(image)
    print(f"Blurring process for {image} har started")
    dst = blur_entire_image(src)

    if blurred_name is not None:
        if len(blurred_name) > 5:
            cv2.imwrite(blurred_name, dst)

    print(f"Blurring process finished")
    stop = time.time()
    elapsed_time = stop - start
    write_result_to_file(elapsed_time, dst.shape, image, "report4.txt", "blur_4")

if __name__ == '__main__':
    """
    Main method runs the program
    :return: no return value
    """
    start = time.time()
    image = "beatles.jpg"
    src = cv2.imread(image)
    print(f"Blurring process for {image} har started")
    dst = blur_entire_image(src)
    cv2.imwrite(f"blurred_{image}", dst)
    print(f"Blurring process finished")
    stop = time.time()
    elapsed_time = stop - start
    write_result_to_file(elapsed_time, dst.shape, image, "report4.txt", "blur_4")
