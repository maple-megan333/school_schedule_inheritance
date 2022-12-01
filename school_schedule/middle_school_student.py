from .student import Student

# add MiddleSchoolStudent here
# 1 Track whether the student receives school transportation using the boolean attribute gets_transportation (can be set in the constructor, defaults to False)
# 2 Update the summary method to include information about the student's transportation status
# 3 Include tests for the additional functionality
# There is one test provided (currently commented out)
# Uncomment the test and implement the MiddleSchoolStudent class so that it passes
# If there is time, implement additional tests for the MiddleSchoolStudent class (review the HighSchoolStudent class for ideas)

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation
    
    def summary(self):
        student_summary = super().summary()
        if self.gets_transportation:
            return student_summary + ". Student has transportation"
        return student_summary + f". Student does not have transportation" # lol hi. YO homie. Going to do them line breaks after the classes :D
