class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        current_question =self.q_list[self.q_number].text
        current_answer =self.q_list[self.q_number].answer
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question}(True or False)")
        self.check_answer(user_answer,current_answer)

    def still_has_question(self):
       return self.q_number < len(self.q_list)

    def check_answer(self,user_answer,current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score+=1
            print('Congrats! You are right!')

        else:
            print('Sorry, you are wrong!')
        print(f"The correct answer is {current_answer}")
        print(f'Your current score is: {self.score}/{self.q_number}.\n')

