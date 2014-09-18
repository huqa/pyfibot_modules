# -*- coding: utf-8 -*-
"""
Created on 24.9.2012

@author: huqa / pikkuhukka@gmail.com
"""

import random
import time
import logging


class Gun:
    """Russian roulette gun"""
    
    def __init__(self):
        self.has_bullet = False
        self.in_use = False
        self.bullet_slot = 0
        self.current_slot = 0

    def start(self):
        """Puts a bullet in the gun"""
        self.has_bullet = True
        self.bullet_slot = random.randint(0, 5)

    def stop(self):
        """Resets the gun"""
        self.has_bullet = False
        self.bullet_slot = 0
        self.current_slot = 0
        self.in_use = False

    def set_current_slot(self, index):
        """Spins the barrel of the gun index-times"""
        full_circles = index % 6
        for i in range(0, full_circles):
            self.incr_current_slot(self)

    def incr_current_slot(self):
        if self.current_slot >= 5:
            self.current_slot = 0
        else:
            self.current_slot += 1

    def gun_in_use(self, in_use):
        self.in_use = in_use


pyssy = Gun()
gulp_msgs = ["nostaa aseen tärisevin käsin ohimolleen.",
             "laittaa silmänsä kiinni.",
             "*gulp*",
             "ottaa aseen vakain käsin.",
             "tietää jo mitä tulee tapahtumaan.",
             "kokeilee onneaan.",
             "hikoilee..",
             "HUH HUH",
             "tärisee",
             "*nyt ei käy hyvin*",
             "*gulp*"]
klik_msgs = ["*KLIK*",
             "*KLIK* huhhuh",
             "*CLIQUE*",
             "*KLICK*",
             "*KLIK*",
             "*BONK*",
             ".... *KLIK*",
             "*KLIK*..."]
see_msgs = ["*KOTKANSILMÄ*",
            "*HAUKANKATSE*",
            "*INTUITIO*",
            "*RAINMAN*",
            "*KESKITTYMINEN*",
            "*SISÄINEN NINJA*"]
lucky_msgs = ["*JÄRKYTTÄVÄ MUNKKI*",
              "*MITÄ VITT-*",
              "*KAUHEETA SÄKÄÄ*",
              "*JUMALALLINEN VÄLIINTULO*",
              "*IDDQD*",
              "*NO JUST*"]
lucky_reason_msgs = ["*PYSSY RUOSTUU KASAAN*",
                     "*PATRUUNA OLI SUUTARI*",
                     "*LOKKI VARASTAA PYSSYN KÄDESTÄSI*",
                     "****PAM! *PATRUUNA KIMPOAA PÄÄSTÄSI*",
                     "*PATRUUNA OLI SUUTARI!*",
                     "*PYSSY OLI OSTETTU BILTEMASTA* *MITÄÄN EI TAPAHDU*",
                     "*PYSSY OLIKIN LEIKKIASE*"]


def command_pyssy(bot, user, channel, args):
    """Laittaa patruunan revolveriin"""
    nick = getNick(user)
   
    if pyssy.has_bullet is False:
        pyssy.start()
        bot.say(channel, "%s laittaa uuden patruunan revolveriin" % nick)
    
    return bot.say(channel, "!pyor sekoittaa pakan, !ammu ampuu")


def command_pyor(bot, user, channel, args):
    """Pyöräyttää pistoolin pakkaa"""
    nick = getNick(user)
    if pyssy.has_bullet is False:
        return bot.say(channel, "Pyssy on tyhjänä tonko %s" % nick)
    else:
        if not pyssy.is_in_use:
            pyssy.gun_in_use(True)
            spin_str = random.randint(2, 78)    
            pyssy.set_current_slot(spin_str)
            bonus = random.randint(0,9)
            if bonus >= 8:
                see_len = len(see_msgs)
                bot.say(channel, "%s *pyööörrrrrr* -- %s rulla liikkuu %d kierrosta" % (nick, see_msgs[random.randint(0,see_len-1)], (spin_str / 6)))
            else:
                bot.say(channel, "%s *pyööörrr* " % nick)
            time.sleep(1)
            return shoot_gun(bot, nick, channel)
        else:
            return


def command_ammu(bot, user, channel, args):
    """Ampuu pistoolilla"""
    nick = getNick(user)
    if pyssy.has_bullet is False:
        return bot.say(channel, "Pyssy on tyhjänä tonko %s" % nick)
    else:
        if not pyssy.is_in_use:
            pyssy.gun_in_use(True)
            return shoot_gun(bot, nick, channel)
        else:
            return


def shoot_gun(bot, nick, channel):
    gulp_len = len(gulp_msgs)
    wait_time = random.randint(2,3)
    #time.sleep(1)
    bot.say(channel, "%s %s" % (nick, gulp_msgs[random.randint(0,gulp_len-1)]))
    time.sleep(1)
    if pyssy.current_slot == pyssy.bullet_slot:
        bonus = random.randint(0, 99)
        if bonus >= 90:
            time.sleep(wait_time)
            lck_len = len(lucky_msgs)
            reason_len = len(lucky_reason_msgs)
            bot.say(channel, "%s %s %s" % (nick, lucky_msgs[random.randint(0,lck_len-1)], lucky_reason_msgs[random.randint(0,reason_len-1)]))
        else:
            time.sleep(wait_time)
            bot.kick(channel, nick, "**PAM!!!!!!* <o\x038*\x035~'´'´´'´ '´ ´")
            
        pyssy.gun_in_use(False)
        pyssy.stop()
        return
    else:
        time.sleep(wait_time)
        klik_len = len(klik_msgs)
        bot.say(channel, "%s" % klik_msgs[random.randint(0, klik_len-1)])
        pyssy.incr_current_slot()
        pyssy.gun_in_use(False)
        return



