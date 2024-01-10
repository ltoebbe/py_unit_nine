from dog import Dog


class Pack:
    def __init__(self, dog):
        self.dog = dog
        self.members = []
        self.leader_index = 0

    def get_leader_name(self):
        print('the leader is ', self.members[self.leader_index].get_name())

    def add_member(self, new_member):
        self.members.append(new_member)

    def print_pack(self):
        # for x in range(len(self.members)):
        for member in self.members:
            print(member.get_name())

    def new_leader(self, members):
        print(members[3], 'ousts', members[0], 'from leadership.')


dog1 = Dog('Dakota')
dog2 = Dog('Lucy')
dog3 = Dog('Sasha')
dog4 = Dog('Franklin')

pack1 = Pack(dog1)

pack1.add_member(dog1)
pack1.add_member(dog2)
pack1.add_member(dog3)
pack1.add_member(dog4)

pack1.print_pack()
pack1.get_leader_name()
pack1.new_leader()
