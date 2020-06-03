import re

def add_color(m):
    " comment "
    syntax_dictionary = {}
    theme_dictionary = {}

    return_value = ""
    for s in syntax_dictionary.items():
        r = re.findall(r"" + s[1], m.group(0))
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