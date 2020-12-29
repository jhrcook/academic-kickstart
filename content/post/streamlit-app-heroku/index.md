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

This tutorial is meant to act as a guide for deploying [Streamlit]() applications on [Heroku]() using [Docker]() and [GitHub Actions]().
As a data scientist, Streamlit offers the simplest route from analysis to application by providing an API to create an interactive UI in a normal Python script.
We'll see more about this in the example later on, but there are many examples in their [gallery]().

Once the application is built and running locally, we just need to package it up using Docker and deploy to Heroku.
In addition, I have included a step to use GitHub Actions to build and push the Docker image, saving my local computer some computation and time.
Below, I walk through this process, step-by-step.

## Create a Streamlit application

### Introduction to Streamlit

Streamlit is built for data scientists and analysts.
Instead of building applications like many software engineers, we often write scripts that collect and clean data, visualize the data, design and train models, etc.
While it is possible to turn these scripts into applications to interactive use, Streamlit offers a clever API: just "print" the plots, text, etc. and accept user input to variables.
Streamlit then handles all of the UI design, reacts to the user, and presents interactive widgets.
If this seems appealing to you, I would recommend looking through their [website](), [gallery](), and [documentation]() to see examples and guidance on implementation. 

### Example: text-summarizing application

As an example of using Streamlit, I built an application that summarizes text.

First things first, it is generally a good idea (and will be necessary for using Docker) to create a virtual environment for this project and installing ['summa']() and ['streamlit'](); 'summa' is the library that I used to summarize the text.

```bash
$ python3 -m venv env
$ source env/bin/activate
(env)$ pip install summa streamlit
```

Below is the ***entire*** Streamlit application!
I won't provide much explination because I don't think much is required - in most cases, it is very obvious what Streamlit is doing.
Using the `st.title()` function, a title is placed at the top of the app.
Then some text is collected from the user by the `st.text_area()` function - this text is saved as a string to `input_sent`.
The summarization ratio is obtained using a slider with the `st.slider()` function.
Finally, the text is summarized using the 'summa' library and printed to the application using `st.write()` in a for-loop.

```python
#!/usr/bin/env python

from summa import summarizer
import streamlit as st

# Add title to the page.
st.title("Text summarization")

# Ask user for input text.
input_sent = st.text_area("Input Text", "", height=400)

# User input on what fraction of the original text to return.
ratio = st.slider(
    "Summarization fraction", min_value=0.0, max_value=1.0, value=0.2, step=0.01
)

# Summarize the original text.
summarized_text = summarizer.summarize(
    input_sent, ratio=ratio, language="english", split=True, scores=True
)

# Print out the results.
for sentence, score in summarized_text:
    st.write(sentence)
```

The application can be run locally with the following command and going to [http://localhost:8501](http://localhost:8501) in your browser.
The initial blank application is shown below followed by an example of summarizing the opening scene to [Monty Python and the Holy Grail]() ([text source](http://www.montypython.50webs.com/scripts/Holy_Grail/Scene1.htm))

```bash
(env)$ streamlit run app.py
```

<img src="assets/demo_blank.png" width="85%">

<img src="assets/demo_monty-python.png" width="85%">


## Build a Dockerfile

The next step is to construct a file called "Dockerfile" that provide instructions to produce a Docker image with the running application.
Below is the complete Dockerfile and I have provided a brief explination afterwards.

```docker
FROM python:3.9
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run app.py
```

The `FROM python:3.9` at the beginning of the file means that this Dockerfile builds ontop of another that has Python 3.9 already installed and configured.
In order to use this, you must have a [Dockerhub]() account and link it to the Docker application on you computer.
Here is the link to the Python Dockerhub page: [https://hub.docker.com/\_/python](https://hub.docker.com/\_/python).

Next, the `EXPOSE 8501` command exposes port 8501 from the Docker image so that it can be reached when the image is run.

All of the commands from `WORKDIR /app` to `COPY . .` set-up of the Docker environment and create the virtual environment. I'm no expert in Docker, so the details are lost on me, but I think the overall objective is clear from the statements.

Finally, `CMD streamlit run app.py` declares that the Docker image should run `streamlit run app.py` and exit when it finishes.

With the Dockerfile in place, the Docker image can be built and run.

```bash
$ docker build -t app:latest .
$ docker run -p 8501:8501 app:latest
```

Going to the same [http://localhost:8501](http://localhost:8501), you should again see the application.

## Connect and publish to Heroku

### Setting up Heroku

The next step is to deploy the application on the World Wide Web using [Heroku](https://heroku.com).
In order to do so, you will need to create an account - there is a free tier for hobbyists that will be sufficient.

Then the command line interface (CLI) for interfacing with Heroku from your computer must be installed.
Full instructions can be found [here](https://devcenter.heroku.com/categories/command-line); I use a Mac, so I used the Homebrew option.

```bash
$ brew tap heroku/brew && brew install heroku
```
With a Heroku account created and the CLI installed, the next step is to login with the CLI.
The command `heroku login` will open a login window in your browser.

```bash
$ heroku login
heroku: Press any key to open up the browser to login or q to exit
 ›   Warning: If browser does not open, visit
 ›   https://cli-auth.heroku.com/auth/browser/***
heroku: Waiting for login...
Logging in... done
Logged in as me@example.com
```

Finally, we can create a Heroku app by running `heroku create` while within the project directory.

```bash
heroku create
```

### Deploying a Heroku app

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
