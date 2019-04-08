from itertools import product
import random


class Game(object):
    def __init__(self):
        self.deck = self.generate_deck()
        self.values = {
            'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'J': 10, 'Q': 10, 'K': 10
        }
        self.finished = False
        self.player_cards = []
        self.dealer_cards = []

    @staticmethod
    def generate_deck():
        suits = [':spades:', ':hearts:', ':clubs:', ':diamonds:']
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck = list(product(suits, cards))
        random.shuffle(deck)
        return deck

    def start_game(self):
        for n in range(0, 2):
            self.player_hit()
            self.dealer_hit()

    def player_hit(self):
        self.player_cards.append(self.deck.pop())

    def dealer_hit(self):
        self.dealer_cards.append(self.deck.pop())

    def get_player_score(self):
        score = 0
        for (suit, card) in self.player_cards:
            score += self.values[card]
        return score

    def get_dealer_score(self):
        score = 0
        for (suit, card) in self.dealer_cards:
            score += self.values[card]
        return score

    def player_card_string(self):
        output = []
        for (suit, card) in self.player_cards:
            output.append('%s %s' % (suit, card))
        return ', '.join(output)


class Blackjack(object):
    current_games = {}

    def create_new_game(self, user):
        self.current_games[user] = Game()
        self.current_games[user].start_game()
        self.response_message("Game started! Your cards: %s, Score: %d" % (self.current_games[user].player_card_string(), self.current_games[user].get_player_score()))

    def get_game(self, user):
        if user not in self.current_games:
            return None

        return self.current_games[user]

    def player_hit(self, user):
        current_game = self.get_game(user)

        if not current_game:
            return self.response_message("You have not currently started a game.")

        if current_game.finished:
            return self.response_message("Current game already finished.")

        current_game.player_hit()

        player_points = current_game.get_player_score()
        if player_points > 21:
            current_game.finished = True
            return self.response_message("You busted!")
        elif player_points == 21:
            current_game.finished = True
            return self.response_message("You win Blackjack!")
        else:
            return self.response_message("Your move, current score: %d" % player_points)

        return None

    def player_stand(self):
        pass

    def response_message(self, message):
        print(message)
        return True

    def handle_command(self, command, channel, user):
        pass


x = Blackjack()
x.create_new_game('Brandon')

x.player_hit('Brandon')
x.player_hit('Brandon')
x.player_hit('Brandon')
x.player_hit('Brandon')