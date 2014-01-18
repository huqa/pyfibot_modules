# -*- coding: utf-8 -*-
"""
The classic magic 8-ball toy.
Created on 18.1.2014

@author: huqa / pikkuhukka@gmail.com
"""
from random import randint

_ANSWERS = ["asia on varma",
            "asia on päätetty varmaksi",
            "ilman muuta",
            "kyllä, varmasti",
            "voit luottaa siihen",
            "näen asian niin, että kyllä",
            "hyvin todennäköisesti",
            "asia näyttää oikein hyvältä",
            "kyllä",
            "asianhaarat osoittavat, että kyllä",
            "ei ole varmaa tietoa, kokeile uudelleen",
            "kysy uudestaan myöhemmin",
            "parempi etten kerro sinulle nyt",
            "en pysty ennustamaan asiaa tällä hetkellä",
            "keskity ja kysy uudestaan",
            "älä luota siihen",
            "vastaukseni on: ei",
            "lähteeni sanovat ei",
            "asianhaarat osoittavat, että ei",
            "hyvin epätodennäköisesti"]


def command_8ball(bot, user, channel, args):
    nick = getNick(user)
    if not args:
        return bot.say(channel, "Kysy jokin kyllä/ei-kysymys %s" % nick)

    ans_length = len(_ANSWERS)
    answer = randint(0, ans_length-1)
    output = nick + ": " + str(_ANSWERS[answer])
    return bot.say(channel, output)