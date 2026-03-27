def evaluate(score):
    if score < 0 or score > 100:
        return "Invalid score!"

    if score >= 90:
        return "Great! You succeeded."
    elif score >= 50:
        return "You passed, but it could be better."
    else:
        return "Unfortunately, you failed."

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"