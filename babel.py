import random
from re import L

class Lang:
    def encoder(self,text):
        return text
    def decoder(self,text):
        return text


class Hexa(Lang):

    def encoder(self, text):
        
        return " ".join([hex(ord(i)) for i in text])

    def decoder(self, text):
        return "".join([chr(int(i.split('x')[1],16)) for i in text.split(' ')])
class Runy(Lang):
    runs={
        "a":"ᚨ",
        "b":"ᛒ",
        "c":"ᚲ",
        "d":"ᛞ",
        "e":"ᛖ",
        "f":"ᚠ",
        "g":"ᚷ",
        "h":"ᚺ",
        "i":"ᛁ",
        "j":"ᛃ",
        "k":"ᚲ",
        "l":"ᛚ",
        "m":"ᛗ",
        "n":"ᚾ",
        "o":"ᛟ",
        "p":"ᛈ",
        "r":"ᚱ",
        "s":"ᛊ",
        "t":"ᛏ",
        "u":"ᚢ",
        "w":"ᚹ",
        'x':"ᛦ",
        'y':"ᚣ",
        'z':"ᛉ"
    }
    def encoder(self, text):
        text=text.lower()
        #print(text)
        newtext=""
        
        for i in text:
            if i in self.runs:
                newtext+=self.runs[i]
            elif i == " ":
                newtext+=" "
            else:
                newtext+="¿"
        return newtext
    def decoder(self, text):
        text=text.lower()
        newtext=""
        runes={v:k for k,v in self.runs.items()}
        for i in text:
            if i in runes:
                newtext+=runes[i]
            elif i == " ":
                newtext+=" "
            else:
                newtext+="¿"
        return newtext
langs = {"hex":Hexa(),'Hexa':Hexa()} 

def translate_to(text,lang=None):
    if lang==None:lang=random.choice(langs)
    lang=langs[lang]
    p=lang.encoder(text)
    #print(p)
    return p
def translate_from(text,lang):
    lang=langs[lang]
    p=lang.decoder(text)
    #print(p)
    return p
