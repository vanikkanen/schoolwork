'''
COMP.SC.100 # Tulostaa Yogi bear laulun halutulla toistomäärällä ja nimellä
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def repeat_name(name,number):
    """Tulostaa halutun määrän haluttua nimeä"""
    for rivi in range(0, number):
        print(name,', ',name,' Bear',sep = '')

def verse(lyric,name):
    """Tulostaa halutun säkeistön"""
    print(lyric)
    print(name,', ', name, sep = '')
    print(lyric)
    repeat_name(name,3)
    print(lyric)
    print(name, ', ', name,' Bear', sep='')
    print()

def main():

    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == "__main__":
    main()
