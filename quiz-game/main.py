from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from random import shuffle


def main():
    question_bank = []
    for qa in question_data:
        question_bank.append(Question(qa['question'], qa['correct_answer']))

    shuffle(question_bank)

    qb = QuizBrain(question_bank)
    while qb.still_has_question() and qb.alive:
        qb.next_question()
    if qb.alive:
        print(f"Congratulations, you have completed the quiz with a score of {qb.score}")


if __name__ == "__main__":
    main()
