from Jatekos import Jatekos
class Jatekos:
    def __init__(self):
        self.harcos=Jatekos("Tubamtolog",0,"harcos","👲")
        self.varazslo=Jatekos("Pötyi Laci",2,"varazslo","🧙‍♀️")
        self.lista=["_", "_" ,"_"]
        self.lista[self.harcos.poz]=self.harcos.emo
        self.lista[self.varazslo.poz]=self.varazslo.emo
        self.kor=1
        self.kiir()

    def kiir(self):
        print(f"{self.kor}. kör")
        print("*"*15," ","-"*27," "*29," ")
        print(f"* {self.lista[0]:<3} {self.ista[1]:^3} {self.lista[2]:>3} * | A harcos neve: {self.harcos.nev} Harcos HP-ja: {self.harcos.hp} Varázsló neve: {self.varazslo.nev} |")
        print("*"*15," ", "-"*27," "*29," ")
        print("")
    n=1
    kiir(n)
    
    def jatekmenet(self):
        while(self.harcos.hp>0 and self.varazslo.hp>0):
            self.harcos.set_pozicio() #lép a harcos
            self.varazslo.set_pozicio() #lép a varázsló
            self.lista=["_", "_" ,"_"]
            self.lista[self.harcos.poz]=self.arcos.emo
            self.lista[self.varazslo.poz]=self.varazslo.emo
            if(self.harcos.poz==self.varazslo.poz):
                self.lista[self.varazslo.poz]="⚔"
                self.harcos.set_hp()
                self.varazslo.set_hp()
    n+=1
    kiir(n)
    input()    

