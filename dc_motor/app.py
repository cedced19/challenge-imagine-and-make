from megapi import *
bot = MegaPi()
bot.start("/dev/ttyUSB0")
bot.motorRun(1,50)
bot.motorMove(0,50)
