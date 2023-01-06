#question 3
def misc(n):
    out = []
    ctr = 1
    while len(out) < n:
        new_val = int(input("Enter a number:"))
        if 1 < new_val < 256:
            out.append(new_val * ctr)
        else:
            print("No")
    return out


def misc_3(n):
    if n > 0:
        new_val=int(input("Enter a number:"))
        if 1 < new_val < 256:
            if n-1 != 0:
                return [new_val]+ misc_3(n-1)
            else:
                return [new_val]
        else:
            print('No')
            return misc_3(n)

print(misc_3(3))


#question 2
# class Course:
#     def __init__(self, subject, sections, course):
#         self.subject = subject
#         self.sections = sections
#         self.course = course
#     def get_subject(self):
#         return self.subject 
#     def new_section(self,time):
#         self.time = time
#         self.sections.append(self.time)
#         return self.sections 
#     def __str__(self):
#         return f'{self.subject}.{self.sections}.{self.course}'


# math = Course("Math", ["10AM", "8AM"], "Calc I")
# math.get_subject()
# math.course
# math.sections
# math.new_section("5PM")
# math.sections



class Book:
    def __init__(self, title, year_printed, pages):
        self.title = title
        self.year = year_printed
        self.pages = pages

    def get_year(self):
        return self.year
    def __repr__(self):
        return f"{self.title} Printed: {self.year}"

