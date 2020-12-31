---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Text Summarization App"
summary: "A web application that summarizing text down to an adjustable percentage of the the most important sentences."
authors: []
tags: ["Python", "programming", "Streamlit", "web application", "data science", "data analysis"]
categories: ["programming"]
date: 2020-12-31T08:37:42-08:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: true

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
links:
- name: Application
  url: https://textrank-summarizer.herokuapp.com/
  icon_pack: far
  icon: compass
- name: Source
  url: https://github.com/jhrcook/textrank-streamlit
  icon_pack: fab
  icon: github
- name: Follow
  url: https://twitter.com/JoshDoesa
  icon_pack: fab
  icon: twitter

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

A simple web application built using [Streamlit](https://www.streamlit.io) that summarizes long text by extracting a fraction of the most important sentences.
The sentences are ranked using the TextRank method of the ['summa'](https://github.com/summanlp/textrank) Python library that employs the [PageRank](https://en.wikipedia.org/wiki/PageRank) algorithm using the proportion of shared words as the metric of sentence similarity.

The initial blank application is shown below followed by an example of summarizing the opening scene to [Monty Python and the Holy Grail](https://en.wikipedia.org/wiki/Monty_Python_and_the_Holy_Grail) ([text source](http://www.montypython.50webs.com/scripts/Holy_Grail/Scene1.htm)).

<img src="assets/demo_blank.png" width="95%">

<img src="assets/demo_monty-python.png" width="95%">
