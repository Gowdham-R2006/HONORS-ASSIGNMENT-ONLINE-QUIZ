from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["Python", "JavaScript", "C++", "Java"],
        "answer": "JavaScript"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Retrieve user answers
        user_answers = request.form
        score = 0
        total_questions = len(quiz_questions)

        # Calculate the score
        for i, question in enumerate(quiz_questions):
            if question['answer'] == user_answers.get(f'question-{i}'):
                score += 1

        # Redirect to the result page
        return redirect(url_for('result', score=score, total=total_questions))

    return render_template('quiz.html', questions=quiz_questions)

@app.route('/result')
def result():
    score = request.args.get('score', type=int)
    total = request.args.get('total', type=int)
    return render_template('result.html', score=score, total=total)

if __name__ == '__main__':
    app.run(debug=True)
