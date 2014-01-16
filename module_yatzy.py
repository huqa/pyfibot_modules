# -*- coding: utf-8 -*-
"""
A game of yatzy in finnish for pyfibot. 
Started as a code kata and ended up as an irc game.
@version: 0.9 beta
@author: huqa / pikkuhukka@gmail.com
"""
from random import randint, shuffle
from operator import itemgetter
import logging

# @type: YatzyManager
manager = None
log = logging.getLogger('yatzy')


def init(botfactory):
    global manager
    manager = YatzyManager()


def command_j(bot, user, channel, args):
    """
    The command that players use to message the bot.
    """
    nick = getNick(user)
    #log.info("%s %s %s" % (str(nick), str(channel), str(args)))
    global manager
    if not manager:
        log.info("manager not found")
        manager = YatzyManager()
    if manager.channel_status(channel, "lobby"):
        if manager.is_lobby_starter(channel, nick):
            if args:
                # eisit or aloita
                if args == "eisit":
                    output = manager.stop_lobby(channel, nick)
                    return bot.say(channel, output)
                elif args == "aloita":
                    output = manager.start_game_for_channel(channel, nick)
                    for o in output:
                        bot.say(channel, o)
                    return
        else:
            if args:
                # eisit
                if manager.is_in_lobby(channel, nick):
                    if args == "eisit":
                        return bot.say(channel, manager.cancel_join(channel, nick))
                return
            else:
                # !j
                if not manager.is_in_lobby(channel, nick):
                    output = manager.join_game(channel, nick)
                    return bot.say(channel, output)
    elif manager.channel_status(channel, "game"):
        if not args:
            args = ""
        output = manager.process_command(channel, nick, args)
        #log.info("process command called with %s %s %s" % (str(channel), str(nick), str(args)))
        #log.info("output is %s" % str(output))
        if type(output) is list:
            for o in output:
                bot.say(channel, o)
            return
        else:
            if output:
                return bot.say(channel, output)


def command_jatsi(bot, user, channel, args):
    """
    Starts a lobby and marks the user as a lobby-starter.
    """
    nick = getNick(user)
    global manager
    if not manager:
        log.info("manager not found")
        manager = YatzyManager()
    if not manager.channel_status(channel, "lobby") and not manager.channel_status(channel, "game"):
        output = manager.start_lobby_for_channel(channel, nick)
        for o in output:
            bot.say(channel, o)
        return
    else:
        return

# Used for local testing        
#def getNick(user):
#    return user
    

