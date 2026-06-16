import re

with open("/tmp/paper_body.tex", "r") as f:
    c = f.read()

# Replace \dimexpr(...) with linewidth
# Pattern in the file: p{\dimexpr(\columnwidth - 4\tabcolsep)*0.4375\relax}
# Want to extract: 0.4375 and replace with: 0.4375\linewidth
pattern = r"\\dimexpr\([^)]+\)\*([0-9.]+)\\relax"
replacement = r"\1\\linewidth"
c_new = re.sub(pattern, replacement, c)

n_changed = c.count("\\dimexpr") - c_new.count("\\dimexpr")
print(f"Converted {n_changed} \\dimexpr column specs to \\linewidth")

with open("/tmp/paper_body.tex", "w") as f:
    f.write(c_new)
