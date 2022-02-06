from itertools import permutations
from time import time

def recursiveCheck(testList, index, sumIndex, totalIndex):
    if index == len(testList) / 2:
        if sumIndex == totalIndex:
            return False

        else:
            return True

    dnes = [
        testList[3],
        testList[2],
        testList[1],
        testList[0]
        ]

    erom = [
        testList[1],
        testList[6],
        testList[5],
        testList[4]
        ]

    yenom = [
        testList[7],
        testList[1],
        testList[2],
        testList[5],
        testList[4]
        ]

    sumIndex += dnes[index] * 10 ** index
    sumIndex += erom[index] * 10 ** index
    totalIndex += yenom[index] * 10 ** index
    
    if sumIndex != totalIndex and sumIndex != totalIndex + 10 ** (index + 1):
        return False

    else:
        return recursiveCheck(testList, index + 1, sumIndex, totalIndex)

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

    index = 0
    sumIndex = 0
    totalIndex = 0
    
    while index < len(send):
        sumIndex += send[len(send) - 1 - index] * 10 ** index
        sumIndex += more[len(more) - 1 - index] * 10 ** index
        totalIndex += money[len(money) - 1 - index] * 10 ** index

        if(sumIndex != totalIndex and sumIndex != totalIndex + 10 ** (index + 1)):
            return False
        
        else:
            index += 1
    
    if(sumIndex == totalIndex + 10 ** (index)):
        return True

    else:
        return False

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
        if recursiveCheck(permutation, 0, 0, 0):
            answer = permutation
            break
'''
        if heuristicCheck(permutation):
            for i in permutation:
                answer.append(i)
            break

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
