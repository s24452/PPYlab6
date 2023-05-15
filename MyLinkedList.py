class Element:
    def __init__(self, data=None, nextE=None):
        self.data=data
        self.nextE=nextE
class MyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0


    def __str__(self):
        #return str(self.head)+", tail"+str(self.tail)+", size= "+str(self.size)
        if self.size==0:
          return "Pusta lista"
        obecna=self.head
        elementy=[]
        while obecna is not None:
            elementy.append(str(obecna.data))
            obecna=obecna.nextE
        return " ".join(elementy)
    def get(self, e):
        obecna=self.head
        while obecna is not None:
            if obecna.data==e:
                return obecna.data
            obecna=obecna.nextE
        return None
    def delete(self, e):
        if self.head is None:
            return
        if self.head.data==e:
            self.head=self.head.nextE
            self.size-=1
            return
        obecna=self.head
        while obecna.nextE is not None:
            if obecna.nextE.data==e:
                obecna.nextE=obecna.nextE.nextE
                if obecna.nextE is None:
                    self.tail=obecna
                self.size-=1
                return
            obecna=obecna.nextE

    def append(self, e, func=None):
        nowy_ele=Element(data=e)

        if self.head is None:
            self.head=nowy_ele
            self.tail=nowy_ele
        else:
            if func is None:
                func=lambda a,b:a<=b

                obecna=self.head
                poprzednia=None
                while obecna is not None and func(obecna.data,e):
                    poprzednia=obecna
                    obecna=obecna.nextE

                if poprzednia is None:
                    nowy_ele.nextE=self.head
                    self.head=nowy_ele
                else:
                    poprzednia.nextE=nowy_ele
                    nowy_ele.nextE=obecna

                if obecna is None:
                    self.tail=nowy_ele
            self.size+=1


class Lista:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
