class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber,scores):
        Person.__init__(self,firstName, lastName, idNumber)

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        a=0
        for i in scores:
            a=a+i
        total=a/len(scores)    
        my_grade=''
        if total >= 90 and total <=100:
            my_grade='O'
        elif total >= 80 and total <90:
            my_grade='E'
        elif total >= 70 and total <80:
            my_grade='A' 
        elif total >= 55 and total <70:
            my_grade='P' 
        elif total >= 40 and total <55:
            my_grade='D'
        elif total <40:
            my_grade='T'                        
        return my_grade    
        
    
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())