import os
def vytvor_pocet_slozek(jmeno_slozky, soubory):
    list_jmen = []
    for i in range(1,6):
        list_jmen.append(jmeno_slozky+str(i))
    for jmeno_sl in list_jmen:
        os.mkdir(jmeno_sl)
        vytvoreni_souboru(list_jmen, soubory)

def vytvoreni_souboru(list_jmen, soubory):
    for jmeno in list_jmen:
        for soubor in soubory:
            with open(f"{jmeno}/{soubor}", mode="w") as file:
                print(f"soubor byl vytvoren: {soubor}")