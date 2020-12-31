---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Sudoku Solver"
summary: "A web application that solves [Sudoku puzzles] using linear integer programming."
authors: []
tags: ["Python", "programming", "Streamlit", "web application", "data science", "data analysis"]
categories: ["programming"]
date: 2020-12-31T08:37:28-08:00

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
  url: https://streamlit-sudoku-solver.herokuapp.com/
  icon_pack: far
  icon: compass
- name: Source
  url: https://github.com/jhrcook/streamlit-sudoku
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

A web application that solves [Sudoku puzzles](https://en.wikipedia.org/wiki/Sudoku).
The user inputs the known values in the grid, clicks the *Solve* button, and the solution is displayed below almost instantly.
The web application is built using [Streamlit](https://www.streamlit.io/) and the solving engine uses the optimization library [Pyomo](https://www.pyomo.org/).

<img src="assets/demo.gif" width="95%">
