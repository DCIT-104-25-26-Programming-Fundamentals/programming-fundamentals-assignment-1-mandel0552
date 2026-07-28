def get_grade(score):
    if score < 0:
        return None
    if score >100:
        return None
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
if __name__ == "__main__":

    score = int(input("Enter a student score(0-100):"))
   
    if get_grade(score) is None:
        print("Error: Score must be between 0 to 100")
    else:
        print(f"Grade: {get_grade(score)}")
