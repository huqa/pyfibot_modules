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
               "m�kis",
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
               "etel�-naval",
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
               "etel�-koreas",
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
             "ryypp��",
             "parkouraa",
             "seilaa",
             "wakeboardaa",
             "ty�harjottelus",
             "kokkaa",
             "mets�st��",
             "ampumas",
             "juoksee",
             "bodaamas",
             "deejiin�",
             "ratsastaa",
             "py�r�ilee",
             "t�is",
             "travellaa",
             "reissaa",
             "r�pp��",
             "tappelemas",
             "kouluttaa",
             "suihkussa",
             "punnertaa",
             "snowboardaa",
             "maratoonis",
             "piirt��",
             "maalaan",
             "paskal",
             "kusel",
             "nyrkkeilee",
             "meditoimas"]
aija_tanaa = ["t�n�� meik� kokkaa",
              "t�n�� meik�ij� kokkaa",
              "t�n�� m� v�s��n",
              "t�n��n meik� tekee",
              "t�n��n meitsi v�s�� dinneriks",
              "t�n��n m� duunaan",
              "pist�n koht tost snadit v��nn�t"]
aija_ruoat = ["�ij�wokkii",
              "viikon marinoitunutta kengurufilett�",
              "t�ytettyj� crepej�",
              "�ij�pihvii",
              "paahdettuu lammast",
              "pakurik��p��",
              "kanttarellej",
              "virtahepoo",
              "koiraa",
              "aasinpotkaa",
              "kaviaarii",
              "miekkakalaa",
              "torvisienii",
              "j�ttil�ismustekalaa",
              "hanhenmaksaa",
              "kobe-pihvii",
              "kateenkorvaa",
              "porsaankylkee",
              "�ij�salaattii",
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
              "vy�ti�ist�",
              "hamstereit",
              "nokkosii",
              "apinanaivoja",
              "p�ssin kiveksii",
              "merihevost",
              "etanoit",
              "merimakkaraa",
              "muurahaiskarhuu",
              "haggista",
              "karitsaa",
              "k��rmett�"]
aija_lisukkeet = ["wasabiemulsiol",
                  "ranskalaisil",
                  "pastal",
                  "korianteril",
                  "hummeril",
                  "m�d�tettyn�",
                  "kanansiivil",
                  "riisill�",
                  "ruisleiv�l",
                  "keitettyn�",
                  "sushil",
                  "k�ristettyn�",
                  "couscousil",
                  "sokerikuorrutuksel",
                  "juustol",
                  "virtahevon suolessa",
                  "kermaviilil",
                  "yrtti�ljyl",
                  "maustekurkumal",
                  "katkaravuil",
                  "friteerattuna",
                  "keittona",
                  "kaviaaril",
                  "h�yrytettyn�",
                  "muurahaisilla",
                  "paistettuna",
                  "liekitettyn�",
                  "fazerin sinisell�",
                  "makkaral",
                  "silvottuna",
                  "jugurtil",
                  "vetisen�"]
aija_yrtit = ["tashimoto-hein�� jonka poimin shiribetsu-joen rannalt kun olin reilaa japanis",
              "abessiinialaist kurttuviikunaa jota saan paikalliselt tarhurilt etiopiast",
              "m�kin takapihalt poimittuu pitk�lehtikihokkii",
              "sichuanin maakunnast poimittuu sareptaninsinappii",
              "t�mm�sii tyrnimustikka-risteytysmarjoi joita sain turun yliopiston genetiikan laitoksen �ijilt",
              "perus suomalaist japaninpersiljaa jota ny l�ytyy kaikkien pihast",
              "neidonhiuspuu-uutet",
              "mustanmeren merilev��",
              "jauhettuu ruusunjuurta",
              "dodon h�yhenii",
              "omakasvattamaa ananast",
              "jauhettuu k��pi�poninkavioo",
              "mustanmerenruusua jotka poimin georgian haikil",
              "kuopas paahdettui maakastanjoit",
              "frendin luomutilal kasvattamaa mukulakirvelii",
              "makeen kirpeit ananaskirsikoit",
              "saframii",
              "tasmanian tuholaisen karvoi",
              "basilikaa",
              "sitruunamehuu",
              "j�ttil�ispunapuun ydint�",
              "jakinmaitorahkaa",
              "valaanrasvaa",
              "vaimon kasvattamaa minttuu",
              "jauhettuu ykssarvisen sarvee",
              "viimesen dinosauruksen suomuja",
              "murkkujen kusta",
              "koivun kaarnaa",
              "mes-juustoo pari siivuu"]
