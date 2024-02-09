import tkinter as tk

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # Check if the current position is safe for the queen
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                return False
        return True

    def backtrack(row):
        if row == n:
            # All queens are placed, add the solution to the list
            solutions.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'  # Place the queen

                # Recur to the next row
                backtrack(row + 1)

                board[row][col] = '.'  # Remove the queen

    backtrack(0)
    return solutions
'''
# Example usage
n = int(input("Enter the size of the chessboard: "))
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-queens problem: {len(solutions)}")
for solution in solutions:
    print('\n'.join(solution))
    print()
'''
# Function to handle button click event
def solve_n_queens_gui():
    # Get the value from the entry widget
    n = int(entry.get())

    # Solve the N-Queens problem
    solutions = solve_n_queens(n)

    # Clear the text widget
    text.delete('1.0', tk.END)

    # Display the number of solutions
    text.insert(tk.END, f"Number of solutions for {n}-queens problem: {len(solutions)}\n\n")

    # Display each solution
    for solution in solutions:
        text.insert(tk.END, '\n'.join(solution))
        text.insert(tk.END, '\n\n')

# Create the main window
window = tk.Tk()
window.title("N-Queens Problem Solver")

# Create the label and entry widgets for user input
label = tk.Label(window, text="Enter the size of the chessboard:")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Create the solve button
button = tk.Button(window, text="Solve", command=solve_n_queens_gui)
button.pack()

# Create the text widget to display the solutions
text = tk.Text(window, height=10, width=50)
text.pack()

# Start the GUI main loop
window.mainloop()
