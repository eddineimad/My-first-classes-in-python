class Player():
    def __init__(self, name, age, post, club, rank):
        # Initialization
        self.name = name
        self.age = age
        self.post = post
        self.club = club
        self.rank = rank
    def info(self):
        # infos about the player
        print("the player name is {}, aged {}, his post is {}, play with {}, and his ranking is {}.".format(self.name, self.age, self.post, self.club, self.rank))
    

# Create instances of the Player class(instanciation)
player1 = Player("Cristiano Ronaldo", 38, "ST", "Paris Saint-Germain", 1)
player2 = Player("Erling Haaland", 23, "ST", "Manchester City", 2)
player3 = Player("Sofiane Amrabt", 28, "CM", "Manchester United", 3)

# Display infos about each player
player1.info()
player2.info()
player3.info()