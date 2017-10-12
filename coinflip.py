# module imports
"""importing module for randint function"""
import random
# global variables
# classes

class CoinFlipperClass(object):
    """Class for managing coin flip attibutes and methods
    This is a poor use of class..."""
    def __init__(self):
        self.headscount = 0
        self.tailscount = 0

    def heads_or_tails(self, flipresult):
        """method to convert randint for flip to heads or tails value"""
        if next(flipresult) == 1:
            return "heads"
        return "tails"

    def flip_exec(self):
        """generator of 1 or 2"""
        yield random.randint(1, 2)

    def flip_loop(self, flips):
        """executes a loop to get values 1 or 2 from generator"""
        while flips > 0:
            flips -= 1
            if self.heads_or_tails(self.flip_exec()) == 'heads':
                self.headscount += 1
            else:
                self.tailscount += 1

    def flip_stats(self, flips):
        """prints stats about the flip including totals and percentages"""
        self.flip_loop(flips)
        headspercent = (self.headscount / flips * 100)
        tailspercent = (self.tailscount / flips * 100)
        print(('You had %s heads and %s tails.  ') % (str(self.headscount), str(self.tailscount)))
        print(('%s of your tosses were heads, the other %s were tails.') % (str(round(headspercent, 2)) + "%", str(round(tailspercent, 2)) + "%"))

# General Functions
def quarter_flip():
    """let the flipping begin"""
    fliprequest = 0
    while fliprequest == 0:
        fliptemp = int(input("How many flips shall I do today, sir? "))
        if fliptemp > 0:
            fliprequest = fliptemp
    quar = CoinFlipperClass()
    quar.flip_stats(fliprequest)
# Start up of app
quarter_flip()
