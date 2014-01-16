# -*- coding: utf-8 -*-
"""
Created on 24.9.2012

@author: huqa / pikkuhukka@gmail.com
"""

import random
import time
import sqlite3


def init(botconfig):
    """Create database"""
    
    db_conn = sqlite3.connect("pyssy.db")
    d = db_conn.cursor()
    d.execute("CREATE TABLE IF NOT EXISTS stats (id INTEGER PRIMARY KEY, player TEXT, deaths INT, lucks INT);")
    db_conn.commit()
    d.close()
    db_conn.close()


class Pyssy:
    """The gun object for russian roulette irc game"""
    
    """Gun on the table"""
    has_bullet = False
    """Gun in use"""
    is_in_use = False
    current_slot = 0
    bullet_slot = 0
    
    def __init__(self):
        Pyssy.has_bullet = False
        Pyssy.bullet_slot = 0
        Pyssy.current_slot = 0

    def start(self):
        """Puts a bullet in the gun"""
        Pyssy.has_bullet = True
        Pyssy.bullet_slot = random.randint(0, 5)

    def stop(self):
        """Resets the gun"""
        Pyssy.has_bullet = False
        Pyssy.bullet_slot = 0
        Pyssy.is_in_use = False

    def set_current_slot(self, index):
        """Spins the barrel of the gun index-times"""
        full_circles = index % 6
        for i in range(0,full_circles):
            Pyssy.incr_current_slot(self)

    def incr_current_slot(self):
        if Pyssy.current_slot >= 5:
            Pyssy.current_slot = 0
        else:
            Pyssy.current_slot = Pyssy.current_slot + 1

    def gun_in_use(self, in_use):
        Pyssy.is_in_use = in_use


pyssy = Pyssy()
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
             "*paskoo housuihinsa*"]
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
    if args:
        args = str(args).strip()
        player = get_player(args)
        if player != False:
            line = "!pyssy pelaaja %s on kuollut %d kertaa" % (str(args), int(player[2]))
            if int(player[3]) > 0:
                line = line + " ja on ollut jumalten valittu %d kertaa" % (int(player[3]),)
            return bot.say(channel, line)
        else:
            return bot.say(channel, "!pyssy pelaajaa %s ei löydy, %s" % (args, nick))
    
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
        if pyssy.is_in_use == False:
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
            shoot_gun(bot, nick, channel)
        else:
            return
    
def command_ammu(bot, user, channel, args):
    """Ampuu pistoolilla"""
    nick = getNick(user)
    if pyssy.has_bullet is False:
        return bot.say(channel, "Pyssy on tyhjänä tonko %s" % nick)
    else:
        if pyssy.is_in_use == False:
            pyssy.gun_in_use(True)   
            shoot_gun(bot, nick, channel)
        else:
            return

def shoot_gun(bot, nick, channel):
    gulp_len = len(gulp_msgs)
    wait_time = random.randint(2,3)
    #time.sleep(1)
    bot.say(channel, "%s %s" % (nick, gulp_msgs[random.randint(0,gulp_len-1)]))
    time.sleep(1)
    if pyssy.current_slot == pyssy.bullet_slot:
        if not is_in_db(nick):
            add_user(nick)
        bonus = random.randint(0,99)
        if bonus >= 90:
            lck_len = len(lucky_msgs)
            reason_len = len(lucky_reason_msgs)
            incr_lucks(nick)
            bot.say(channel, "%s %s %s" % (nick, lucky_msgs[random.randint(0,lck_len-1)], lucky_reason_msgs[random.randint(0,reason_len-1)]))
        else:
            time.sleep(wait_time)
            incr_deaths(nick)    
            bot.kick(channel, nick, "**PAM!!!!!!* <o\x038*\x035~'´'´´'´ '´ ´")
            
        pyssy.gun_in_use(False)
        pyssy.stop()
    else:
        time.sleep(wait_time)
        klik_len = len(klik_msgs)
        bot.say(channel, "%s" % klik_msgs[random.randint(0,klik_len-1)])
        pyssy.incr_current_slot()
        pyssy.gun_in_use(False)


#Quickly made sqlite functions for saving users
def is_in_db(nick):
    db_conn = sqlite3.connect("pyssy.db")
    d = db_conn.cursor()
    d.execute("SELECT id FROM stats WHERE player = ?", (nick,))
    player = d.fetchone()
    d.close()
    db_conn.close()    
    if not player:
        return False
    else:
        return True

def get_player(nick):
    db_conn = sqlite3.connect("pyssy.db")
    d = db_conn.cursor()
    d.execute("SELECT * FROM stats WHERE player = ?", (str(nick),))
    player = d.fetchone()
    d.close()
    db_conn.close()    
    if not player:
        return False
    else:
        return player

def add_user(nick):
    db_conn = sqlite3.connect("pyssy.db")
    d = db_conn.cursor()
    d.execute("INSERT INTO stats (player, deaths, lucks) VALUES (?,?,?)", (nick, 0, 0))
    db_conn.commit()
    d.close()
    db_conn.close()
    
def incr_deaths(nick):
    db_conn = sqlite3.connect("pyssy.db")
    d = db_conn.cursor()
    d.execute("SELECT id, deaths FROM stats WHERE player = ?", (nick,))
    player = d.fetchone()
    deaths = int(player[1])
    deaths = deaths + 1
    d.execute("UPDATE stats SET deaths = ? WHERE id = ?", (int(deaths),int(player[0])))
    db_conn.commit()
    d.close()
    db_conn.close()
    
    
def incr_lucks(nick):
    db_conn = sqlite3.connect("pyssy.db")
    d = db_conn.cursor()
    d.execute("SELECT id, lucks FROM stats WHERE player = ?", (nick,))
    player = d.fetchone()
    lucks = int(player[1])
    lucks = lucks + 1
    d.execute("UPDATE stats SET lucks = ? WHERE id = ?", (int(lucks),int(player[0])))
    db_conn.commit()
    d.close()
    db_conn.close()
