if __name__ == '__main__':


    mark_1 = int(input("Enter Mark #1"))
    mark_2 = int(input("Enter Mark #1"))
    mark_3 = int(input("Enter Mark #1"))
    mark_4 = int(input("Enter Mark #1"))
    mark_5 = int(input("Enter Mark #1"))

    highest = max(mark_1, mark_2, mark_3, mark_4, mark_5)
    Lowest = min(mark_1, mark_2, mark_3, mark_4, mark_5)

    average = (mark_1 + mark_2 + mark_3 + mark_4 + mark_5) / 5


    print()
    print(f"Highest Mark: {highest}")
    print(f"Lowest Mark: {Lowest}")
    print(f"Average Mark: {average}")

    print(f"The Highest mark was {highest}, the lowest was {Lowest} and the average was {average}")


