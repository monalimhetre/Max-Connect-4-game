import maxconnect4
from MaxConnect4Game import maxConnect4Game
from copy import deepcopy
import sys

def alphabetadecision(state):
    list_of_a_and_v = []
    for a,s in succesors(state):
        v = MinValue(state=s, minint=-2147483647, maxint=2147483648, depth=deepcopy(state.depth))
        list_of_a_and_v.append((a,v))
    counter = 0
    for a_and_v in list_of_a_and_v:
        if counter == 0:
            a = a_and_v[0]
            v = a_and_v[1]
            counter = counter + 1
            continue
        if a_and_v[1] > v:
            a = a_and_v[0]
            v = a_and_v[1]
        counter = counter + 1
        # print(a,v)
    return a

def MinValue(state, minint, maxint, depth):
    if state.checkPieceCount() == 42 or depth == 1:
        state.countScore()
        return state.scoreCount()
    v = 2147483648
    for a,s in succesors(state):
        v = min(v,MaxValue(s,minint,maxint,deepcopy(depth-1)))
        if v <= minint:
            return v
        maxint = min(maxint,v)
    return v

def MaxValue(state, minint, maxint, depth):
    if state.checkPieceCount() == 42 or depth == 1:
        state.countScore()
        return state.scoreCount()

    v = -2147483647
    for a,s in succesors(state):
        v = max(v,MinValue(s,minint,maxint,deepcopy(depth-1)))
        if v >= maxint:
            return v
        minint = max(minint, v)
    return v

def succesors(state):
    playPieceList = []
    if state.currentTurn == 1:
        childTurn = 2
    else:
        childTurn = 1
    for i in range(7):
        new_gameBoard = maxConnect4Game()
        new_gameBoard.gameBoard = deepcopy(state.gameBoard)
        new_gameBoard.currentTurn = childTurn
        if new_gameBoard.playPiece(i):
            # new_gameBoard.checkPieceCount()
            playPieceList.append((i,new_gameBoard))
    return playPieceList

