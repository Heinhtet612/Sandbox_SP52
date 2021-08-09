"""
Replace the contents of this module docstring with your own details
Name: Hein Htet Ko
Student ID: 13807190
Date started: 06/August/2021
GitHub URL: https://github.com/Heinhtet612/SP52_Assignment01
"""

name = "places.csv"

def main():
    print("Travel Tracker 1.0 - by <Hein Htet Ko>")
    print(readfile(), "Places loaded from places.csv")
    callmenu = menu()
    # CALLING MENU #
    while callmenu != "Q":
        if callmenu == "L":
            open1()
            callmenu = menu()
        elif callmenu == "A".upper():
            add()
            callmenu = menu()
        elif callmenu == "M".upper():
            visitplace = readfile1()
            if visitplace > 0:
                open1()
                visit()
                callmenu = menu()
            else:
                print("No Unvisited Place")
                callmenu = menu()
        else:
            print("Invalid menu choice")
            callmenu = menu()

    print(readfile(), "Places saved in places.csv")
    print("Have a nice day :) ")
    sortcsvfile()


def menu():
    # display menu and input choice of menu
    menuinput = input("""Menu:
    L - List Places
    A - Add new place
    M - Mark a place as visited
    Q - Quit
    >>>""").upper()
    return menuinput


def open1():
    # open csv file and display
    import csv
    with open('places.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        datasort = sorted(reader, key=lambda row: (row[3], (int(row[2]))))
        count = 0
        row_count = sum(1 for row in datasort)
        row_count1 = 0
        for row in datasort:
            if row[3] == 'n':
                row_count1 = row_count1 + 1
            count = count + 1
            notvis = row[3].replace('n', '*').replace('v', ' ')

            print(notvis, '{:>1}'.format(count), '{:>0}'.format('.'), '{:<10}'.format(row[0]), "in",
                  '{:<20}'.format(row[1]), "Times", '{:<10}'.format(row[2]))
        if row_count1 == 0:
            print(row_count, "Places, No places left to visit. Why not add a new place?")
        else:
            print(row_count, "Places, you still want to visit", row_count1, "places")

    csvFile.close()


def add():
    # to append and add new line data in csv
    import csv
    while True:
        x = input("Name: ")

        if x.isalpha() or '':
            break
        print("Input can not be blankl")
    while True:
        y = input("Country: ")

        if y.isalpha() or '':
            break
        print("Input can not be blank")

    class NotPositiveError(UserWarning):
        pass

    while True:
        z = input("Times: ")

        try:
            number = int(z)
            if number <= 0:
                raise NotPositiveError
            break
        except ValueError:
            print("Invalid input; enter a valid number")
        except NotPositiveError:
            print("Number must be > 0")

    vn = "n"

    print(x, "in", y, ("Times", z), "Has been added to travel tracker")
    newrow = [x, y, z, vn]

    with open('places.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(newrow)
    csvFile.close()


def visit():
    # to mark unvisited place to visited
    import csv
    with open('places.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        datasort = sorted(reader, key=lambda row: (row[3], (int(row[2]))))

    while True:  # cheching og error
        try:
            x = int(input("Enter the number of a place to mark as visited"))
            if x > sum(1 for row in datasort):
                print("Invalid place number!")
                continue
            elif x <= 0:
                print("Number must be > 0")
                continue
        except ValueError:
            print("Invalid! Enter a valid number")
            continue
        else:
            break

    with open('places.csv', 'w', newline='') as csvFile1:
        writer = csv.writer(csvFile1)
        num = 0
        for row in datasort:
            num = num + 1
            if num == "x":
                if row[3] == "v":
                    print("Place is already visited")
                else:
                    row[3] = "v"
                    print(row[0], "in", row[1], "is visited")

            writer.writerow(row)

    csvFile.close()
    csvFile1.close()


def readfile():
    # to sum lines in csv
    import csv
    with open('places.csv', 'r') as csvfile2:
        reader = csv.reader(csvfile2)
        row_count = sum(1 for row in reader)
    return row_count
    csvfile2.close()


def readfile1():
    import csv
    with open('places.csv', 'r') as csvfile2:
        reader = csv.reader(csvfile2)
        visit = 0
        for row in reader:
            if row[3] == 'n':
                visit = visit + 1
            else:
                visit = visit
    csvfile2.close()
    return visit


def sortcsvfile():
    import csv
    with open("places.csv", "r") as csvfile3:
        data = csv.reader(csvfile3)
        sortedlist = sorted(data, key=lambda row: (row[3], int(row[2])))
    with open("places.csv", "w", newline='') as f:
        fileWriter = csv.writer(f)
        for row in sortedlist:
            fileWriter.writerow(row)
    csvfile3.close()
    f.close()


main()

if __name__ == '__main__':
    main()