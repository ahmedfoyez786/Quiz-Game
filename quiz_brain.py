class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number} : {current_question.text}. (True/False)? :").lower()
        self.check_answer(user_ans, current_question.answer)

    def still_has_question(self):
        if self.question_number != len(self.question_list):
            return True
        else:
            return False

    def check_answer(self,user_answer, correct_answer ):
        if user_answer == correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That is Wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")


