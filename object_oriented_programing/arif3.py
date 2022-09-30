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
        
    def dil_elave_et(self,yeni_dil):
    
         self.diller.append(yeni_dil)
    
         print("dil Elave olundu")
         
    def maas_artir(self,artim_miqdari):
        
        self.maas += artim_miqdari
        
        print("maas artirildi")
        
    
programist1 = Programist("David","aliyev",17536,2000,["c","phyton","assembler"])

programist1.dil_elave_et("java")
programist1.maas_artir(2000)

programist1.informasa_goster()