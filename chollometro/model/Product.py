class Product:

    def __init__(self, category, image, name, price, old_price, rate, delivery, msg, user, link):
        self.__category = category
        self.__image = image
        self.__name = name
        self.__price = price
        self.__old_price = old_price
        self.__rate = rate
        self.__delivery = delivery
        self.__msg = msg
        self.__user = user
        self.__link = link

    def get_category(self): return self.__category

    def set_category(self, category): self.__category = category

    def get_image(self): return self.__image

    def set_image(self, image): self.__image = image

    def get_name(self): return self.__name

    def set_name(self, name): self.__name = name

    def get_price(self): return self.__price

    def set_price(self, price): self.__price = price

    def get_old_price(self): return self.__old_price

    def set_old_price(self, old_price): self.__old_price = old_price

    def get_rate(self): return self.__rate

    def set_rate(self, rate): self.__rate = rate

    def get_delivery(self): return self.__delivery

    def set_delivery(self, delivery): self.__delivery = delivery

    def get_msg(self): return self.__msg

    def set_msg(self, msg): self.__msg = msg

    def get_user(self): return self.__user

    def set_user(self, user): self.__user = user

    def get_link(self): return self.__link

    def set_link(self, link): self.__link = link






