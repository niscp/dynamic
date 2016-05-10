from app import app
from flask import jsonify, render_template,request,redirect,url_for,session
from app import interface
import flask
from webargs.core import Arg
from webargs.flaskparser import parser

app.secret_key = '#UIJDDNFKDLKSNSKNFFNNLNE'

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/survey')
def survey():
    result = interface.getQuestion()
    a = {'data': result}
    return jsonify(a)


@app.route('/survey/<id>')
def survey_one(id):
    flask.session['rep'] = []
    result = interface.getQuestionbyId(id)
    return render_template('question.html', data=result)

@app.route('/end')
def end():
    data = flask.session['rep']
    a = {'result':data}
    return 'questions ended'

@app.route('/add',methods={'GET','POST'})
def add():
    if request.method == 'POST':
        question = request.form['question']
        option_one = request.form['option_one']
        option_two = request.form['option_two']
        option_three = request.form['option_three']
        option_four = request.form['option_four']
        res = interface.insert_question(question,option_one,option_two,option_three,option_four)
        if res:
            a = {'data':res}
            return jsonify(a)
        return 'failed'
    return render_template('new_question.html')


@app.route('/next',methods={'GET','POST'})
def next_question():
    if request.method == 'POST':
        answer = request.form['answer']
        question = request.form['question']
        a = {'question':question,'submit':answer}
        flask.session['rep'].append(a)
        d = interface.find_next_question(question,answer)
        next = 0
        if answer == '1':
            next = d[0]['option_one']
        if answer == '2':
            next = d[0]['option_two']
        if answer == '3':
            next = d[0]['option_three']
        if answer == '4':
            next = d[0]['option_four']
        if next == '0' or next == 0:
            return redirect(url_for('end'))
        else:
            return redirect(url_for('survey_one',id=next))


@app.route('/api/questions/all',methods={'GET','POST'})
def all_question():
    result = interface.getQuestion()
    a = {'data': result}
    return jsonify(a)


@app.route('/api/question/<id>',methods={'GET','POST'})
def get_question(id):
    result = interface.getQuestionbyId(id)
    a = {'data': result}
    return jsonify(a)


@app.route('/api/questions/add',methods={'GET','POST'})
def add_question():
    args = {
        'question': Arg(str, required=True),
        'option_one': Arg(str, required=True),
        'option_two': Arg(str, required=True),
        'option_three': Arg(str),
        'option_four': Arg(str)
    }
    data = parser.parse(args, request)
    res = interface.insert_question(data['question'],data['option_one'],data['option_two'],data['option_three'],data['option_four'])
    if res:
        a = {'data':res}
        return jsonify(a)
    return 'failed'


#        a = {'answer':answer,
#             'question':question,
#             'next':d,
#            'my next':next}
#        return jsonify(a)

