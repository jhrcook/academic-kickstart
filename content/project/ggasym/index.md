---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "ggasym (\"gg-awesome\")"
summary: "'ggasym' (pronounced \"gg-awesome\") plots a symmetric matrix with three different fill aesthetics."
authors: ["admin"]
tags: ["R", "programming", "CRAN", "package"]
categories: ["Programming"]
date: 2019-08-12T20:32:28-04:00

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
 - name: Source
   url: https://github.com/jhrcook/ggasym
   icon_pack: fab
   icon: github
 - name: Documentation
   url: https://jhrcook.github.io/ggasym/index.html
   icon_pack: fab
   icon: github
 - name: CRAN
   url: https://cran.r-project.org/web/packages/ggasym/index.html
   icon_pack: fab
   icon: r-project
 - name: RStudio Top 40
   url: "https://rviews.rstudio.com/2019/04/26/march-2019-top-40-new-cran-packages/"
   icon_pack: fas
   icon: thumbs-up
 - name: R-Weekly
   url: "https://rweekly.org/2019-11.html#NewPackages"
   icon_pack: fas
   icon: thumbs-up

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

'ggasym' (pronounced \"gg-awesome\") plots a symmetric matrix with three different fill aesthetics for the top-left and bottom-right triangles and along the diagonal. It operates within the Grammar of Graphics paradigm implemented in 'ggplot2'.

Below is an axample of how seamlessly 'ggasym' fits into 'ggplot2'. More information can be found in the documentation linked at the top.

---

## Basic Usage

Here is a basic example. `tib` is a "tibble" (ie. fancy "data.frame") of comparisons between groups "A" through "E". There are two values to be plotted, `val_1` and `val_2`, that hold data on the comparison between `g1` and `g2`. `tib` is first passed to `asymmetrise()` to fill in all the missing combinations between `g1` and `g2` such that the symmetric matrix can be built. All added values take the value `NA`. The modified data table is finally passed to `ggplot()` and `geom_asymmat()` is added on. Here, `asymmetrise()` added the rows where `g1` and `g2` are equal, thus will fill the diagonal. I set these values to `val_3`.

```r
tib <- tibble(g1 = c("A", "A", "A", "A", "B", "B", "B", "C", "C", "D"),
              g2 = c("B", "C", "D", "E", "C", "D", "E", "D", "E", "E"),
              val_1 = seq(1, 10, 1),
              val_2 = rnorm(10, mean = 0, sd = 3))
tib <- asymmetrise(tib, g1, g2)
tib$val_3 <- runif(nrow(tib))
ggplot(tib, aes(x = g1, y = g2)) +
    geom_asymmat(aes(fill_tl = val_1, fill_br = val_2, fill_diag = val_3)) +
    scale_fill_tl_gradient(low = "lightpink", high = "tomato") +
    scale_fill_br_gradient(low = "lightblue1", high = "dodgerblue") +
    scale_fill_diag_gradient(low = "yellow", high = "orange3")
```
{{< figure src="example1-1.png" title="" lightbox="true" >}}

## Full ggplot2 integration

Since the new geom is a normal 'ggplot2' object, it can be introduced into a standard 'ggplot2' workflow. Note that the labels can be adjusted like normal using the `labs` function and using the `fill_tl`, `fill_br`, and `fill_diag` arguments.

```{r example3}
ggplot(tib, aes(x = g1, y = g2)) +
    geom_asymmat(aes(fill_tl = log(val_1),
                     fill_br = val_2,
                     fill_diag = val_3)) +
    scale_fill_tl_gradient(low = "lightpink", high = "tomato",
                           guide = guide_colourbar(direction = "horizontal",
                                                   order = 1,
                                                   title.position = "top")) +
    scale_fill_br_gradient(low = "lightblue1", high = "dodgerblue",
                           guide = guide_colourbar(direction = "horizontal",
                                                   order = 3,
                                                   title.position = "top")) +
    scale_fill_diag_gradient(low = "grey80", high = "grey20",
                           guide = guide_colourbar(direction = "horizontal",
                                                   order = 2,
                                                   title.position = "top")) +
    labs(fill_tl = "top-left fill",
         fill_br = "bottom-right fill",
         fill_diag = "diagonal fill",
         title = "Example of ggasym") +
    theme_bw() +
    theme(axis.title = element_blank(),
          plot.title = element_text(hjust = 0.5),
          panel.background = element_rect(fill = "grey70"),
          panel.grid = element_blank()) +
    scale_x_discrete(expand = c(0, 0)) +
    scale_y_discrete(expand = c(0, 0))
```

{{< figure src="example3-1.png" title="" lightbox="true" >}}

## Facetting

If you have multiple categories, facetting works as expected. The only difference is in the preparation of the data table: you must `group_by()` the value(s) you will facet by before passing to `asymmetrise()`. This is shown below.

```{r facetting_setup}
tib <- tibble(g1 = rep(c("A", "A", "B"), 2),
              g2 = rep(c("B", "C", "C"), 2),
              val_1 = seq(1, 6),
              val_2 = rnorm(6),
              grps = c(1, 1, 1, 2, 2, 2))
```

Grouping first by `grps`, the tibble is asymmetrized while retaining the `grps` assignments. I then added values to the diagonal.

```{r grouped_asymm}
tib <- tib %>% group_by(grps) %>% asymmetrise(g1, g2) %>% ungroup()
tib <- tib %>% mutate(val_3 = ifelse(g1 == g2, runif(nrow(tib)), NA))
```

```{r facetting_plot}
ggplot(tib, aes(x = g1, y = g2)) +
    geom_asymmat(aes(fill_tl = log(val_1),
                     fill_br = val_2,
                     fill_diag = val_3)) +
    scale_fill_tl_gradient(low = "lightpink", high = "tomato",
                           guide = guide_colourbar(direction = "horizontal",
                                                   order = 1,
                                                   title.position = "top")) +
    scale_fill_br_gradient(low = "lightblue1", high = "dodgerblue",
                           guide = guide_colourbar(direction = "horizontal",
                                                   order = 3,
                                                   title.position = "top")) +
    scale_fill_diag_gradient(low = "grey80", high = "grey20",
                           guide = guide_colourbar(direction = "horizontal",
                                                   order = 2,
                                                   title.position = "top")) +
    labs(fill_tl = "top-left fill",
         fill_br = "bottom-right fill",
         fill_diag = "diagonal fill",
         title = "Example of facetting with ggasym") +
    theme_bw() +
    theme(axis.title = element_blank(),
          plot.title = element_text(hjust = 0.5),
          panel.background = element_rect(fill = "grey70"),
          panel.grid = element_blank()) +
    scale_x_discrete(expand = c(0, 0)) +
    scale_y_discrete(expand = c(0, 0)) +
    facet_grid(. ~ grps)
```

{{< figure src="facetting_plot-1.png" title="" lightbox="true" >}}
