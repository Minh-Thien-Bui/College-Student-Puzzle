from itertools import permutations

def checkList(testList):
    send = testList[0] * 1000 + testList[1] * 100 + testList[2] * 10 + testList[3]
    more = testList[4] * 1000 + testList[5] * 100 + testList[6] * 10 + testList[1]
    money = testList[4] * 10000 + testList[5] * 1000 + testList[2] * 100 + testList[1] * 10 + testList[7]

    if send + more == money:
        for index in testList:
            answer.append(index)

numList = []
answer = []

for i in range(10):
    numList.append(i)

permList = list(permutations(numList, 8))

for permutation in permList:
    if permutation[0] != 0 and permutation[4] != 0:
        #Check if (D + E = Y) or (D + E = Y + 10) Contributed by Nathaniel Mutkus
        if permutation[3] + permutation[1] == permutation[7] or permutation[3] + permutation[1] == permutation[7] + 10:
            checkList(permutation)

print(len(permList))
print(answer)


'''
01234567
SENDMORY
95671082
'''
