"""
Small command line tool to generate a html version of a junit report file
"""

from optparse import OptionParser
import sys
from junit2htmlreport import parser


USAGE = "usage: %prog JUNIT_XML_REPORT [OUTFILE.html]"
PARSER = OptionParser(usage=USAGE, prog="junit2html")


def run(args):
    """
    Run this tool
    :param args:
    :return:
    """
    (opts, args) = PARSER.parse_args(args) if args else PARSER.parse_args()
    if not len(args):
        PARSER.print_usage()
        sys.exit(1)

    outfilename = args[0] + ".html"
    if len(args) > 1:
        outfilename = args[1]

    report = parser.Junit(args[0])
    html = report.html()

    # In python3 this is going to be a str
    bytes_mode = ""
    if isinstance(html, bytes):
        bytes_mode = "b"

    with open(outfilename, "w" + bytes_mode) as outfile:
        outfile.write(html)


def start():
    """
    Run using the current sys.argv
    """
    run(sys.argv[1:])


if __name__ == "__main__":
    start()
