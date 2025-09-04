class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_name(self):
        return f"Player: {self.name}"

    def get_age(self):
        return self.age


if __name__ == "__main__":
    p1 = Player("Ghost", 21)
    p2 = Player("Ninja", 19)

    print(p1.display_name(), "| Age:", p1.get_age())
    print(p2.display_name(), "| Age:", p2.get_age())
