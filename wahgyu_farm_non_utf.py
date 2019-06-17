#!/bin/bash
## Kuangwei Huang
## w200 Python Project 1
## WAH!-Gyu Farm

class gameplay:

    dict_cows = {"Easy" : 2, "Medium" : 3, "Rare": 4}
    cow_names = ["Betsy", "Malone", "Duke", "Brie"]

    def __init__(self, diff_setting="Easy", dict_cows=dict_cows, cow_names=cow_names):
        self.diff_setting = diff_setting
        self.num_cows = self.dict_cows[self.diff_setting]
        self.cow_names = cow_names[0:self.dict_cows[self.diff_setting]]
        self.num_turns = 0
        self.max_turns = 10
        self.ipod = farm_supply("iPod", 5, "songs", 1, "song", 5)
        self.beer_fridge = farm_supply("Big Beer Fridge", 5, "buckets of beer", 1, "bucket of beer", 5)
        self.player = player(self.diff_setting, self.ipod, self.beer_fridge)
        self.player_action = None
        self.player_cow_choice = None
        self.cows_marbling = []
        self.rank = {2: "'What am I paying your for?'",
                     4: "'Capable Farmhand'",
                     6: "'Deputy Chief of Beef'",
                     8: "'Maestro of Marbling!'"}

    def startup(self):
        self.num_turns = 0
        self.cows_marbling = []
        os.system('clear')
        print("\nDifficulty: {}, Number of Cows: {}".format(self.diff_setting, self.num_cows))
        print("Cows", ', '.join(self.cow_names[:-1]), "and",
              self.cow_names[-1], "are in your care!\n")

        print(self.ipod)
        print(self.beer_fridge)
        print()

        for c in range(self.num_cows):
            self.cow_names[c] = wahgyu(c,self.cow_names[c], self.num_cows)
            print(self.cow_names[c])

        while self.num_turns < self.max_turns:
            self.new_turn()

        self.end_game()

    def new_turn(self):
        self.num_turns += 1
        print("\nTurn No:", self.num_turns)
        # Resets player action and which cow to act on (if relevant) for the new turn
        self.player_action = 0
        self.player_cow_choice = 0
        # Query player for action and which cow to act on (if relevant)
        self.player_action, self.player_cow_choice = self.player.query_action()

        # Enter the game turn
        self.game_turn()

    def game_turn(self):

        # 1. Feed a cow some beer
        if self.player_action == 1:
            self.beer_fridge.reduce_stocks()
            self.cow_names[self.player_cow_choice-1].drink_beer()

        # 2. Give a cow a massage
        elif self.player_action == 2:
            self.cow_names[self.player_cow_choice-1].get_massage()

        # 3. Play some music
        elif self.player_action == 3:
            self.ipod.reduce_stocks()
            for c in range(self.num_cows):
                self.cow_names[c].listen_music()

        # 4. Buy more beer
        elif self.player_action == 4:
            self.beer_fridge.add_stocks()

        # 5. Buy more tunes
        elif self.player_action == 5:
            self.ipod.add_stocks()

        self.end_turn()

    def end_turn(self):

        print(self.ipod)
        print(self.beer_fridge)
        print()

        for c in range(self.num_cows):
            # Reset emotional state if there is no beer drunk this turn
            if self.player_action != 1:
                self.cow_names[c].emotional = ""
            # Reset music ascii art if there is not music played this turn
            if self.player_action != 3:
                self.cow_names[c].reset_music()

            self.cow_names[c].update_status()
            print(self.cow_names[c])

    def end_game(self):
        for c in range(self.num_cows):
            self.cows_marbling.append(self.cow_names[c].marbling)
        print("\nCongratulations on completing the game!")
        print("\nYou have achieved a total {} marbling points for your {} cows!".format(
            sum(self.cows_marbling), self.num_cows))

        rank_index = int(sum([i/self.num_cows for i in self.cows_marbling]))// 2 * 2
        print("\nYour have a rank of:", self.rank[max([x for x in self.rank.keys() if x <= rank_index])])

        menu.enter_to_cont()


