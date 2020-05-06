#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import unicodedata

import latuni

##
## Main Program
##
def main():
    parser = argparse.ArgumentParser(description="Format latin text with unicode")
    parser.add_argument("-s", "--style", dest="style", metavar="STYLE",
            choices=latuni.styles.keys(),
            default="serif",
            help="Text style to use: %(choices)s (default:%(default)s)")
    parser.add_argument("-b", "--bold", dest="flags",
            action='append_const', const=latuni.FACE_BOLD,
            help="Bold")
    parser.add_argument("-i", "--italic", dest="flags",
            action='append_const', const=latuni.FACE_ITAL,
            help="Italic")
    parser.add_argument("--from-string", dest="in_string", metavar="STRING",
            type=str,
            default="",
            help="format STRING instead of file")
    parser.add_argument("infile", metavar="INFILE",
            nargs="?",
            type=argparse.FileType(mode="rt", encoding="UTF-8"),
            default=sys.stdin,
            help="Read text from INFILE (default:stdin)")
    parser.add_argument("outfile", metavar="OUTFILE",
            nargs="?",
            type=argparse.FileType(mode="wt", encoding="UTF-8"),
            default=sys.stdout,
            help="Write formatted text to OUTFILE (default:stdout)")

    args = parser.parse_args()

    if args.in_string:
        text = args.in_string+"\n"
    else:
        text = args.infile.read()

    text = unicodedata.normalize('NFD', text);
    flags = sum(args.flags or [], latuni.styles[args.style])
    args.outfile.write(latuni.format(flags, text))

if __name__ == '__main__':
    sys.exit(main() or 0)

# Editor modelines - http://www.wireshark.org/tools/modelines.html
#
# Local variables:
# c-basic-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# coding: utf-8
# End:
#
# vi:set shiftwidth=4 tabstop=4 expandtab fileencoding=utf-8:
# :indentSize=4:tabSize=4:noTabs=true:coding=utf-8:
