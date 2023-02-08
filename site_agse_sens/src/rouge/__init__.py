import os

path = os.path.split(os.path.abspath(__file__))[0] + "/"
filelist = sorted([i for i in os.listdir(path) if i[-3:] == ".md" or i[-5:] == ".html"])
title = ""
subtitle = ""
description = ""

with open(path + "title.txt", "r") as f:
    title = f.readline().rstrip()
    subtitle = [i.rstrip() for i in f.readlines()]

with open(path + "description.txt", "r") as f:
    description = f.read()
