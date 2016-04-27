#!/usr/bin/env python
import time
import re
yes = ['Y','y','yes','Yes']
no = ['N','n','no','No']
quit = ['X','x','Q','q']

class Game:
    def __init__(self):
        self.apples = 0
        self.gold = 0
        self.name = ''
        self.delay = 0
        #self.running = True   # we could create a variable that is evaluated in the main loop
        
        self.start()
        
    def start(self):
        print("Hello and welcome!")
        self.name=raw_input("What's your name: ")
        print("Welcome, " + self.name + "!")
        print("The objective of this game is to collect apples.")
        print("After collecting the apples you sell them.")
        choice = self.ynPrompt("Do you want to play?")
        if choice in yes:
            print "Let's get started!"
            self.initiateLoop()
        else:
            self.bye()
            
        ### no real need to specifically check for anything other than yes
        ### also no need to specificall do exit here, it will return and exit on its own
        ##elif choice in no or choice in quit:
        ##    print "Okay, bye..."
        ##    exit()
        ##else:
        ##    exit()
        
    def bye(self,message = "Okay, bye"):  # basically prints message, if not provided, there is a default.
        print message
        exit(0)
    
    # we COULD just loop on self.running and basically change that when needed...
    # pros and cons
    def initiateLoop(self):
        # while self.running:    # use self.running to control loop.
        while True:
            self.begin()

    def ynPrompt(self,string):
        return raw_input(string+' Y/N/X: ')
        
    def pickApple(self):
        time.sleep(self.delay)
        print("Pick an apple")
        self.apples += 1
        self.printInventory()
        
    def askHowManyApplesToSell(self):
        howmany = raw_input("How many apples do you want to sell? ")
        # have to verify that string contains only ints (use regex via import re)
        mo = re.match(r'^[0-9]+$',howmany)
        if not mo:
            print "I was unable to recognize your entry as a number, sorry, try again later."
        return int(mo.group(0)) if mo else 0        
    
    def sellApples(self):
        self.printInventory()
        # reworked this to prompt user for how many apples to sell!!
        # notice that asside from doing the regex, that the logic is simpler
        toSell = self.askHowManyApplesToSell()
        if toSell > self.apples:
            print "You don't have that many apples, but we can sell all you have!"
            toSell = self.apples
                
        if self.apples < 1:
            print("Sorry, " +self.name+ " . You have no apples to sell.")
            
        suff= '' if toSell == 1 else 's'
        self.gold += toSell*10
        self.apples -= toSell
        # use our own pluralize function to pluralize, so we dont have to check 
        # each time for how many apples.
        print "You've sold",toSell,self.pluralize('apple',toSell)+"."
        
        #else:
        #    print("You've sold your apples.")
        #    self.gold += self.apples*10
        #self.apples = 0
        self.printInventory()
    
    def quit(self):
        self.bye("Okay, we are quitting by request.")  # call bye, but change message

    def checkOnSale(self):
        sell = self.ynPrompt("Do you want to sell your apples?")
        if sell in yes:
            self.sellApples()
        elif sell in no:
            print("Okay, have fun with your apple.")
        elif sell in quit:
            self.quit()
        else:
            print("Should have followed my instructions. Have fun at the beginning!")
        
    def begin(self):
        pick = self.ynPrompt("Do you want to pick an apple?")
        if pick in yes:
            self.pickApple()
        elif pick in no:
            self.checkOnSale()
        elif pick in quit:
            self.quit()
            
    def pluralize(self,item,num):
        suff = '' if num == 1 else 's'
        return item+suff
        
    def printInventory(self):        
        suff = '' if self.apples == 1 else 's'
        print "You currently have,",self.apples,self.pluralize('apple',self.apples),"and",self.gold,"gold"

g = Game()
