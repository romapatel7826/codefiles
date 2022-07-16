class Programmer():
    company = "google"

    def __init__(self, name, product):
        self.name = name
        self.product = product
        print("the emplyee company name is google")

    def getinfo(self):
        print(f"the employe {self.name} work in {self.product}")


roma = Programmer("roma", "github")
sanju = Programmer("sanju", "skype")

roma.getinfo()
sanju.getinfo()