# Server

import multiprocessing.connection
import random


winner = 0 # used for determining winner
address = ('127.0.0.1', 0x1234)
listener = multiprocessing.connection.Listener(address, authkey=b"secret")
while True:
    print("Waiting for connection 1....")
    connection1 = listener.accept()
    print("Connection accepted from:", listener.last_accepted)
    print("Waiting for connection 2....")
    connection2 = listener.accept()
    print("Connection accepted from:", listener.last_accepted)

    connection1.send("You are 'Player1' - You are 'X'")
    connection2.send("You are 'Player2' - You are 'O'")


    firstMove = random.randint(1, 2)
    boardState = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # randomly decides who goes first
    if firstMove == 1:
        turn = 1
    else:
        turn = 2
    game = 1


    while game == 1:
        # serializedData = pickle.dumps(boardState)
        if turn == 1:
            connection1.send(1)
            connection2.send(0)
            connection1.send(boardState)
            connection2.send(boardState)
            move = connection1.recv()
            if boardState[int(move) - 1] > 9 or boardState[int(move) - 1] < 1:
                connection1.send("Invalid move, try again")

            elif boardState[int(move)-1] == 'O':
                connection1.send("Invalid move, try again")

            elif boardState[int(move) - 1] == 'X':
                connection1.send("Invalid move, try again")

            else:
                connection1.send("Success!")
                boardState[int(move) - 1] = 'X'
                turn = 2
        else:
            connection1.send(0)
            connection2.send(1)
            connection1.send(boardState)
            connection2.send(boardState)
            move = connection2.recv()

            if boardState[int(move) - 1] > 9 or boardState[int(move) - 1] < 1:
                connection2.send("Invalid move, try again")

            elif boardState[int(move) - 1] == 'X':
                connection2.send("Invalid move, try again")

            elif boardState[int(move) - 1] == 'O':
                connection2.send("Invalid move, try again")

            else:
                connection2.send("Success!")
                boardState[int(move) - 1] = 'O'
                turn = 1

        b1 = boardState[0]
        b2 = boardState[1]
        b3 = boardState[2]
        b4 = boardState[3]
        b5 = boardState[4]
        b6 = boardState[5]
        b7 = boardState[6]
        b8 = boardState[7]
        b9 = boardState[8]

        if b1 == 'X' and b2 == 'X' and b3 == 'X':
            winner = 1
        elif b4 == 'X' and b5 == 'X' and b6 == 'X':
            winner = 1
        elif b7 == 'X' and b8 == 'X' and b9 == 'X':
            winner = 1
        elif b1 == 'X' and b4 == 'X' and b7 == 'X':
            winner = 1
        elif b2 == 'X' and b5 == 'X' and b8 == 'X':
            winner = 1
        elif b3 == 'X' and b6 == 'X' and b9 == 'X':
            winner = 1
        elif b1 == 'X' and b5 == 'X' and b9 == 'X':
            winner = 1
        elif b3 == 'X' and b5 == 'X' and b7 == 'X':
            winner = 1

        if b1 == 'O' and b2 == 'O' and b3 == 'O':
            winner = 2
        elif b4 == 'O' and b5 == 'O' and b6 == 'O':
            winner = 2
        elif b7 == 'O' and b8 == 'O' and b9 == 'O':
            winner = 2
        elif b1 == 'O' and b4 == 'O' and b7 == 'O':
            winner = 2
        elif b2 == 'O' and b5 == 'O' and b8 == 'O':
            winner = 2
        elif b3 == 'O' and b6 == 'O' and b9 == 'O':
            winner = 2
        elif b1 == 'O' and b5 == 'O' and b9 == 'O':
            winner = 2
        elif b3 == 'O' and b5 == 'O' and b7 == 'O':
            winner = 2

        if winner == 1:
            game = 0
            connection1.send(3)
            connection2.send(3)
            connection1.send(boardState)
            connection2.send(boardState)
            connection1.send("Player1 won!")
            connection2.send("Player1 won!")
        if winner == 2:
            game = 0
            connection1.send(3)
            connection2.send(3)
            connection1.send(boardState)
            connection2.send(boardState)
            connection1.send("Player2 won!")
            connection2.send("Player2 won!")



