from dog import Dog


class Pack:
    def __init__(self, dog):
        self.dog = dog
        self.members = []
        self.leader_index = 0

        def get_leader_name():
            print(self.members[self.leader_index].get_name())

        def add_member():
            self.members.append('')

        def print_pack():
            for x in range(len(self.members)):
                print(self.members)
        print_pack()
        get_leader_name()
