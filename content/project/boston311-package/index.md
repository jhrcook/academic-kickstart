---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "boston311"
summary: "Python package for interfacing with Boston 311 API."
authors: ["admin"]
tags: ["Python", "programming", "PyPI", "package", "Boston"]
categories: ["R Packages"]
date: 2021-08-15T08:00:00-00:00
draft: false

# Optional external URL for project (replaces project detail page).

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: False

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
links:
 - name: Source
   url: https://github.com/jhrcook/boston311
   icon_pack: fab
   icon: github
 - name: Documentation
   url: https://jhrcook.github.io/boston311/
   icon_pack: fas
   icon: book
 - name: PyPI
   url: https://pypi.org/project/boston311/0.1.1/
   icon_pack: fab
   icon: python

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

I recently made a request to have some graffiti removed by the city of Boston and used their 311 service for reporting non-emergency crimes. I found it an interesting service and decided to look closer into it. They provide an free API for the service, so I decided to make this Python package to interface with the API.

Below are features of this package:

1. Get a collection of all services offered by Boston 311.
2. Get a collection of all service requests with some useful filters.
3. Get information for a specific service request.

All underlying data models were **parsed and validated with ['pydantic'](https://pydantic-docs.helpmanual.io/)** so there is increased type safety and helpful hints for your IDE.

**Use the links at the top of the page to check out the source code, documentation, or find the package on PyPI.**

