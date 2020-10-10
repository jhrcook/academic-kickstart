---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Bayesian Data Analysis"
summary: "The steps I have taken to learn how to conduct Bayesian data analysis."
authors: []
tags: ["Bayesian", "Bayesian", "data analysis", "data", "data science", "statistics"]
categories: ["Bayesian Data Analysis"]
date: 2020-10-04T18:04:32-04:00
draft: false

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
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

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

For the past few months, I have been learning about and implementing Bayesian techniques for data analysis.
Below is a record of the resources I have used followed by examples of my work that have employed these techniques.

---

## Books

Below are the books I have worked through or are currently studying.

**Statistical Rethinking** (2e) by Richard McElreath

[repo](https://github.com/jhrcook/statistical-rethinking)

<img width="25%" src="assets/statistical-rethinking.png">

**Doing Bayesian Data Analysis** (2e) by John Kruschke

<img width="25%" src="assets/doing-bayesian-data-analysis.png">

**Bayesian Analysis with Python** (2e) by Osvaldo Martin

[repo](https://github.com/jhrcook/bayesian-analysis-with-python_e2)

<img width="25%" src="assets/bayesian-analysis-with-python.png">

**Bayesian Data Analysis** (3e) by Andrew Gelman

<img width="25%" src="assets/bayesian-data-analysis.png">

---

## Examples

### Computational biology

Below are some instances where I have used Bayesian methods in my research.

#### *KRAS* A59 comutation with the MAPK pathway

[code](https://github.com/jhrcook/comutation/blob/master/src/90_40_kh_A59-mutations.R)

I worked with a post-doc in the Haigis lab on analyzing the comutation of the rare *KRAS* A59 mutations with the MAPK pathway in human colorectal cancer sequencing data.
We found that a hypermutation phenotype (likely due to MSI) was associated with an increase in odds of a MAPK pathway, regardless of the mutational status of *KRAS*.
However, *KRAS* A59E/T mutant tumor samples had similar probabilities of having a concomitant MAPK mutation as *KRAS* WT tumors, far higher than other *KRAS* mutant tumors.

<img width="75%" src="assets/kras-a59/prop-hypermutants.png">
<img width="75%" src="assets/kras-a59/m3_hdi.png">
<img width="75%" src="assets/kras-a59/m3_fitted_draws.png">

#### Comutation of *SIRT4* in colorectal cancer

[GitHub repo](https://github.com/jhrcook/sirt4-comutations) (currently private)

For a collaboration with Prof. Marcia Haigis, I conducted a comutation analysis with *SIRT4* with various genes in PI3K pathway, *KRAS*, and *BRAF*.
We found novel comutation interactions that she used as preliminary data in a grant proposal.

<img width="75%" src="assets/sirt4-comutation/unnamed-chunk-25-1.png">
<img width="75%" src="assets/sirt4-comutation/unnamed-chunk-32-1.png">
<img width="75%" src="assets/sirt4-comutation/unnamed-chunk-33-1.png">

#### Hierarchical modeling of gene dependency in a CRISPR-Cas9 knockout screen

[GitHub repo](https://github.com/jhrcook/speclet) (currently private)

I am currently building a hierarchical model to identify synthetic lethal targets with specific *KRAS* mutations using CRISPR-Cas9 knockout screen.
This work is meant to help select candidate genes for follow up experimentation in organoids and mouse models.

For some practice with the data, I experimented with recreating parts of a previously published model [DEMETER2](https://www.nature.com/articles/s41467-018-06916-5) using STAN.
That repository is available on [GitHub](https://github.com/jhrcook/demeter2-stan).

---

### TidyTuesdays

[TidyTuesday](https://github.com/rfordatascience/tidytuesday) is a tradition in the R programming community where a new dataset is provided each Tuesday for everyone to play with.
While some days I try to create visually appealing data visualizations, I generally take the opportunity to experiment with modeling.
Below are the instances where I have explored Bayesian data analysis. 

**August 11, 2020 [Avatar: The Last Airbender](https://github.com/jhrcook/tidy-tuesday/blob/master/2020-08-11_avatar.md)**: I experimented with prior predictive checks.  
**August 4, 2020 [European energy](https://github.com/jhrcook/tidy-tuesday/blob/master/2020-08-04_european-energy.md)**: Using multi-level models to explain energy source usage per country.  
**July 14, 2020 [Astronaut database](https://github.com/jhrcook/tidy-tuesday/blob/master/2020-07-14_astronaut-database.md)**: Compared the results of a Poisson regression model using Frequentist and Bayesian methods.  
**July 7, 2020 [Coffee ratings](https://github.com/jhrcook/tidy-tuesday/blob/master/2020-07-07_coffee-ratings.md)**: Using various regression models to explain coffee rating using qualitative metrics.  
**June 23, 2020 [Caribou location tracking](https://github.com/jhrcook/tidy-tuesday/blob/master/2020-06-23_caribou-location-tracking.md)**: Hierarchical modeling of caribou speeds.  
**June 9, 2020 [Passwords](https://github.com/jhrcook/tidy-tuesday/blob/master/2020-06-09_passwords.md)**: Experimented with modeling the security of passwords based off of their characteristics.  
**May 5, 2020 [Animal Crossing - New Horizons](https://github.com/jhrcook/tidy-tuesday/blob/master/2020-05-05_animal-crossing-new-horizons.md)**: I used sentiment analysis of game reviews to model a players rating of the game.

---

### Blog Posts

I wrote a [blog post](https://joshuacook.netlify.app/post/uncanny-x-men-bayesian-analysis/) as a follow-up on an article to Julia Silge's [Uncanny X-Men analysis](https://juliasilge.com/blog/uncanny-xmen/).
She used a bootstrapping method to build confidence intervals for an estimate of some feature of the comic books (more details are in my original post).
My analysis was focussed on how this was similar to using a Bayesian technique, while also highlighting how a fit Bayesian model is more easily interpreted than 95% confidence intervals from a permutation test.










