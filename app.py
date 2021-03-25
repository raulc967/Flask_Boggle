from boggle import Boggle
import threading
from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)

boggle_game = Boggle()
app.secret_key = 'apple1234!'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/board')
def board():
    return render_template('board.html', board=session['board'], correct=session['correct'], high_score=session['high_score'])

@app.route('/start')
def start():
    session['board'] = boggle_game.make_board()
    session['correct'] = 0
    session['high_score'] = 0
    return redirect('http://127.0.0.1:5000/board')

@app.route('/restart')
def restart():
    session['board'] = boggle_game.make_board()
    session['correct'] = 0
    return redirect('http://127.0.0.1:5000/board')

@app.route('/check', methods=['POST'])
def check():
    guess = request.form['guess']
    result = boggle_game.check_valid_word(session['board'], guess)
    if result == 'ok':
        session['correct'] = session['correct'] + 1
        if session['correct'] > session['high_score']:
            session['high_score'] = session['correct']
    return redirect("http://127.0.0.1:5000/board")
