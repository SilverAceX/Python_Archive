class Person(object):
    def __init__(self, name, phone, address):
        self.__name = name
        self.__phone = phone
        self.__address = address
        self.__number = int(address.split()[0])

    def get_number(self):
        return self.__number

    def __lt__(self, other):
        return self.__number < other.get_number()

    def __eq__(self, other):
        return self.__number > other.get_number()

    def __gt__(self, other):
        return self.__number > other.get_number()

    def __repr__(self):
        return "{}\n{}     {}\n".format(self.__name, self.__phone, self.__address)

    def __str__(self):
        return "{}\n{}     {}\n".format(self.__name, self.__phone, self.__address)
