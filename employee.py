class Employer():
    def __init__(self, name, sales, bonushrs, basesalary=0):
        # Initialization
        self.name = name
        self.sales = sales
        self.bonushrs = bonushrs
        self.basesalary = basesalary
    
    def info(self):
        # infos about the employee
        print("Name is {}. Base salary is {}. Sales are {}.".format(self.name, self.basesalary, self.sales))

# Create instances of the Employer class(instanciation)
emp1 = Employer("imad", 20000, 42, 80000)
emp2 = Employer("yahya", 1000, 65, 60000)

# Display infos about the employee
emp1.info()
emp2.info()