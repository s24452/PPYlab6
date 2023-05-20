class Student:
    def __init__(self,imie,nazwisko,email,punkty,ocena=None,status=None):
        self.imie=imie
        self.nazwisko=nazwisko
        self.email=email
        self.punkty=punkty
        self.ocena=ocena
        self.status=status
class MySortedList:
    def __init__(self,file):
        self.list=[];
        self.file = "plikStudenci.txt"

    def dodajStudenta(self,student):
        self.list.append(student)
        self.zapiszDoPliku()

    def usunStudenta(self,index):
       if 0<=index<len(self.list):
        self.list.pop(index)
        self.zapiszDoPliku()

    def zapiszDoPliku(self):
        wynik=""
        for student in self.list:
            wynik+=f"{student.imie} {student.nazwisko} {student.email} {student.punkty} {student.ocena} {student.status}\n"
        with open(self.file,"plikStudenci.txt") as fileObject:
            fileObject.write(wynik)

    def wyslijMaile(selfself):
                pass
    def wystawianieOcen(self):
        pass
    def dane(self):
        with open(self.file) as fileObject:
            for line in fileObject:
                linia=line.rsplit().split(" ")
                studenci= Student()
                studenci.imie=linia[0]
                studenci.nazwisko = linia[1]
                studenci.email = linia[2]
                studenci.punkty = linia[3]
                if len(linia)==4:
                    studenci.ocena=self.wystawianieOcen(int(linia[3]))
                    studenci.status=""
                elif len(linia)==5:
                    if linia[4]=="GRADED" or linia[4]=="MAILED":
                        studenci.ocena=self.wystawianieOcen(int(linia[3]))
                        studenci.status=linia[4]
