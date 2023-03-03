import os

path = os.path.split(os.path.abspath(__file__))[0] + "/"
filelist = sorted([i for i in os.listdir(path) if i[-3:] == ".md" or i[-5:] == ".html"])
title = ""
subtitle = ""
page_title = str(__name__).split(".")[-1]
description = ""
use_head = True

try :
    with open(path + "title.txt", "r") as f:
        title = f.readline().rstrip()
        subtitle = [i.rstrip() for i in f.readlines()]
except FileNotFoundError :
    use_head = False

try :
    with open(path + "description.txt", "r") as f:
        description = f.read().rstrip()
except FileNotFoundError :
    pass

try :
    with open(path + "page_title.txt", "r") as f:
        page_title = f.read().rstrip()
except FileNotFoundError :
    pass

