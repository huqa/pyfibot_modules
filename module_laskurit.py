# -*- coding: utf-8 -*-
"""
"Calculates" whattodo and odds. 
Created on 9.9.2012

@author: huqa / pikkuhukka@gmail.com
"""

import random


def command_whattodo(bot, user, channel, args):
    """Päättää puolestasi mitä tehdä. Käyttö !whattodo mitä, mitä, mitä (n kertaa)"""
    if not args:
        return
    nick = getNick(user)
    choices = args.split(",")
    num_choices = len(choices)
    if num_choices == 1:
        return bot.say(channel, "%s, anna enempi vaihtoehtoja" % nick)

    #TODO fixme
    number = 1.0
    percents = []
    for x in range(1,num_choices+1):
        if x != num_choices:
            rand = random.uniform(0.0,number) 
            number = number - rand
            #bot.say(channel, "x is %d" % x)
            percents.append(rand)
        elif x == num_choices:
            #bot.say(channel, "x is num_choices %f" % number)
            percents.append(number)
    
    out = nick + ", (whattodo) "        
    i = 1;
    for q, a in zip(choices, percents):
        out += str(q) + ": " + str("{0:.0f}%".format(a*100))
        i += 1
        if i != len(choices)+1:
            out += ","
        
    return bot.say(channel, out)


def command_oddsit(bot, user, channel, args):
    """Kertoo millä todennäköisyydellä jokin asia tulee tapahtumaan. Käyttö !oddsit voitan lotossa"""
    nick = getNick(user)
    if not args:
        return bot.say(channel, "%s, painu takas neukkulaan" % nick)
    
    rand = random.random()
    bot.say(channel, "%s, oddsit: %s %s" % (nick, args, str("{0:.0f}%".format(rand*100))))