class YatzyManager(object):
    """
    Manages different Yatzy-games across channels
    @author: huqa
    """
    _status = ["lobby","game"]
    _messages = {"wants_to_play": "!j - %s haluaa pelata jatsia. Ilmoittaudu peliin komennolla !j", 
                 "wants_to_play_help": "!j - %s voi aloittaa pelin komennolla (!j aloita) - (!j eisit) peruu pelin (tai peruuttaa ilmoittautumisen)",
                 "joins_game": "!j - %s liittyi peliin!",
                 "lobby_closed": "!j - liittyminen suljettu",
                 "join_canceled": "!j - %s liittyminen peruttu",
                 "game_canceled": "!j - %s peli on peruttu" }
    _games = {}
    _game_status = {}
    _player_lobby = {}
    _lobby_starters = {}
    
    def __init__(self):
        self._games = {}

    def join_game(self, channel, player):
        """
        @type channel: str
        @type player: str  
        """
        if channel and player:
            if self._game_status[channel] is self._status[0]:
                if player not in self._player_lobby[channel]:
                    self._player_lobby[channel].append(player)
                    return self._messages['joins_game'] % str(player)
            else:
                return self._messages['lobby_closed'] % str(player)
                
    def start_lobby_for_channel(self, channel, player):
        """
        Starts a lobby for a channel
        @type channel: str
        @type player: str
        @rtype: list or None  
        """
        if channel and player:
            if channel not in self._game_status:
                self._game_status[channel] = self._status[0]
                self._player_lobby[channel] = []
                self._player_lobby[channel].append(player)
                self._lobby_starters[channel] = player
                output = []
                output.append(self._messages["wants_to_play"] % player)
                output.append(self._messages["wants_to_play_help"] % player)
                return output
            if self._game_status[channel] is not self._status[0] and self._game_status[channel] is not self._status[1]:
                self._game_status[channel] = self._status[0]
                self._player_lobby[channel] = []
                self._player_lobby[channel].append(player)
                self._lobby_starters[channel] = player
                output = []
                output.append(self._messages["wants_to_play"] % player)
                output.append(self._messages["wants_to_play_help"] % player)
                return output
            else:
                return 
        
    def start_game_for_channel(self, channel, player):
        """
        Starts a game for a channel in lobby-mode 
        @type channel: str
        @type player: str
        """
        if channel and player:
            if channel in self._game_status:
                if self._game_status[channel] is self._status[0] and self._game_status[channel] is not self._status[1]:
                    if self.is_lobby_starter(channel, player):
                        self._game_status[channel] = self._status[1]
                        #output = []
                        shuffle(self._player_lobby[channel])
                        game = YatzyGame(self._player_lobby[channel], self, channel)
                        self._games[channel] = game
                        #self._player_lobby[channel] = [] 
                        return game.start_game()
    
    def channel_status(self, channel, status):
        """
        Determines the status of the game for a channel.
        @type channel: str
        @type status: str 
        """
        if channel in self._game_status:
            return self._game_status[channel] == status
        else:
            return False
    
    def cancel_join(self,channel, player):
        """
        Cancels join.
        @type: channel: str
        @type: player: str
        """
        if channel and player:
            if channel in self._game_status:
                if self._game_status[channel] is self._status[0]:
                    if player in self._player_lobby[channel]:
                        idx = 0
                        for a in self._player_lobby[channel]:
                            if a == player:
                                del self._player_lobby[channel][idx]
                                return self._messages['join_canceled'] % str(player)
                            idx = idx + 1
    
    def is_lobby_starter(self,channel, player):
        """
        Is this player the original lobby starter?
        @type channel: str
        @type player: str
        """
        if channel in self._lobby_starters:
            return self._lobby_starters[channel] == player
        else:
            return False
    
    def is_in_lobby(self,channel,player):
        """
        Is the player in the current channels lobby?
        @type channel: str
        @type player: str
        """
        if player in self._player_lobby:
            return player in self._player_lobby[channel]
        else:
            return False

    def stop_lobby(self, channel, player):
        """
        @type channel: str
        @type player: str  
        """
        if self.is_lobby_starter(channel, player):
            self._player_lobby[channel] = [] 
            self._lobby_starters[channel] = ""
            self._game_status[channel] = None
            return self._messages['game_canceled'] % str(player)
            
    def stop_game(self, channel):
        """
        @type channel: str
        @type player: str  
        """
        self._player_lobby[channel] = [] 
        self._lobby_starters[channel] = ""
        self._game_status[channel] = None
        
    def process_command(self, channel, player, args):
        """
        Handles command from each channel and forwards it to the corresponding game
        @type channel: str
        @type player: str 
        @type args: str
        @rtype: list or str or None
        @return: Strings from a YatzyGame
        """
        if channel and player:
            #log.info("games are: %s" % str(self._games))
            if self._games[channel]:
                #log.info("game in channel?")
                game = self._games[channel]
                #log.info("is player turn? %s %s" % (str(player), str(game.is_player_turn(player))))
                if game.is_player_turn(player):
                    #log.info("player turn")
                    #find out what command the player trying to say
                    msg = game.do_player_turn(player, args)
                    return msg
    
    """
    def localtest(self,player="huqa",channel="sk"):
        self.start_lobby_for_channel(channel, player)
        self.join_game(channel, "keke")
        return self.start_game_for_channel(channel, player)
                     
    def huqa_move(self,args):
        return self.process_command("sk", "huqa", args)

    def keke_move(self,args):
        return self.process_command("sk", "keke", args)
    """
