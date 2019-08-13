+++
# Slider widget.
widget = "slider"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 68  # Order that this section will appear.

# Slide interval.
# Use `false` to disable animation or enter a time in ms, e.g. `5000` (5s).
interval = 5000

# Slide height (optional).
# E.g. `500px` for 500 pixels or `calc(100vh - 70px)` for full screen.
height = "300px"

# Slides.
# Duplicate an `[[item]]` block to add more slides.
[[item]]
  title = "My Academic History"
  content = ""
  align = "center"  # Choose `center`, `left`, or `right`.

  # Overlay a color or image (optional).
  #   Deactivate an option by commenting out the line, prefixing it with `#`.
  overlay_color = ""  # An HTML color value.
  overlay_img = "headers/HMS_snow.jpg"  # Image path relative to your `static/img/` folder.
  overlay_filter = 0.5  # Darken the image. Value in range 0-1.

  # Call to action button (optional).
  #   Activate the button by specifying a URL and button label below.
  #   Deactivate by commenting out parameters, prefixing lines with `#`.
  cta_label = "Academia"
  cta_url = "academia/"
  cta_icon_pack = "fas"
  cta_icon = "graduation-cap"

[[item]]
  title = "Leadership"
  content = "*If the highest aim of a captain were to preserve his ship, he would keep it in port for ever.  - Thomas Aquinas*"
  align = "center"

  overlay_color = ""  # An HTML color value.
  overlay_img = "headers/little_league_indians.jpg"  # Image path relative to your `static/img/` folder.
  overlay_filter = 0.2  # Darken the image. Value in range 0-1.
  
  cta_label = "Experiences"
  cta_url = "leadership/"
  cta_icon_pack = ""
  cta_icon = ""

[[item]]
  title = "Research Experience"
  content = "Since high school, I have participated in biological research in several labs on various topics."
  align = "center"

  overlay_color = ""  # An HTML color value.
  overlay_img = "headers/islet_microscopy.jpg"  # Image path relative to your `static/img/` folder.
  overlay_filter = 0.3  # Darken the image. Value in range 0-1.
  
  cta_label = "More information"
  cta_url = "research_experience/"
  cta_icon_pack = ""
  cta_icon = ""
  
[[item]]
  title = "Curriculum Vitae"
  content = ""
  align = "center"

  overlay_color = ""  # An HTML color value.
  overlay_img = "headers/fall_2_crop.jpg"  # Image path relative to your `static/img/` folder.
  overlay_filter = 0.3  # Darken the image. Value in range 0-1.
  
  cta_label = "Download"
  cta_url = "files/cv.pdf"
  cta_icon_pack = "fas"
  cta_icon = "download"

+++
