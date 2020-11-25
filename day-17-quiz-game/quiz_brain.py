class QuizBrain:

    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.question_number = 0
        self.score = 0
        self.alive = True


    def next_question(self):
        answer = input(f"Q.{self.question_number+1}: {self.question_bank[self.question_number].text} (True/False)? ")
        self.check_answer(self.question_bank[self.question_number].answer, answer)


    def still_has_question(self):
        return self.question_number < len(self.question_bank)


    def check_answer(self, q_answer, user_answer):
        if q_answer.lower() == user_answer.lower():
            self.score += 1
            print(f"You're right! Your score is {self.score}/{len(self.question_bank)}")
            self.question_number += 1
        else:
            self.alive = False
            print(f"You're wrong, your score was {self.score}/{len(self.question_bank)}!")
