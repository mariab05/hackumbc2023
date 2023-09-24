score_movies=0
score_hobbies=0
score_music=0
score_winter=0
score_fall=0
score_spring=0
score_summer=0
score_personality=0

def rev(score):
    if (score == 10):
        return 1
    elif(score==9):
        return 2
    elif(score==8):
        return 3
    elif(score==7):
        return 4
    elif(score==6):
        return 5
    elif(score==5):
        return 6
    elif(score==4):
        return 7
    elif(score==3):
        return 8
    elif(score==2):
        return 9
    elif(score==1):
        return 10

print("Hello, Welcome to the Kiki-Bouba Personality Test!")
start=str(input("Would you like to start?\n "))
if start.lower()=="yes" or start.lower()=="y":
    print("Remember to answer each question from a scale of 1 to 10!")
    Q1_movies=int(input("Question 1:\nHow bad are your nightmares after watching a scary movie? "))
    score_movies+=Q1_movies
    Q2_movies=int(input("Question 2:\nHow much do you talk during a movie? "))
    score_movies+=rev(Q2_movies)
    Q3_movies=int(input("Question 3:\nHow much do you like indie film or A24 movies? "))
    score_movies+=Q3_movies
    Q4_movies=int(input("Question 4:\nHow much do you analyze a movie's cinematography? "))
    score_movies+=rev(Q4_movies)
    Q5_movies=int(input("Question 5:\nHow crazy are you about marvel movies? "))
    score_movies+=Q5_movies
    Q6_movies=int(input("Question 6:\nHow often do you nerd out to others about film? "))
    score_movies+=Q6_movies

    Q1_hobbies=int(input("Question 7:\nHow often do you draw? "))
    score_hobbies+=Q1_hobbies
    Q2_hobbies=int(input("Question 8:\nHow active are you? "))
    score_hobbies+=rev(Q2_hobbies)
    Q3_hobbies=int(input("Question 9:\nHow much do you like chess? "))
    score_hobbies+=rev(Q3_hobbies)
    Q4_hobbies=int(input("Question 10:\nHow much do you like to sing? "))
    score_hobbies+=Q4_hobbies
    Q5_hobbies=int(input("Question 11:\nHow often do you play an instrument? "))
    score_hobbies+=rev(Q5_hobbies)

    q1_music =int(input("Question 12:\nHow hard would you break the bank to go to your favorite artist's concert? "))
    score_music += rev(q1_music)
    q2_music = int(input("Question 13:\nHow mainstream is your music taste? "))
    score_music += rev(q2_music)
    q3_music = int(input("Question 14:\nHow often do you have the same song or album on repeat? "))
    score_music += q3_music
    q4_music = int(input("Question 15: \nHow much would you defend your artist if they get cancelled? "))
    score_music += rev(q4_music)
    q5_music = int(input("Question 16: \nHow loud do you play your songs in the car? "))
    score_music += rev(q5_music)
    q6_music = int(input("Question 17: \nHow immersed do you get when you listen to music? "))
    score_music += q6_music
    q7_music = int(input("Question 18:\nHow often do you listen to classical artist? "))
    score_music += q6_music

    q1_personality = int(input("Question 19: \nHow dark is your humor? "))
    score_personality += rev(q1_personality)
    q2_personality = int(input("Question 20: \nHow much banter do you have in your friend group? "))
    score_personality += rev(q2_personality)
    q3_personality = int(input("Question 21: \nHow affectionate are you around others? "))
    score_personality += q3_personality
    q4_personality = int(input("Question 22: \nHow girlboss are you? "))
    score_personality += rev(q4_personality)
    q5_personality = int(input("Question 23:\nHow often did you argue with your team this hackathon? "))
    score_personality += rev(q5_personality)

    result_movies=(score_movies/60)*100
    if score_movies<30:
        print(f"Your tastes in movies are {100-int(result_movies)}% Kiki!")
    elif score_movies>30:
        print(f"Your tastes in movies are {int(result_movies)}% Bouba!")
    else:
        print(f"Your tastes in movies are perfectly neutral")

    result_hobbies=(score_hobbies/50)*100
    if score_hobbies<25:
        print(f"Your hobbies are {100-int(result_hobbies)}% Kiki!")
    elif score_hobbies>25:
        print(f"Your hobbies are {int(result_hobbies)}% Bouba!")
    else:
        print(f"Your tastes in movies are perfectly neutral")

    result_music=(score_music/70)*100
    if score_music<35:
        print(f"Your tastes in music is {100-int(result_music)}% Kiki!")
    elif score_hobbies>35:
        print(f"Your tastes in music is {int(result_music)}% Bouba!")
    else:
        print(f"Your tastes in movies are perfectly neutral")

    result_personality=(score_personality/50)*100
    if score_personality<25:
        print(f"Your personality is {int(100-result_personality)}% Kiki!")
    elif score_personality>25:
        print(f"Your personality is {int(result_personality)}% Bouba!")
    else:
        print(f"Your tastes in movies are perfectly neutral")

overall_score=((score_movies+score_hobbies+score_music+score_personality)/230)*100

final_question=str(input("Do you want to see your overall Kiki-Bouba score?\n "))
if final_question.lower()=="yes" or final_question.lower()=="y":
    if overall_score<50:
        print(f"\nYou are overall {100-int(overall_score)}% Kiki!")
    elif overall_score>50:
        print(f"\nYou are overall {int(overall_score)}% Bouba!")
    else:
        print(f"\nYour tastes in movies are perfectly neutral")
