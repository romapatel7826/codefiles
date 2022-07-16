class Employee:
    company = "google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("hello this is roma here")

    def getDetails(self):
        print(f"the employee name is {self.name}")
        print(f"the employee salary is {self.salary}")
        print(f"the employee  subunit is {self.subunit}")
    
    
    def getSalary(self, signiture):
        print(f"the working company {self.company} is salary {self.salary}\n {signiture}" )

    @staticmethod   
    def greet():
        print("good morning")

roma = Employee("roma", 100, "hitalent")
roma.getDetails()