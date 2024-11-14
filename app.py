import streamlit as st
import pandas as pd
import random

# Load questions from CSV
questions_df = pd.read_csv('questions.csv')
questions = questions_df.to_dict('records')

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_times' not in st.session_state:
    st.session_state.question_times = []

# Function to show a question
def show_question():
    question = questions[st.session_state.current_question]
    st.write(f"### {question['pregunta']}")
    answers = [
        question['respuesta_correcta'],
        question['respuesta_incorrecta1'],
        question['respuesta_incorrecta2'],
        question['respuesta_incorrecta3']
    ]
    random.shuffle(answers)
    for answer in answers:
        if st.button(answer):
            handle_answer(answer)

# Function to handle an answer
def handle_answer(answer):
    question = questions[st.session_state.current_question]
    if answer == question['respuesta_correcta']:
        st.session_state.score += 1
    st.session_state.current_question += 1
    if st.session_state.current_question < len(questions):
        show_question()
    else:
        show_game_over()

# Function to show game over screen
def show_game_over():
    st.write("## ¡Juego Terminado!")
    st.write(f"Puntuación Final: {st.session_state.score} de {len(questions)}")
    st.write(f"Preguntas Intentadas: {len(questions)}")

# Main app logic
st.title("DesaFasia")
if st.session_state.current_question < len(questions):
    show_question()
else:
    show_game_over()
