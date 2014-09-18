# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import logging
import dataset
import os


MONITOR_URL_INT = "http://lissu.tampere.fi/monitor.php?stop=%d"


STOPS_TABLE = 'stops'

db = dataset.connect('sqlite:///databases/tkl.db')
log = logging.getLogger('tkl')


def init(botconfig):
    if not os.path.exists('databases'):
        os.makedirs('databases')
    #db = dataset.connect('sqlite:///databases/tkl.db')


def is_int(number):
    try:
        number = int(number)
        return True
    except:
        return False

def command_tkl(bot, user, channel, args):
    if not args:
        nick = getNick(user)
        data = find_first(nick)
        if data:
            msg = "%s, (%s) " % (nick, str(data['key']))
            msg += fetch_stop_data(int(data['stop']))
            return bot.say(channel, msg)
        else:
            return
    insert = args.split()
    if len(insert) >= 2:
        if is_int(insert[0]):
            nick = getNick(user)
            #nick = "huqa"
            stop = insert[0]
            key = insert[1]
            upsert_stop(nick, str(key), stop)
            msg = "%s, (%s) " % (nick, key)
            msg += fetch_stop_data(int(stop))
            return bot.say(channel, msg)
    else:
        try:
            args = int(args)
            nick = getNick(user)
            #nick = "huqa"
            data = fetch_db_data(nick, args)
            if data:
                msg = "%s, (%s) " % (nick, args)
                msg += data
                return bot.say(channel, msg)
            else:
                msg = fetch_stop_data(args)
                return bot.say(channel, "!tkl %s" % (msg))
        except:
            nick = getNick(user)
            #nick = "huqa"
            #log.info(args)
            data = fetch_db_data(nick, args)
            if data:
                msg = "%s, (%s) " % (nick, args)
                msg += data
                return bot.say(channel, msg)
            else:
                return
    #msg = fetch_stop_data(args)
    #return bot.say(channel, "!tkl %s" % (msg))
    return

def upsert_stop(nick, key, stop):
    data = dict(nick=nick, key=key, stop=stop)
    db[STOPS_TABLE].upsert(data, ['nick','key'])

def fetch_db_data(nick, key):
    stop = db[STOPS_TABLE].find_one(nick=nick, key=key)
    if not stop:
        return
    else:
        return fetch_stop_data(int(stop['stop']))

def find_first(nick):
    stop = db[STOPS_TABLE].find_one(nick=nick)
    if not stop:
        return
    else:
        return stop
        

def fetch_stop_data(stop):
    if isinstance(stop, int):
        url = getUrl(MONITOR_URL_INT % stop)
        #url = urllib2.urlopen(MONITOR_URL_INT % stop)
        soup = BeautifulSoup(url.content)
        #soup = BeautifulSoup(url)
        rows = soup.find_all('tr')
        stop_name = rows[0].find('td').string.strip()
        stop_name = ' '.join(stop_name.split())
        msg = stop_name + " "
        rows = rows[3:]
        for row in rows:
            data = row.find_all('td')
            line = data[0].string.strip()
            where = data[2].string.strip()
            arr1 = data[3].contents
            arr2 = data[4].contents
            arr1 = arr1[0].string.strip()
            arr2 = arr2[0].string.strip()
            if not ":" in arr1:
                arr1 += "min"
            if not ":" in arr2:
                arr2 += "min"
            msg += "[(%s -> %s) %s & %s] " % (line, where, arr1, arr2)
        return msg
    else:
        log.info('fetch_stop_data not int :DD')
        return None
 
        


#if __name__ == "__main__":
    #init("config")
    #print fetch_db_data("huqa", "koti")
    #upsert_stop("huqa", "koti", 2031)
    #print fetch_db_data("huqa", "koti")
    #print fetch_stop_data(503)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
