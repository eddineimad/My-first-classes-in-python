class Mobile():
    def __init__(self, name, companyName, storage, serialNum, dualSim, support4K):
        # Initialization
        self.name = name
        self.companyName = companyName
        self.storage = storage
        self.serialNum = serialNum
        self.dualSim = dualSim
        self.support4K = support4K
    
    def info(self):
        # Display infos about the phone
        print("The {} is produced by {} Company. It has {}GB storage capacity, its serial number is {}, and it {}supports dual SIM functionality. With {} support, it has a 4K display.".format(self.name, self.companyName, self.storage, self.serialNum, self.dualSim, self.support4K))

# Create instances of the Mobile class(instanciation)
mobile1 = Mobile("Samsung S23 ultra", "Samsung", 128, 976436705324, "", "not")
mobile2 = Mobile("iPhone 15", "Apple", 256, 368403556327, "not", "")

# Display infos about each mobile device
mobile1.info()
mobile2.info()