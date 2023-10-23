class Bird:
    amount = 0
    tweet = "Tweet!"

    def __init__(self, name, age, species, owner) -> None:
        self.name = name
        self.age = age
        self.species = species
        self.owner = owner
        Bird.amount += 1

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old, {self.species} species, owner is {self.owner}"
    
    def chirp(self):
        print(self.tweet)
    
    def get_older(self):
        self.age += 1

    def get_age(self):
        return self.age
    
    def change_owner(self, new_owner):
        self.owner = new_owner

bird1 = Bird("Tweety", 2, "Canary", "John")
bird2 = Bird("Polly", 1, "Parrot", "Jane")
bird3 = Bird("Rio", 3, "Macaw", "David")

# Polly �������
bird2.chirp()

# �������� �� ������ ������ �� �������� ���� �� 1 ��
print(bird3.get_age())
bird3.get_older()
print(bird3.get_age())

# ������� �������� ����� ������
bird1.change_owner("Mary")

# �������� ���������� ��� ����� ������
print(bird1)

# �������� ������� ��������� ������
print("ʳ������ ������������� ������: " + str(Bird.amount))
