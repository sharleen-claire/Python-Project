class student :
    def __init__(self,fullname,course,age,feespaid) :
        self.fullname = fullname
        self.course = course
        self.age = age
        self.feespaid = feespaid

    def display_details(self) :
        print("Fullname:",self.fullname)
        print("Course:",self.course)
        print("Age:",self.age)
        print("Feespaid:",self.feespaid)
        print("-----------------")

#Task 2
student1 = student("Claire Sharleen","MIT",20,30000)
student2 = student("Christian Kimani","Cyber Security",22,10000)
student3 = student("Moses kuria","Datascience",21,20000)


student1.display_details()
student2.display_details()
student3.display_details()