class YatzyGame(object):
    """
    A representation of a game of Yatzy
    @author: huqa
    """
    _messages = {"its_your_turn": "!j - %s on sinun vuorosi. Heitä noppia komennolla !j. ",
                 "rolled": "!j - %s heitti %s Yht: %s - heittoja jäljellä: %d",
                 "rolled_some":"!j - %s heitti %s = %s Yht: %s - heittoja jäljellä: %d",
                 "play_help": "",
                 "dice_saved":"!j - %s lukitsee %s",
                 "dice_saved_error":"!j - %s tuollaisia noppia ei olekaan",
                 "dice_already_saved":"!j - %s kaikki nopat on lukittu (hölömö)",
                 "move_list":"!j - %s %s",
                 "score_board":"!j - %s tuloksesi: %s",
                 "move_saved":"!j - %s tallensi tuloksen %s = %s",
                 "option_error":"!j - tuo ei toimi %s",
                 "bonus_get":"!j - %s - sait yläkerta-bonuksen _b",
                 "bonus_not":"!j - %s - et saanut yläkerta-bonusta",
                 "override_move": "valitse nollattava kenttä %s",
                 "overridden": "!j - %s, %s on nollattu",
                 "game_over_1": "!j - peli on päättynyt. Tulokset %s",
                 "game_over_2": "!j - **%s** onnittelut voittajalle!"}
    
    
    def __init__(self, players, manager, channel):
        """
        @type players: list
        """
        # create score cards for the players
        self._score_cards = {}
        self._player_list = []
        for name in players:
            #@var name: str
            self._player_list.append(name)
            self._score_cards[name] = YatzyScoreCard(name) 
        #print self._score_cards
        self._whos_turn = ""
        self._game_is_on = False
        self.manager = manager
        self.channel = channel
            
    def start_game(self):
        """
        @rtype: str
        """
        self._game_is_on = True
        self._whos_turn = self._player_list.pop(0)
        output = []
        output.append(self._messages["its_your_turn"] % self._whos_turn)
        scores = self.build_score_list(self.get_score_card(self._whos_turn))
        output.append(self._messages["score_board"] % (self._whos_turn, scores))
        return output
        
    def change_player(self, output): 
        """
        Changes player
        @type output: list
        """
        self._player_list.append(self._whos_turn)
        self._whos_turn = self._player_list.pop(0)
        _card = self.get_score_card(self._whos_turn)
        _card.reset_rolls()
        _card.reset_saved()
        if _card.all_fields_used():
            #game is over, calculate scores
            all_scores = {}
            for c in self._score_cards:
                scores = self._score_cards[c].get_scores()
                psum = 0
                for field in scores:
                    psum += int(scores[field])
                if self._score_cards[c].gets_upstairs_bonus():
                    psum += 50
                all_scores[c] = psum
            sorted_scores = sorted(all_scores.iteritems(), key=itemgetter(1))
            sorted_scores.reverse()
            rankings = ""
            pos = 1
            for sc in sorted_scores:
                rankings = rankings + "(" + str(pos) + ". " + str(sc[0]) + ": " + str(sc[1]) + ") "
                pos += 1
            output.append(self._messages['game_over_1'] % rankings)
            output.append(self._messages['game_over_2'] % str(sorted_scores[0][0]))
            self.stop_game()
        else:
            output.append(self._messages["its_your_turn"] % self._whos_turn)
            scores = self.build_score_list(_card)
            output.append(self._messages["score_board"] % (self._whos_turn, scores))
        return output
        
    def do_player_turn(self, player, args):
        """
        @type player: str
        @type args: str
        """
        #log.info("do player turn")
        card = self.get_score_card(player)
        if args:
            arg_list = args.split(" ")
            is_digit = args.replace(" ","").isdigit()
            if is_digit:
                # all arguments are numbers
                # should have at least one roll left if saving dice
                if card.rolls_left >= 1:
                    if len(arg_list) <= 5:
                        if self.valid_dices(arg_list, card):
                            card.reset_saved()
                            d_int = [int(a) for a in arg_list if a]
                            card.save_dice(d_int)
                            # return message that the dice are saved
                            output = []
                            output.append(self._messages["dice_saved"] % (str(player), str(d_int)))
                            #remove this to stop auto-roll
                            card.reset_moves()
                            output.append(self.roll_dice(player, card))
                            return output
                        else:
                            # return msg that dices are wrong
                            return self._messages["dice_saved_error"] % str(player)
                else:
                    # no rolls left for saving dice
                    return self._messages['option_error'] % str(player)
            else:
                # user trying to save a score with a letter perhaps
                if len(args) == 1:
                    if args in card.move_list:
                        score = card.get_move_score(args)
                        card.save_move_score(args)
                        index = card.get_field_index(card.get_field_by_key(args))
                        output = []
                        output.append(self._messages['move_saved'] % (str(player), str(card.field_names[index]), str(score)))
                        if card.upstairs_full() and card.gets_upstairs_bonus is False:
                            if card.gets_upstairs_bonus():
                                output.append(self._messages['bonus_get'] % (str(player)))
                        return self.change_player(output)
                    else:
                        #player might be overriding a field
                        if not card.has_rolls_left():
                            if not card.is_field_used(card.get_field_by_key(args)):
                                card.set_score(args, 0)
                                index = card.get_field_index(card.get_field_by_key(args))
                                output = []
                                output.append(self._messages['overridden'] % (str(player), str(str(card.field_names[index]))))
                                return self.change_player(output)
                            else:
                                return self._messages['option_error'] % str(player)
                        
                        else:
                            return self._messages['option_error'] % str(player)
                else:
                    #input too long
                    return self._messages['option_error'] % str(player)
        else:
            # roll dice if throws still left etc.
            return self.roll_dice(player, card)
            
    def roll_dice(self, player, card):
        """
        @type card: YatzyScoreCard
        @type player: str 
        """
        # roll dice if throws still left etc.
        if card.has_rolls_left():
            dices_amount = 5 - len(card.saved_dice)
            #if dices_amount == 0:
                #return message that all dices are already locked
                #return self._messages["dice_already_saved"] % str(player)
            rolled_dice = self._roll_dice(player, dices_amount)
            card.decrease_rolls()
            log.info(rolled_dice)
            # get the sum of the die
            if card.saved_dice:
                dice_together = rolled_dice + card.saved_dice
            else:
                dice_together = rolled_dice
            #Timed the lambda-function and the for-loop, turns out the loop is faster
            #dice_sum = reduce(lambda x,y: x+y, dice_together)
            dice_sum = 0
            for d in dice_together:
                dice_sum = dice_sum + d
            msg = ""
            if dices_amount == 5:
                msg = self._messages["rolled"] % (str(player),str(rolled_dice),str(dice_sum),int(card.rolls_left))
            else:
                msg = self._messages["rolled_some"] % (str(player),str(rolled_dice),str(dice_together),str(dice_sum),int(card.rolls_left))
            # create list of options etc.
            card.set_last_roll(dice_together)
            card.reset_saved()
            card.reset_moves()
            moves = card.check_dice(dice_together)
            if self.moves_are_empty(moves) and not card.has_rolls_left():
                override = self.build_override_list(card)
                ovr_str = self._messages['override_move'] % (str(override))
                msg = msg + " | " + ovr_str
            elif not card.has_rolls_left():
                # a player can override fields if he wants
                move_str = self.build_move_list(moves, card)
                msg = msg + " | " + move_str   
                override = self.build_override_list(card)
                ovr_str = self._messages['override_move'] % (str(override))
                msg = msg + "tai " + ovr_str                 
            else: 
                move_str = self.build_move_list(moves, card)
                msg = msg + " | " + move_str
            return msg
        else:
            return self._messages['option_error'] % str(player)        
        
                

    def moves_are_empty(self, moves):
        upstairs = moves['upstairs']
        downstairs = moves['downstairs']
        if len(upstairs) <= 0:
            for d in downstairs:
                if downstairs[d]:
                    return False
            return True
        else:
            return False
            
                
    def build_move_list(self, moves, card):
        """
        @type moves: dict
        @type card: YatzyScoreCard 
        """ 
        upstairs = moves["upstairs"]
        downstairs = moves["downstairs"]
        move_str = ""
        
        sorted_upstairs = sorted(upstairs)
        
        for u in sorted_upstairs:
            dgt = int(u.replace("s", ""))
            score = dgt * upstairs[u]
            index = card.get_field_index(u)
            card.add_move(card.fields_to_keys[index], score)
            move_str = self.get_move_string(move_str, card, score, index) 

        fields = card.get_fields()
        for d in downstairs:
            if downstairs[d]:
                if d in fields:
                    if d is fields[6]:
                        #one pair
                        d_max = max(downstairs[d])
                        score = d_max * 2
                    elif d is fields[7]:
                        #two pair
                        score = 0
                        for a in downstairs[d]:
                            if downstairs[d][a] >= 4:
                                score = score + (a * 4)
                            elif downstairs[d][a] >= 2:
                                score = score + (a * 2)
                    elif d is fields[8]:
                        #toak
                        d_max = max(downstairs[d])
                        score = (d_max * downstairs[d][d_max])                             
                    elif d is fields[9]:
                        #foak
                        d_max = max(downstairs[d])
                        score = (d_max * downstairs[d][d_max])
                    elif d is fields[10]:
                        #small straight
                        score = 15
                    elif d is fields[11]:
                        #large straight
                        score = 20
                    elif d is fields[12]:
                        #full house
                        score = 0
                        for a in downstairs[d]:
                            score = score + (int(a) * downstairs[d][a])
                    elif d is fields[13]:
                        #chance
                        score = 0
                        for a in downstairs[d]:
                            score = score + int(a) 
                    elif d is fields[14]:
                        #_yatzy
                        score = 50
                    index = card.get_field_index(d)
                    card.add_move(card.fields_to_keys[index], score)
                    move_str = self.get_move_string(move_str, card, score, index) 
        return move_str   
    
    def build_score_list(self, card=None):      
        """
        Builds a formatted string of scores in a score card.
        @type card: YatzyScoreCard
        @rtype: str
        """
        scores = ""
        all_sum = 0
        for field in card.get_fields():
            index = card.get_field_index(field)
            #key = card.fields_to_keys[index]
            name = card.field_names[index]
            all_scores = card.get_scores()
            if card.is_field_used(field):
                scores = scores + "(" + name + " = " + str(all_scores[field]) + ") "
            else:
                scores = scores + "(" + name + ": " + str(all_scores[field]) + ") "
            all_sum = all_sum + all_scores[field] 
        if card.gets_upstairs_bonus():
            all_sum = all_sum + 50
        scores = scores + "Yht: " + str(all_sum)
        return scores
    
    def build_override_list(self,card):
        """
        Builds a formatted string of overridable fields.
        @type card: YatzyScoreCard
        @rtype: str
        """        
        items = ""
        for field in card.get_fields():
            if not card.is_field_used(field):
                index = card.get_field_index(field)
                key = card.fields_to_keys[index]
                name = card.field_names[index]
                if key not in card.move_list: # filter out the ones that are in the moves list
                    items = items + key + "(" + name + ") "
        return items
                    
    def get_move_string(self, move_str, card, score, index):
        """
        @return: A formatted string in form key(field: score)
        @rtype: str
        """
        return move_str + card.fields_to_keys[index] + "(" + card.field_names[index] + ": " + str(score) + ") " 

    def valid_dices(self, dices, card):
        """
        @type dices: list
        @type card: YatzyScoreCard
        """
        #FIXME 
        int_d = []
        for n in dices:
            if n:
                int_d.append(int(n))
        for n in set(int_d):
            # this is wrong e.g. if the player wants to lock only one of a pair
            if int_d.count(n) > card.last_roll.count(n):
                return False
        return True

    def stop_game(self):
        """Stops the game and notifies the game manager"""
        self._game_is_on = False
        self._whos_turn = ""
        self._score_cards = {}
        self._player_list = []
        self.manager.stop_game(self.channel)
        
    def get_score_card(self, player):
        """
        Returns a score card for a player
        @rtype YatzyScoreCard
        """
        if player in self._score_cards:
            return self._score_cards[player]
        
    def _roll_dice(self, roller, dice_amount=5):
        """
        @type roller: str
        @type dice_amount: int
        @rtype list
        """
        if roller == self._whos_turn:
            return [randint(1,6) for a in range(dice_amount)]
        else:
            return None
        
    def is_player_turn(self, player):
        """
        @type player: str
        @rtype bool
        """
        #log.info("whos turn %s" % str(self._whos_turn))
        return player == self._whos_turn
    
            
    def is_number(self,n):
        """
        @type n: str or int or float
        """
        try:
            float(n)
            return True
        except ValueError:
            return False       

