'''
You are given an integer array of size N, representing jars of chocolates. Three
students A, B, and C respectively, will pick chocolates one by one from each chocolate
jar, till the jar is empty, and then repeat the same with the rest of the jars. Your task
is to fine and return an integer value representing the total number of chocolates that
student A will have, after all the chocolates have been picked from all the jars.
Note: Once a jar is done A will start taking the chocolates from the new jar.
Input Format :
input1: An integer array representing the quantity of chocolates in each jar.
input2: An integer value N representing the number of jars.
Output Format:
Return an integer value representing the total number of chocolates that student A
will have, after all the chocolates are picked.
Example:
Input:
10 20 30
3
Output:
21
'''
def chocolates_for_A(jars,N):
    count_A=0
    for chocolates in jars:
        # Every 3 turns, A gets the 1st, 4th, 7th... chocolates
        # So A gets 1 out of every 3 chocolates
        # Which is (chocolates + 2) // 3 (ceil of chocolates / 3)
        count_A += (chocolates + 2) // 3
    return count_A

input1=[10, 20, 30]
input2=3
print(chocolates_for_A(input1,input2))  
