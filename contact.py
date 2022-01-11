class List:




    def __init__(self):

        self.all_contacts = []




    def search_by_name(self, *name):

        for i in name:

            self.all_contacts.append(i.title())

        ss = [i for i in self.all_contacts if self.all_contacts.count(i) > 1]

        sss = set(ss)

        print("Список совпадений: ")

        for a in sss:

            print("\t",a)

class ContactList(List):




    def __init__(self):

        super().__init__()

my_contacts = ContactList()

my_contacts.search_by_name("monkey","flowers","donkey","smile","donkey","monkey","books")
