'''
Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8
PM and will run until midnight (12 AM) i.e., for 4 hours. He also needs to travel to the
party venue within this time which takes him P minutes. The contest comprises
of N problems that are arranged in order of difficulty, with problem 1 being the
simplest and problem N being the most difficult. Max is aware that he will require 5*i
minutes to solve the ith problem.
Your task is help Max find and return an integer value, representing the number of
problems Max can solve and reach the party venue within the given time frame of 4
hours.
Note: Max will leave his home at exactly 8 PM to reach the party venue.
Input Format:
input1: An integer value N, representing the total number of problems.
input2: An integer value P, Representing the time to travel in minutes from his home
to the party venue.

'''
def max_problems_solved(N, P):
    available_time = 240 - P
    time_used = 0
    count = 0

    for i in range(1, N + 1):
        time_needed = 5 * i
        if time_used + time_needed <= available_time:
            time_used += time_needed
            count += 1
        else:
            break

    return count
N = 10  # total problems
P = 30  # travel time

print(max_problems_solved(N, P))  # Output will depend on N and P
