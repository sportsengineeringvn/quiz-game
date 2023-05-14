import csv
import time
test_key = 0

# The function to load each question 
# Each question will have some properties:
#The first element is the question, The second to fifth element is four choice of answer.
#The six element is the answer for the question
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

# The function to ask_question 
def ask_question(question):
    print(question['text'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    start_time = time.time()
    answer_index = int(input("Your answer (1-4): "))
    elapsed_time = time.time() - start_time
    print()

    
# Time limit for each question is 10 seconds  
    if elapsed_time > 10:
        print("Your answer is run out of time")
        return False
    answer = ""
#Because the input of user is number 1->4 so we use the switch function to convert to the text and then compare
    switcher = {
        1: question['options'][0],
        2: question['options'][1],
        3: question['options'][2],
        4: question['options'][3]
    }
    answer = switcher.get(answer_index, "")
    return answer == question['answer']


#Check the final score 
def run_quiz():
    file_path = "/home/bearminerals/quiz-game/quiz_questions.csv"
    questions = load_questions(file_path)
    score = 0
    for question in questions:
        if ask_question(question):
            score += 1
            print("Your answer is correct")

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
    run_quiz()
