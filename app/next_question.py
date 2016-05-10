__author__ = 'Nishank Singh'

from app import mysql
from flask import jsonify


class Next_question:
    def __init__(self, nid=None, question_id=None, option_one=None, option_two=None,
                 option_three=None, option_four=None, soft_delete=None):
        self.nid = nid
        self.question_id = question_id
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


    def getNextquestionId(self):
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from next_question where soft_delete = 0 and question_id = "+str(self.question_id))
        data = cursor.fetchall()
        my_question = []
        for i in data:
            self.nid = i[0]
            self.option_one = i[2]
            self.option_two = i[3]
            self.option_three = i[4]
            self.option_four = i[5]
            my_question.append({'nid':self.nid,
                            'option_one':self.option_one,
                            'option_two':self.option_two,
                            'option_three':self.option_three,
                            'option_four':self.option_four})
        return my_question

    def get(self):
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from next_question where soft_delete = 0")
        data = cursor.fetchall()
        my_question = []
        for i in data:
            self.nid = i[0]
            self.option_one = i[2]
            self.option_two = i[3]
            self.option_three = i[4]
            self.option_four = i[5]
            my_question.append({'nid':self.nid,
                            'option_one':self.option_one,
                            'option_two':self.option_two,
                            'option_three':self.option_three,
                            'option_four':self.option_four})
        return my_question
