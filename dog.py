class Dog:
    def __init__(self, name):
        self.name = name
        self.trick_list = []

    def get_name(self):
        return self.name

    def sit(self):
        self.trick_list.append('sit')
        print(self.name, 'sits')

    def fetch(self):
        self.trick_list.append('fetch')
        print(self.name, 'fetches')

    def eat_homework(self):
        self.trick_list.append('eat homework')
        print(self.name, 'eats homework')

    def boogie(self):
        self.trick_list.append('boogie')
        print(self.name, 'boogies')

    def turn_inside_out(self):
        self.trick_list.append('turn inside out')
        print(self.name, 'turns inside out')

    def print_trick_list(self):
        print(self.trick_list)


dog1 = Dog("Dakota")
dog1.get_name()
dog1.sit()
dog1.fetch()
dog1.eat_homework()
dog1.boogie()
dog1.turn_inside_out()
dog1.print_trick_list()

dog2 = Dog("Lucy")
dog2.get_name()
dog2.sit()
dog2.fetch()
dog2.eat_homework()
dog2.boogie()
dog2.turn_inside_out()
dog2.print_trick_list()

dog3 = Dog("Sasha")
dog3.get_name()
dog3.sit()
dog3.fetch()
dog3.eat_homework()
dog3.boogie()
dog3.turn_inside_out()
dog3.print_trick_list()

dog4 = Dog("Franklin")
dog4.get_name()
dog4.sit()
dog4.fetch()
dog4.eat_homework()
dog4.boogie()
dog4.turn_inside_out()
dog4.print_trick_list()
