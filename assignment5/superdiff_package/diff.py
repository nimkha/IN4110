from highlighter_package import highlighter
import re
import sys


def missing_content(original, modified, result):
    """
    searches for the missing content in modified file compared to original. Writes to file what is missing and what has
    stayed the same
    :param original: original file
    :param modified: modified file
    :param result: filename to print result
    :return: no return value
    """
    original_content = open(original, "r")
    modified_content = highlighter.extract_text(modified)

    for line in original_content.readlines():
        match = re.findall(line, modified_content, flags=re.MULTILINE)
        if match:
            match[0] = has_newline(match[0])
            no_diff = f"0 {match[0]}"
            write_to_file(result, no_diff)
            print(no_diff)
        else:
            line = has_newline(line)
            removed = f"- {line}"
            write_to_file(result, removed)
            print(removed)

    original_content.close()


def added_content(original, modified, result):
    """
    searches for the added content in modified file compared to original. Writes to file what is added
    :param original: original file
    :param modified: modified file
    :param result: filename to print result
    :return: no return value
    """
    original__content = highlighter.extract_text(original)
    modified_content = open(modified, "r")

    for line in modified_content.readlines():
        if line.endswith("\n"):
            match = re.findall(line[:-1], original__content, flags=re.MULTILINE)
        else:
            match = re.findall(line, original__content, flags=re.MULTILINE)
        if not match:
            line = has_newline(line)
            added = f"+ {line}"
            write_to_file(result, added)
            print(added)

    modified_content.close()


def write_to_file(filename, content):
    """
    helper function that appends content to a file
    :param filename: file to append content
    :param content: what is added to file
    :return: no return value
    """
    file = open(filename, "a")
    file.write(content)
    file.close()


def has_newline(line):
    """
    helper function that checks if line ends with newline character and adds it if not.
    :param line: line to check
    :return: returns a string based on condition
    """
    newline_regex = r"$\n"
    match = re.findall(newline_regex, line, flags=re.MULTILINE)

    if match:
        return line
    else:
        return line + "\n"


if __name__ == "__main__":
    missing_content(sys.argv[1], sys.argv[2], sys.argv[3])
    added_content(sys.argv[1], sys.argv[2], sys.argv[3])
