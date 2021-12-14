

from abc import abstractmethod


class PC:
    def __init__(self,name_company,cpu,ram,power_supply):
        self.name_company=name_company
        self.cpu=cpu
        self.ram=ram
        self.power_supply=power_supply
        
           
    def components_name(self,name_cpu,name_ram):
        self.cpu=self.cpu, name_cpu
        self.ram=self.ram, name_ram
        
            
   
    def __str__(self):
         return f"Name computer is: {self.name_company}, his cpu is: {self.cpu}, his ram is {self.ram} and power supply {self.power_supply}"
     
 
 
 
    def checking_power_supply(self):
        if self.power_supply>0:
            print("PC has positive supplies power")
        else:
            print("Ps has negative draws power")