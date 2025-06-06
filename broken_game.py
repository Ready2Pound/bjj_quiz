# modularized version wont function as expected. 

import random

questions = [
  {
    "question": "What does BJJ stand for?",
    "options": ["Brazilian Jiu-Jitsu", "Boxing Jiu-Jitsu", "Battle Jutsu Journey", "Brazilian Judo Jitsu"],
    "correct_answer": "Brazilian Jiu-Jitsu"
  },
  {
    "question": "Who is considered the founder of Brazilian Jiu-Jitsu?",
    "options": ["Helio Gracie", "Rickson Gracie", "Jigoro Kano", "Carlos Gracie"],
    "correct_answer": "Helio Gracie"
  },
  {
    "question": "What is the primary goal in BJJ competitions?",
    "options": ["Knockout", "Pin opponent", "Submit opponent", "Score points by takedowns"],
    "correct_answer": "Submit opponent"
  },
  {
    "question": "Which position is often referred to as the 'guard' in BJJ?",
    "options": ["Mount", "Back control", "Side control", "Open or closed guard"],
    "correct_answer": "Open or closed guard"
  },
  {
    "question": "What is a common submission move in BJJ?",
    "options": ["Armbar", "Kimura", "Triangle choke", "All of the above"],
    "correct_answer": "All of the above"
  },
  {
    "question": "Which belt color typically signifies a beginner level in BJJ?",
    "options": ["Blue", "White", "Black", "Purple"],
    "correct_answer": "White"
  },
  {
    "question": "What does the term 'passing the guard' refer to?",
    "options": ["Swapping positions", "Moving from guard to mount", "Getting past the opponent's legs", "Sweeping"],
    "correct_answer": "Getting past the opponent's legs"
  },
  {
    "question": "Which part of the body is primarily targeted in a triangle choke?",
    "options": ["Neck", "Arm", "Legs", "Torso"],
    "correct_answer": "Neck"
  },
  {
    "question": "What is 'sweeping' in BJJ?",
    "options": ["Reversing positions from bottom to top", "Substituting submission moves", "Moving from mount to back control", "Transitioning between guard positions"],
    "correct_answer": "Reversing positions from bottom to top"
  },
  {
    "question": "How long is a typical BJJ match at the adult competitive level?",
    "options": ["5 minutes", "10 minutes", "15 minutes", "20 minutes"],
    "correct_answer": "10 minutes"
  },
  {
    "question": "In BJJ, 'mount' refers to which position?",
    "options": ["Opponent’s back on the ground", "Sitting cross-legged", "Straddling the opponent's torso", "Standing control"],
    "correct_answer": "Straddling the opponent's torso"
  },
  {
    "question": "What is the primary benefit of practicing BJJ?",
    "options": ["Self-defense", "Physical fitness", "Mental discipline", "All of the above"],
    "correct_answer": "All of the above"
  },
  {
    "question": "Which move is used to escape from the back control position?",
    "options": ["Trap and roll", "Bridge escape", "Knee slide escape", "All of the above"],
    "correct_answer": "All of the above"
  },
  {
    "question": "What is 'nogi' in Brazilian Jiu-Jitsu?",
    "options": ["Training without gi clothes", "Using only leg submissions", "Practicing with a belt", "Focusing on striking techniques"],
    "correct_answer": "Training without gi clothes"
  },
  {
    "question": "Which belt color indicates an intermediate level in BJJ?",
    "options": ["Purple", "White", "Green", "Black"],
    "correct_answer": "Purple"
  },
  {
    "question": "What is a 'kimura' in BJJ?",
    "options": ["An arm lock", "A choke", "A sweep", "A positional control"],
    "correct_answer": "An arm lock"
  },
  {
    "question": "Which is not a common BJJ position?",
    "options": ["Mount", "Back mount", "Knee-on-belt", "Side control"],
    "correct_answer": "Knee-on-belt"
  },
  {
    "question": "What does the term 'tap out' signify?",
    "options": ["Winning the match", "Submitting or conceding", "Starting a new position", "Passing the guard"],
    "correct_answer": "Submitting or conceding"
  },
  {
    "question": "Which weight class is typically the heaviest in BJJ tournaments?",
    "options": ["Roosterweight", "Super heavyweight", "Lightweight", "Middleweight"],
    "correct_answer": "Super heavyweight"
  },
  {
    "question": "What is a 'guard pass'?",
    "options": ["Moving from guard to side control", "Passing the opponent's legs to achieve a dominant position", "Subduing the opponent", "Escaping back control"],
    "correct_answer": "Passing the opponent's legs to achieve a dominant position"
  },
  {
    "question": "In BJJ, what is a 'sweep'?",
    "options": ["Attacking choke", "Reversing positions from bottom to top", "Striking technique", "Submission attempt"],
    "correct_answer": "Reversing positions from bottom to top"
  },
  {
    "question": "Which of these is a common BJJ competition rule?",
    "options": ["Striking allowed", "Points awarded for takedowns", "No gi submissions allowed", "All of the above"],
    "correct_answer": "Points awarded for takedowns"
  },
  {
    "question": "Who is credited with popularizing BJJ in the United States?",
    "options": ["Helio Gracie", "Rorion Gracie", "Mitsuyo Maeda", "Jigoro Kano"],
    "correct_answer": "Rorion Gracie"
  },
  {
    "question": "Which position is often used to set up submissions from the back?",
    "options": ["Mount", "Back control", "Side control", "Knee-on-belly"],
    "correct_answer": "Back control"
  }
]


# Initialize score to 0
score = 0


def ask_question(q):
    for idx, q in enumerate(questions, start=1):
        print(f"\n{idx}. {q['question']}\n")
        for idx, option in enumerate(q["options"], start=1):
            print(f"{idx}. {option}")
        answer = input("Choose the correct answer (1-4): ")
        return answer

def check_answer(answer, q):
    global score
    try:
        if q["options"][int(answer) - 1] == q["correct_answer"]:
            print("Correct!")
            global score
            score += 1  
        else:
            print(f"Wrong! The correct answer is: {q['correct_answer']}")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number between 1 and 4.")

def run_game():
    global score
    score = 0 # Reset score at the start of the game

    shuffled_questions = random.sample(questions, len(questions))
    for q in shuffled_questions:
        answer = ask_question(q)
        check_answer(answer, q)
    print(f"\nYour final score is: {score}/{len(questions)}")



run_game()