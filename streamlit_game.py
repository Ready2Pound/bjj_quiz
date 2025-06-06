import streamlit as st
import random   
import time
import pandas as pd
from datetime import datetime 
import os

# ---------------------------
# 1. Define the questions for each difficulty level
# ---------------------------

difficulty = {
   "Easy": [
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
],
  "Hard": [
      {
    "question": "What is the primary difference between the closed guard and open guard in BJJ?",
    "options": ["The opponent's posture", "Number of grips", "Leg positioning", "Use of gi"],
    "correct_answer": "Leg positioning"
  },
  {
    "question": "In advanced BJJ tactics, what is the purpose of a 'pull' in guard work?",
    "options": ["To initiate a takedown", "To reset the position", "To set up submissions", "To create space for passes"],
    "correct_answer": "To create space for passes"
  },
  {
    "question": "Which sequence best describes the concept of 'gradual pressure' in positional control?",
    "options": ["Applying quick joint locks", "Incrementally increasing pressure to force mistakes", "Using explosive movements", "Constantly switching positions"],
    "correct_answer": "Incrementally increasing pressure to force mistakes"
  },
  {
    "question": "What is a 'leg weave' in BJJ passing techniques?",
    "options": ["A grip on the opponent's waist", "A guard pass variation involving weaving under the opponent’s leg", "A sweep from the bottom", "A submission move"],
    "correct_answer": "A guard pass variation involving weaving under the opponent’s leg"
  },
  {
    "question": "In terms of biomechanics, why is the 'overhook' control useful in BJJ?",
    "options": ["It restricts the opponent's arm movement", "It allows for better posture control", "It opens up submissions", "All of the above"],
    "correct_answer": "All of the above"
  },
  {
    "question": "What does 'stack passing' involve in BJJ?",
    "options": ["Pushing the opponent's legs back towards their head", "Lifting and pushing the legs forward over the opponent's face", "Passing the guard by underhooking", "Swiping the hips"],
    "correct_answer": "Lifting and pushing the legs forward over the opponent's face"
  },
  {
    "question": "Which is a key detail when executing a 'triangle choke' from the guard?",
    "options": ["Locking the ankle behind the knee", "Pulling the opponent's head down", "Compressing the carotid arteries", "All of the above"],
    "correct_answer": "All of the above"
  },
  {
    "question": "How does 'knee slice' guard pass work in advanced BJJ?",
    "options": ["Driving the knee across the opponent's thigh to pass", "Using the knee to unbalance the opponent", "Shrimping to escape", "Attacking with a submission"],
    "correct_answer": "Driving the knee across the opponent's thigh to pass"
  },
  {
    "question": "What is the main purpose of 'frame formation' in guard retention?",
    "options": ["To create distance and prevent pass attempts", "To set up submissions", "To execute sweeps", "To transition to mount"],
    "correct_answer": "To create distance and prevent pass attempts"
  },
  {
    "question": "In competitive BJJ, what is the strategic importance of 'risk management' during positional exchanges?",
    "options": ["To avoid penalties", "To set up high-percentage submissions", "To conserve energy", "To minimize mistakes and avoid counterattacks", 
    "All of the above"],
    "correct_answer": "All of the above"
  },
  {
    "question": "In advanced passing, what is the benefit of 'butterfly hook' in guard?",
    "options": ["Creating mobility and control", "Setting up sweeps", "Countering submissions", "All of the above"],
    "correct_answer": "All of the above"
  },
  {
    "question": "What is the key principle behind 'angle passing' in BJJ?",
    "options": ["Passing through the middle", "Creating angles to bypass the opponent's frames", "Passing from the back", "Rolling the opponent over"],
    "correct_answer": "Creating angles to bypass the opponent's frames"
  },
  {
    "question": "Which technique is fundamental for transitioning from half guard to back control?",
    "options": ["Back step escape", "Knee slide pass", "Underhook escape", "Back take sweep"],
    "correct_answer": "Back step escape"
  },
  {
    "question": "In submissions, what distinguishes a 'submission chain'?",
    "options": ["Sequential submission attempts from a single position", "Multiple variations of the same submission", "Combining submissions for increased effectiveness", "All of the above"],
    "correct_answer": "All of the above"
  },
  {
    "question": "Which aspect is most critical when executing a 'kimura' from guard?",
    "options": ["Control of opponent's wrist", "Positioning of the hips", "Alignment of the shoulder", "All of the above"],
    "correct_answer": "All of the above"
  },
  {
    "question": "What is the primary function of 'frame creation' during escape attempts in BJJ?",
    "options": ["To prevent submission", "To create space and leverage", "To secure a dominant position", "To control the opponent's hips"],
    "correct_answer": "To create space and leverage"
  },
  {
    "question": "In BJJ, what is 'dynamic progression' in positional transitions?",
    "options": ["Moving quickly through positions without control", "Systematic advancement towards dominant positions", "Using brute force to pass guard", "Remaining static to conserve energy"],
    "correct_answer": "Systematic advancement towards dominant positions"
  },
  {
    "question": "Which concept is vital when applying 'pressure passing' in 'heavy' top control?",
    "options": ["Maintaining balance", "Reducing opponent's movement", "Gradually increasing pressure", "All of the above"],
    "correct_answer": "All of the above"
  },
  {
    "question": "What distinguishes a 'reverse De La Riva' guard from standard De La Riva?",
    "options": ["The direction of the hook", "The type of grips used", "The position of the opponent", "It is not a real guard"],
    "correct_answer": "The direction of the hook"
  },
  {
    "question": "When executing a 'deep half guard sweep,' what is critical to success?",
    "options": ["Controlling the opponent's posture", "Creating angulation", "Maintaining leverage on the opponent's leg", "All of the above"],
    "correct_answer": "All of the above"
  },
  {
    "question": "In advanced BJJ, what is the purpose of 'button hook' setups?",
    "options": ["To bait the opponent into a trap", "To create opening for submissions", "To confuse the opponent", "All of the above"],
    "correct_answer": "All of the above"
  },
  {
    "question": "What is the primary focus when transitioning from a defensive posture to an attacking position in advanced BJJ?",
    "options": ["Timing and patience", "Exploiting opponent's mistakes", "Maintaining correct biomechanics", "All of the above"],
    "correct_answer": "All of the above"
  }
  ]}

