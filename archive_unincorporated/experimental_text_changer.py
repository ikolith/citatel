import sys

text = (
    open(sys.argv[1], encoding="utf-8")
    .read()
    # For replacing the unicode characters pdflatex is scared of with good, hardy tex math mode glyphs (and ascii emoticon). Can be used on original markdown (will pass through the process, and be interpreted, correctly) or in the interstitial tex document.
    .replace("▲", "$\\blacktriangle$")
    .replace(
        "▷▷▶",
        "$\\triangleright\\mkern-7mu\\triangleright\\mkern-7mu\\blacktriangleright$",
    )
    .replace(
        "▶▷▷",
        "$\\blacktriangleright\\mkern-7mu\\triangleright\\mkern-7mu\\triangleright$",
    )
    .replace("ツ", "'v'")
    # For post-processing tex before it is PDFified. Unclear if this is actually a good way to deal with... any of this, really, but the logntable business is especially sus.
    .replace(r"\begin{minipage}[b]{\linewidth}\raggedright", "")
    .replace(r"\end{minipage}", "")
    .replace(
        "\\documentclass[\n]{article}",
        "\\documentclass[letterpaper, twoside, twocolumn, openany]{book}"
        + "\n"
        + """%IMPORTANT: this must be in our custom template's logic somewhere:
%% fixes the tables mucking up the columns if uncommented... does not fix everything about the tables, though.
\\let\\longtable\\supertabular
\\let\\endlongtable\\endsupertabular
\\let\\endhead\\relax %% ??""",
    )  # I think this has to be after the longtable include?
    .replace("longtable", "supertabular")  # I think this breaks it
    .replace(
        r"""  >{\raggedright\arraybackslash}p{(\columnwidth - 4\tabcolsep) * \real{0.4545}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 4\tabcolsep) * \real{0.2727}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 4\tabcolsep) * \real{0.2727}}@{}}""",
        "ll@{}}",
    )
)

open(sys.argv[2], "w", encoding="utf-8").write(text)
    