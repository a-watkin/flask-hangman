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
            self.guesses = 5

        if 'hidden_word' not in self.__dict__:
            self.hidden_word = self.get_random_word()

        if 'display_word' not in self.__dict__:
            print('getting new display word?')
            self.display_word = self.get_display_word()

        self.game_won = False
        # Number of guesses determines the score out of 100
        self.score = (self.guesses * 2) * 10

    def __str__(self):
        rtn_list = ['Hangman object:\n']
        for attr in self.__dict__:
            if attr is not 'db':
                rtn_srt = str(attr) + ': ' + \
                    str(self.__dict__[attr]) + '\n'
                rtn_list.append(rtn_srt)
        return ''.join(rtn_list)

    def get_class_as_dict(self):
        return self.__dict__

    def get_random_word(self):
        """
        Returns a random word.
        """
        return random.choice(self.words)

    def get_display_word(self):
        """
        Returns a list of spaces equal to the length of the current hidden_word.
        """
        return list(len(self.hidden_word) * ('_'))

    def check_state(self):
        """
        Check if the player has won the game.
        """

        if self.guesses < 0:
            print('You lose')
            self.game_won = False
        elif '_' not in self.display_word:
            print('You win')
            self.game_won = True
            print(self.guesses, self.score, self.game_won)

        self.get_score()

    def get_score(self):
        """
        Updates the game score.
        """
        # I am counting a correct guess of the word from start as a score of 100.
        if self.guesses == 4 and self.game_won is True:
            self.score = 100
        elif self.guesses > 0:
            # Each guess out of 5 loses 20 points
            self.score = (self.guesses * 2) * 10
        else:
            self.score = 0

    def check_current_guess(self, guess):
        """
        Checks a single character guess or an entire word guess.
        """
        if self.game_won is False and self.guesses >= 0:
            # Situation where guess is one char long.
            if len(guess) == 1:
                # Get the index value of chars that match the guess.
                index_values = [i for i, x in enumerate(
                    self.hidden_word) if x == guess]
                # Set correct characters.
                for i in index_values:
                    self.display_word[i] = guess

            # Situation where the guess is the lenght of the word.
            elif len(guess) == len(self.hidden_word):
                if ''.join(self.hidden_word) == guess:
                    self.display_word = ''.join(self.hidden_word)

            if guess not in self.hidden_word:
                self.guesses -= 1

            # Update game state.
            self.check_state()


if __name__ == "__main__":
    # testing passing in values
    h = Hangman({
        'guesses': 5,
        'display_word': [
            "3",
            "d",
            "_",
            "_",
            "_",
            "_"
        ]
    })

    print(h)

    # pretend game
    # move 1
    # print('1', h.check_current_guess('x'))
    # print(h.display_word)

    # # move 2
    # print('2', h.check_current_guess('h'))
    # print(h.display_word)

    # # move 3
    # print('3', h.check_current_guess('s'))
    # print(h.display_word)

    # # move 4
    # print('4', h.check_current_guess('3d'))
    # print(h.display_word)

    # # move 5 game over
    # print('5', h.check_current_guess('b'))
    # print(h.display_word)

    # print(h.check_current_guess('a'))
    # print(h.display_word)

    # print(h.guesses)

    # print(h)
