import json

def yakuniy(baholar):
    s = 0
    for baho in baholar:
        if baho == "":
            baho = 0
        s += float(baho)
    return s / len(baholar)

def gpa(talabalar):
    fanlar = []
    for subjects in talabalar.values():
        for subject, baholar in subjects.items():
            fanlar.append(subject)
    kreditlar = []

    for i in talabalar['Axmedov Alisher'].keys():
        kreditlar.append(int(input(f"{i} fanni krediti :")))
    for names,subjects in talabalar.items():
        t = 0
        i = 0
        for subject, baholar in subjects.items():
            t += kreditlar[i] * yakuniy(baholar)
            i += 1

        print(f"{names} ning GPA bali >> {t/sum(kreditlar)}")


with open('talaba.json','rb')as file:
    talabalar = json.load(file)

print(gpa(talabalar))