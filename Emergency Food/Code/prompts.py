import time
import random

class Prompt:

    def __init__(self):
      # Randomizer Seed
      random.seed(time.time())

    def join(self):
        return ("Hey there! Normally Paimon would be Paimon, " +
                "but Paimon is right now 'Emergency Food' thanks " +
                "to Strike's... bad coding. \n\n" +
                "Eh heh... \n\n" +
                "Anyways, Paimon will be able to remind you on " +
                "the things you need to do! Assuming Strike tells me about it.")


    def startup(self):

        number = 4
        
        rand = random.randint(1, number)
        if rand == 1:
            return ("What happens to Paimon if her status icon goes offline...? " +
                    "Paimon can't seem to remember anything after going out... ")
        if rand == 2:
            return ("Paimon sometimes wonders if our travelers never fished Paimon out... " +
                    "would Paimon still be in this mess?")
        if rand == 3:
            return ("Paimon misses Golden Apple Archipelago... " +
                    "Paimon wishes that she had her own mirage! " +
                    "Paimon bets that it's filled with treasure... ")
        if rand == 4:
            return ("Paimon is out of brain juice to think about anything... >->")
        if rand == 5:
            return ("Note to Paimon: never bring Klee along to Sumeru. " +
                    "Paimon already got in trouble by Tighnari for burning a few trees... ")
    
    def daily(self):
        return ("<@&1001671128852463630>\n\n" +
                "Paimon has noticed the day has changed! Paimon will now remind you on a few things!"
                "Here are a few regular things to remember!\n\n" +
                "__**Daily List:**__ \n" +
                "> - Daily Commissions [60 Primogems] \n" +
                "> - Resin! \n" +
                "> - Login Web Event \n\n" +
                "Here's the link to the web event: \n\n" +
                "https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481")

    def beforeWeek(self):
      return ("Paimon has also noticed that tomorrow is the weekly reset! " +
              "Remember to do these things before they reset for the week! \n\n" +
              "__**Pre-Weekly Reset List:**__\n" +
              "> - Bosses \n" +
              "> - Battle Pass Quests \n")

    def weeklyRefresh(self):
      return ("Paimon has noticed the week has changed! Paimon will now remind you on a few things!")

    def weekly(self):
      return ("Here's a list of all things that have been reset for the week! \n\n" +
              "__**Weekly Reset List:**__\n" + 
              "> - Bosses \n" +
              "> - Battle Pass Quests \n")

    def events(self, eventList):
      temp = ""
      for i in eventList:
        temp += "> - " + i

      return ("Paimon has information regarding events! " +
              "Please see the list to make sure you've done them today! \n\n" +
              "__**Event List:**__ \n" +
              temp)

    def noEvents(self):
      return ("Paimon does not have any information regarding events! " +
              "Please tell Strike to give me information... >_<")

    def begin(self):
        return ("Looks like {} needs Paimon to remind the server on some things. " +
                "Don't worry, Paimon will remind you on some things!")

    def spiral(self):
        ctime = time.localtime(time.time()).tm_mday

        if ctime < 16:
            left = 15 - ctime
        else:
            left = self.monthDays(time.localtime(time.time())) - ctime

        if left > 1:
          left = str(left) + " days"
        elif left == 1:
          left = str(left) + " day"
        else:
          left = "today"

        return ("Paimon knows that you love grinding out the Spiral Abyss for those pesky Primogems! " +
                "Paimon doesn't understand why you grind it that much. \n\n" +
                "Currently, you only have " + left + " left to finish the Spiral Abyss!")

    def annoy(self):

        number = 8
        
        rand = random.randint(1, number)
        if rand == 1:
           return ("How many times do I have to keep telling you {}! " +
                   "Paimon. Is. Not. Emergency. Food!")
        if rand == 2:
           return ("Haha, very funny {}. " +
                   "Would you like it if Paimon called you emergency food?")
        if rand == 3:
            return ("I wonder if Paimon can convince Klee to throw bombs at you to uh... " +
                    "'persuade' you to stop calling Paimon emergency food {}...")
        if rand == 4:
            return ("Paimon should think of an ugly nickname for you {} " +
                    "for all the times you've called Paimon emergency food... some day.")
        if rand == 5:
            return ("You know, Paimon thinks your lost sibiling is much better than you {}! " +
                    "Maybe they won't called Paimon emergency food if Paimon joined them!")
        if rand == 6:
            return ("If you're going to keep calling Paimon emergency food, " +
                    "you better be prepared to spend all your mora for *Sticky Honey Roast* {}!")
        if rand == 7:
            return ("Paimon wonders if Paimon can complain to MiHoYo to block you " +
                    "from typing emergency food... or even worse, prevent you from " +
                    "finding your long lost sibiling {}!")
        if rand == 8:
            return ("Why don't we try another ping {}? Oh wait, here's one: {}.")

    def monthDays(self, month):
        if month.tm_mon == 1:
            return 31
        if month.tm_mon == 2:
            if month.tm_year % 4 == 0:
                return 29
            return 28
        if month.tm_mon == 3:
            return 31
        if month.tm_mon == 4:
            return 30
        if month.tm_mon == 5:
            return 31
        if month.tm_mon == 6:
            return 30
        if month.tm_mon == 7:
            return 31
        if month.tm_mon == 8:
            return 31
        if month.tm_mon == 9:
            return 30
        if month.tm_mon == 10:
            return 31
        if month.tm_mon == 11:
            return 30
        if month.tm_mon == 12:
            return 31

    def pinged(self):
        return ("Can Paimon not get pinged {}? And stop calling me Emergency Food! It's Paimon!")
