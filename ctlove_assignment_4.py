student_name = "Cameron Love"
current_gpa = 4.0
study_hours = 21
social_points = 60
stress_level = 35

print(f"Welcome! Here are your stats: Name: {student_name} Current GPA: {current_gpa} Study Hours: {study_hours} Social Points: {social_points} Stress Level: {stress_level}")

print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    if current_gpa >= 3.5:
        if study_hours > 20 and stress_level >= 40:
            stress_level = stress_level - 20
            print("Stop stressing so much! Your doing great.")
        else:
            print("Your doing great! Keep it up")
    elif current_gpa >= 2.5:
        if study_hours <= 15:
            study_hours = study_hours + 10
            print("You need to study more!")
        else:
            print("You are studying a good amount. Maybe ask your professor for help.")
        if social_points >= 60:
            print("Stop socializing and lock in!")
    elif current_gpa <= 1.0:
        print("Might be time to drop out bud.")
elif choice == "B":
    if current_gpa >= 3.5 and study_hours >= 25:
        print("Your locked in! Keep up the great work")
    elif current_gpa >= 3.5 and study_hours <= 25:
        print("You must be gifted huh!")
    elif (current_gpa <= 3.4 and current_gpa >= 3.0) and stress_level <= 20:
        stress_level = stress_level + 20 
        study_hours = study_hours + 10
        print("You can get that 3.5+ GPA, you just have to put in a little more work")
        if current_gpa >= 3.4:
            current_gpa = current_gpa + 0.1
            print(f"I told you! Look at your GPA now! GPA: {current_gpa}")
        elif current_gpa >= 3.3:
            current_gpa = current_gpa + 0.2
            print(f"I told you! Look at your GPA now! GPA: {current_gpa}")
        elif current_gpa >= 3.2:
            current_gpa = current_gpa + 0.3
            print(f"I told you! Look at your GPA now! GPA: {current_gpa}")
        elif current_gpa >= 3.1:
            current_gpa = current_gpa + 0.4
            print(f"I told you! Look at your GPA now! GPA: {current_gpa}")
        else: 
            current_gpa = current_gpa + 0.5
            print(f"I told you! Look at your GPA now! GPA: {current_gpa}")
    elif current_gpa >= 2.0:
        if social_points > 51 or study_hours < 16:
            print("You need to create better habits!")
        elif stress_level <= 30:
            print("Why are you not stressed? Your failing!")
        else:
            print("You might need to switch majors.")
    elif current_gpa <= 1.0:
        print("Might be time to drop out bud.")
elif choice == "C":
    if current_gpa >= 4.0:
        print("Are you a genius? Amazing Job!")
    elif current_gpa >= 3.5:
        print("Your a scholar! Keep up the great work.")
    elif current_gpa >= 3.0 and study_hours >= 25:
        print("Your working hard! I know you can get that 3.5+ GPA!")
    elif current_gpa >= 2.5 and social_points >= 50:
        print("Hey maybe a little less socializing!")
        if stress_level <= 20:
            stress_level = stress_level + 20
            current_gpa = current_gpa + 0.5
            print ("Start working harder!")
    elif current_gpa <= 1.0:
        print("Might be time to drop out bud.")
else:
    print("Invalid Input. Try again.")

print ("What are you studying? Study Pathways: Programming | Math | English | History")
study_choice = input()
study_options = ["Programming", "Math", "English", "History"]

if study_choice in study_options:
    if study_choice == "Programming":
        print("Your life is gonna be a lot more difficult.")
        study_hours = study_hours + 10
        print("+10 study hours")
        if stress_level <= 80:
            stress_level = stress_level + 20
            print("+20 stress level")
        elif social_points >= 20:
            social_points = social_points - 20
            print("-20 social points")
        elif current_gpa >= 3.5 and stress_level <= 50:
            print("")
            print("Hey programming may be hard, but your still doing a great job though!")
        elif (current_gpa <= 3.9 and current_gpa >= 3.0) or study_hours >= 30:
            print("Your undoubtedly locked in!")
            print("+ 0.1 GPA boost")
            current_gpa = current_gpa + 0.2
        elif current_gpa <= 2.5:
            print("You can do better then that!")
            if social_points >= 50: 
                current_gpa = current_gpa - 0.2
                print("Yeah stop being friendly bud. Go do your work.")
    elif study_choice == "Math":
        print("Your life is gonna be a litte more difficult.")
        study_hours = study_hours + 5
        print("+5 study hours")
        if stress_level <= 90:
            stress_level = stress_level + 10
            print("+10 stress level")
        elif social_points >= 10:
            social_points = social_points - 10
            print("-10 social points")
        elif current_gpa >= 3.0 and stress_level <= 50:
            print("")
            print("Hey math may be hard, but your still doing a great job though!")
        elif (current_gpa <= 3.8 and current_gpa >= 3.0) or study_hours >= 25:
            print("Your extremely locked in!")
            print("+ 0.2 GPA boost")
            current_gpa = current_gpa + 0.2
        elif current_gpa <= 2.5:
            print("You can do better then that!")
            if social_points >= 60: 
                current_gpa = current_gpa - 0.2
                print("Yeah stop being friendly bud. Go lock in.")
    elif study_choice in "History":
        print("Your life is a litter easier then the STEM majors!")
        social_points = social_points + 10
        print("+10 social points")
        if study_hours >= 5:
            study_hours = study_hours - 5
            print("5 study hours")
        if stress_level >= 10:
            stress_level = stress_level - 10
            print("-10 stress level")
        elif study_hours >= 5:
            study_hours = study_hours - 5          
        elif current_gpa >= 3.0 and stress_level <= 50:
            print("")
            print("Hey your doing a outstanding job!")
        elif (current_gpa <= 3.8 and current_gpa >= 3.0) or study_hours >= 25:
            print("Your really locked in!")
            print("+ 0.2 GPA boost")
            current_gpa = current_gpa + 0.2
        elif current_gpa <= 2.5:
            print("You can do better!")
            if not (social_points >= 20): 
                social_points = social_points + 20
                print("Go make some friends!")
    elif study_choice in "English":
        print("Your have the easiest major!")
        social_points = social_points + 20
        print("+20 social points")
        if study_hours >= 10:
            study_hours = study_hours - 10
            print("-10 study hours")
        elif stress_level >= 10:
            stress_level = stress_level - 20
            print("-20 stress level")
        elif study_hours >= 10:
            study_hours = study_hours - 10          
        elif current_gpa >= 3.0 and stress_level <= 30:
            print("")
            print("Hey your doing a great job!")
        elif (current_gpa <= 3.7 and current_gpa >= 3.0) or study_hours >= 15:
            print("Your super locked in!")
            print("+ 0.3 GPA boost")
            current_gpa = current_gpa + 0.3
        elif current_gpa <= 2.7:
            print("You can do better then that!")
            if (not social_points >= 30): 
                social_points = social_points + 30
                print("Go make some friends! You have the time.")
elif study_choice not in study_options:
    print("Invalid Choice. Try again.")
