# type: ignore

#   A script for converting from the ASCII (normal keyboard) romanization scheme to the "official" one
#   that includes diacritics for long vowels and geminate consonants
#   Can output as unicode text or TeX code

# SYNTAX:
#   make sure input file is in same directory, then:
#   python3 transcribe.py -i input-file -o output-file
#   if no output file is specified, will output to tr-input-file.txt

# optional flags:
#   -v gives output on command line as well as in file (not recommended for large files)
#   -l converts to LaTex formatting instead of unicode using the tipa package syntax
#   make sure \usepackage{tipa} is in the header


import sys
import re

args = [a.lower() for a in sys.argv]
input_filename = ""

if "-i" in args:
    input_filename = args[args.index("-i") + 1]
else:
    input_filename = args[1]

if "-o" in args:
    output_filename = args[args.index("-o") + 1]
else:
    output_filename = "tr-" + input_filename


def unicodify(input_string):
    input_string = re.sub(r"(?<=([aiueoAIUEO]))\1", "\u0304", input_string)
    input_string = re.sub(r"(?<=([a-zA-Z]))\1", "\u0323", input_string)
    return input_string


def texify(input_string):
    input_string = re.sub(r"([aiueoAIUEO])\1", r"\\textipa{\=\1}", input_string)
    input_string = re.sub(r"(\w)\1", r"\\textipa{\.*\1}", input_string)
    return input_string


output_text = "ERROR"

with open(input_filename, "r") as input_file:
    input_text = input_file.read()
    if "-l" in args:
        output_text = texify(input_text)
    else:
        output_text = unicodify(input_text)

if "-v" in args:
    print(output_text)
with open(output_filename, "w") as output_file:
    output_file.write(output_text)
