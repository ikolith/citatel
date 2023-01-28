#!/usr/bin/env python3
r"""LORIC_TRANSCRIBE (this is possibly a bad name. perhaps we should rename it to "fancify romanization". Or perhaps we should implement de-fancification as well...)
A script for converting from the ASCII (normal keyboard) romanization scheme to the "official" one that includes diacritics for long vowels and geminate consonants. Can output as unicode text or TeX code.

SYNTAX:
Make sure input file is in same directory, then:
  python3 transcribe.py -i input-file -o output-file
If no input file is specified, will read input from the first argument. Note: this means, perhaps unfortunately, that if you pass in only the flags -o whatever, this program will attempt to read from a file called -o.
If no output file is specified, will output to tr-[input argument].
If - is provided, standard in or out will be used as the sole input or output source, respectively. If you actually need to output to a file called -, use ./- or something.

Optional flags:
  -t [text] give input text directly by a command line argument
  -v gives output on command line as well as in file (not recommended for large files).
  -l converts to LaTex formatting instead of unicode using the tipa package syntax. Make sure \usepackage{tipa} is in the header of the tex file you are using this for."""
# Hypothetically, we could allow a flag -d that converts from unicode romanization to ascii romanization, but this could be somewhat annoying to investigate the unicode implications of.

import sys
import re

if len(sys.argv) <= 1:
    print(__doc__)
    exit()

args = sys.argv

if "-i" in args:
    input_filename = args[args.index("-i") + 1]
else:
    input_filename = args[1]

if "-o" in args:
    output_filename = args[args.index("-o") + 1]
else:
    output_filename = "tr-" + input_filename


def unicodify(input_string: str) -> str:
    input_string = re.sub(
        r"(?<=([aiueoAIUEO]))\1", "\u0304", input_string, flags=re.IGNORECASE
    )
    input_string = re.sub(
        r"(?<=([a-zA-Z]))\1", "\u0323", input_string, flags=re.IGNORECASE
    )
    return input_string


def texify(input_string: str) -> str:
    input_string = re.sub(
        r"([aiueoAIUEO])\1", r"\\textipa{\=\1}", input_string, flags=re.IGNORECASE
    )
    input_string = re.sub(
        r"(\w)\1", r"\\textipa{\.*\1}", input_string, flags=re.IGNORECASE
    )
    return input_string


if "-t" in args:
    input_text = args[args.index("-t") + 1]
else:
    with sys.stdin if input_filename == "-" else open(
        input_filename, "r", encoding="utf-8"
    ) as input_file:
        input_text = input_file.read()
if "-l" in args:
    output_text = texify(input_text)
else:
    output_text = unicodify(input_text)

if output_filename == "-" or "-v" in args:
    print(output_text)
if not output_filename == "-":
    with open(output_filename, "w", encoding="utf-8") as output_file:
        output_file.write(output_text)
