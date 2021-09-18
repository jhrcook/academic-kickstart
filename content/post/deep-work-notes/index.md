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

[**Definitions**](#definitions) - key terms and ideas <br>
[**Part I. The Idea**](#part-i-the-idea) - why care about deep work <br>
[**Part II. The Rules**](#part-ii-the-rules) - how to do deep work <br>
[**Personal Implementation Notes**](#personal-implementation-notes) - my personal notes on how accomplish deep work <br>

---

## Definitions

> **deep work**: Professional activities performed in a state of distraction-free concentration that push your cognitive capabilities to their limit.
> These effects create new value, improve your skill, and are hard to replicate (pg. 3).

> **shallow work**: Non-cognitively demanding, logistical-style tasks, often performed while distracted.
> These efforts tend to not create much new value in the world and are easy to replicate (pg. 6).

> **deliberate practice**: Deliberate effort to improve performance in a specific domain (pg. 34).

> **attention residue**: When switching between tasks, it takes time for our brains to fully switch attention to the new task.
> Instead, our brain keeps thinking about the first task (pg. 42).

> **metric black hole**: Metrics about the "bottom-line impact of depth-destroying behaviors... fall into an opaque region resistant to easy measurement," (pg. 55). An example is the amount of time spent on emails by employees.

> **principle of least resistance**: In a business setting, without clear feedback on the impact of various behaviors to the bottom line, we will tend toward behaviors that are easiest in the moment (pg. 58). An example is setting up regular meetings.

> **the any-benefit approach to network tool selection**: You're justified in using a network tool if you can identify *any* possible effect to its use, or *anything* you might possibly miss out on if you don't use it (pg. 186).

> **the craftsman approach to tool selection**: Identify the core factors that determine success and happiness in your professional and personal like. Adopt a tool only if its positive impacts on these factors substantially outweigh its negative impacts (pg. 191).

> **fixed-schedule productivity**: Fix the firm foal of not working past a certain time, then work backward to find the productivity strategies that allow me to satisfy this declaration (pg. 236).
## Part I. The Idea

### Ch 1. Deep Work is Valuable

- Two core abilities for thriving in the new economy (pg. 29):
  1. The ability to quickly master hard things.
  2. The ability to produce at an elite level, in terms of both quality and speed.
- deep work is *required* to to achieve these core abilities
- **deliberate practice** requires (pg. 35):
  1. your attention is focussed tightly on a specific skill you're trying to improve or an idea you're trying to master
  2. you receive feedback so you can correct your approach to keep your attention exactly where it's most productive
- $\text{high-quality work produced} = \text{time spent} \times \text{intensity of focus}$

### Ch 2. Deep Work is Rare

- many businesses prioritize shallow work instead of deep work (pg. 51)
	- such as open floor plans, instant messaging, encouraging social media presence
- *culture of connectivity*: expected to promptly read and respond to emails, messages, etc.(pg. 56)
- business as a proxy for productivity (pg. 64)
	- occurs without a clear measure of true productivity
	- often an attempt to publicly appear productive
- trendy to have an automatic proclivity for all things "Internet" (pg. 68)
	- "idolize these digital doodads asa signifier of progress"

### Ch 3. Deep Work is Meaningful

- we innately derive greater meaning and purpose from deep work

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
	3. **rhythmic**: consistently start deep work sessions at a set time and make it a regular habit (pg. 110)
		- can help to have visual indicator of accomplishing deep work each day (called the "chain method")
		- trade-off in level of depth compared to bimodal philosophy, but likely more practical for most people
	4. **journalistic**: fit deep work wherever you can into your schedule (pg. 115)
		- often best for deadline-driven professions
		- difficult to do

#### Strategy 2. Ritualize

- build rituals with a high-level of strictness and idiosyncrasy to reduce friction to transition to depth (pg. 119)
- address the following components (pg. 119):
	- *where you'll work and for how long* (ideally have a special spot for deep work)
	- *how you'll work once you start to work*; rules and processes to keep your efforts structured
	- *how you'll support your work*; coffee, food, walks, etc.
- will require some experimentation

#### Strategy 3. Make grand gestures

- adding a radical change to your normal environment can increase your perceived importance of the task (pg. 122)
	- often requires a significant investment of effort or money

#### Strategy 4. Don't work alone

- expose yourself to ideas from others on a regular basis, but maintain a place and time for isolated deep work (pg. 132)
	- "hub-and-spoke" model as a combination of soundproofed offices connected to large common areas (pg. 131)
- can have collaborative forms of deep learning when working on a shared problem with another person (pg. 133)

#### Strategy 5. Execute like a business

- the 4 disciplines of execution (i.e. *how* to do deep work; pg. 136)
	1. *focus on the wildly important*; execution should be aimed at a small number of goals (pg. 136)
	2. *act on the lead measures*; measure the new behaviors that will drive success; *time spent in a state of deep work*
	3. *keep a compelling scoreboard*; physical marker of numbers of deep work hours
	4. *create a cadence of accountability*; weekly meetings to review scoreboard and what did/didn't work from week before
- more difficult to execute than strategize

#### Strategy 6. Be lazy

- at the end of the workday, shut down your consideration of work issues until the next morning (pg. 144)
	- can extend the workday if needed, but make sure to fully finish at some point
- reasons (pg. 144):
	- aids in insight from unconscious thoughts of brain (pg. 145)
	- helps recharge the energy needed to work deeply later (specifically walks through nature) (pg. 146)
	- we have a limited capacity for deep work and should hit the limit during the workday (pg. 150)
- make a *shutdown ritual* to finish the day (pg. 151)
	- for an incomplete, need to have a plan for its completion and record it in a standard place to be revisited later
	- have a phrase you say when done for the day (e.g. "Shutdown complete.")

### Rule 2. Embrace Boredom

- the ability to concentrate intensely is a skill that must be trained
	- goals: improve ability to concentrate and overcome the desire for distraction

#### Strategy 1. Don't take breaks from distraction, instead take breaks from focus

- schedule in advance when you'll allow a distraction and avoid it at all times outside of then (pg. 159)

#### Strategy 2. Work like Teddy Roosevelt

- work on the task at hand exclusively and with *high intensity* ("Roosevelt dash")
	- "incompatible with distraction"
- impose a deadline to force the intensity

#### Strategy 3. Meditate productively

- during periods of physical activity, but mental inactivity, focus your attention on a single well-defined professional problem
	- goal is to improve your ability to think deeply, though will also likely see direct productivity improvements
- two common issues:
	- be wary of distractions (mind wandering) and looping (thinking about a solved problem over and over)
	- structure your deep thinking
		- recommends first listing all variables related to the problem and them working one step at a time towards a solution

#### Strategy 4. Memorize a deck of cards

- recommends memory training; deck of cards is a good place to start

### Rule 3. Quit Social Media

- social media services are tools and can be used for good or bad
- important to measure the pros and cons of using the services (avoid the "any-benefit" fallacy and use the "craftsman's approach")
	- these services are meant to be addictive and can be time- and attention-robbing
- how to choose network services:
	1. identify the your main high-level goals, personally and professionally
	2. list 2-3 important activities to help satisfy the goal
	3. for each service, identify to what extent the service helps you participate in the activity
	4. decide if the positives substantially outweigh the negatives
- use the 80-20 rule: 80% of an effect is due to 20% of the possible causes (pg. 201)
- try not using a service for 30 days and see if, at the end, anyone noticed you were gone or if not using it had a negative impact on you (pg. 204)
- "Put more though into your leisure time," (pg. 212)
	- do not fall to lowest common denominator of entertainment
	- figure out what you'll do in your free time beforehand (pg. 213)


### Rule 4. Drain the Shallows

- strategies to identify the shallowness in your current schedule, then cull it down to minimum levels
	- goal is not to remove *all* shallow work - some is necessary

#### Strategy 1. Schedule every minute of your day

- if not managed properly, we often do not give much thought to what we do with our time (pg. 222)
- get the habit of asking, "What makes the most sense right now?" before acting (pg. 222)
- method: at the beginning of each workday, schedule activities in blocks covering the entire day (minimum 30 minutes) (pg. 223)
	- can batch smaller tasks into "task blocks" and add the specific tasks as comments/notes
	- *if the schedule is disrupted, just adjust the schedule - goal is not to stick to a set schedule, but to control what you spend your time on* (pg. 224)
- tips:
	- will likely underestimate the time required for activities, but will get better over time (pg. 224)
	- use "overflow conditional" blocks where you can continue working on the previous activity if needed, or have another option if not (pg. 225)
	- be liberal with task blocks to handle unexpectedly long tasks or new ones that pop up (pg. 225)

#### Strategy 2. Quantify the depth of every activity

- metric: *How long would it take (in months) to train a smart recent college graduate with no specialized training in my field to complete this task?* (pg. 229)

#### Strategy 3. Ask your boss for a shallow work budget

- "What percentage of my time should be spent on shallow work?"
	- for non-entry-level jobs, 30-50% is normal (no more than 50%, though)
	- change behavior to achieve this goal

#### Strategy 4. Finish your work by five thirty

- use *fixed-schedule productivity* to cap the amount of shallow work and protect the deep work (pg. 240)
	- forces you to be conscientious about managing your time
- be careful to agree to new task that will add shallow work (default to "no")
	- a tactic for a good refusal: be clear in the refusal, but ambiguous in the explanation for the refusal (pg. 239)

#### Strategy 5. Become hard to reach

1. Make people who send you e-mail do more work by adding a few obstacles or other options (pg. 243)
2. Do more work when you send or reply to emails by directly addressing the goal of the communication of taking steps to successfully completing it (pg. 248)
	- called "process-centric approach to email"
	- do not get stuck in back-and-forth
3. Don't respond to all emails; it's the sender's responsibility to convince the receiver that a reply is worthwhile
	- *Professorial E-mail Sorting*: do not reply to an email if any of the following applies:
		- it's ambiguous or hard to generate a reasonable response
		- it's uninteresting
		- nothing really good would happen if you did respond and nothing bad would happen if you didn't
---

## Personal Implementation Notes

- I should use the *rhythmic* philosophy of deep work with less frequent ventures into the *bimodal* philosophy.
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
- Experiment with the Rooseveltian method (described at the bottom of pg. 167).
- Experiment with "productive meditation" - I like letting my mind wander while exercising or focus on the exercise, but this strategy is worth trying; might be best while showering, walking, commuting, etc.
- Put together a list of activities, hobbies, jobs to do in free time and leave in a visible area.
- Not too much to do for social media. Can put a specific time limit and notification rules on specific apps.
- Get in the habit of scheduling the day every morning.
- Score the depth of each activity using the "college grad" test
	- How to integrate this with the scheduling and weekly review?
- Finish working by 5:30 pm.

### Other books

1. *The Shallows* by Nicholas Carr
2. *Hamlet's BlackBerry* by William Powers
3. *The Tyranny of E-mail* by John Freeman
4. *The Distraction Addiction* by Alex Soojung-Kin Pang
5. *Getting Things Done* by David Allen
6. *So Good They Can't Ignore You* by Cal Newport
7. *Digital Minimalism* by Cal Newport
8. *A World Without Email* by Cal Newport

- look into [the "time-block" planner](https://www.timeblockplanner.com)
