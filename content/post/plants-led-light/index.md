---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Cutstom Plant LED Lights"
subtitle: ""
summary: "A LED lighting set-up for my indoors plants"
authors: ["admin"]
tags: ["hobby", "plants", "cacti", "succulents", "electronics", "Arduino"]
categories: []
date: 2019-08-14T10:42:06-04:00
lastmod: 2019-08-14T10:42:06-04:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: "Center"
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []

links:
 - name: Source
   url: https://github.com/jhrcook/led_growlights_controller
   icon_pack: fab
   icon: github

 - name: Wiring Schematic
   url: lighting_schematic.fzz
   icon_pack: fas
   icon: dove


---

{{< figure src="images/IMG_8445.JPG" title="" lightbox="true" >}}




Due to the drastic differences between the natural environment of lithops and Boston, I have to grow the plants indoors and under artificial light. Below is to documentation of how I built my set up. The lights are setup and running, though I am still in the process of assembling the hanging mechanism.

## Materials

**Lighting**

* [Cree XLamp XP-G2 High Power LED Star](https://www.ledsupply.com/leds/cree-xlamp-xpg2-high-power-led) x 6
* [Mean Well APC-25-1050 CC LED driver](https://www.ledsupply.com/led-drivers/mean-well-apc-constant-current-led-driver) x 1
* [MakersHEATSINK SLIM](https://www.ledsupply.com/led-heatsinks/makersheatsink-slim) x 1
* [Arctic Silver Thermal Paste](https://www.amazon.com/gp/product/B0087X728K/ref=ox_sc_act_title_1?smid=AUVJO2CJIN6KY&psc=1) x 1
* [20 AWG wire](https://www.ledsupply.com/accessories/awg-stranded-wire)
* [electrical tape](https://www.amazon.com/gp/product/B001B19JLS/ref=ox_sc_act_title_3?smid=ATVPDKIKX0DER&psc=1)
* [barrel connectors](https://www.amazon.com/gp/product/B01E9SWZEM/ref=ox_sc_act_title_1?smid=A3QVW3NC44QWSK&psc=1)
* miscellaneous power cable

**Controller**

* [Arduino Uno Rev3](https://store.arduino.cc/usa/arduino-uno-rev3)
* [DS3231 Real Time Clock module (with separate battery)](https://learn.adafruit.com/adafruit-ds3231-precision-rtc-breakout/overview)
* [4-channel relay module](https://www.amazon.com/JBtek-Channel-Module-Arduino-Raspberry/dp/B00KTEN3TM/ref=sr_1_3?s=electronics&ie=UTF8&qid=1549852651&sr=1-3&keywords=4+channel+relay)
* [DS18B20 water-proof temperature sensor](https://www.adafruit.com/product/381?gclid=Cj0KCQiAtP_iBRDGARIsAEWJA8gnjaDDMvyFB49-ovRTHASqT-mh_DW6y0mJw7bwMVawazBzAA523qsaAoWJEALw_wcB)
* [128x64 OLED monochrome display](https://www.adafruit.com/product/938)
* push button
* [Arduino proto-shield](Arduino proto-shield)

NB. Some of these pieces, especially for the controller, are available for cheap on Amazon and eBay. *However, the quality of these components is likely lesser than from the sources linked above.*

## Assembling the LEDs

{{% alert warning %}}
CAUTION: This project requires the use of high-powered electricity and should not be attempted unless you know what you are doing. I am not liable for any injuries suffered by those using the information I provide below for their own projects.
{{% /alert %}}

The wiring was actually fairly straight-forward. I have a bit of experience with soldering and electrics, but have no official training, still I did not have too much trouble. I began by getting the LEDs on to the heatsink. The heatsink I used has grooves where I can slide a bolt and nut along to clasp the LEDs in place. This saved me from having to drill any holes and is flexible for future changes should I want to add any more LEDs. Fig. 1 shows a side shot of the attachment system. I added a generous amount of thermal paste between the LEDs and the heatsink to aid in conduction of heat away from the LEDs (Fig. 2). I don’t know how much I applied, but there was always some squeezed out the sides when I tightened the LED down. I assume this means I added enough.

{{< figure src="images/IMG_8200_markup.png" title="Figure 1. The attachment of the LEDs to the heatsink made use of the grooves of the heatsink. A bolt, nut, and nylon washer clasped the LED in place." lightbox="true" >}}

{{< figure src="images/IMG_8202_markup.png" title="Figure 2. A glob of thermal paste was applied to the heatsink before attaching the LEDs. The clasping mechanism was slid down the grooves (see Fig 1)." lightbox="true" >}}

I distributed the LEDs equally over the heatsink. Once they were all in place, I pre-tinned the connections I was going to use on each star and the wires to connect them. Finally, I soldered the wires to the stars to fully connect the LEDs together in series (ie. in one line). The LEDs were all connected + to –. This is important because a diode (the “d” in LED) only allows for the flow of electricity in one direction. If even one LED is mis-wired, none will turn on. To the first and last LED, I added a long length of wire to be connected to the LED driver. To aid me in disassembling the system in the future, I wired the driver to the LEDs through a barrel connector (Fig. 3). Thus, I can detach the heatsink from the rest of the electrics to make the system more mobile in general. For this connection, the V+ of the driver’s DC out goes to the remaining + LED. The V– of the driver’s DC out attaches to the remaining – connection of the LEDs.

{{< figure src="images/IMG_8223_markup.png" title="Figure 3. The barrel connection from the LEDs to the LED driver. This connection is + to + and – to –." lightbox="true" >}}

The last step was to wire the driver to the wall outlet. I used a cable I found at my work on a piece of equipment that was being thrown-out. Its a thick cable and took quite a bit of effort to cut and strip the wires. There are three wires inside, green, white, and black. The green in ground, white AC Neutral (ACN), and the black is AC Live (ACL). I cut off the remaining green wire as the driver does not have (nor need) a ground. I wired the white wire from the wall to the blue (ACN) wire of the driver. I decided to use the ACL connection for controlling the lights with the relay switch. Therefore, I screwed the black wire from the wall into the middle “Common” terminal of the relay switch. The blue wire was then screwed into the “Normally Open” (NO) terminal. I used the normal open so that the connection is broken (ie. the lights are off) when no powered is supplied. This will ensure that the default state is off, a good safety measure. See Fig. 4. for a better look at the relay.

That’s it. The LEDs were wired and read to be connected to the controller in the next section.

{{< figure src="images/IMG_8224_markup.png" title="Figure 4. A close-up of the relay switch. Either wire could have gone into the Common and the other into the NO terminal. NC stands for “Normally Closed” which would have the connection On by default." lightbox="true" >}}

## Controller

The controller of the LEDs is based on an Arduino. I have attached the code here and will eventually upload it to my GitHub. It’s a very simple script that reads the time from the Real Time Clock (RTC) module and turns the lights on through the relay switch. I added an “over-ride” button that allows me to switch the lights On or Off manually at any time. Here is a link to setting up the [RTC by Adafruit](https://learn.adafruit.com/adafruit-ds3231-precision-rtc-breakout/overview) (a great resource for learning about Arduino and other electronics). Once the time has been set once, it will maintain the correct time even if disconnected from power because it has its own battery to keep the crystal vibrating. 

Fig. 5 shows the schematic of my wiring, and Fig. 6 shows the actual bird’s-nest. The schematic is fairly true to the real wiring except I used a lower wattage resistor in my wiring and a few of the wires are not the correct color to aid in readability. The RTC connects to the Arduino via I2C, a communication protocol. Thankfully, using the RTClib library in Arduino means I don’t have to do any explicit communication over I2C.

The [Fritzing](http://fritzing.org/home/) schematic is available for download at the link at the top.

{{< figure src="images/lighting_schematic_v1.png" title="Figure 5. Schematic of the wiring of the controller for the lights." lightbox="true" >}}

{{< figure src="images/IMG_8221_markup.png" title="Figure 6. An image of the actual wiring.It’s a bit of a mess." lightbox="true" >}}

**Update**

Since taking and posting these photos, I swapped the 8-channel relay for a 4-channel to save space. Also, to make the wiring more compact, I moved all of the components on the breadboard to a proto-shield that fits comfortably on top of the Arduino. The actual wiring connections have remained the same (except I had to access the I2C SDA and SCL connections via analog pins A4 and A5, instead of the designated pins along the digital pin side). I will soon move this more compact system into a project box. I have also added a temperature sensor and a small OLED screen to print the temperature.

I create a GitHub repo for the Arduino code, containing explainations of the controller code and custom `GrowLight` class, linked at the top.

## Light Stand

Until I was able to source the parts, I had the heatsink perched on the edges of a tub I had laying about. Obviously, though, this was not to be a permanent solution. Yesterday, I was finally able (willing) to walk to Home Depot and get the PVC pipe that my local hardware store was missing. The overall idea was to build a frame out of PVC and hang the heatsink from it. The point behind using a hanging mechanism is that allows for easy and fine-grained adjustments to the height of the fixture.

The hanging mechanism is composed of picture frame hangers and wire cord. I attached the picture frame hangers to the back of the heatsink using the nuts and bolts that came with the kit so I knew they would fit perfectly in the grooves (Fig. 7). I made four attachment points and cut two lengths of cord. I fixed each cord to one of the hangers, threaded the two open ends through the two remaining hangers, and tied the loose ends together (Fig 8.). This will leave me with an each way to contract/release the wire to move the lights up/down. Finally, the cords were draped over the PVC frame cross-bar (Fig 9.) I won’t go through the details of the frame, since it is a very simple arrangement, and there are plenty of ways to accomplish the same effect.

{{< figure src="images/IMG_8251 copy.JPG" title="Figure 7. A picture frame wall hanger was attached to the heatsink using the built-in grooves and the included nut and bolt. A washer was placed between the heatsink and hanger and between the hanger and bolt." lightbox="true" >}}

{{< figure src="images/IMG_8254 copy.JPG" title="Figure 8. Four attachment points and two wires tied together to make up the hanging assembly." lightbox="true" >}}

{{< figure src="images/IMG_8255.JPG" title="Figure 9. The entire setup with the heatsink hanging on a PVC frame. (LED lights are off.)" lightbox="true" >}}

{{< figure src="images/IMG_8257.JPG" title="Figure 10. The entire setup with the heatsink hanging on a PVC frame. (LED lights are on.)" lightbox="true" >}}

