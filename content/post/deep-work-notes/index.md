---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Notes on 'Deep Work'"
subtitle: "My notes on the book *Deep Work* by Cal Newport about how to maximize productivity and success on meaningful work."
summary: "My notes on the book *Deep Work* by Cal Newport about how to maximize productivity and success on meaningful work."
authors: []
tags: ["Deep Work", "productivity", "Newport", "notes"]
categories: [Productivity]
date: 2021-09-18T09:08:45-04:00
lastmod: 2021-09-18T09:08:45-04:00
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
---

I have finally read the book [*Deep Work*](https://www.calnewport.com/books/deep-work/) where he describes the reasons and methods for focussing on maximizing "deep" work over "shallow" work. 
From the popularity of this book and my own experience with some of the strategies explained in the book, I believe it is worthwhile to experiment with Newport's proposed system. 
To this end, I have compiled abbreviated notes of the book here with a focus on the methods, only mentioning the reasoning if it is critical for implementation. 
I have appended implementation notes for myself at the end of the post.

---

[**Definitions**](#definitions) - keey terms and ideas <br>
[**Part I. The Idea**](#part-i-the-idea) - why care about deep work <br>
[**Part II. The Rules**](#part-ii-the-rules) - how to do deep work <br>
[**Personal Implementation Notes**](#personal-implementation-notes) - my personal notes on how accomplish deep work <br>

---

## Definitions

> **deep work**: Professional activities performed in a state of distraction-free concentration that push your cognitive capabilities to their limit.
> These effects create new value, improve your skill, and are hard to replicate (pg. 3).

> **shallow work**: Noncognitively demanding, ogistical-style tasks, often performed while distracted.
> These efforts tend to not create much new value in the world and are easy to replicate (pg. 6).

> **deliberate practice**: Deliberate effort to improve performance in a specific domain (pg. 34).

> **attention residue**: When switching between tasks, it takes time for our brains to fully switch attention to the new task.
> Instead, our brain keeps thinking about the first task (pg. 42).

> **metric black hole**: Metrics about the "bottom-line impact of depth-destroying behaviors... fall into an opaque region resistant to easy measurement," (pg. 55). An example is the amount of time spent on emails by employees.

> **principle of least resistance**: In a business setting, without clear feedback on the impact of various behaviors to the bottom line, we will tend toward behaviors that are easiest in the moment (pg. 58). An example is setting up regular meetings.

## Part I. The Idea

### Ch 1. Deep Work is Valuable

- Two core abilities for thriving in the new economy (pg. 29):
  1. The ability to quickly master hard things.
  2. The ability to produce at an elite level, in terms of both quality and speed.
- deep work is *required* to to achieve these core abilities
- **deliberate practice** requires (pg. 35):
  1. your attention is focussed tichtly on a specific skill you're trying to improve or an idea you're trying to master
  2. you recieve feedback so you can correct your approach to keep your attention exactly where it's most productive
- $\text{high-quality work produced} = \text{time spent} \times \text{intensity of focus}$

### Ch 2. Deep Work is Rare

- many businesses prioritize shallow work instead of deep work (pg. 51)
	- such as open floor plans, instant messaging, encouraging social media prescence
- *culture of connectivity*: expected to promptly read and respond to emails, messages, etc.(pg. 56)
- business as a proxy for productivity (pg. 64)
	- occurs without a clear measure of true productivity
	- often an attempt to publically appear productive
- trendy to have an automatic proclivity for all things "Internet" (pg. 68)
	- "idolize these digital doodads asa signifier of progress"

### Ch 3. Deep Work is Meaningful

- we inately derive greater meaning and purpose from deep work

## Part II. The Rules

### Rule 1. Work Deeply

- develop *routines* and *rituals* to your working like designed to minimize the willpower necessary to transition into and maintain a state of unbroken concentration (pg. 100)

#### Strategy 1. Decide on your depth philosophy

- Four philosophies of deep work:
	1. **monastic**: maximize deep efforts by *eliminating or radically minimizing* shallow obligations (pg. 103)
		- tend to have a well-defined and highly valued professional goal
	2. **bimodal**: divide your time, dedicating some clearly defined stretches to deep pursuits and leaving the rest open to everything else (pg. 106)
		- during the deep time, act monastically, but during shallow time, such focus is not prioritized
		- different time-scales; can be a split of days in a week, or a year into months
		- for those who admire the productivity of monastics but also respect the value from their shallow behaviors
	3. **rythmic**: consistently start deep work sessions at a set time and make it a regular habit (pg. 110)
		- can help to have visual indicator of accomlishing deep work each day (called the "chain method")
		- trade-off in level of depth compared to bimodal philosophy, but likely more practical for most people
	4. **journalistic**: fit deep work wherever you can into your schedule (pg. 115)
		- often best for deadline-driven professions
		- difficult to do

#### Strategy 2. Ritualize

- build rituals with a high-level of strictness and idiosyncransy to reduce friction to transition to depth (pg. 119)
- address the following components (pg. 119):
	- *where you'll work and for how long* (ideally have a special spot for deep work)
	- *how you'll work once you start to work*; rules and processes to keep your efforts structured
	- *how you'll support your work*; coffee, food, walks, etc.
- will require some experimentation

#### Strategy 3. Make grand gestures

- adding a radical change to your normal environment can increase your precieved importance of the task (pg. 122)
	- often requires a significant investment of effort or money

#### Strategy 4. Don't work alone

- expose yourself to ideas from others on a regular basis, but maintain a place and time for isolated deep work (pg. 132)
	- "hub-and-spoke" model as a combination of soundproofed offices connected to large common areas (pg. 131)
- can have collabariative forms of deep learning when working on a shared problem with another person (pg. 133)

#### Strategy 5. Execute like a business

- the 4 disciplines of execution (i.e. *how* to do deep work; pg. 136)
	1. *focus on the wildly important*; execution should be aimed at a small number of goals (pg. 136)
	2. *act on the lead measures*; measure the new bahviors that will drive success; *time spent in a state of deep work*
	3. *keep a compelling scoreboard*; physical marker of numbers of deep work hours
	4. *create a cadence of accountability*; weekly meetings to review scoreboard and what did/didn't work from week before
- more difficult to execute than strategize

#### Strategy 6. Be lazy

- at the end of the workday, shut down your consideration of work issues until the next morning (pg. 144)
	- can extend the workday if needed, but make sure to fully finish at some point
- reasons (pg. 144):
	- aids in insight from unconcious thoughts of brain (pg. 145)
	- helps recharge the energy needed to work deeply later (specifically walks through nature) (pg. 146)
	- we have a limited capacity for deep work and should hit the limit during the workday (pg. 150)
- make a *shutdown ritual* to finish the day (pg. 151)
	- for an incomplete, need to have a plan for its completion and record it in a standard place to be revisted later
	- have a phrase you say when done for the day (e.g. "Shutdown complete.")

### Rule 2. Embrace Boredom

HEREHEREHERHEREHREHREREHREREHREREHREREHRERE

### Rule 3. Quit Social Meda

### Rule 4. Drain the Shallows

---

## Personal Implementation Notes

- I should use the *rythmic* philosophy of deep work with less frequent ventures into the *bimodal* philosophy.
- Need to implement some rules for the different types of deep work I do (e.g. different rules when trying to code vs trying to read papers or reading online articles).
- Figure out a few good places to do work (Boston Public Library, etc.) as a ritual and grand gesture.
- Implement the 4DX principles:
	1. Write down all goals and select few for each deep work session.
	2. Decide on lead measures and make a system of record keeping.
	3. Create a "scoreboard" for tallying number of deep work hours per day.
- Need a shutdown ritual.
	- to-do: check email, check Slack, check notes, check GitHub, record incomplete tasks, look ahead on calendar
	- Newport's example on page 152
- Have a central location where all larger projects are listed.

### Other books

1. *The Shallows* by Nicholas Carr
2. *Hamlet's BlackBerry* by William Powers
3. *The Tyranny of E-mail* by John Freeman
4. *The Distraction Addiction* by Alex Soojung-Kin Pang
5. *Getting Things Done* by David Allen

- look into [the "time-block" planner](https://www.timeblockplanner.com)
