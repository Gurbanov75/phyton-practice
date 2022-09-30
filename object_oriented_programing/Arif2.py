class Programist():
    def __init__(self,ad,soyad,no,maas,diller):
        self.ad = ad
        self.soyad = soyad 
        self.no =no
        self.maas=maas
        self.diller = diller
    def informasa_goster(self):
        
        print("""
              Programist datalari 
              AD:{}
              SOYAD:{}
              NO:{}
              MAAS:{}
              DILLER:{}
              """.format(self.ad,self.soyad,self.no,self.maas,self.diller))
        
        
programist1 = Programist("Arif","Qurbanov",1700,1000,["C++","C#","phyton"])

programist1.informasa_goster()


print("---------------------------------------------")

programist2 = Programist("shariyar","mirzoyev,",18423,10000,["c","phyton","html"])

programist2.informasa_goster()


