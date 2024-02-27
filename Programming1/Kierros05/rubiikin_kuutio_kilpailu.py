'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def avg_score(times):
    """
    Calculates the correct score from the list
    :param times: list, contains the times
    :return:
    """
    times.sort()
    del times[0]
    del times[3]

    avg_score = (times[0] + times[1] + times[2])/3
    return avg_score

def make_list():
    """
    Makes a list of the scores
    :return:
    """
    list = []

    for index in range(1,6):
        score = float(input(f"Enter the time for performance {index}: "))
        list.append(score)

    return list

def main():

    times = make_list()
    score = avg_score(times)

    print(f"The official competition score is {score:.2f} seconds.")

if __name__ == "__main__":
    main()
