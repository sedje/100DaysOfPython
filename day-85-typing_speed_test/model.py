import random
# keep track of CPM And WPM
MAX_LL = 6


class WordList:
    def __init__(self):
        self.highscore = HighScore()
        self.current_word = ''
        self.wordlist = []
        for word in open('wordlist.txt').readlines():
            self.wordlist.append(word.strip())

        self.line_position = 0
        self.lines = []
        for i in range(MAX_LL*3):
            word = random.choice(self.wordlist).lower()
            if (i+1) % MAX_LL == 0:
                word = f"{word}\n"
            self.lines.append(word)

    def get_word(self):
        return self.lines[self.line_position]

    def check_word(self, word=None):
        word_correct = False
        if word:
            if word.strip() == self.lines[self.line_position].strip():
                word_correct = True

            if self.line_position < MAX_LL-1:
                self.line_position += 1
            else:
                self.line_position = 0
                self.get_newline()
        return word_correct

    def get_current_line(self):
        return self.lines

    def get_newline(self):
        for i in range(MAX_LL):
            del self.lines[0]
            word = random.choice(self.wordlist).lower()
            if (i + 1) % MAX_LL == 0:
                word = f"{word}\n"
            self.lines.append(word)

        return self.lines


class HighScore:
    def __init__(self):
        self.highscore = 0
        self.cpm = 0

    def increase_highscore(self, word_length):
        self.highscore += 1
        # Remove additional space/line end from word_length
        self.cpm += word_length-2

    def get_highscore(self):
        return [self.highscore, self.cpm]

    def reset(self):
        self.highscore = 0
        self.cpm = 0
