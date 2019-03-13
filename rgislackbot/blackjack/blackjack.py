from itertools import product
import random


class Blackjack(object):
    current_games = {}

    def create_deck(self):
        suits = [':spades:', ':hearts:', ':clubs:', ':diamonds:']
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck = list(product(suits, cards))
        return deck

    def create_new_game(self, user):
        deck = self.create_deck()
        random.shuffle(deck)

        self.current_games[user] = {
            "deck": deck,
            "dealer": [],
            "player": [],
            "finished": False
        }

    def get_points(self, cards):
        return 0

    def player_hit(self, user):
        if user not in self.current_games:
            return self.response_message("You have not currently started a game.")

        if self.current_games[user]['finished']:
            return self.response_message("Current game already finished.")

        self.current_games[user]['player'].append(self.current_games[user]['deck'].pop(0))

        player_points = self.get_points(self.current_games[user]['player'])

        if player_points > 21:
            self.current_games[user]['finished'] = True
            return self.response_message("You busted!")

        if player_points == 21:
            self.current_games[user]['finished'] = True
            return self.response_message("You win Blackjack!")

    def response_message(self, message):
        pass

    def handle_command(self, command, channel, user):
        pass


x = Blackjack()
x.create_new_game('Brandon')

print(x.current_games)