# -*- coding: utf-8 -*-
"""
Created on 19.11.2012

@author: huqa / pikkuhukka@gmail.com
"""

from random import shuffle

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
           31, 32, 33, 34, 35, 36, 37, 38, 39]


def command_lotto(bot, user, channel, args):
    """Arpoo seitsemän(7) lottonumeroa väliltä 1-39"""
    nick = getNick(user)
    nrot = list(numbers)
    shuffle(nrot)
    lotto = nrot[0:7]
    lotto.sort()
    output = ""
    for nro in range(0, 7):
        output = output + str(lotto[nro]) + " "

    return bot.say(channel, "%s, lottorivisi: %s" % (nick, output))
