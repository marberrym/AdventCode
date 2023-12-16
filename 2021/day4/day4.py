from os import read
import numpy as np;


f = open('input.txt', 'r');
readings = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

def main(boards):
    numbersToBeCalled = boards[0].split(',');
    calledNumbers = [];
    gameBoards = makeBoards(boards);

    for number in numbersToBeCalled:
        gameBoards = callNumber(gameBoards, number)
        calledNumbers.append(number)

        if len(calledNumbers) >= 5:
            winnerFound = checkForWinner(gameBoards)
            if winnerFound != False:
                print("FOUND A WINNER!")
                return generateAnswer(winnerFound[0], number)

def makeBoards(boards):
    gameBoards = [];
    currentBoard = [];
    for x in range(len(boards)):
        if x != 0 and boards[x] != "":
            currentBoard.append(boards[x].split())
            if x == len(boards) - 1:
                gameBoards.append(currentBoard);
                currentBoard = [];
        elif boards[x] == "" and x != 1:
            gameBoards.append(currentBoard);
            currentBoard = [];
    return gameBoards

def callNumber(boards, number):
    for board in boards:
        for row in board:
            for x in range(len(row)):
                if row[x] == number:
                    row[x] = "X"

    return boards

def checkForWinner(boards):
    for board in boards:
        if checkBoard(board) == True:
            return board, True
    return False

def checkBoard(board):
    for x in range(len(board)):
        if 'X' in board[x]:
            if checkHorizontalWin(board[x]) == True:
                return True
            for y in range(len(board[x])):
                if board[x][y] == 'X':
                    if checkVerticalWin(board, y) == True:
                        return True
    return False

def checkHorizontalWin(row):
    for number in row:
        if number != 'X':
            return False
    return True

def checkVerticalWin(board, position):
    for row in board:
        if row[position] != 'X':
            return False
    return True


def generateAnswer(board, number):
    boardSum = 0
    for row in board:
        for num in row:
            if num != "X":
                boardSum += int(num)
    print("board sum", int(boardSum))
    print("winning number", int(number))
    print("answer is...", boardSum * int(number))

def removeWinner(boards):
    for board in boards:
        if checkBoard(board) == True:
            boards.remove(board)


def main2(boards):
    numbersToBeCalled = boards[0].split(',');
    calledNumbers = [];
    gameBoards = makeBoards(boards);
    amountOfBoards = len(gameBoards);
    wonBoards = 0;

    for number in numbersToBeCalled:
        gameBoards = callNumber(gameBoards, number)
        calledNumbers.append(number)

        if len(calledNumbers) >= 5:
            winnerFound = checkForWinner(gameBoards)
            if winnerFound != False:
                print(gameBoards)
                wonBoards += 1
                print("Winner found")
                print("Win count is...", wonBoards)
                print("total boards is...", amountOfBoards)
                if wonBoards == amountOfBoards or len(gameBoards) == 1:
                    return generateAnswer(winnerFound[0], number)
                else:
                    removeWinner(gameBoards)





main2(readings)