class menu:

    diff_options = ["Easy", "Medium", "Rare"]

    def __init__(self, diff_options=diff_options):
        self.diff_setting = diff_options[0]
        pass

    @staticmethod
    def enter_to_cont():
        try:
            press_enter = (input("\nPress Enter to return to Main Menu > "))
        except NameError:
            pass

    def launch(self, diff_options=diff_options):

        self.diff_options = diff_options

        while True:
            os.system('clear')
            print("""\nWah!-Gyu Farm v1.0
            Current Difficulty Setting is at:""", self.diff_setting,"""
            \nPlease select an option below:

            1. Change Difficulty Setting
            2. Start New Game
            3. What is this game about?
            4. Quit\n""")

            menu_select = input("Selection > ")

            # Error handling, to continue looping for input until correct selection is provided
            if menu_select not in "1234" or menu_select == "":
                print("\nPlease select a valid option (1, 2, 3 or 4)")
                self.enter_to_cont()
            elif int(menu_select) == 1:
                while True:
                    print("""Please choose a difficulty setting:
            1. Easy
            2. Medium
            3. Rare (hardest)\n""")

                    diff_select = input("Selection > ")

                    # Error handling, to continue looping for input until correct selection is provided
                    if diff_select not in "123" or diff_select == "":
                        print("\nPlease select a valid option (1, 2 or 3)")
                    else:
                        self.diff_setting = diff_options[int(diff_select)-1]
                        break

            elif int(menu_select) == 3:
                print("""\nGame premise:

You are a new hire at a farm whereby you are in charge to care for a number of special genetically engineered,
low-carbon footprint, ultra-sustainable cows.  These cows consume very little food, have minimal biological waste
and produce extremely desirable high-grade marbled beef.

These cows are called WAH!-Gyu, and are true a marvel for sustainable meat production!
The only drawback is that WAH!-Gyu’s have a very special low calorie diet of only a bucket of craft trappist beer
a day, and have fickle moods.  These special cows would only produce their superior marbling when they have enough
calories and are kept sufficiently happy.  While WAH-Gyu’s benefit from a good diet of beer, they have a 50% chance
of getting emotionally depressed when they have had 2 beers, and need constant massaging and new indie folk tunes
to keep them happy.

Rules for the game:

1.	Depending on difficulty selected the number of cows would range from 2 to 4 cows.
2.	Each game starts with cows at a calorie rating and a mood rating depending on number of cows.
3.	All cows start with a marbling rating of 0.
4.	Each cow loses one calorie (-1) and one mood point (-1) at the start of each successive turn.
5.	As long as a cow’s calorie and mood are both above 1, the cow gains a marbling point (+1);
	if either calorie or mood rating reaches zero, the cow loses a marbling point (-1).
6.	If a cow’s calorie rating is more than 6, the cow has a 50% chance to be depressed (mood -2)
7.	There are 10 turns in a game and the player can do only 1 action per turn:
	a.	Feed a cow a bucket of beer (+6 calorie), -1 beer stock
	b.	Massage a cow (+5 mood)
	c.	Play music (randomly +1, +2 or +3 mood to all cows, they have different music tastes), -1 tunes stock
	d.	Go to the abbey and get some trappist beer (+5 beer buckets)
	e.	Go to iTunes and buy a bunch of indie songs (+5 songs)
8.	At the end of 10 turns, your dear WAH!-Gyu cows will be sent for slaughter and you will get scored
	by the owner of the farm, based on the sum of the marbling of all the cows under your charge.""")

                menu.enter_to_cont()

            elif int(menu_select) == 4:
                exit()

            else:
                g1 = gameplay(self.diff_setting)
                g1.startup()


class player:

    def __init__(self, diff_setting, ipod, beer_fridge):
        self.diff_setting = diff_setting
        self.action_chosen = []
        self.action_verbs = {1 : "feed", 2 : "massage"}
        self.cow_options = {"Easy" : ["12", """
            1. Betsy
            2. Malone"""], "Medium" : ["123", """
            1. Betsy
            2. Malone
            3. Duke"""], "Rare" : ["1234", """
            1. Betsy
            2. Malone
            3. Duke
            4. Brie"""]}
        self.ipod = ipod
        self.beer_fridge = beer_fridge

    def query_action(self):
        # Reset the 2 conditional checks self.action_chosen list,
        # 1st item in self.action_chosen list refers to a valid option,
        # 2nd item is if the option is actionable.
        self.action_chosen = [False, False]
        action_select = 0
        cow_choice = 0

        while not (self.action_chosen[0] and self.action_chosen[1]):
            print("""\nPlease select an action to perform in this turn below:
            1. Feed a cow some beer
            2. Give a cow a massage
            3. Play some music
            4. Buy more beer
            5. Buy more tunes\n""")

            action_select_str = input("Selection > ")

            # Error handling for wrong option selection
            if action_select_str not in "12345" or action_select_str == "":
                print("Please select a valid option (1, 2, 3, 4 or 5)")
                continue
            else:
                action_select = int(action_select_str)
                self.action_chosen[0] = True

            # 1 and 2. Query player which cow to feed or massage

            if self.action_chosen[0] and action_select < 3:
                while cow_choice == 0:
                    print("\nWhich cow do you want to {}?".format(self.action_verbs[action_select]))
                    print(self.cow_options[self.diff_setting][1])
                    cow_choice_str = input("\nSelection > ")

                    # Error handling for wrong cow selection
                    if cow_choice_str not in self.cow_options[self.diff_setting][0] or cow_choice_str == "":
                        print("Please select a valid option ({} or {})".format(
                            ', '.join([i for i in self.cow_options[self.diff_setting][0][0:-1]]),
                            self.cow_options[self.diff_setting][0][-1] ))
                    else:
                        cow_choice = int(cow_choice_str)

                # 1. Check whether there are beer stocks left

                if action_select == 1:
                    print(self.beer_fridge.any_left()[1])
                    self.action_chosen[1] = self.beer_fridge.any_left()[0]

                elif action_select == 2:
                    self.action_chosen[1] = True

            # 3. Check whether there are tunes stocks left

            elif self.action_chosen[0] and action_select == 3:
                print(self.ipod.any_left()[1])
                self.action_chosen[1] = self.ipod.any_left()[0]

            # 4 and 5. Set condtional to be True

            elif self.action_chosen[0] and (action_select == 4
                                            or action_select == 5):
                self.action_chosen[1] = True

        return (action_select, cow_choice)


