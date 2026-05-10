n = int(input("Enter number of queens: "))

board = [-1] * n

# Check if queen placement is safe
def is_safe(row, col):

    for i in range(row):

        if (board[i] == col or
            abs(board[i] - col) == abs(i - row)):
            return False

    return True


# Solve N Queens
def solve(row):

    if row == n:

        print("\nSolution:")

        for i in range(n):
            for j in range(n):

                if board[i] == j:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")

            print()

        return

    for col in range(n):

        if is_safe(row, col):
            board[row] = col
            solve(row + 1)


solve(0)
