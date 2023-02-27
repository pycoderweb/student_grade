import json
from pprint import *
class Gurux:
    def init(self, lugat1):
        self.lugat1 = lugat1

    def talaba_kirit(self,lugat):
        command = ""
        fanlar = []
        with open('talaba.json', 'rb') as file:
            talabalar1 = json.load(file)
        while command != "no":
            fann = input("qaysi fandan o'tasiz : ")

            for i in talabalar1.values():
                for j in i.keys():
                    fanlar.append(j)

            while fann in fanlar:
                login = input("login >> ")
                parol = input("parol >> ")
                if login == lugat[fann][0] and parol == lugat[fann][1]:
                    for names, subjects in talabalar1.items():
                        baho = input(f"{names} ga baho qoying : ")
                        subjects[fann].append(baho)

                    command = input("yana baho qo'yasizmi(yes/no) : ")
                    break
                else:
                    print("Login yoki parol xato ketti. Iltimos qaytadan kiriting!")
                    continue
            if fann not in fanlar:
                print("bizda bunaqa fan yoq iltimos qaytadan kiriting ")
                continue

            continue
        with open('talaba.json', 'w') as file:
            json.dump(talabalar1, file)
    def vedimus(self):
        with open('talaba.json','rb') as file:
            talabalar1 = json.load(file)

        pprint(talabalar1)

lugat = {
    "Amaliy informatika":["Aminov","1234"],
    "Dasturlash asoslari": ["Davirov","1234"],
    "Diskret matematika": ["Zokirov","1234"],
    "Linux operatsion tizimida adminstratorlik": ["Xatamov","1234"],
    "Malumotlar bazalari texnalogiyasi": ["Eshonqulov","1234"],
    "Paralel dasturlash": ["Oblaqulov","1234"],
    "Python dasturlash tili va kutubxonalari":["Toraqulov","1234"],
    "Xorijiy til":["Usmonov","1234"]
}
Gurux205 = Gurux()


Gurux205.talaba_kirit(lugat)

Gurux205.vedimus()

