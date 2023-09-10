import os
import time

from flask import render_template
from werkzeug.exceptions import abort

import markdown

md_extensions = [
    "extra",
    "legacy_attrs",
    "legacy_em",
    "meta",
    "nl2br",
    "sane_lists",
    "toc",
    "wikilinks",
    "markdown_checklist.extension",
    "markdown_del_ins",
    "markdown_sub_sup",
    "markdown_mark",
    "mdx_unimoji",
]

def get_lastmod_date(url_path, path):
    filelist = [f for f in os.listdir(path + url_path)]
    last_m_date = 0
    for i in filelist:
        if os.path.isfile(path + url_path + "/" + i) and (i[-3:] == ".md" or i[-4:] == ".html"):
            if os.path.getmtime(path + url_path + "/" + i) > last_m_date:
                last_m_date = os.path.getmtime(path + url_path + "/" + i)
    return time.strftime('%Y-%m-%d', time.gmtime(last_m_date))

def render_page(page_path, path):
    if os.path.exists(page_path) == False :
        abort(404)
    filelist = sorted([i for i in os.listdir(page_path) if os.path.splitext(page_path+i)[1] in [".md",".html"]])
    title = ""
    subtitle = ""
    page_title = page_path.split("/")[-1]
    description = ""
    use_head = True
    title = ""
    noindex = True if path[-9:] == "/private/" else False
    try :
        with open(page_path + "TITLE", "r") as f:
            title = f.readline().rstrip()
            subtitle = [i.rstrip() for i in f.readlines()]
    except FileNotFoundError :
        use_head = False

    try :
        with open(page_path + "DESCRIPTION", "r") as f:
            description = f.read().rstrip()
    except FileNotFoundError :
        pass

    try :
        with open(page_path + "NAME", "r") as f:
            page_title = f.read().rstrip()
    except FileNotFoundError :
        pass

    return render_template(
        "main/md.html",
        filelist=[
            [
                os.path.splitext(page_path+i)[1][1:],
                markdown.markdown(
                    open(page_path + i, "r").read(),
                    extensions=md_extensions,
                )
                if os.path.splitext(page_path+i)[1] == ".md"
                else open(page_path + i, "r").read(),
            ]
            for i in filelist
        ],
        title=title,
        subtitle=subtitle,
        page_title=page_title,
        description=description,
        use_head=use_head,
        noindex=noindex,
    )
