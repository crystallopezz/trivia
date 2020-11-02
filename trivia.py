"""a trivia game"""
import json
import random
#round = 10 qs
#qs displayed one at a time
#no repeating qs
#only select one answer
#correct answer revealed after answer submitted
#score revealed at end of round

#extract question data from the json file
with open('Apprentice_TandemFor400_Data.json') as qs: 
    question_data = json.loads(qs.read())

#organize question data in dictionary
#questions = {
#   question_id: {
#       question: "",
#       possibilites: [], 
#       correct_ans: "",
#   }
# }
questions = {}
current_id = 0
for q in question_data: 
    current_id += 1
    q["incorrect"].append(q["correct"]) 
    questions[current_id] = {
        "question": q["question"],
        "possibilities": q["incorrect"],
        "correct": q["correct"]
    }

#convert keys to list
qs_avail = list(questions.keys())
#randomize keys
random.shuffle(qs_avail)
#choose first 10 keys that will be the questions asked during the game
round_qs = qs_avail[0:10]

score = 0
    
for curr_question in round_qs: 
    possible_ans = questions[curr_question]["possibilities"]
    correct = questions[curr_question]["correct"]
    # randomly generate answer order
    random.shuffle(possible_ans)
    print(f"{questions[curr_question]['question']}")

    #print out mult choice options
    for i in range(0, len(possible_ans)): 
        print(f"{i+1}: {possible_ans[i]}")
    
    #store user's answer
    guess = int(input("Please choose one of the above options by writing the number corresponding to your choice."))
    
    #when user answers: 
    #to do: make sure input is valid
    #compare the answer with correct answer from dict
    if correct == possible_ans[guess-1]:  
        #plus 1 to score
        score += 1
        #inform user answer is correct
        print(f"{questions[curr_question]['correct']} is correct!")
        #else: 
    else: 
            #inform user answer incorrect, display correct ans
        print(f"Sorry, the correct answer was {questions[curr_question]['correct']}")

print(f"You finished the game! Here's your score: {score}/10")

# ATTEMPTS AT VALIDATING USER INPUT, not enought time to implement
# def guess_validation(): 
#     try: 
#         guess = int(input("Please choose one of the above options by writing the number corresponding to your choice."))
#     except ValueError: 
#         guess = int(input("Please enter a valid number."))
    
#     if 1 <= guess <= 4    

#     while !guess_validation(guess):
#         guess = input("Please enter a valid option.")
    
    # try: 
    #     guess = int(input("Please choose one of the above options by writing the number corresponding to your choice."))
    # except ValueError: 
    #     guess = int(input("Please enter a valid number."))

    # if guess < 1 or guess > 4: 
    #     guess = int(input("Please choose a number corresponding to one of the options"))



#code from when i was going to increment qs_asked until 10 and randomly choose a question each time
#while questions_asked < total_questions (10): 
# while questions_asked < 10: 
#     #randomly choose q from list of keys
#     curr_question = random.choice(qs_avail)
#     qs_avail.remove(curr_question)
#     possible_ans = questions[curr_question]["possibilities"]
#     #randomly generate answer order
#     random.shuffle(possible_ans)
#     for i in range(0, len(possible_ans)): 
#         print(f"{i+1}: {possible_ans[i]}")

#     questions_asked += 1