#!/usr/bin/env python
import sys


def count_words(file_name):
    """
    Takes file name and calculates number of words in file
    :param file_name:
    :return: number of words in file
    """
    file = open(file_name)
    number_of_words = 0

    for word in file.read().split():
        number_of_words += 1

    return number_of_words


def count_lines(file_name):
    """
    Takes file name and calculates number of lines in file
    :param file_name:
    :return: number of lines in file
    """
    number_of_lines = len(open(file_name).readlines())

    return number_of_lines


def count_characters(file_name):
    """
    Takes file name and calculates number characters in a file. This version excludes white spaces
    :param file_name:
    :return: number of characters in file excluding white spaces
    """
    file = open(file_name)
    data = file.read().replace(" ", "")
    counter = len(data)

    return counter


def main():
    """
    Main function, runs the program
    :return: no return value
    """
    arguments = sys.argv[1:]
    for file in arguments:
        number_of_words = count_words(file)
        number_of_lines = count_lines(file)
        number_of_characters = count_characters(file)

        print(f"#characters -> {str(number_of_characters)}, #words -> {str(number_of_words)}, #lines -> {str(number_of_lines)}, file name -> {file}")


main()
