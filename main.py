import Stos
import Studenci
stos = Stos.Stos(3)
print(stos)
stos.push(5)
print(stos)
stos.pop()
print(stos)
stos.pop()

student=Studenci.Student("ala@gmail.com","Ala","Kot")
student2=Studenci.Student("janK@gmail.com","Jan","Kowalski")
slownik={}
slownik[0]=student
slownik[1]=student2

print(slownik)

print(Studenci.Student.compareStudentName(student, student2))
print(Studenci.Student.compareStudentSurname(student, student2))

def alphabeticGreater(x,y,func):
    return func(x,y)
print(alphabeticGreater(student,student2,Studenci.Student.compareStudentName))
print(alphabeticGreater(student,student2,Studenci.Student.compareStudentSurname))

#list.append(e,Studenci.Student.compareStudentName)

email, name, surname = student.getPersonalData()
print(email, name, surname)


