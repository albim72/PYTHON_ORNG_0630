class Osoba:

    def __init__(self,imie,nazwisko,wiek,waga,wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        self.info()

    def info(self):
        print("Tworzenie nowej osoby.....")

    def print_osoba(self):
        print(f"dane osoby -> imię: {self.imie}, nazwisko: {self.nazwisko}, wiek: {self.wiek} lat"
              f"wzrost: {self.wzrost} cm, waga: {self.waga} kg")

    def wiekza10lat(self):
        return self.wiek + 10

    def czypracownik(self):
        return False


p1 = Osoba("Jan","Kowal",40,99,171)
print(f"kolor oczu: {p1.kolor_oczu}")
p1.print_osoba()
print(f"wiek za 10 lat: {p1.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {p1.czypracownik()}")


print("____________________________________________________")

p2 = Osoba("Olga","Kot",31,52,169)
p2.kolor_oczu = "niebieskie"
print(f"kolor oczu: {p2.kolor_oczu}")
p2.print_osoba()
print(f"wiek za 10 lat: {p2.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {p2.czypracownik()}")


class Pracownik(Osoba):

    # konstuktor z dziedziczeniem
    def __init__(self,imie,nazwisko,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie):
        super().__init__(imie,nazwisko,wiek,waga,wzrost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie

    def print_pracownik(self):
        super().print_osoba()
        print(f"dane pracownika -> firma: {self.firma}, stanowisko pracy: {self.stanowisko}, lata pracy: "
              f"{self.latapracy}, wynagrodzenie: {self.wynagrodzenie} zł")

    def czypracownik(self):
        return True;


e1 = Pracownik("Tomasz","Pyć",45,98,180,"ABC","dyektor",5,10800)
print(f"kolor oczu: {e1.kolor_oczu}")
e1.print_pracownik()
print(f"wiek za 10 lat: {e1.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {e1.czypracownik()}")

class Sport:

    def __init__(self, dyscyplina,lataupr,best_wynik):
        self.dyscyplina = dyscyplina
        self.lataupr = lataupr
        self.best_wynik = best_wynik

    def infosport(self):
        print(f"dysycyplina: {self.dyscyplina}, lata uprawiania: {self.lataupr}, życiówka: {self.best_wynik}")


class Ekstra:
    pass

class Student(Pracownik,Sport,Ekstra):

    # konstruktor z wielodziedziczeniem`

    def __init__(self,imie,nazwisko,wiek,waga,wzrost,nrstudenta,kierunek,rokstudiow,
                 firma="",stanowisko="",latapracy="",wynagrodzenie="",dyscyplina="",lataupr="",best_wynik=""):
        Pracownik.__init__(self,imie,nazwisko,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie)
        Sport.__init__(self,dyscyplina,lataupr,best_wynik)
        self.nrstudenta = nrstudenta
        self.kierunek = kierunek
        self.rokstudiow = rokstudiow

    def print_student(self):
        print(f"infromacje o studencie: {self.nrstudenta}, kierunek studiów: {self.kierunek}, "
              f"rok studiów: {self.rokstudiow}")

    def czypracownik(self):
        return self.firma != ""


print("___________________________________________________")
s1 = Student("Henryk","Kot",50,78,178,435353,"informatyka",4,"XYX","programista",1,3200)
s1.print_pracownik()
s1.print_student()
print(f"wiek za 10 lat: {s1.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {s1.czypracownik()}")


print("___________________________________________________")
s2 = Student("Henryk","Jonik",22,69,171,4343234,"budowa mostów",3)
s2.print_osoba()
s2.print_student()
print(f"wiek za 10 lat: {s2.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {s2.czypracownik()}")

print("___________________________________________________")
s3 = Student("Hanna","Bryzga",24,53,172,6456345,"filozofia",3,dyscyplina="biegi ultra",
             lataupr=4, best_wynik="102km 18h 54min 2s")
s3.print_osoba()
s3.print_student()
s3.infosport()
print(f"wiek za 10 lat: {s3.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {s3.czypracownik()}")






