from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for sessions

DB_PATH = 'questions.db'  # Path to your database

# Helper function to get a question by its ID
def get_question_by_id(question_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions WHERE id = ?", (question_id,))
    question = cursor.fetchone()
    conn.close()
    return question

# Helper function to get total number of questions
def get_total_questions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM questions")
    total = cursor.fetchone()[0]
    conn.close()
    return total

@app.route('/')
def welcome_page():
    return render_template('welcome.html')

@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question_page(question_id):
    if 'responses' not in session:
        session['responses'] = []

    total_questions = get_total_questions()

    if request.method == 'POST':
        user_response = request.form.get('response')
        
        if user_response is not None:  # Ensure a response was provided
            try:
                # Convert response to integer and store it in session
                session['responses'].append(int(user_response))  
                session.modified = True  # Mark session as modified
            except ValueError:
                print(f"Invalid response received: {user_response}")  # Debugging line
        
        # If it's the last question, redirect to results page
        if question_id == total_questions:
            return redirect(url_for('results'))

        # Otherwise, go to the next question
        return redirect(url_for('question_page', question_id=question_id + 1))

    question = get_question_by_id(question_id)
    if not question:
        return "Question not found", 404

    return render_template('question.html', 
                           question_text=question[1], 
                           jamais=question[2], 
                           parfois=question[3], 
                           souvent=question[4], 
                           toujours=question[5], 
                           question_id=question_id)

@app.route('/results')
def results():
    responses = session.get('responses', [])
    try:
        total_score = sum(map(int, responses))  # Ensure all values are integers
    except ValueError as e:
        print(f"Error when calculating score: {e}")
        total_score = 0

    # Generate feedback based on the score
    if 0 <= total_score <= 10:
        feedback = "Bien-être élève vous semblez bien gérer vos émotions et vos stress. Continuez."
    elif 11 <= total_score <= 20:
        feedback = "Bien-être modéré vous pourrez ressentir un certain stress ou des fluctuations émotionnelles mais elles restent gérables. Pensez à des activités relaxantes."
    else:
        feedback = "Risque élevé de détresse vous montrez des signes de stress ou de mal-être significatifs, une discussion avec un professionnel est recommandée."

    session.pop('responses', None)  # Clear responses after displaying results
    return render_template('results.html', total_score=total_score, feedback=feedback)


if __name__ == '__main__':
    app.run(debug=True)
