__author__ = 'Nishank Singh'

from app import mysql


class Question_value:
    def __init__(self, aid=None, question=None, option_one=None, option_two=None,
                 option_three=None, option_four=None, soft_delete=None):
        self.aid = aid
        self.question = question
        self.option_one = option_one
        self.option_two = option_two
        self.option_three = option_three
        self.option_four = option_four
        self.soft_delete = soft_delete

    def getQuestionAll(self):
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from question_value")
        data = cursor.fetchall()
        if data is None:
            return False
        else:
            return data


    def getQuestionbyId(self):
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from question_value where soft_delete = 0 and aid = "+str(self.aid))
        data = cursor.fetchall()
        my_question = []
        for i in data:
            self.aid = i[0]
            self.question = i[1]
            self.option_one = i[2]
            self.option_two = i[3]
            self.option_three = i[4]
            self.option_four = i[5]
            my_question.append({'aid':self.aid,
                         'question':self.question,
                            'option_one':self.option_one,
                            'option_two':self.option_two,
                            'option_three':self.option_three,
                            'option_four':self.option_four})
        return my_question


    def get(self):
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from question_value where soft_delete = 0")
        data = cursor.fetchall()
        my_question = []
        for i in data:
            self.aid = i[0]
            self.question = i[1]
            self.option_one = i[2]
            self.option_two = i[3]
            self.option_three = i[4]
            self.option_four = i[5]
            my_question.append({'aid':self.aid,
                         'question':self.question,
                            'option_one':self.option_one,
                            'option_two':self.option_two,
                            'option_three':self.option_three,
                            'option_four':self.option_four})
        return my_question


    def insert(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into question_value(question,option_one,option_two,option_three,option_four) values("'+self.question+'","'+self.option_one+'","'+self.option_two+'","'+self.option_three+'","'+self.option_four+'")')
        conn.commit()
        return 'success'

