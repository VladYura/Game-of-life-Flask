from flask import Flask, render_template
from game_of_life import *

app = Flask(__name__)  # Экземпляр сервера


@app.route('/')
def index():
    GameOfLife(25, 25)
    return render_template('index.html')


@app.route('/live')
def live():
    game = GameOfLife()
    if game.counter > 0:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game, life=game.counter)


if __name__ == '__main__':
    app.run(debug=True)  # Запуск сервера
