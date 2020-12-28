---
title: "Creating a Streamlit web app, building with Docker + GitHub Actions, and hosting on Heroku"
subtitle: "A step-by-step tutorial on creating a web application with Streamlit, building a Docker image with GitHub Actions, and hosting on Heroku."
summary: "A step-by-step tutorial on creating a web application with Streamlit, building a Docker image with GitHub Actions, and hosting on Heroku."
authors: []
tags: [programming, Python, Docker, Heroku, website, application]
categories: [Programming]
date: 2020-12-24T16:56:35-08:00
lastmod: 2020-12-24T16:56:35-08:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []

links:
 - name: GitHub Repo
   url: https://github.com/jhrcook/textrank-streamlit
   icon_pack: fab
   icon: github
 - name: Web Application
   url: https://textrank-summarizer.herokuapp.com/
   icon_pack: far
   icon: compass

---

Quick introduction.
- link to text summarization app that this guide creates: https://textrank-summarizer.herokuapp.com/
- how easy it is to do
- introduce Streamlit
- general steps: Streamlit app dev; Docker; Heroku; GitHub Action

## Create a Streamlit application

### Overview of using Streamlit

- general idea
- link to website, documentation, and gallery

### Example: text-summarizing application

- virtual environment, libraries, and "requirements.txt"

```bash
$ python3 -m venv env
$ source env/bin/activate
(env)$ pip install summa streamlit
```

- the code with explination focusing on the Streamlit portion

```python
#!/usr/bin/env python
from summa import summarizer
import streamlit as st

# Add title on the page
st.title("Text summarization")

# Ask user for input text
input_sent = st.text_area("Input Text", "", height=400)

ratio = st.slider(
    "Summarization fraction", min_value=0.0, max_value=1.0, value=0.2, step=0.01
)

# Display named entities
summarized_text = summarizer.summarize(
    input_sent, ratio=ratio, language="english", split=True, scores=True
)

for sentence, score in summarized_text:
    st.write(sentence)
```

- code on command line to run the app locally

```bash
(env)$ streamlit run app.py
```

- image of working app (blank and with example text)

<img src="assets/demo_blank.png" width="85%">

- example with script of Holy Grail (http://www.montypython.50webs.com/scripts/Holy_Grail/Scene1.htm)

<img src="assets/demo_monty-python.png" width="85%">

## Build a Docker file

- overview of Docker and explination of pieces
- include the text of the docker file

```docker
FROM python:3.9
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run app.py
```

- build and run (make sure Docker is running on your computer)

```bash
$ docker build -t app:latest .
$ docker run -p 8501:8501 app:latest
```


## Connect and publish to Heroku

- set-up user
- install CLI (doc: https://devcenter.heroku.com/categories/command-line)

```bash
$ brew tap heroku/brew && brew install heroku
```
- CLI login (opens browser)

```bash
$ heroku login
heroku: Press any key to open up the browser to login or q to exit
 ›   Warning: If browser does not open, visit
 ›   https://cli-auth.heroku.com/auth/browser/***
heroku: Waiting for login...
Logging in... done
Logged in as me@example.com
```

- create Heroku app (in project directory)

```bash
heroku create
```

- Heroku doc for deplying Docker images: https://devcenter.heroku.com/articles/container-registry-and-runtime
- adjust Dockerfile

```docker
...
# CMD streamlit run app.py
CMD streamlit run --server.port $PORT app.py
```
- login to Heroku's container registry

```bash
$ heroku container:login
```

- build & push image to registry

```bash
$ heroku container:push web
```

- release the image to the app

```bash
$ heroku container:release web
```

- verify it worked

```bash
$ heroku open
```

## Set up deployment with GitHub Actions

- create CI.yml

```yaml
name: Build Docker image and deploy to Heroku
on:
  # Trigger the workflow on push or pull request,
  # but only for the main branch
  push:
    branches:
      - master
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v1
      - name: Login to Heroku Container registry
        env:
          HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
        run: heroku container:login
      - name: Build and push
        env:
          HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
        run: heroku container:push -a textrank-summarizer web
      - name: Release
        env:
          HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
        run: heroku container:release -a textrank-summarizer web
```

- describe general steps and link to GitHub Actions documentation
- set up Heroku auth GitHub secrets

```bash
$ heroku authorizations:create
```

## Conclusion

- simple way to turn a fun project into a web application
- make a template and copy it every time
- etc.
