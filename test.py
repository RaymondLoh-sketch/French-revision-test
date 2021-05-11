
import sys
score = 0
guesses= 0

french_questions = ['what is Timide in English__?', 'What is jeune in English__?', 'What is ennuyeux in English__?', 'what is fatigue in English__?',
'What is bon in English__?', 'what is dernier in English__?', 'What is vieux in English__?', 'what is favorj in English__?', 'What is mignon in English__?',
'what is gros in English__?', 'What is doux in English__?', 'what is facile a vivre in English__?', 'what is checher in English__?', 'What is partir in English__?',
'what is demain soir in English__?']
english_questions = ['what is to be in French__?', 'what is to have in French__?', 'what is to go in French__?', 'what is know in French__?', 'what is to want in French__?',
'what is are you free? in French__?','what is lets meet in French__?', 'what is thank you for your kind invitaion in French','what is im sorry, but i cant accept your invitation in French__?',
'what is beautiful in French__?', 'what is round in French__?',]
english_answers =['etre', 'avoir', 'aller', 'savoir', ' vouloir', 'tu es libre', ' on se retrouve', 'merci pou gentille invitation', 'je suis desole, mais je ne peux pas accepter ton invitation',
'beau', 'gros']
french_answers = ['shy', ' young', 'boring', 'tired', 'good', 'last', 'old', 'panic', ' cute', 'round', 'soft', 'easygoing', 'to find', 'to leave', 'tomorrow evening']
number_of_questions = 10

question_number = 0

print('welcome to English-French vocacabulary Drill')

print('*********************************************')

print('To be drilled in English Press 1')

print('To be drilled in French Press 2')

print('*********************************************')

option = int(input('Please Enter option:'))

while option not in (1,2) and type(option) == int:
    option = int(input('Please enter valid option'))

if option == 1:
    questions = english_questions
    answers = french_answers
elif option == 2:
    questions = french_questions
    answers = french_answers


def check_answer(user_answer, answer):
    global question_number
    if user_answer in answers:
        print('')
        print('Correct')
        global score
        score += 1

    else:
        print('')
        print('Incorrect, try again')
        global guesses

        guesses = guesses + 1
    question_number = question_number + 1
    
while question_number < number_of_questions:
    cur_question = questions[question_number]
    user_answer = answers[question_number]
    print('')
    user_answer = input (cur_question + '+')
    print (check_answer(user_answer, answers))
    print('')

print('score : ' +str(score) )