class YatzyScoreCard(object):
    """ 
    Yatzy Score card and dice checker
    @author: huqa
    """
    
    _max_rolls = 3
    
    field_names = ["1t",
                   "2t",
                   "3t",
                   "4t",
                   "5t",
                   "6t",
                   "pari",
                   "2paria",
                   "3samaa",
                   "4samaa",
                   "p.suora",
                   "i.suora",
                   "tkasi",
                   "sttma",
                   "jatsi"]
    
    # Name of each field
    _fields = [ "1s",
                "2s",
                "3s",
                "4s",
                "5s",
                "6s",
                "one_pair",
                "two_pair",
                "three_of_a_kind",
                "four_of_a_kind",
                "small_straight",
                "large_straight",
                "full_house",
                "chance",
                "yatzy" ]

    # These are the corresponding keys to the fields for irc
    _keys_to_fields = {'a': 0,
                      'b': 1,
                      'c': 2,
                      'd': 3,
                      'e': 4,
                      'f': 5,
                      'g': 6,
                      'h': 7,
                      'i': 8,
                      'j': 9,
                      'k': 10,
                      'l': 11,
                      'm': 12,
                      'n': 13,
                      'o': 14}
    fields_to_keys = ['a',
                       'b',
                       'c',
                       'd',
                       'e',
                       'f',
                       'g',
                       'h',
                       'i',
                       'j',
                       'k',
                       'l',
                       'm',
                       'n',
                       'o']
    
    def __init__(self, player_name=""):
        self.player_name = player_name
        self._used_fields = {self._fields[0]: False,
                            self._fields[1]: False,
                            self._fields[2]: False,
                            self._fields[3]: False,
                            self._fields[4]: False,
                            self._fields[5]: False,
                            self._fields[6]: False,
                            self._fields[7]: False,
                            self._fields[8]: False,
                            self._fields[9]: False,
                            self._fields[10]: False,
                            self._fields[11]: False,
                            self._fields[12]: False,
                            self._fields[13]: False,
                            self._fields[14]: False}
        self._scores = {self._fields[0]: 0,
                        self._fields[1]: 0,
                        self._fields[2]: 0,
                        self._fields[3]: 0,
                        self._fields[4]: 0,
                        self._fields[5]: 0,
                        self._fields[6]: 0,
                        self._fields[7]: 0,
                        self._fields[8]: 0,
                        self._fields[9]: 0,
                        self._fields[10]: 0,
                        self._fields[11]: 0,
                        self._fields[12]: 0,
                        self._fields[13]: 0,
                        self._fields[14]: 0}
        self.gets_bonus = False
        self.last_roll = []
        self.saved_dice = []
        self.move_list = {}
        self.rolls_left = self._max_rolls
        
        
    def set_last_roll(self, dice):
        if dice:
            self.last_roll = dice
            
    def save_dice(self,dice):
        if dice:
            if len(self.saved_dice) + len(dice) <= 5:
                for d in dice:
                    self.saved_dice.append(int(d))
    
    def reset_saved(self):
        self.saved_dice = []
    
    def reset_rolls(self):
        self.rolls_left = self._max_rolls
        
    def has_rolls_left(self):
        return self.rolls_left > 0
    
    def get_fields(self):
        return self._fields
        
    def decrease_rolls(self):
        if self.rolls_left > 0:
            self.rolls_left = self.rolls_left - 1
    
    def add_move(self, key, score):
        self.move_list[key] = score

    def reset_moves(self):
        self.move_list = {}
    
    def save_move_score(self, key):
        if key in self.move_list:
            self.set_score(key, self.get_move_score(key))
            self.reset_moves()
    
    def get_move_score(self, key):
        if key in self.move_list:
            return self.move_list[key]

    def is_field_used(self, field):
        if field in self._used_fields:
            return self._used_fields[field]
      
    def all_fields_used(self):
        for f in self._used_fields:
            if self._used_fields[f] is False:
                return False
        return True
    
    def get_field_by_key(self, key):
        if key in self._keys_to_fields:
            return self._fields[self._keys_to_fields[key]]
        else:
            return None

    def get_field_index(self, field):
        if field in self._fields:
            return self._fields.index(field)
        else:
            return None

    def set_score(self, key, score=0):
        field = self.get_field_by_key(key)
        if field:
            self._scores[field] = score
            self._used_fields[field] = True
            
    def get_score(self, field):
        return self._scores[field]
            
    def get_scores(self):
        return self._scores
       
    def upstairs_full(self):
        for i in range(6):
            if not self.is_field_used(self._fields[i]):
                return False
        return True
    
    def gets_upstairs_bonus(self):
        score = 0
        for i in range(6):
            if self.is_field_used(self._fields[i]):
                score = score + self.get_score(self._fields[i])
        if score >= 63:
            self.gets_bonus = True
            return True
        else:
            return False
    
    def check_dice(self, dice):
        """Checks a list of dice for combination of moves"""
        dice_amount = len(dice)
        if dice_amount <= 0:
            return []
        
        combinations = {}
        upstairs_results = self.calculate_upstair_combinations(dice)
        downstairs_results = self.calculate_downstair_combinations(dice)
        combinations['upstairs'] = upstairs_results
        combinations['downstairs'] = downstairs_results
        return combinations

    def calculate_upstair_combinations(self,dice):
        """Fetches number counts on a dice-set"""
        results = {}
        for n in range(1,7):
            if dice.count(n) > 0:
                # Let's not count used fields to the results
                if not self.is_field_used(self._fields[(n-1)]):
                    results[self._fields[(n-1)]] = dice.count(n)
        return results
                    
    def calculate_downstair_combinations(self,dice):
        results = {}
        for n in range(7,16):
            # Let's not count used fields to the results
            if not self.is_field_used(self._fields[(n-1)]):
                if n is 7:
                    results[self._fields[(n-1)]] = self._one_pair(dice)
                elif n is 8:
                    results[self._fields[(n-1)]] = self._two_pair(dice)
                elif n is 9:
                    results[self._fields[(n-1)]] = self._three_of_a_kind(dice)
                elif n is 10:
                    results[self._fields[(n-1)]] = self._four_of_a_kind(dice)
                elif n is 11:
                    results[self._fields[(n-1)]] = self._small_straight(dice)
                elif n is 12:
                    results[self._fields[(n-1)]] = self._large_straight(dice)
                elif n is 13:
                    results[self._fields[(n-1)]] = self._full_house(dice)
                elif n is 14:
                    #chance
                    results[self._fields[(n-1)]] = dice
                elif n is 15:
                    results[self._fields[(n-1)]] = self._yatzy(dice)
        return results
    
    def _one_pair(self, dice):
        results = {}
        for d in range(1,7):
            if dice.count(d) >= 2:
                results[d] = dice.count(d)
        return results
    
    def _two_pair(self, dice):
        results = self._one_pair(dice)
        if len(results) >= 2:
            return results
        else:
            # there can also be 4-of-a-kind two pairs
            for d in results:
                if results[d] >= 4:
                    return results
            return {}
            
    def _three_of_a_kind(self, dice):
        results = {}
        for d in range(1,7):
            if dice.count(d) >= 3:
                results[d] = 3
        return results        
    
    def _four_of_a_kind(self, dice):
        results = {}
        for d in range(1,7):
            if dice.count(d) >= 4:
                results[d] = 4
        return results  
    
    def _small_straight(self, dice):
        small_st = [1,2,3,4,5]
        sorted_dice = sorted(dice)
        return small_st == sorted_dice

    def _large_straight(self, dice):
        large_st = [2,3,4,5,6]
        sorted_dice = sorted(dice)
        return large_st == sorted_dice
    
    def _full_house(self, dice):
        results = {}
        pair_used = False
        for d in range(1,7):
            if dice.count(d) == 2 and pair_used is False:
                results[d] = dice.count(d)
                pair_used = True
            elif dice.count(d) == 3:
                results[d] = dice.count(d)
        if len(results) == 2:
                return results
        else:
                return {}
        
    def _yatzy(self, dice):
        results = {}
        for d in range(1,7):
            if dice.count(d) == 5:
                results[d] = dice.count(d)
        return results 
    