class wahgyu:

    def __init__(self, index_no=0, cow_name="Allo", num_cows=2):
        self.cow_name = cow_name
        self.cow_index = index_no
        self.calories = num_cows
        self.mood = num_cows
        self.max_calories = 10
        self.min_calories = 0
        self.beer_calories = 6
        self.max_mood = 10
        self.min_mood = 0
        self.depress_mood = -2
        self.massage_mood = 5
        self.music_mood = 3
        self.emotional = ""
        self.marbling = 0

        self.music_prt_r1 = "      "
        self.music_prt_r2 = "      "
        self.beer_prt_r5 = "\----/"
        self.beer_prt_r6 = " \__/ "
        self.space_prt = "      "

    def drink_beer(self):
        print("{} has enjoyed some beer!".format(self.cow_name))
        if self.calories < (self.max_calories - self.beer_calories):
            self.calories += self.beer_calories
        else:
            self.calories = self.max_calories
        # if cows has more calories than 1 beer, 50% chance to enter alcoholic depression
        if (self.calories > self.beer_calories and random.randint(0,1) == 1):
            self.depressed()

    def depressed(self):
        print("Looks like {} has had a little too much to drink...".format(self.cow_name))
        if self.mood > (self.min_mood + self.depress_mood):
            self.mood += self.depress_mood
        else:
            self.mood = self.min_mood
        self.emotional = "{} is suffering alcoholic depression!".format(self.cow_name)

    def get_massage(self):
        print("{} is all loosed up after that massage!".format(self.cow_name))
        if self.mood < (self.max_mood - self.massage_mood):
            self.mood += self.massage_mood
        else:
            self.mood = self.max_mood

    def listen_music(self):
        self.mood += self.music_mood - random.randint(0,2)
        self.music_prt_r1 = " la~la"
        self.music_prt_r2 = "de~da~"
        # " \u266b \u266b  " ==> " ♫ ♫  "
        # "\u266b \u266b   " ==> "♫ ♫   "

    def reset_music(self):
        self.music_prt_r1 = "      "
        self.music_prt_r2 = "      "

    def update_status(self):
        # Check if marbling should increase or decrease
        if self.calories > 1 and self.mood > 1:
            self.marbling += 1
        elif (self.calories < 1 or self.mood < 1) and self.marbling > 0:
            self.marbling -= 1
        # Reduce calories and mood for the next turn
        if self.calories > self.min_calories:
            self.calories -= 1
        if self.mood > self.min_mood:
            self.mood -= 1

    def __str__(self):

        self.cow_prt_r1 = "(\__/)              Name: {}".format(self.cow_name)
        self.cow_prt_r2 = "\o__o/__________    Calories: {}".format(self.calories)
        self.cow_prt_r3 = "( .. ) @ @   @  |   Mood: {}".format(self.mood)
        self.cow_prt_r4 = " \--/-|  @ @|  | \\  {}".format(self.emotional)
        self.cow_prt_r5 = "   |  |\----|w/|  * Marbling: {}".format(self.marbling)
        self.cow_prt_r6 = "   ^  ^     ^  ^   "

        return (self.music_prt_r1 + self.cow_prt_r1 + "\n"
            + self.music_prt_r2 + self.cow_prt_r2 + "\n"
            + self.space_prt + self.cow_prt_r3 + "\n"
            + self.space_prt + self.cow_prt_r4 + "\n"
            + self.beer_prt_r5 + self.cow_prt_r5 + "\n"
            + self.beer_prt_r6 + self.cow_prt_r6 + "\n")

    def __repr__(self):
        return self.__str__()


class farm_supply:

    def __init__(self, name="Haystack", ini_stocks=1, units="items",
                 use_stock=1, unit="item", re_stock=5):
        self.name = name
        self.stocks = ini_stocks
        self.units = units
        self.unit = unit
        self.use_stock = use_stock
        self.re_stock = re_stock

    def any_left(self):
        if self.stocks >= self.use_stock:
            return [True, "You will use up {} {}, {} will remain".format(
                self.use_stock, self.unit, (self.stocks-self.use_stock))]
        else:
            return [False, "You need to buy more {}!".format(self.units)]

    def add_stocks(self):
        self.stocks += self.re_stock

    def reduce_stocks(self):
        self.stocks -= self.use_stock

    def __str__(self):
        return "The {} has {} remaining {}".format(self.name, self.stocks, self.units)

    def __repr__(self):
        return self.__str__()


## Scripting Starts
import os
import random
m1 = menu()
m1.launch()
