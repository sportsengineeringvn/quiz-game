import csv
import time

def load_questions(file_path):
    questions = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            question = {
                'text': row[0],
                'options': row[1:5],
                'answer': row[5]
            }
            questions.append(question)
    return questions

def ask_question(question, time_limit):
    print(question['text'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    start_time = time.time()
    answer = input(f"Your answer (1-4). You have {time_limit} seconds: ")
    elapsed_time = time.time() - start_time
    print()
    if elapsed_time > time_limit:
        print(f"Time's up! You took too long to answer the question.")
        return False
    return answer == question['answer']

def run_quiz(time_limit):
    file_path = "/home/bearminerals/quiz-game/quiz_questions.csv"
    questions = load_questions(file_path)
    score = 0
    for question in questions:
        if ask_question(question, time_limit):
            score += 1
    print(f"Your final score is {score}/{len(questions)}.")

    # Storing the score in a file
    with open('/home/bearminerals/quiz-game/scores.txt', 'a') as file:
        file.write(f"{score}\n")

    # Displaying the list of high scores
    print("High scores:")
    with open('scores.txt', 'r') as file:
        scores = [int(line.strip()) for line in file]
        scores.sort(reverse=True)
        for i, score in enumerate(scores[:10]):
            print(f"{i+1}. {score}")

if __name__ == "__main__":
    time_limit = 10
    run_quiz(time_limit)