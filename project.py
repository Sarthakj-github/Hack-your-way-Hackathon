class Person:
    def __init__(self,person,residents):
        self.__person=person
        self.__residents=residents
        self.__name=person["Name"]
        self.__relations=[]
        self.__app=""
    
    def if_female(self):
        if self.__person["Gender"]=="Female":
            return True
        return False
    
    def ret_relation(self):
        self.Self()
        return self.__relations

    def wardswife_wardswards(self):
        for relation in list(self.__relations):
            if relation[1]=="Son":
                for resident in self.__residents:
                    if resident["Father"]==relation[0]:
                        if resident["Gender"]=="Female":
                            self.__relations.append((resident["Name"],"Grand-daughter"))
                        else:
                            self.__relations.append((resident["Name"],"Grand-son"))
                        self.__residents.remove(resident)

    def wards(self):
        for resident in list(self.__residents):
            if resident["Father"]==self.__name:
                if resident["Gender"]=="Female":
                    self.__relations.append((resident["Name"],"Daughter"))
                else:
                    self.__relations.append((resident["Name"],"Son"))
                self.__residents.remove(resident)
        self.wardswife_wardswards()

    def siblings(self):
        for resident in list(self.__residents):
            if resident["Father"]==self.__person["Father"]:
                if resident["Gender"]=="Female":
                    self.__relations.append((resident["Name"],"Sister"+self.__app))
                else:
                    self.__relations.append((resident["Name"],"Brother"+self.__app))
                self.__residents.remove(resident)
        self.wards()

    def parents(self):
        for resident in list(self.__residents):
            if resident["Name"]==self.__person["Father"]:
                self.__relations.append((resident["Name"],"Father"+self.__app))
                self.__residents.remove(resident)
            elif resident["Husband"]==self.__person["Father"]:
                self.__relations.append((resident["Name"],"Mother"+self.__app))
                self.__residents.remove(resident)
        self.siblings()

    def husband(self):
        for resident in list(self.__residents):
            if resident["Name"]==self.__name:
                self.__relations.append((resident["Name"],"Husband"))
                self.__person=resident
                break
        self.parents()

    def Self(self):
        self.__relations.append((self.__name,"Self"))
        if self.if_female():
            if self.__person["Father"]=="None":
                self.__name=self.__person["Husband"]
                self.app="-in-law"
                self.__residents.remove(self.__person)
                self.husband()
            else:
                self.app=""
                self.__residents.remove(self.__person)
                self.parents()
        else:
            self.app=""
            self.__residents.remove(self.__person)
            self.parents()

 #Taking Input.
AC=input("Enter Assembly Constituency:")
ac=0
with open("AC_No.txt",'r') as f:
    for i in f.readlines():
        l=(i.strip("\n")).split(',')
        if l[0]==AC:
            ac.int(l[1])

residents=[]
person=eval(input("Enter a set of details:"))
person["AC"]=ac
with open("Peoples.txt",'r') as f:
    for i in f.readlines():
        l=(i.strip("\n")).split(',')
        d={"AC":l[-1],"Name":l[0],"Gender":l[3],"Father":l[1],"Husband":l[2],"House_no":l[4]}
        if person["House_no"]==d["House_no"] and person["AC"]==d["AC"]:
            residents.append(d)

a=Person(person,residents)
print(a.ret_relation())
