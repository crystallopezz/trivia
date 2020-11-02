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
#       incorrect_ans: [], 
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
random.shuffle(qs_avail)
round_qs = qs_avail[0:10]

score = 0

for curr_question in round_qs: 
    possible_ans = questions[curr_question]["possibilities"]
    # randomly generate answer order
    random.shuffle(possible_ans)
    print(f"{questions[curr_question]['question']}")

    
    for i in range(0, len(possible_ans)): 
        print(f"{i+1}: {possible_ans[i]}")

    guess = int(input("Please choose one of the above options by writing the integer of the answer you choose."))
    
    #when user answers: 
        #make sure input is valid
        #compare the answer with correct answer from dict
    if questions[curr_question]["correct"] == possible_ans[guess-1]: 
        #if answer correct: 
            #plus 1 to score
        score += 1
            #inform user answer is correct
        print(f"{questions[curr_question]['correct']} is correct!")
        #else: 
    else: 
            #inform user answer incorrect, display correct ans
        print(f"Sorry, the correct answer was {questions[curr_question]['correct']}")

print(score)

    

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