from assignment import Assignment

if __name__ == "__main__":
    try:

        days = int(input("Enter number of days:"))
    except Exception as e:
        print(e)
    else:
        assignment = Assignment(days)
        print("Number of ways to attend classes {} days is {}".format(days, assignment.no_ways_attend_classes()))
        print("probability to miss ceremony is {}".format(assignment.probability_to_miss_ceremony()))



