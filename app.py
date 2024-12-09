from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for sessions

DB_PATH = 'questions.db'  # Path to your database
TOTAL_QUESTIONS = 9  # Update based on your total questions

# Helper function to get a question by its ID
def get_question_by_id(question_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions WHERE id = ?", (question_id,))
    question = cursor.fetchone()
    conn.close()
    return question

@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question_page(question_id):
    if 'responses' not in session:
        session['responses'] = []

    if request.method == 'POST':
        user_response = int(request.form.get('response'))
        session['responses'].append(user_response)

        # If last question, redirect to results
        if question_id == TOTAL_QUESTIONS:
            return redirect(url_for('results'))

        return redirect(url_for('question_page', question_id=question_id + 1))

    question = get_question_by_id(question_id)
    if not question:
        return "Question not found", 404

    return render_template('question.html', question_text=question[1],
                           jamais=question[2], parfois=question[3],
                           souvent=question[4], toujours=question[5], question_id=question_id)

@app.route('/results')
def results():
    total_score = sum(session['responses'])
    session.pop('responses', None)  # Clear responses after displaying results
    return render_template('results.html', total_score=total_score)

if __name__ == '__main__':
    app.run(debug=True)
