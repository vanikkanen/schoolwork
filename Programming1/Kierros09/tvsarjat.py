"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.
    :param filename: str, name of the file to be read
    :return: dict, returns a dictionary of the shows and genres
    """

    shows = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            for genre in genres:
                if genre in shows:
                    shows[genre] += "," + name
                else:
                    shows[genre] = name

        file.close()
        return shows

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)
    genres = ""

    for data in sorted(genre_data.keys()):
        if genres == "":
            genres = str(data)
        else:
            genres += (f", {str(data)}")

    print(f"Available genres are: {genres}")

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        if genre not in genre_data:
            pass
        else:
            shows = genre_data[genre].split(",")
            for show in sorted(shows):
                print(show)


if __name__ == "__main__":
    main()
