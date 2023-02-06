import os

from flask import render_template

path = os.path.split(os.path.abspath(__file__))[0] + "/"
filelist = sorted([i for i in os.listdir(path) if i[-3:] == ".md" or i[-5:] == ".html"])
title = ""
subtitle = ""
with open(path + "title.txt", "r") as f:
    title = f.readline().rstrip()
    subtitle = f.readline().rstrip()
