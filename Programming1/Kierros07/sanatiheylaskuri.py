'''
COMP.SC.100 # Laskee ja tulostaa käyyätjän syöttämän tekstin sanojen ilmenemis
määrän.
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    words = {}
    do_loop = True
    print("Enter rows of text for word counting. Empty row to quit.")

    while do_loop:
        text = input().lower()
        text_in_words = text.split(" ")

        if text == "":
            do_loop = False

        else:
            for word in text_in_words:
                if word not in words:
                    words[word] = 1
                else:
                    words[word] += 1

    for entry in sorted(words):
        print(entry, ":", words[entry], "times")

if __name__ == "__main__":
    main()