aija_dressing = ["vatikaanist saatuu balsamicoo, terveisii vaa konklaavin �ijille :D",
                 "maap�hkin�-vinegrettee",
                 "timjamis liuotettuu inkiv��rii",
                 "t�mm�st viskisiirappii",
                 "oliivi�ljy�",
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
aija_toimenpiteet = ["py�r�yt� valkokastikkees",
                     "glaseerataan nopee",
                     "py�r�ytet�� pannul limen kaa",
                     "flambeerataa punkul",
                     "paistetaan nelj� tuntii",
                     "keitet��n etikassa",
                     "suurustetaan",
                     "kuivatetaan"]
aija_loppuun = ["loppuun viel pikku suola",
                "lopuks viel silaus curacaoo",
                "lopuks viel pikku pippurit",
                "lopuks heitet��n koko paska roskiin",
                "lopuks viel pienet �ljyt",
                "lopuks viel annetaan paahtua pari tuntii",
                "lopuks viel pikku limet",
                "lopuks viel pikku chilit",
                "lopuks viel pienet py�r�ytykset",
                "lopuks annetaan j��htyy pari p�iv��",
                "mut alkuun pienet �ij�tumut",
                "mut alkuun otetaa pienet paukut",
                "lopuks annetaan hautuu pari minsaa"]
aija_tuo = ["tuomaan",
        "antaan",
        "lis��n"]
aija_mitatuo = ["semmost syvyyt siihe",
                "v�h� semmost it�maist twistii siihe",
                "ter�vyytt� t�h�",
                "pehmeytt� reunoihi",
                "v�h� siihe semmost twistii",
                "v�h� semmost �ij�m�isyyt sekaa",
                "makuhermoil v�h� lomafiilist",
                "v�h� semmost bl��stii siihe",
                "tulista twistii siihe"]
aija_siistii = ["siistii",
                "hyv�",
                "helmee",
                "�ij��",
                "siistii",
                "asiallist",
                "kuulii"]
aija_aijat = ["�ij�t",
              "leidit",
              "frendit",
              "�ij�",
              "vaimo",
              "kundi",
              "j�tk�t",
              "homiet",
              "homot",
              "pellet",
              "dudet",
              "j�b�",
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
    output = "moro %s :D mit� %s." % (aijat, aijat)
    lots = aijat[-1] == 't'
    #siisti n�h� teit
    if lots:
        output = output + " %s n�h� teit :D " % (siistii,)
    else:
        output = output + " %s n�h� sua :D " % (siistii,)
    #t�n�� m� v�s��n
    if lots:
        output = output + "%s teil " % (tanaa,)
    else:
        output = output + "%s sulle " % (tanaa,)
    
    #ruoaks
    output = output + ruoka + " %s." % (lisuke)
    
    #resepti
    output = output + " t�n reseptin opin kun olin %s %s :D" % (mestat, teot)
    
    #sekaan
    output = output + " pistet�� sekaa v�h� %s %s %s :D" % (yrtit, tuo, mita)
    
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
        output = output + "m� rakastan teit %s :D" % (aijat,)
    else:
        output = output + "m� rakastan sua %s :D" % (aijat,)
    
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
        return "kiop�-.,l"
    elif c == "m":
        return "nhjk, m"
    elif c == "n":
        return "bghjmn "
    elif c == "o":
        return "i890p�lok"
    elif c == "p":
        return "o90+���pl"
    elif c == "q":
        return "�12wsqa"
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
    elif c == "�":
        return "p0+��'���"
    elif c == "�":
        return "�p�'-�"
    elif c == "�":
        return "lop��-.�"
    else:
        return c
    