# -*- coding: utf-8 -*-
'''
Created on Feb 4, 2013

@author: huqa
'''
from random import randint
aija_mestat = ["thaikuis",
               "briteis",
               "jenkeis",
               "indois",
               "baaris",
               "balil",
               "japanis",
               "malil",
               "mäkis",
               "pohjoisnaval",
               "turkis",
               "olympialaisis",
               "ausseis",
               "brasseis",
               "meksikos",
               "kanadas",
               "gobin aavikol",
               "kapkaupungis",
               "lontoos",
               "intias",
               "asuntomessuil",
               "pakistanis",
               "etelä-naval",
               "tiibetis",
               "kiinas",
               "siperias",
               "x-gamesis",
               "ymca:s",
               "tongal",
               "tulivuores",
               "lontoos",
               "muukalaislegioonas",
               "vietnamis",
               "etelä-koreas",
               "luolas",
               "vankilassa",
               "fudiksen mm-finaalis",
               "pohjois-koreas",
               "viidakos",
               "hervannas",
               "superbowlissa",
               "hesburgeris",
               "lastentarhassa"]
aija_teot = ["surffaa",
             "skeittaa",
             "reilaa",
             "roadtripil",
             "daivaa",
             "suunnistaa",
             "kiipeilee",
             "ryyppää",
             "parkouraa",
             "seilaa",
             "wakeboardaa",
             "työharjottelus",
             "kokkaa",
             "metsästää",
             "ampumas",
             "juoksee",
             "bodaamas",
             "deejiinä",
             "ratsastaa",
             "pyöräilee",
             "töis",
             "travellaa",
             "reissaa",
             "räppää",
             "tappelemas",
             "kouluttaa",
             "suihkussa",
             "punnertaa",
             "snowboardaa",
             "maratoonis",
             "piirtää",
             "maalaan",
             "paskal",
             "kusel",
             "nyrkkeilee",
             "meditoimas"]
aija_tanaa = ["tänää meikä kokkaa",
              "tänää meikäijä kokkaa",
              "tänää mä väsään",
              "tänään meikä tekee",
              "tänään meitsi väsää dinneriks",
              "tänään mä duunaan",
              "pistän koht tost snadit väännöt"]
aija_ruoat = ["äijäwokkii",
              "viikon marinoitunutta kengurufilettä",
              "täytettyjä crepejä",
              "äijäpihvii",
              "paahdettuu lammast",
              "pakurikääpää",
              "kanttarellej",
              "virtahepoo",
              "koiraa",
              "aasinpotkaa",
              "kaviaarii",
              "miekkakalaa",
              "torvisienii",
              "jättiläismustekalaa",
              "hanhenmaksaa",
              "kobe-pihvii",
              "kateenkorvaa",
              "porsaankylkee",
              "äijäsalaattii",
              "hampurilaisii",
              "kebabbii",
              "kissaa",
              "banaaneita",
              "falafelii",
              "kanansiipii",
              "valaanlihaa",
              "kenguruu",
              "sammalta",
              "pizzaa",
              "perunoit",
              "gorillaa",
              "vyötiäistä",
              "hamstereit",
              "nokkosii",
              "apinanaivoja",
              "pässin kiveksii",
              "merihevost",
              "etanoit",
              "merimakkaraa",
              "muurahaiskarhuu",
              "haggista",
              "karitsaa",
              "käärmettä"]
aija_lisukkeet = ["wasabiemulsiol",
                  "ranskalaisil",
                  "pastal",
                  "korianteril",
                  "hummeril",
                  "mädätettynä",
                  "kanansiivil",
                  "riisillä",
                  "ruisleiväl",
                  "keitettynä",
                  "sushil",
                  "käristettynä",
                  "couscousil",
                  "sokerikuorrutuksel",
                  "juustol",
                  "virtahevon suolessa",
                  "kermaviilil",
                  "yrttiöljyl",
                  "maustekurkumal",
                  "katkaravuil",
                  "friteerattuna",
                  "keittona",
                  "kaviaaril",
                  "höyrytettynä",
                  "muurahaisilla",
                  "paistettuna",
                  "liekitettynä",
                  "fazerin sinisellä",
                  "makkaral",
                  "silvottuna",
                  "jugurtil",
                  "vetisenä"]
