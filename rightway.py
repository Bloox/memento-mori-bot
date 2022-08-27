"""Podstawowe jednostki
waga:gram
czas:minuty
długość:cm"""
def base_convert(j,d):
    if d[0]=='d':return j/d[1]
    elif d[0]=='m':return j*d[1]
class Si:...
class Cu_Ol_Ln:
    mass="¹²C Atoms weights" 
    mass_symbol="♀"
    mass_number=62
    MOL_TO_GRAM=114.818
    lenght="Oliver Height(from only murders in building)"
    lenght_symbol="🎩"
    lenght_number=170.18
    time="Longest night"
    time_symbol="🝰"
    time_number=14*60+28

    def gram_to_mol(self,gram):
        return gram*self.MOL_TO_GRAM

    def waga(self,gram):
        data=self.gram_to_mol(gram)
        #print(data/mass_number,data/12)
        return f"{data/self.mass_number}{self.mass_symbol}"

    def dlug(self,cm):
        return f"{cm/self.lenght_number}{self.lenght_symbol}"
    def czas(self,min):
        return f"{min/self.time_number}{self.time_symbol}"

systemy={"SI":Si(),"Cool":Cu_Ol_Ln()}
jednostki={
    "czas":{"s":['d',60],"m":['m',1],"H":['m',60],'d':['m',60*24]},
    "dlug":{'mm':['d',10],'cm':['m',1],"m":["m",100],'km':['m',100000]},
    "waga":{"g":['m',1],'kg':['m',1000],'t':['m',1000000]}
}