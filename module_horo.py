# -*- coding: utf-8 -*-
'''
Fetches horoscopes from iltalehti.fi
Created on Oct 17, 2012

@author: huqa / pikkuhukka@gmail.com
'''

import re
horo_url = "http://www.iltalehti.fi/horoskooppi"

def command_horo(bot, user, channel, args):
    """Hakee päivittäisen horoskoopin. Käyttö !horo <horoskooppimerkki>"""
    nick = getNick(user)
    if not args:
        return bot.say(channel, "lähe ny pelle menee %s" % nick)
    
    haku = args.decode('iso-8859-1')
    haku = haku.title()
    soup = getUrl(horo_url).getBS()

    merkki = None
    
    for m in soup.findAll("div", "valiotsikko"):
        if m.find(text=re.compile(haku+"*")):
            merkki = m.find(text=re.compile(haku+"*"))
            break
            
    if not merkki:
        return bot.say(channel, "opettele ny kirjottaan kevyt pelle %s" % nick)
    
    tekstit = merkki.next.contents[0]
    bot.say(channel, "%s %s" % (str(merkki), str(tekstit)))
