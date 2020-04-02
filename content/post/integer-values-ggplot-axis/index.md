---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Setting axes to integer values in 'ggplot2'"
subtitle: "A seemingly simple task took quite a bit of research and experimentation to figure out."
summary: ""
authors: [~]
tags: [R, programming]
categories: [Programming]
date: 2019-11-09T08:09:23-05:00
lastmod: 2019-11-09T08:09:23-05:00
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
 - name: Gist
   url: https://gist.github.com/jhrcook/eb7b63cc57c683a6eb4986c4107a88ec
   icon_pack: fab
   icon: github-alt

 - name: Source
   url: integer-values-ggplot-axis.R
   icon_pack: fab
   icon: r-project

---

## The problem

I stumbled across this problem as a TA for an introductory R course.
It was a minor question on a Problem Set focussed on creating a Shiny app that the instructor had seeminly dismissed as trivial and not bothered to include in his solution guide.
Anyways, I needed to be able to grade the problem set, so I gave it a shot.

Like any good programmer, I Googled the question and clicked on the most appealing Stack Overflow response. Here is a link to the post I pulled up: ["How to display only integer values on an axis using ggplot2."](https://stackoverflow.com/questions/15622001/how-to-display-only-integer-values-on-an-axis-using-ggplot2)
The question was essentially that and the accepted answer was:

> With `scale_y_continuous()` and argument `breaks=` you can set the breaking points for y axis (sic) to integers you want to display.

```r
ggplot(data2, aes(x =factor(IR), y = value, fill = Legend, width=.15)) +
  geom_bar(position='dodge', colour='black')+
  scale_y_continuous(breaks=c(1,3,7,10))
```

This was simple solution, but having to define the axes values with some [magic numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)) seemed wrong.
Further, it would be clunky to implement in the Shiny app as the axes are being adjusted based on user input.

The next answer was a bit more promising.

> If you have the 'scales' package, you can use `pretty_breaks()` without having to manually specify the breaks.

```r
q + geom_bar(position='dodge', colour='black') + 
  scale_y_continuous(breaks= pretty_breaks())
```

Still though, this doesn't actually solve the issue - at a small enough scale, this does not force integers.
Here is an example using the classic `iris` data set that comes with R.

```r
iris %>% 
  ggplot(aes(x = Petal.Width, y = Sepal.Width)) +
  geom_point(aes(color = Species)) +
  scale_y_continuous(breaks = scales::pretty_breaks()) +
  theme_bw()
```

{{< figure src="prettybreaks-axes.png" >}}

Looking through the next few answers gave a hint as to what I needed to do.
I needed to pass a function, to the `breaks` argument that takes a vector of values to make the axes for and a number indicating the number of ticks.
I decided to take a look at what `pretty_breaks()` does and see if I could augment that.

```r
scales::pretty_breaks
#> function (n = 5, ...) #> {#>   force_all(n, ...)#>   function(x) {#>     breaks <- pretty(x, n, ...)#>     names(breaks) <- attr(breaks, "labels")#>     breaks#>   }#> }#> <bytecode: 0x7ff8a81061d8>#> <environment: namespace:scales>
```

It was such a simple function that I was pretty quickly able to see how I could make it only return integer values.
Therefore, I created `integer_breaks()`.

```r
# A function factory for getting integer y-axis values.
integer_breaks <- function(n = 5, ...) {
  fxn <- function(x) {
    breaks <- floor(pretty(x, n, ...))
    names(breaks) <- attr(breaks, "labels")
    breaks
  }
  return(fxn)
}
```

And here is an example of it being used in practice.

```r
iris %>% 
  ggplot(aes(x = Petal.Width, y = Sepal.Width)) +
  geom_point(aes(color = Species)) +
  scale_y_continuous(breaks = integer_breaks()) +
  theme_bw()
```
{{< figure src="integer-axes.png" >}}

As a quick comparison, I used ['cowplot'](https://cran.r-project.org/web/packages/cowplot/index.html) to show the same plot with and without the integer axes.

{{< figure src="cowplot_plot.png" >}}

---

The code to generate all of the above plots is linked at the top. 
I also created a [Gist](https://gist.github.com/jhrcook/eb7b63cc57c683a6eb4986c4107a88ec) on GitHub with the `integer_breaks()` function.
