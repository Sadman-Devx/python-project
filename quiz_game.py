def start_quiz():
    # Using a list of dictionaries - much easier to read and maintain
    quiz_data = [
        {
            "question": "What is the capital of France?",
            "options": ["a) London", "b) Berlin", "c) Paris", "d) Madrid"],
            "answer": "c"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["a) 3", "b) 4", "c) 5", "d) 6"],
            "answer": "b"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
            "answer": "c"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["a) Charles Dickens", "b) William Shakespeare", "c) Mark Twain", "d) Jane Austen"],
            "answer": "b"
        },
        {
            "question": "What is the boiling point of water in Celsius?",
            "options": ["a) 90", "b) 100", "c) 110", "d) 120"],
            "answer": "b"
        }
    ]

    score = 0
    total = len(quiz_data)

    for i, item in enumerate(quiz_data, 1):
        print(f"\nQuestion {i}/{total}")
        user_answer = get_user_answer(item["question"], item["options"])
        
        if user_answer == item["answer"]:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Wrong! The correct answer was: {item['answer']}")

    display_results(score, total)


def get_user_answer(question, options):
    print(question)
    for option in options:
        print(f"  {option}")
    
    # Input validation loop
    while True:
        answer = input("Your answer (a/b/c/d): ").strip().lower()
        if answer in ('a', 'b', 'c', 'd'):
            return answer
        print("Invalid input. Please enter a, b, c, or d.")


def display_results(score, total):
    percentage = (score / total) * 100
    print("\n" + "=" * 30)
    print(f"Quiz Complete!")
    print(f"Score: {score}/{total} ({percentage:.0f}%)")
    
    if percentage == 100:
        print("Perfect score! Excellent!")
    elif percentage >= 70:
        print("Great job!")
    elif percentage >= 50:
        print("Not bad, keep practicing!")
    else:
        print("Better luck next time!")
    print("=" * 30)


def main():
    print("=" * 30)
    print("  Welcome to the Quiz Game!")
    print("=" * 30)
    
    if input("\nStart quiz? (yes/no): ").strip().lower() == 'yes':
        start_quiz()
    else:
        print("Maybe next time! Goodbye!")


if __name__ == "__main__":
    main()