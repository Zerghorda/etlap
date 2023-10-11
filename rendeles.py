def rendeles(jel1, rendelt, rendeltAr, penznem, jel2, etlap_hossz):
    hossz: int = etlap_hossz - (len(jel1) + len(jel2))
    print(f"{jel1},{rendelt:^},{rendeltAr},{penznem},{jel2}")


def osszeg(jel1, szoveg, szam, penznem, jel2, etlap_hossz):
    hossz: int = int(etlap_hossz / 5)
    szamhossza = str(szam)
    print(f"{jel1:<{hossz-4}}{szoveg:>{hossz}}{szam:>{hossz*2}}{penznem}{jel2:>{hossz+4}}")
