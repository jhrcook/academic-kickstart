
library(cowplot)
library(tidyverse)

theme_bw <- function() {
    ggplot2::theme_bw(base_family = "Arial")
}



# A function factory for getting integer y-axis values.
integer_breaks <- function(n = 5, ...) {
    fxn <- function(x) {
        breaks <- floor(pretty(x, n, ...))
        names(breaks) <- attr(breaks, "labels")
        breaks
    }
    return(fxn)
}


iris %>% 
    ggplot(aes(x = Petal.Width, y = Sepal.Width)) +
    geom_point(aes(color = Species)) +
    scale_y_continuous(breaks = scales::pretty_breaks()) +
    theme_bw()
ggsave("prettybreaks-axes.svg", width = 7, height = 5)

iris %>% 
    ggplot(aes(x = Petal.Width, y = Sepal.Width)) +
    geom_point(aes(color = Species)) +
    theme_bw()
ggsave("noninteger-axes.svg", width = 7, height = 5)


iris %>% 
    ggplot(aes(x = Petal.Width, y = Sepal.Width)) +
    geom_point(aes(color = Species)) +
    scale_y_continuous(breaks = integer_breaks()) +
    theme_bw()
ggsave("integer-axes.svg", width = 7, height = 5)

featured_image <-iris %>% 
    ggplot(aes(x = Petal.Width, y = Sepal.Width)) +
    geom_point(aes(color = Species)) +
    scale_y_continuous(breaks = integer_breaks()) +
    theme_bw() +
    theme(legend.position = "none")
ggsave("featured.png", featured_image, width = 4, height = 4)

p1 <- iris %>% 
    ggplot(aes(x = Petal.Width, y = Sepal.Width)) +
    geom_point(aes(color = Species)) +
    theme_bw() +
    theme(
        legend.position = "none",
        plot.title = element_text(hjust = 0.5)
    ) +
    labs(title = "Not integer y-axis")
p2 <- iris %>% 
    ggplot(aes(x = Petal.Width, y = Sepal.Width)) +
    geom_point(aes(color = Species)) +
    scale_y_continuous(breaks = integer_breaks()) +
    theme_bw() +
    theme(
        legend.position = "none",
        plot.title = element_text(hjust = 0.5)
    ) +
    labs(title = "Integer y-axis")
cowplot_plot <- cowplot::plot_grid(p1, p2, nrow = 1, align = "h")
ggsave("cowplot_plot.svg", cowplot_plot, width = 7, height = 4)