aija_yrtit = ["tashimoto-heinää jonka poimin shiribetsu-joen rannalt kun olin reilaa japanis",
              "abessiinialaist kurttuviikunaa jota saan paikalliselt tarhurilt etiopiast",
              "mökin takapihalt poimittuu pitkälehtikihokkii",
              "sichuanin maakunnast poimittuu sareptaninsinappii",
              "tämmösii tyrnimustikka-risteytysmarjoi joita sain turun yliopiston genetiikan laitoksen äijilt",
              "perus suomalaist japaninpersiljaa jota ny löytyy kaikkien pihast",
              "neidonhiuspuu-uutet",
              "mustanmeren merilevää",
              "jauhettuu ruusunjuurta",
              "dodon höyhenii",
              "omakasvattamaa ananast",
              "jauhettuu kääpiöponinkavioo",
              "mustanmerenruusua jotka poimin georgian haikil",
              "kuopas paahdettui maakastanjoit",
              "frendin luomutilal kasvattamaa mukulakirvelii",
              "makeen kirpeit ananaskirsikoit",
              "saframii",
              "tasmanian tuholaisen karvoi",
              "basilikaa",
              "sitruunamehuu",
              "jättiläispunapuun ydintä",
              "jakinmaitorahkaa",
              "valaanrasvaa",
              "vaimon kasvattamaa minttuu",
              "jauhettuu ykssarvisen sarvee",
              "viimesen dinosauruksen suomuja",
              "murkkujen kusta",
              "koivun kaarnaa",
              "mes-juustoo pari siivuu"]
aija_dressing = ["vatikaanist saatuu balsamicoo, terveisii vaa konklaavin äijille :D",
                 "maapähkinä-vinegrettee",
                 "timjamis liuotettuu inkiväärii",
                 "tämmöst viskisiirappii",
                 "oliiviöljyä",
                 "sivetindroppingei",
                 "orpolapsien kyynelii",
                 "savulohismetanaa",
                 "tummaa rommii",
                 "kolaa",
                 "vladimirin pirtuu",
                 "kossuu",
                 "hp-kastiket",
                 "ketsuppii",
                 "poron verta",
                 "meduusan limaa",
                 "sinivalaan verta"]
aija_toimenpiteet = ["pyöräytä valkokastikkees",
                     "glaseerataan nopee",
                     "pyöräytetää pannul limen kaa",
                     "flambeerataa punkul",
                     "paistetaan neljä tuntii",
                     "keitetään etikassa",
                     "suurustetaan",
                     "kuivatetaan"]
aija_loppuun = ["loppuun viel pikku suola",
                "lopuks viel silaus curacaoo",
                "lopuks viel pikku pippurit",
                "lopuks heitetään koko paska roskiin",
                "lopuks viel pienet öljyt",
                "lopuks viel annetaan paahtua pari tuntii",
                "lopuks viel pikku limet",
                "lopuks viel pikku chilit",
                "lopuks viel pienet pyöräytykset",
                "lopuks annetaan jäähtyy pari päivää",
                "mut alkuun pienet äijätumut",
                "mut alkuun otetaa pienet paukut",
                "lopuks annetaan hautuu pari minsaa"]
aija_tuo = ["tuomaan",
        "antaan",
        "lisään"]
aija_mitatuo = ["semmost syvyyt siihe",
                "vähä semmost itämaist twistii siihe",
                "terävyyttä tähä",
                "pehmeyttä reunoihi",
                "vähä siihe semmost twistii",
                "vähä semmost äijämäisyyt sekaa",
                "makuhermoil vähä lomafiilist",
                "vähä semmost bläästii siihe",
                "tulista twistii siihe"]
aija_siistii = ["siistii",
                "hyvä",
                "helmee",
                "äijää",
                "siistii",
                "asiallist",
                "kuulii"]
aija_aijat = ["äijät",
              "leidit",
              "frendit",
              "äijä",
              "vaimo",
              "kundi",
              "jätkät",
              "homiet",
              "homot",
              "pellet",
              "dudet",
              "jäbä",
              "spede",
              "dude"]

