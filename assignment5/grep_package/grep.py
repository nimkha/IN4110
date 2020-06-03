import re
from highlighter_package import highlighter


def grep_find(filename, regex):
    """
    Finds all matches of regex in file
    :param filename: sourcefile
    :param regex: arbitrary number for regex
    :return: prints the result
    """
    content = highlighter.extract_text(filename)
    for reg in regex:
        print(f"Line containing match(es) => {re.findall(r'.*{}.*'.format(reg), content)}")


def grep_highlight(filename, regex):
    """
    Highlights regex part of file
    :param filename: sourcefile
    :param regex: arbitrary number of regex
    :return:
    """
    content = highlighter.extract_text(filename)
    colors = [31, 32, 33, 34, 35, 36, 37]
    color_index = 0

    def add_color(m):
        """
        helper function that adds color to line
        :param m: string to be colored
        :return: string with added color value
        """
        start_code = "\033[{}m".format(colors[color_index])
        end_code = "\033[0m"
        return start_code + m.group(0) + end_code

    for i in range(len(regex)):
        if color_index > len(colors) - 1:
            color_index = 0
        content = re.sub(regex[i], add_color, content)
        color_index += 1

    print(content)


if __name__ == "__main__":
    grep_find("grep_package/grep_demo", [r"\d+", r"\b[C|c]\w+"])
    grep_highlight("grep_package/grep_demo", [r"\d+", r"\b[C|c]\w+", r"\bit\b", r"\bis\b", r"\ba\b",  r"\bthe\b", r"\bfew\b", r"\balso\b", r"\bexpect\b"])
