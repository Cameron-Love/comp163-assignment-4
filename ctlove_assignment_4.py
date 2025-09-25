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
