---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Plant Tracker iOS App"
summary: "An app to help my mom keep track of and care for her plants."
authors: ["admin"]
tags: ["iOS", "Swift", "application", "app", "open source", "programming"]
categories: ["Programming"]
date: 2019-08-12T11:55:41-04:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
links:
 - name: Source
   url: https://github.com/jhrcook/PlantTracker
   icon_pack: fab
   icon: github

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

# Purpose

The goal of this iOS application is to help the user (my mom) care for his/her plants. To this end it will record when the user last watered each plant, have their specific seasons (eg. growing or dormant seasons), and provide useful links for further care information. There is also a section where the user can take notes on each specimen. In addition, it will record the progress of each plant by storing and ordering their photos.


# Design and layout

## Library

The app will be divided into multiple tabs. The first is the Library, a collection of all the types of plants that the user has encountered and documented. There is only one entry per plant type which will hold general information on the plant.

## Collection

The Collection tab will hold all of the plants owned by the user. Whereas the Library entries were referencing the general plant variety, the collection holds specific plant specimens. Therefore, along with general care information, there will also be information specific to the plant such as when it was last watered and from who and when it was aquired.

## To-Do

The third tab will hold the To-Do list for the garden. A specific feature that will be quite handy is that specific To-Do's can be linked to specific plants in Collection. Also, notifications to water plants will be automatically added here.

# Current status

This app is very much in production. I am still working on the Library tab, though it is almost far enough along to begin working on the Collection tab.

You can check out the up-to-date status of this app at it's GitHub repository linked at the top.

{{< figure src="Aug-10-2019 08-20-06.gif" title="" lightbox="true" >}}

