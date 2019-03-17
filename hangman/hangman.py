import random


class Hangman(object):
    def __init__(self, *args, **kwargs):
        self.words = ['3dhubs']

        """
        If args are passed into the class as a dict then use those.

        This is to facilitate creating a new instance using values from the frontend.
        """
        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])

        """
        If there are keyword arguments then use those.
        """
        for key in kwargs:
            setattr(self, key, kwargs[key])

        """
        Some default vales to apply if not present.
        """
        if 'guesses' not in self.__dict__:
            # score will be a multiple of this value * 2
            self.guesses = 5

        if 'guess_word' not in self.__dict__:
            self.guess_word = self.get_random_word()

        if 'display_word' not in self.__dict__:
            self.display_word = self.get_display_word()

        self.game_won = False

    def get_random_word(self):
        """
        Returns a random word.
        """
        return random.choice(self.words)

    def get_display_word(self):
        """
        Returns a list of spaces equal to the length of the current guess_word.
        """
        return list(len(self.guess_word) * ('_'))

    def check_state(self):
        """
        Check if the player has won the game.
        """
        if self.guesses <= 0:
            print('You lose')
            self.game_won = False
        elif '_' not in self.display_word:
            print('You win')
            self.game_won = True

    def make_guess(self, guess):
        if self.game_won is False and self.guesses >= 0:
            self.guesses -= 1
            # Situation where guess is one char long.
            if len(guess) == 1:
                # Get the index value of chars that match the guess.
                index_values = [i for i, x in enumerate(
                    self.guess_word) if x == guess]
                # Set correct characters.
                for i in index_values:
                    self.display_word[i] = guess

            # Situation where the guess is the lenght of the word.
            if len(guess) == len(self.guess_word):
                if ''.join(self.guess_word) == guess:
                    self.display_word = ''.join(self.guess_word)

            # Update game state.
            self.check_state()


if __name__ == "__main__":
    # testing passing in values
    h = Hangman({
        'guesses': 5
    })
    print(h.display_word)

    # faking a win
    # h.display_word = h.guess_word
    # print(h.check_state(), h.game_won)

    # pretend game
    # move 1
    print(h.make_guess('x'))
    print(h.display_word)

    # move 2
    print(h.make_guess('h'))
    print(h.display_word)

    # move 3
    print(h.make_guess('s'))
    print(h.display_word)

    # move 4
    print(h.make_guess('3'))
    print(h.display_word)

    # move 5
    print(h.make_guess('b'))
    print(h.display_word)

    print(h.make_guess('a'))
    print(h.display_word)

    print(h.guesses)
