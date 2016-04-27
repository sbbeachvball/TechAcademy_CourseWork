#!/usr/bin/env python
import time
yes = ['Y','y','yes','Yes']
no = ['N','n','no','No']
quit = ['X','x','Q','q']

class Game:
    def __init__(self):
        self.apples = 0
        self.gold = 0
        self.name = ''
        self.delay = 1
        
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
        elif choice in no or choice in quit:
            print "Okay, bye..."
            exit()
        else:
            exit()
            
    def initiateLoop(self):
        while True:
            self.begin()

    def ynPrompt(self,string):
        return raw_input(string+' Y/N/X: ')
        
    def pickApple(self):
        time.sleep(self.delay)
        print("Pick an apple")
        self.apples += 1
        self.printInventory()
    
    def sellApples(self):
        self.printInventory()
        if self.apples < 1:
            print("Sorry, " +self.name+ " . You have no apples to sell.")
        elif self.apples == 1:
            print("You've sold your apple.")
            self.gold += self.apples*10
        else:
            print("You've sold your apples.")
            self.gold += self.apples*10
        self.apples = 0
    
    def quit(self):
        print("Okay, we are quitting by request.")
        exit(0)

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

    def printInventory(self):        
        suff = '' if self.apples == 1 else 's'
        print "You currently have,",self.apples,'apple'+suff," and",self.gold,"gold"

g = Game()
