+++
# Slider widget.
widget = "slider"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 5  # Order that this section will appear.

# Slide interval.
# Use `false` to disable animation or enter a time in ms, e.g. `5000` (5s).
interval = 5000

# Slide height (optional).
# E.g. `500px` for 500 pixels or `calc(100vh - 70px)` for full screen.
height = "300px"

# Slides.
# Duplicate an `[[item]]` block to add more slides.
[[item]]
  title = "Open Source"
  content = "I contribute to open source projects."
  align = "center"  # Choose `center`, `left`, or `right`.

  # Overlay a color or image (optional).
  #   Deactivate an option by commenting out the line, prefixing it with `#`.
  overlay_color = ""  # An HTML color value.
  overlay_img = "Open-Source-Word-Cloud.jpg"  # Image path relative to your `static/img/` folder.
  overlay_filter = 0.5  # Darken the image. Value in range 0-1.

  # Call to action button (optional).
  #   Activate the button by specifying a URL and button label below.
  #   Deactivate by commenting out parameters, prefixing lines with `#`.
  cta_label = "GitHub"
  cta_url = "https://github.com/jhrcook"
  cta_icon_pack = "fab"
  cta_icon = "github-alt"

[[item]]
  title = "Haigis Lab"
  content = "Curing *KRAS* driven cancers."
  align = "center"

  overlay_color = ""  # An HTML color value.
  overlay_img = "haigis_lab_1.jpg"  # Image path relative to your `static/img/` folder.
  overlay_filter = 0.2  # Darken the image. Value in range 0-1.
  
  cta_label = "lab website"
  cta_url = "https://www.haigislab.org"
  cta_icon_pack = "fas"
  cta_icon = "dna"

[[item]]
  title = "Park Lab"
  content = "Computational methods to understanding cancer biology."
  align = "center"

  overlay_color = ""  # An HTML color value.
  overlay_img = "isidro_figure.png"  # Image path relative to your `static/img/` folder.
  overlay_filter = 0.5  # Darken the image. Value in range 0-1.
  
  cta_label = "lab website"
  cta_url = "https://compbio.hms.harvard.edu/index"
  cta_icon_pack = "fas"
  cta_icon = "laptop-code"
+++
