import argparse
from grep_package import grep

parser = argparse.ArgumentParser(description="Text highlighter")

parser.add_argument("filename", help="sourcefile with content")
parser.add_argument("regex", help="arbitrary number of regex", nargs="+")
parser.add_argument("--highlight", help="highlights matched content", action="store_true")

args = parser.parse_args()

print("===== Highlighter program =====")

if args.highlight:
    grep.grep_highlight(args.filename, args.regex)
else:
    grep.grep_find(args.filename, args.regex)
