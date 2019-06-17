# MIDS_w200_python_oop_project
Object Oriented Programming Project for W200 Python Fundamentals

# WAH!-Gyu Farm Game

## 1. Introduction and Installation
This project is a simple text-based game using Python and object oriented programming.  The [final report](w200_project1_Final_writeup-Kuangwei.pdf) provides the details of the various classes and methods used to build the game, and the [design document](w200_project1_Design_doc-Kuangwei.pdf) shows the initial design prior to coding.  A screenshot of the game can be found [below](#sample-screenshot).

Download and run the program `wahgyu_farm.py`, and follow the in game instructions.  Should there be issues rendering UTF-8 characters particularly those denoting the music note “♫” (\u266b), run the program `wahgyu_farm_non_utf.py` instead. 

If you have Python 3.6 installed, this would be simply opening cmd, navigating to the directory with the downloaded `wahgyu_farm.py` file and entering `python wahgyu_farm.py`.

## 2. Game Premise

You are a new hire at a farm whereby you are in charge to care for a number of special genetically engineered, low-carbon footprint, ultra-sustainable cows.  These cows consume very little food, have minimal biological waste and produce extremely desirable high-grade marbled beef.

These cows are called WAH!-Gyu, and are true a marvel for sustainable meat production! The only drawback is that WAH!-Gyu’s have a very special low calorie diet of only a bucket of craft trappist beer a day, and have fickle moods.  These special cows would only produce their superior marbling when they have enough calories and are kept sufficiently happy.  While WAH-Gyu’s benefit from a good diet of beer, they have a 50% chance of getting emotionally depressed when they have had 2 beers, and need constant massaging and new indie folk tunes to keep them happy.

## 3. Rules for the game

1.	Depending on difficulty selected the number of cows would range from 2 to 4 cows.
2.	Each game starts with cows at a calorie rating and a mood rating depending on number of cows.
3.	All cows start with a marbling rating of 0.
4.	Each cow loses one calorie (-1) and one mood point (-1) at the start of each successive turn.
5.	As long as a cow’s calorie and mood are both above 1, the cow gains a marbling point (+1); if either calorie or mood rating reaches zero, the cow loses a marbling point (-1).
6.	If a cow’s calorie rating is more than 6, the cow has a 50% chance to be depressed (mood -2)
7.	There are 10 turns in a game and the player can do only 1 action per turn:
	a.	Feed a cow a bucket of beer (+6 calorie), -1 beer stock
	b.	Massage a cow (+5 mood)
	c.	Play music (randomly +1, +2 or +3 mood to all cows, they have different music tastes), -1 tunes stock
	d.	Go to the abbey and get some trappist beer (+5 beer buckets)
	e.	Go to iTunes and buy a bunch of indie songs (+5 songs)
8.	At the end of 10 turns, your dear WAH!-Gyu cows will be sent for slaughter and you will get scored by the owner of the farm, based on the sum of the marbling of all the cows under your charge.""")

## 4. Sample Screenshot
![screenshot_1](screenshot_1.png?raw=true "Wah!-Gyu in game screenshot")
