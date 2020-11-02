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

print(questions)

#convert keys to list
qs_avail = questions.keys()

questions_asked = 0

#while questions_asked < total_questions (10): 
# while questions_asked < 10: 
#     #randomly choose q from list of keys
#     curr_question = choice(qs_avail)
    #combine correct and incorrect answers and randomly generate answer order
    #when user answers: 
        #make sure input is valid
        #compare the answer with correct answer from dict
        #if answer correct: 
            #plus 1 to score
            #inform user answer is correct
        #else: 
            #inform user answer incorrect, display correct ans
        #plus one to questions_asked
        #remove question_id from list of qs_avail
#when questions_asked == total_questions: 
    #display score
    #display some nice message