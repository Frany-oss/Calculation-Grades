
class Class:

    def __init__(self, credits = 0):
        self.grades = []
        self.credits = credits


    def CalculateGrades(self, grade, weight):
        tempgrade = grade * (weight/100)
        return self.grades.append(tempgrade)

    def CalculateAverage(self, grades):
        temp = 0
        for i in range(len(grades)):
            temp += grades[i]
        
        return temp

    def ToCalculateFinalGrade(self, grades):
        grade = CalculateAverage(grades)
        return self.credits * grade
