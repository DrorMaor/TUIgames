import random
import argparse

def GenerateRandom(KW, AMFM):
    CallLetters = ""
    if KW == "":
        random.seed()
        CallLetters = "W" if random.randint(0, 1) == 0 else "K"
    else:
        CallLetters = KW
    for i in range (1, 4):
        random.seed()
        CallLetters += chr(random.randint(65, 90))

    if AMFM == "":
        random.seed()
        AMFM = "AM" if random.randint(0, 1) == 0 else "FM"

    Frequency = 0
    if AMFM == "AM":
        Frequency = random.randint(54, 160) * 10
    else:
        Frequency = random.randint(88, 108) + (random.randint(0, 10) / 10)

    print (f"{CallLetters} {str(Frequency)} {AMFM}")

def main():
    parser = argparse.ArgumentParser(description="Process arguments.")
    parser.add_argument("-a", action="store_true", help="AM")
    parser.add_argument("-f", action="store_true", help="FM")
    parser.add_argument("-k", action="store_true", help="K - West of the Mississipi")
    parser.add_argument("-w", action="store_true", help="W - East of the Mississipi")
    args = parser.parse_args()
    #print(args)

    AMFM = ""
    KW = ""
    if args.a is not None and args.f is None:
        AMFM = "AM"
    elif args.f is not None and args.a is None:
        AMFM = "FM"
    elif args.w is not None and args.k is None:
        KW = "W"
    elif args.k is not None and args.w is None:
        KW = "K"

    GenerateRandom(KW, AMFM)

if __name__ == "__main__":
    main()
