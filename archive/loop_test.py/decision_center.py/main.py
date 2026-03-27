import decision_center

while True:
    data = input("Enter score (q to quit): ")

    if data == "q":
        break

    try:
        score = int(data)

        comment = decision_center.evaluate(score)
        grade = decision_center.letter_grade(score)

        print("Letter Grade:", grade)
        print("Comment:", comment)

    except ValueError:
        print("Invalid input! Please enter a number.")