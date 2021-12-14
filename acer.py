from pc import PC
class Acer(PC):
    def __init__(self, name_company, cpu, ram, power_suplly):
        super().__init__(name_company, cpu, ram, power_suplly)
        
    def __str__(self):
        return super().__str__()
         
    
acer=Acer("acer","intel core i7",16,11)

 
acer.components_name("cpu","ram")
print(acer.checking_power_supply())
print(acer)
