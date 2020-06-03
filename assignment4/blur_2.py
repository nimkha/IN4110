import numpy
import cv2
import time
import sys


def blur_entire_image(image):
    """
    Blures an entire image with use of numpy array
    :param image: that will be blurred
    :return: the blurred image
    """

    image = image.astype("uint32")
    padded_image = numpy.lib.pad(image, 1, "edge")[:, :, 1:4]

    row0_clm0 = padded_image[:-2, :-2, :]
    row0_clm1 = padded_image[:-2, 1:-1, :]
    row0_clm2 = padded_image[:-2, 2:, :]
    row1_clm0 = padded_image[1:-1, :-2, :]
    row1_clm1 = padded_image[1:-1, 1:-1, :]
    row1_clm2 = padded_image[1:-1, 2:, :]
    row2_clm0 = padded_image[2:, :-2, :]
    row2_clm1 = padded_image[2:, 1:-1, :]
    row2_clm2 = padded_image[2:, 2:, :]

    blurred_image = calculate_average(row0_clm0, row0_clm1, row0_clm2, row1_clm0, row1_clm1, row1_clm2, row2_clm0, row2_clm1, row2_clm2)
    blurred_image = blurred_image.astype("uint8")

    return blurred_image


@numpy.vectorize
def calculate_average(r0_c0, r0_c1, r0_c2, r1_c0, r1_c1, r1_c2, r2_c0, r2_c1, r2_c2):
    """
    Calculates the average of parameters
    :param r0_c0: row 0 x column 0
    :param r0_c1: row 0 x column 1
    :param r0_c2: row 0 x column 2
    :param r1_c0: row 1 x column 0
    :param r1_c1: row 1 x column 1
    :param r1_c2: row 1 x column 2
    :param r2_c0: row 2 x column 0
    :param r2_c1: row 2 x column 1
    :param r2_c2: row 2 x column 2
    :return: returns the calculated average
    """
    return (r0_c0 + r0_c1 + r0_c2 + r1_c0 + r1_c1 + r1_c2 + r2_c0 + r2_c1 + r2_c2) / 9


def write_result_to_file(time, shape, image_name, file_name, python_file_name):
    """
    Writes result to file. Creates file if it does not exist and appends results
    :param time: elapsed time/run time
    :param shape: shape of the image
    :param image_name: name of the image being blurred
    :param file_name: name of file to use for storing results
    :return: no return value. Values will be stored in file
    """
    file = open(file_name, "a")
    file.write(f"Run time for {image_name} using {python_file_name} with shape {shape} is: {time}\n")
    file.close()

def run(image_name, blurred_name):
    """
    Runs the entire program
    :param image_name: name of the source image
    :param blurred_name: optional destination name for blurred image
    :return: numpy array representing the image
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
    write_result_to_file(elapsed_time, dst.shape, image, "report2.txt", "blur_2")

if __name__ == '__main__':
    """
    Test method runs the program
    :return: no return value
    """
    start = time.time()
    image = "beatles.jpb"
    src = cv2.imread(image)
    print(f"Blurring process for {image} har started")
    dst = blur_entire_image(src)
    cv2.imwrite(f"vector_blurred_{image}", dst)
    print(f"Blurring process finished")
    stop = time.time()
    elapsed_time = stop - start
    write_result_to_file(elapsed_time, dst.shape, image, "report2.txt", "blur_2")

