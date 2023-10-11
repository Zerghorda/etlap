import etlapmodul
import rendelesFel
import rendeles
i = 0
etlap_hossz = 60
levesek = ["Húsleves", "Gyűmőlcsleves"]
levesAr = [1999, 1500]
foetelek = ["Csirkepörkölt", "Mátrai borzaska"]
foetelAr = [2980, 4570]
rendelt = []
rendeltAr = [1999, 1500, 2980, 4570]

etlapmodul.sor("*", etlap_hossz)
etlapmodul.cim("*", "Étlap", "*", etlap_hossz)
etlapmodul.sor("*", etlap_hossz)
etlapmodul.cim("*", "# Levesek #", "*", etlap_hossz)
etlapmodul.kaja("*", levesek[0], levesAr[0], "Ft", "*", etlap_hossz)
etlapmodul.kaja("*", levesek[1], levesAr[1], "Ft", "*", etlap_hossz)
etlapmodul.cim("*", "# Főételek #","*",etlap_hossz)
etlapmodul.kaja("*", foetelek[0], foetelAr[0], "Ft", "*", etlap_hossz)
etlapmodul.kaja("*", foetelek[1], foetelAr[1], "Ft", "*", etlap_hossz)
etlapmodul.sor("*", etlap_hossz)
etlapmodul.cim("*", "Jó Étvágyat!", "*", etlap_hossz)
etlapmodul.sor("*", etlap_hossz)






#while i < len(rendelt):
 #   rendeles.rendeles("*", rendelt, rendeltAr, "FT", "*", etlap_hossz)
#rendeles.osszeg("*", "Összesen:", sum(levesAr), "FT", "*", etlap_hossz)
