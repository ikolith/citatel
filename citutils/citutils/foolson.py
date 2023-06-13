import json
import warnings

"""
This version of foolson is experimental, and creates as yet no standard.
Foolson is a serialization format like json except:
1. Indentation instead of curly braces. For simplicity, indentation is centered around "indentons", which each are 2 single-space characters (ASCII 0x20, U+0020). An "indentation" at the beginning of a line is made up of one or more indentons. The key concept of indentation is that one greater level of indentation indicates the interior of a json object. Note that this means the KEYS are the thing we're primarily concerned with getting indented; indenting the values is just a side-effect. TODO: this means that to have a file of key-value pairs, the entire file must be indented by one. 
2. quotes are unnecessary (this feature currently pending). Thus, 
3. All foolson files begin with the "magic number" foolson followed by a newline (foolson2, etc, as well as anything else after the foolson but before the newline, is reserved for future versions of foolson. The 1 has been omitted from the magic number of foolson version 1 because we hope it will not need additional versions.)
4. The file extension of foolson is fool
"""
indenton = "  "
foolson_magic_number = 'foolson\n'

#TODO: this is bad, "string typing". We should have a foolson and json type that subtype of str (unless this is not pythonic). I could look into this, but I choose not to at the moment.
def foolson_to_json(foolson: str) -> str: #TODO: consider using the "json_from_foolson" convention instead of the "foolson_to_json" convention.
  #Validate magic number:
  if foolson.startswith(foolson_magic_number):
    foolson = foolson.removeprefix(foolson_magic_number)
  else:
    raise SyntaxError("The foolson data does not begin with the foolson magic number, 'foolson\\n'")
  
  json_buffer = ""
  linecount = 0
  prev_indenton_level = 0
  for line in foolson.splitlines(): #going line-by-line might be dumb, or might necessitate we repair the lines later, but whatever.
    linecount+=1
    stripped_line = line.lstrip(' ')
    prefix_len = len(line) - len(stripped_line)

    #extra, perhaps misguided, whitespace enforcement
    if prefix_len % len(indenton) != 0:
      raise IndentationError("Indentation is not uniformly composed of whole indentons; perhaps you only typed half an indenton? An indenton, which makes a level of indentation, is two spaces. Problem is on line %d" % linecount)
    if line.lstrip() != stripped_line:
      raise IndentationError("You seem to have tried to include some non-space whitespace character in the indentation. This is illegal in the foolson spec (forthcoming). Problem is on line %d" % linecount)

    #OK, let's actually do the transformation.
    indenton_count = prefix_len//len(indenton)
    if indenton_count > prev_indenton_level:
      if indenton_count == prev_indenton_level+1:
        json_buffer += "{\n"
      else:
        raise IndentationError("You seem to have tried to indent more than one level at once, as the indenton level has gone from %d to %d. Problem is on line %d" % (prev_indenton_level,indenton_count,linecount) )
    elif indenton_count < prev_indenton_level:
      json_buffer += "}"*(prev_indenton_level-indenton_count) #It's perfectly fine to close multiple levels at once.
    #we always add the line of json...
    json_buffer += line
    prev_indenton_level = indenton_count
  json_buffer += "}"*prev_indenton_level #as we are now done with the string, we may close all remaining json objects
  return json_buffer

def json_to_foolson(json: str) -> str:
  raise NotImplementedError("Literally no one has ever needed json→foolson capability up to this point, so it has not been implemented. Please file a bug report if you need this.")

def values_to_foolson(obj) -> str:
  raise NotImplementedError("Literally no one has ever needed value→foolson capability up to this point, so it has not been implemented. Please file a bug report if you need this.")

def foolson_to_values(foolson: str):
  return json.loads(foolson_to_json(foolson))

def test():
  print( foolson_to_json('foolson\n  "blah":\n    "blah": "blah"') )
  print( foolson_to_values('foolson\n{"blah":\n  "blah": "blah"}') )
  #Example from https://docs.python.org/3/library/json.html
  print(
    json.loads("""["foo", {"bar":["baz", null, 1.0, 2]}]""") == #print(
      foolson_to_values("""foolson\n["foo",\n  "bar":  ["baz", null, 1.0, 2]\n]""")
    #)
  )
  print(
  #Example from https://json.org/example.html
  json.loads("""
{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
""") == foolson_to_values("""foolson
  "glossary": 
    "title": "example glossary",
    "GlossDiv": 
      "title": "S",
      "GlossList": 
        "GlossEntry": 
          "ID": "SGML",
          "SortAs": "SGML",
          "GlossTerm": "Standard Generalized Markup Language",
          "Acronym": "SGML",
          "Abbrev": "ISO 8879:1986",
          "GlossDef": 
            "para": "A meta-markup language, used to create markup languages such as DocBook.",
            "GlossSeeAlso": ["GML", "XML"]
          ,
          "GlossSee": "markup"
""")
  )

test()