# ---------------------------
# 2. Initialize session state variables (like memory for the app)
#    This only runs once, when the app starts or is reset
# ---------------------------
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.questions = []
    st.session_state.start_time = None
    st.session_state.selected_difficulty = None

# ---------------------------
# 3. Show the title and description at the top of the app
# ---------------------------
st.title("BJJ Quiz Game")
st.write("Test your knowledge of Brazilian Jiu-Jitsu (BJJ) with this quiz game!")

# ---------------------------
# 4. If the quiz hasn't started, show difficulty selection and start button
# ---------------------------
if not st.session_state.quiz_started:
    # User picks difficulty
    difficulty_level = st.selectbox("Select Difficulty Level", ["Easy", "Hard"])

    # When user clicks start quiz
    if st.button("Start Quiz"):
        st.session_state.selected_difficulty = difficulty_level
        # Copy and shuffle the questions for this game
        st.session_state.questions = difficulty[difficulty_level].copy()
        random.shuffle(st.session_state.questions)
        # Shuffle the options for each question
        for q in st.session_state.questions:
            random.shuffle(q["options"])
        # Set up the game state
        st.session_state.quiz_started = True
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.start_time = time.time()
        st.rerun()

# ---------------------------
# 5. If the quiz has started, show the current question or the results
# ---------------------------
if st.session_state.quiz_started:
    questions = st.session_state.questions
    index = st.session_state.current_question

    # Show feedback from the previous answer, if any
    if "last_feedback" in st.session_state and st.session_state.last_feedback:
        st.info(st.session_state.last_feedback)
        st.session_state.last_feedback = ""  # Clear after showing

    # If questions are available, show the current question
    if index < len(questions):
        question = questions[index]
        st.subheader(f"Question {index + 1}: {question['question']}")
        # Let the user pick an answer
        choice = st.radio("Choose an option:", question["options"], key=index)
        # When the user clicks "Submit Answer"
        if st.button("Submit Answer"):
            # Check if the answer is correct
            if choice == question["correct_answer"]:
                st.session_state.score += 1
                st.session_state.last_feedback = "Correct!"
            else:
                st.session_state.last_feedback = f"Wrong! The correct answer is: {question['correct_answer']}"
            st.session_state.current_question += 1
            st.rerun()  

    # If all questions have been answered, show the results            
    else:
        total_time = round(time.time() - st.session_state.start_time, 2)
        st.write(f"Quiz completed! Your score: {st.session_state.score}/{len(st.session_state.questions)}")
        st.write(f"Time taken: {total_time:.2f} seconds")

        if st.button("Restart Quiz"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()

    # --- Leaderboard File ---
    # --- Leaderboard Logic ---
# else:
#     LEADERBOARD_FILE = "leaderboard.csv"
#     start = st.session_state.get("start_time", time.time())
#     if st.session_state.get("start_time") is not None:
#         total_time = round(time.time() - st.session_state.start_time, 2)
#     else:
#         st.error("Quiz timer failed to start. Please restart the quiz.")
#         st.stop()
#     st.success(":tada: Quiz Complete!")
#     st.write(f"**Your Score:** {st.session_state.score} out of {len(st.session_state.questions)}")
#     st.write(f"**Time Taken:** {total_time} seconds")
#     # --- Ask for user's name ---
#     user_name = st.text_input("Enter your name for the leaderboard:")
#     if st.button("Submit Score") and user_name.strip():
#         # Prepare new row
#         new_result = {
#             "Name": user_name.strip(),
#             "Difficulty": st.session_state.selected_difficulty,
#             "Score": st.session_state.score,
#             "Time": total_time,
#             "Date": datetime.now().strftime("%Y-%m-%d %H:%M")
#         }
#         # Load or create leaderboard
#         if os.path.exists(LEADERBOARD_FILE):
#             leaderboard_df = pd.read_csv(LEADERBOARD_FILE)
#         else:
#             leaderboard_df = pd.DataFrame(columns=new_result.keys())
#         # Append and save
#         leaderboard_df = leaderboard_df.append(new_result, ignore_index=True)
#         leaderboard_df.to_csv(LEADERBOARD_FILE, index=False)
#         st.success("Your score has been added to the leaderboard!")
#         st.experimental_rerun()
#     # --- Show leaderboard if file exists ---
#     if os.path.exists(LEADERBOARD_FILE):
#         st.subheader(":trophy: Leaderboard (Top 10 by Score & Time)")
#         df = pd.read_csv(LEADERBOARD_FILE)
#         df_sorted = df.sort_values(by=["Score", "Time"], ascending=[False, True]).head(10)
#         st.dataframe(df_sorted)
#     if st.button("Restart Quiz"):
#         for key in st.session_state.keys():
#             del st.session_state[key]
#         st.experimental_rerun()
        