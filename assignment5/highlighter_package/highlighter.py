"""
This is a syntax highlighter program
"""

import re
import sys


def extract_theme(theme_file):
    """
    Takes in a file and returns a dictionary with themes. .theme files have a specific syntax
    :param theme_file: file with themes
    :return: theme dictionary
    """
    regex = r"(\w+): \d;(\d+)"
    theme_dict = extract_file_to_dictionary(theme_file, regex)

    return theme_dict


def extract_text(text_file):
    """
    Taken in a text file and returns the content of the file
    :param text_file: sourcefile
    :return: file content
    """
    with open(text_file, "r") as f:
        content = f.read()
    return content


def extract_syntax(syntax_file):
    """
    Takes in a syntax file and creates a dictionary. .syntax files have a specific syntax
    :param syntax_file: file with syntax
    :return: syntax dictionary
    """
    regex = r"(\".+\"): (\w+)"
    syntax_dict = extract_file_to_dictionary(syntax_file, regex, "r")

    for match in syntax_dict.items():
        (key, val) = match
        new_val = val[1:-1]
        syntax_dict[key] = new_val

    return syntax_dict


def extract_file_to_dictionary(file, regex, flag="d"):
    """
    This is a helper function for extracting content from file
    :param file: source file
    :param regex: regex for content
    :param flag: indicates which part of dictionary is key and value. Default is 'd', other options are 'r' which will
    reverse the order
    :return: a dictionary
    """
    content = extract_text(file)
    matches = re.findall(regex, content)
    dictionary = {}

    for match in matches:
        if flag == "r":
            (val, key) = match
        else:
            (key, val) = match
        dictionary[key] = val

    return dictionary


if __name__ == "__main__":
    """
    Runs the program and prints the content with highlighted values
    :return: no return value
    """
    syntax_file = sys.argv[1]
    theme_file = sys.argv[2]
    sourcefile_to_color = sys.argv[3]
    theme_dictionary = extract_theme(theme_file)
    syntax_dictionary = extract_syntax(syntax_file)
    text = extract_text(sourcefile_to_color)

    def add_color(m):
        """
        inner helper function that adds color to string. Added functionality so that
        every word gets colored, by doing it like this if, key words get mixed with e.g comments
        they will be ignored
        :param m: string to be colored
        :return: string with added color value
        """
        return_value = ""
        for s in syntax_dictionary.items():
            r = re.findall(r"" + s[1], m.group(0), flags=re.MULTILINE)
            if r:
                for match in r:
                    words = match.split(" ")
                    for w in words:
                        start_code = "\033[{}m".format(int(theme_dictionary.get(s[0])))
                        end_code = "\033[0m"
                        return_value += (start_code + w + end_code)
                        if len(words) > 1 and w != words[len(words)-1]:
                            return_value += " "
        return return_value

    for syntax in syntax_dictionary.items():
        text = re.sub(r"" + syntax[1], add_color, text, flags=re.MULTILINE)

    print(text)

