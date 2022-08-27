"""Podstawowe jednostki
waga:gram
czas:minuty
długość:cm"""
version="2"
name="CCC :)"
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
class BBB:
    "Jednostak bananowej miary"
    lenght="🍌m"
    lenght_number=12.5
    mass="🍌g"
    mass_number=170
    time="🍌c"
    time_number=(365*24*60)*3+(366*24*60)
    def waga(self,g):
        return f"{g/self.mass_number}{self.mass}"
    def dlug(self,cm):
        return f"{cm/self.lenght_number}{self.lenght}"
    def czas(self,min):
        return f"{min/self.time_number}{self.time}"
class ccc:
    mass="cal/c²"
    mass_number=4.65532783453*(10**-14) #też około
    length="c/C₄"
    length_number=1_145_883.651147*100 #około
    time="1/C₄"
    time_number=0.0038222564329 * 60 #około

    def waga(self,g):
        return f"{g/self.mass_number}{self.mass}"
    def dlug(self,cm):
        return f"{cm/self.lenght_number}{self.lenght}"
    def czas(self,min):
        return f"{min/self.time_number}{self.time}"

systemy={"SI":Si(),"Cool":Cu_Ol_Ln(),'bbb':BBB(),"🍌":BBB(),"ccc":ccc()}
jednostki={
    "czas":{"s":['d',60],"m":['m',1],"H":['m',60],'d':['m',60*24]},
    "dlug":{'mm':['d',10],'cm':['m',1],"m":["m",100],'km':['m',100000]},
    "waga":{"g":['m',1],'kg':['m',1000],'t':['m',1000000]}
}