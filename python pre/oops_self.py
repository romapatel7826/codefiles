class Employee:
    company = "google"
    
    def getSalary(self, signiture):
        print(f"the working company {self.company} is salary {self.salary}\n {signiture}" )

    @staticmethod   
    def greet():
        print("good morning")

roma = Employee()

roma.salary = 200
roma.getSalary("thanks")
roma.greet()
# print(roma.company)
# print(roma.salary)
# print(riya.salary)