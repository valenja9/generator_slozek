# prvni budeme importovat nase vytvorene moduly
from soubory_pro_vytvoreni import soubory
from pomocne_funkce import *
import sys


def main():
    jmeno_slozky = sys.argv[1]
    vytvor_pocet_slozek(jmeno_slozky, soubory)


if __name__ == "__main__":
    main()


