import smtplib
from email.mime.text import MIMEText


class Student:
    def __init__(self,imie,nazwisko,email,projekt,listy,praceDomowe,ocena=None,status=None):
        self.imie=imie
        self.nazwisko=nazwisko
        self.email=email
        self.projekt=projekt
        self.listy=listy
        self.praceDomowe=praceDomowe
        self.ocena=ocena
        self.status=status
class MySortedList:
    def __init__(self,file):
        self.list=[];
        self.file = "ocenystudenci"

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
        with open(self.file,"ocenystudenci") as fileObject:
            fileObject.write(wynik)

    def wyslijMaile(self,temat,wiadomosc,adresat,odbiorcy,haslo ):
        message=MIMEText(wiadomosc)
        message['Temat'] = temat
        message['Od']=adresat
        message['Do']=','.join(odbiorcy)
        server=smtplib.SMTP_SSL('',)
        server.login(adresat,haslo)
        server.sendmail(adresat,odbiorcy,message.as_string())
        server.quit()


    def dane(self):
        with open(self.file) as fileObject:
            for line in fileObject:
                linia=line.rsplit().split(" ")
                studenci= Student()
                studenci.email = linia[0]
                studenci.imie=linia[1]
                studenci.nazwisko = linia[2]
                studenci.projekt = linia[3]
                studenci.listy=linia[4:6]
                studenci.praceDomowe=linia[7:15]
                if linia[17]=="GRADED" or linia[16]=="MAILED":
                    studenci.ocena=self.wystawianieOcen(int(linia[16]))
                    studenci.status=linia[17]


    def wystawianieOcen(self, projekt, listy, praceDomowe):
        ocena = 0
        with open(self.file) as fileObject:
            for line in fileObject:
                linia=line.rsplit().split(" ")
                studenci = Student()
                studenci.projekt = linia[3]
                studenci.listy = linia[4:6]
                studenci.praceDomowe = linia[7:15]

        if studenci.projekt == '-1' or studenci.listy == '-1' or studenci.praceDomowe == '-1':
          print("Nie mozna wystawic oceny koncowej, ponieważ nie zostały wystawione wszytskie oceny")
          ocena = -1
        else:
          ocenaProjekt = float(studenci.projekt) * 40
          ocenaListy = sum(studenci.listy) * 20
          sredniaPraceDomowe = sum(studenci.praceDomowe) / len(studenci.praceDomowe)

          if sredniaPraceDomowe >= 80:
              ocenaListy = 60
          elif sredniaPraceDomowe >= 70:
              ocenaListy = 40
          elif sredniaPraceDomowe >= 60:
              ocenaListy = 20

        ocena = ocenaProjekt + ocenaListy