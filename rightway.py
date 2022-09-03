"""Podstawowe jednostki
waga:gram
czas:minuty
długość:cm"""
version="3"
name="r/si"
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
        return f"{cm/self.length_number}{self.length}"
    def czas(self,min):
        return f"{min/self.time_number}{self.time}"
class Pi:
    
    mass_link="https://www.facebook.com/MariekeGouda/photos/do-you-know-how-much-a-cheese-wheel-weighsa-wheel-of-cheese-weighs-20-pounds-dur/10154769862681139/?_rdr"
    mass_calculation="""
    How to calculate mass of somthing in pi? well we still stick to radients!
    if one cheese wheel(acording to link) is weighting 9.07185 and we split it by half(by drawing point on hist cicrufrement every π 
    rad and draw line between) we have 1/2 of this weightt(4.535925kg) and that is our constant
    (symbol is 🧀(π)rad))
    """
    mass="🧀(π)rad"
    mass_number=4.535925*1000 #też około
    length="π²cm" 
    length_number=19.73863 #około
    def waga(self,g):
        return f"{g/self.mass_number}{self.mass}"
    def dlug(self,cm):
        return f"{2*cm/self.length_number}{self.length}"
    def czas(self,min):
        if min>15:
            h=min//60
            min-=h*60
            half=min//30
            min-=half*30
            quat=min/15
            data=h+half+quat*0.5
            if int(data)==data:
                return f"{int(data)}π rad"
            else:
                return f"{data}π rad"
class Redditor:
    "Reditor"
    lenght="RM"
    lenght_number=210.312
    mass="RKG"
    mass_number=31488.382
    time="RS"
    time_number= 2.2092
    def waga(self,g):
        return f"{g/self.mass_number}{self.mass}"
    def dlug(self,cm):
        return f"{cm/self.lenght_number}{self.lenght}"
    def czas(self,min):
        return f"{min/self.time_number}{self.time}"
systemy={"SI":Si(),"Cool":Cu_Ol_Ln(),'bbb':BBB(),"🍌":BBB(),"ccc":ccc(),'pi':Pi(),'r/si':Redditor()}
jednostki={
    "czas":{"s":['d',60],"min":['m',1],"h":['m',60],'d':['m',60*24]},
    "dlug":{'mm':['d',10],'cm':['m',1],"m":["m",100],'km':['m',100000]},
    "waga":{"g":['m',1],'kg':['m',1000],'t':['m',1000000]}
}
