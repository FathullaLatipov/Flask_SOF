# Импортируем нашу Flask
from flask import Flask, render_template, request, redirect, url_for

# Обьект для Flask приложения
app = Flask(__name__)

# Простейшая база данных для хранения вопросов и ответов
questions = [
                {'id': 1, 'title': 'Как использовать Flask?', 'content': 'Я новичок и я хз как начать?'},
                {'id': 2, 'title': 'Что такое Django?', 'content': 'Я слышал про django но я хз?'}
            ]

answers = [
                {'id': 1, 'question_id': 1, 'content': 'Просто скачайте Flask через команду pip install flask'},
                {'id': 2, 'question_id': 2, 'content': 'Просто скачайте Django через команду pip install django'}
          ]


# Создаем первый url на котором мы покажем все вопросы
@app.route('/')
def home():  # В Django как бы наш views.py
    return render_template('index.html', questions=questions)

# Страница с деталями вопроса и ответами
@app.route('/question/<int:question_id>')
def question(question_id):
    question = next((q for q in questions if q['id'] == question_id), None)
    if question:
        question_answers = [a for a in answers if a['question_id'] == question_id]
        return render_template('question.html', question=question, answers=question_answers)
    else:
        return 'Вопрос не найден'

# Страница для добавления нового вопроса
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        new_question = {
            'id': len(questions) + 1,
            'title': title,
            'content': content
        }

        questions.append(new_question)
        return redirect(url_for('home'))
    else:
        return render_template('ask.html')

app.run(debug=True)