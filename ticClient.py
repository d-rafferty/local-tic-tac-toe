# Client
import multiprocessing.connection
import time
while True:

    address = ('127.0.0.1', 0x1234)
    print("Connecting...")
    connection = multiprocessing.connection.Client(address, authkey=b"secret")
    print("Connected to: ", address)
    print("INSTRUCTIONS:")
    print("Enter a number 1-9 to make a move")
    print("The first person to get 3 in a row wins!")
    message = connection.recv()
    print(message)
    print("Waiting for game to start...")

    while True:
        turn = connection.recv()
        boardState = connection.recv()
        print(boardState[0], " | ", boardState[1], " | ", boardState[2])
        print("---+-----+-----")
        print(boardState[3], " | ", boardState[4], " | ", boardState[5])
        print("---+-----+-----")
        print(boardState[6], " | ", boardState[7], " | ", boardState[8], "\n\n")

        if turn == 1:
            move = input("Enter your move: ")
            connection.send(move)
            print("Move sent!")
            results = connection.recv()
            print(results)
        if turn == 2:
            print("Waiting for your turn...")
        if turn == 3:
            gameOver = connection.recv()
            print(gameOver)
            connection.close()
            time.sleep(100)








