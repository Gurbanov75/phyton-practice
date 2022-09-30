class Avtomobil():
    def __init__(self,model,reng,at_gucu,silindir_sayi):
        self.model = model
        self.reng = reng
        self.at_gucu
        self.silindir_sayi
        
avtomobil1 = Avtomobil("Mercedes GLS", "qara",250,6)

print("avtomobil 1 model: ",avtomobil1.model)
print("avtomobil 1 reng: ",avtomobil1.reng)
print("avtomobil 1 at_gucu: ",avtomobil1.at_gucu)
print("avtomobil 1 silindir_sayi : ",avtomobil1.silindir_sayi)

print("---------------------------------------------")

avtomobil2 = Avtomobil("BMW","QARA",180,4)
print("avtomobil 2 model: ",avtomobil2.model)
print("avtomobil 2 reng: ",avtomobil2.reng) 
print("avtomobil 2 at_gucu: ",avtomobil2.at_gucu)
print("avtomobil 2 silindir_sayi : ",avtomobil2.silindir_sayi)


print(type("avtomobil1 obleyk tipi",avtomobil1))
print(type("avtomobil2 obyekt tipi",avtomobil2))