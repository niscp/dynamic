from question_value import Question_value
from next_question import Next_question

def getQuestion():
    q = Question_value()
    result = q.get()
    if result:
        return result
    return None


def getQuestionbyId(id):
    q = Question_value(aid=id)
    result = q.getQuestionbyId()
    if result:
        return result
    return None

def find_next_question(id,answer):
    n = Next_question(question_id=id)
    result = n.getNextquestionId()
    return result

def get_all_link():
    n = Next_question()
    result = n.get()
    return result


def insert_question(question,option_one,option_two,option_three,option_four):
    q = Question_value(question=question,option_one=option_one,option_two=option_two,
                       option_three=option_three,option_four=option_four)
    result = q.insert()
    return result


