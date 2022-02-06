from itertools import permutations
from time import time

def heuristicCheck(testList):
    send = [
        testList[0],
        testList[1],
        testList[2],
        testList[3]
        ]

    more = [
        testList[4],
        testList[5],
        testList[6],
        testList[1]
        ]

    money = [
        testList[4],
        testList[5],
        testList[2],
        testList[1],
        testList[7]
        ]

    index = len(send) - 1
    
    while index >= 0:
        sumIndex = send[index] + more[index]
        totalIndex = [
            money[index + 1],
            money[index + 1] + 10
            ]

        if(sumIndex not in totalIndex):
            return False
        
        elif(sumIndex == totalIndex[1]):
            if(index == 0):
                for i in testList:
                    answer.append(i)
                
                return True

            else:
                send[index - 1] += 1

        index -= 1

def bruteForceCheck(testList):
    send = testList[0] * 1000 + testList[1] * 100 + testList[2] * 10 + testList[3]
    more = testList[4] * 1000 + testList[5] * 100 + testList[6] * 10 + testList[1]
    money = testList[4] * 10000 + testList[5] * 1000 + testList[2] * 100 + testList[1] * 10 + testList[7]

    if send + more == money:
        for index in testList:
            answer.append(index)

# Main Start
startTime = time()
numList = []
answer = []

for i in range(10):
    numList.append(i)

permList = list(permutations(numList, 8))

for permutation in permList:
    if permutation[0] != 0 and permutation[4] == 1:
        if heuristicCheck(permutation):
            break

'''
        #Check if (D + E = Y) or (D + E = Y + 10) Contributed by Nathaniel Mutkus
        if permutation[3] + permutation[1] == permutation[7] or permutation[3] + permutation[1] == permutation[7] + 10:
            bruteForceCheck(permutation)
'''

print(len(permList))
print(answer)

endTime = time()
print(endTime - startTime)

'''
01234567
SENDMORY
95671082
'''
