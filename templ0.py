#!/usr/bin/env python3
# get a file with supposed timings on each line and then prints out mplayer style Mins:secs.centisec
# lines with no number will be ignored.
import sys, regex

# we're going to accept a first argument with a test file in tsv-separated tabular format and then a series of integers representing the columns to include
# when no columns are included, they are all outputted.
argquan=len(sys.argv)
if argquan != 2:
    print("templ0.py, a rough templating effort: 1 arg: list of labels to template upon")
    sys.exit(2)

with open(sys.argv[1]) as f: fl=f.read().splitlines()
li= len(fl)
for i in range(li):
    j=i+1
    print(f"<a href=\"#\">{j}. {fl[i]}<a>")

for i in range(li):
    j=i+1
    print(f"<a id=\"{j}. {fl[i]}\"><h2>{j}. {fl[i]}</h2></a>\
\n<p>A simple , repo <a href=\"https://github.com/rafalcode/{fl[i]}.git\">here</a>.</p>\n")