def aija_story():
    aijat = aija_aijat[randint(0,len(aija_aijat)-1)]
    siistii = aija_siistii[randint(0,len(aija_siistii)-1)]
    mestat = aija_mestat[randint(0,len(aija_mestat)-1)]
    teot = aija_teot[randint(0,len(aija_teot)-1)]
    tanaa = aija_tanaa[randint(0,len(aija_tanaa)-1)]
    ruoka = aija_ruoat[randint(0,len(aija_ruoat)-1)]
    lisuke = aija_lisukkeet[randint(0,len(aija_lisukkeet)-1)]
    yrtit = aija_yrtit[randint(0,len(aija_yrtit)-1)]
    tuo = aija_tuo[randint(0,len(aija_tuo)-1)]
    mita = aija_mitatuo[randint(0,len(aija_mitatuo)-1)]
    
    #moro x
    output = "moro %s :D mitä %s." % (aijat, aijat)
    lots = aijat[-1] == 't'
    #siisti nähä teit
    if lots:
        output = output + " %s nähä teit :D " % (siistii,)
    else:
        output = output + " %s nähä sua :D " % (siistii,)
    #tänää mä väsään
    if lots:
        output = output + "%s teil " % (tanaa,)
    else:
        output = output + "%s sulle " % (tanaa,)
    
    #ruoaks
    output = output + ruoka + " %s." % (lisuke)
    
    #resepti
    output = output + " tän reseptin opin kun olin %s %s :D" % (mestat, teot)
    
    #sekaan
    output = output + " pistetää sekaa vähä %s %s %s :D" % (yrtit, tuo, mita)
    
    if randint(1,100) > 50:
        dressing = aija_dressing[randint(0,len(aija_dressing)-1)]
        output = output + " dressingiks %s." % (dressing,)
    else:
        toimenpide = aija_toimenpiteet[randint(0,len(aija_toimenpiteet)-1)]
        output = output + " ja sit viel %s :D" % (toimenpide,)
        
    if randint(1,100) > 50:
        lopuks = aija_loppuun[randint(0,len(aija_loppuun)-1)]
        output = output + " %s." % (lopuks,)
    
    output = output + " nonii toivottavasti maistuu. "
    
    if lots:
        output = output + "mä rakastan teit %s :D" % (aijat,)
    else:
        output = output + "mä rakastan sua %s :D" % (aijat,)
    
    return output    

def command_aija(bot, user, channel, args):
    output = aija_story()
        
    return bot.say(channel, output)

def command_spurdoaija(bot, user, channel, args):
    output = aija_story()
    output = output.replace("t","d").replace("c","g").replace("k", "g").replace("p", "b").replace("x","gs").replace("z","ds")

    return bot.say(channel, output)

def command_killaaija(bot, user, channel, args):
    output = aija_story()
    output = killavilzaa_lause(output)
    
    return bot.say(channel, output)

def killavilzaa_lause(lause):
    output = ""
    for c in lause:
        k = randint(1,100)
        if k > 90:
            kirjaimet = kirjaimelle_killavilz(c)
            f = kirjaimet[randint(0,len(kirjaimet)-1)]
            output = output + f
            h = randint(1,100)
            if h > 95:
                f = kirjaimet[randint(0,len(kirjaimet)-1)]
                output = output + f
            elif h < 11:
                output = output + f
                output = output + f
                output = output + f
                output = output + f
                output = output + f
        else:
            output = output + c
    return output

def kirjaimelle_killavilz(c):
    c = c.lower()
    if c == "a":
        return "qwsxza"
    elif c == "b":
        return "vfghnb "
    elif c == "c":
        return "xsdfvc "
    elif c == "d":
        return "swerfvcxd"
    elif c == "e":
        return "234rfdswe"
    elif c == "f":
        return "dertgbvcf"
    elif c == "g":
        return "frtyhnbvg"
    elif c == "h":
        return "gtyujmnbh"
    elif c == "i":
        return "u789olkji"
    elif c == "j":
        return "hyuik,mnj"
    elif c == "k":
        return "juiol.,mk"
    elif c == "l":
        return "kiopö-.,l"
    elif c == "m":
        return "nhjk, m"
    elif c == "n":
        return "bghjmn "
    elif c == "o":
        return "i890pölok"
    elif c == "p":
        return "o90+åäöpl"
    elif c == "q":
        return "§12wsqa"
    elif c == "r":
        return "e345tgfdr"
    elif c == "s":
        return "aqwedcxzs"
    elif c == "t":
        return "r456yhgft"
    elif c == "u":
        return "y678ikjhu"
    elif c == "v":
        return "cdfgbv "
    elif c == "w":
        return "q123edsaw"
    elif c == "x":
        return "zasdcx "
    elif c == "y":
        return "t567ujhgy"
    elif c == "z":
        return "asxz "
    elif c == "å":
        return "p0+´¨'äöå"
    elif c == "ä":
        return "öpå¨'-ä"
    elif c == "ö":
        return "lopåä-.ö"
    else:
        return c
    