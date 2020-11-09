class User:
    is_current_user = True # ағымдағы қолданушы || аккаунт иесі 
    
    def __init__(self, username = None, password = None): # Обьекті инициализацисы
        if not username or not password:
            print(
                "\nОбьектінің username немесе password атрибуттарының мәні берілмеген.\n" +
                "Бұл атрибуттарға мән беру үшін User класының create(username, password) әдісін немесе\n" + 
                "сәйкесінше set_username(username) және set_password(password) әдісін пайдаланыңыз."
                )
        else:
            self.create(username, password)
            print("\nКласс обьектісі құрылды")
    
    @property
    def password(self): # getter
        if self.is_current_user:
          return self.__password
        else:
            print("\nСіз бұл аккаунт иесі емессіз. Сондықтан сіз парольға қол жеткізе алмайсыз")

    @password.setter
    def password(self, password): # setter
        if len(password) < 6:
            print("\nПароль ұзыңдығы 6 символдан кем\n")
        else:
            self.__password = password

    @password.deleter
    def password(self): # deleter
        if self.is_current_user:
            # del self.__password
            print("\nПароль атрибуты жойылды")
        else:
            print("\nСіз бұл аккаунт иесі емессіз. Сондықтанда ештеңе жоя алмайсыз")

    def create(self, username, password): # Обьекті құру
        self.username = username
        self.__password = password
        print("\nЖаңа қолданушы ақпараты сақталды")

    def show(self): # Обьекті мәліметтерін көрсету
        print("\nОбьект атрибуттарының тізімі: ", self.__dict__)
        
        if hasattr(self, "username") and hasattr(self, "_User__password"):
            print("username атрибутының мәні: ", self.username)
            print("password атрибутының мәні: ", self.__password)
        else:
             print(
                "\nОбьектінің username немесе password атрибуттарының мәні берілмеген.\n" +
                "Бұл атрибуттарға мән беру үшін User класының create(username, password) әдісін немесе\n" + 
                "сәйкесінше set_username(username) және set_password(password) әдісін пайдаланыңыз."
                )

    def update(self, username, password): # Обьекті мәліметін өзгерту
        if self.is_current_user:
            self.username = username
            self.__password = password
            print("\nҚолданушы ақпараты жаңартылды")
        else:
            print("\nСіз бұл аккаунт ақпараттарын өзгерте алмайсыз")
    
    def delete(self): # Обьекті мәліметтерін жою
        if self.is_current_user:
            print("\nҚолданушы ақпараттары жойылды")
        else:
            print("\nСіз бұл аккаунт ақпараттарын жоюға құзырыңыз жоқ")