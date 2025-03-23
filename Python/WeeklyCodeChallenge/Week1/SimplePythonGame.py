'''
 Simple Quiz Game 🎮
Create a multiple-choice quiz with questions about Python, movies, 
or any fun topic! Display scores at the end and allow the user to play again. 🏆
'''

#import sys

def quiz_game():
    questions = [
        {
            "question": "What is the keyword to define a function in Python?",
            "options": ["A) def", "B) func", "C) function", "D) define"],
            "answer": "A"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": ["A) Steven Spielberg", "B) Christopher Nolan", "C) James Cameron", "D) Quentin Tarantino"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B"
        }
    ]
    
    score = 0
    
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        
        if user_answer == q["answer"]:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer was {q['answer']}.")
    
    print(f"\nGame Over! Your final score: {score}/{len(questions)} 🏆")
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        quiz_game()
    else:
        print("Thanks for playing! 🎮")
        #sys.exit()
        exit()

if __name__ == "__main__":
    quiz_game()
