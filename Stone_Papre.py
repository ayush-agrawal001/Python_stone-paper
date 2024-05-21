import random
import sys

# Initialize win, lose, and tie counters
win = 0
lose = 0
tie = 0

def main():
    global playerMove
    while True:
        # Prompt player for their move
        playerMove = input("(r)ock, (p)aper, (s)cissor or (q)uit: ")
        if playerMove == "q":
            # Exit the game if the player chooses to quit
            sys.exit()
        elif playerMove in ["r", "p", "s"]:
            # Valid move: print the player's move, determine the PC's move, and check the outcome
            printPmove()
            pc()
            winScenario()
            # Print the current score
            print(f"{win} win, {lose} lose, and {tie} tie")
        else:
            # Handle invalid input
            print("Invalid input. Please enter r, p, s, or q.")

def printPmove():
    # Print the player's move
    if playerMove == "r":
        print("rock versus")
    elif playerMove == "p":
        print("paper versus")
    elif playerMove == "s":
        print("scissor versus")

def pc():
    global pcMove
    # Generate a random move for the PC
    pcMove = random.randint(1, 3)
    if pcMove == 1:
        pcMove = "r"
        print("Its Rock")
    elif pcMove == 2:
        pcMove = "p"
        print("Its Paper")
    elif pcMove == 3:
        pcMove = "s"
        print("Its Scissor")

def winScenario():
    global win, lose, tie
    # Determine the outcome of the game
    if pcMove == playerMove:
        print("It's a tie")
        tie += 1
    elif (pcMove == "r" and playerMove == "s") or (pcMove == "p" and playerMove == "r") or (pcMove == "s" and playerMove == "p"):
        print("PC wins")
        lose += 1
    else:
        print("You win")
        win += 1

if __name__ == "__main__":
    # Initial score printout
    print(f"{win} win, {lose} lose, and {tie} tie")
    # Start the main game loop
    main()
