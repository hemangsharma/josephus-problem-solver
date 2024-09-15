import tkinter as tk

def josephus_problem(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * josephus_problem(n // 2) - 1
    else:
        return 2 * josephus_problem((n - 1) // 2) + 1

def calculate():
    n = int(entry.get())
    result = josephus_problem(n)
    result_label.config(text=f"The person at position {result} survives.")

root = tk.Tk()
root.title("Josephus Problem")

# Add a title label with a larger font size
title_label = tk.Label(root, text="Josephus Problem", font=("Arial", 24))
title_label.pack(pady=10)

# Create a frame for the input section
input_frame = tk.Frame(root, bg="lightgray")
input_frame.pack(padx=10, pady=10)

label = tk.Label(input_frame, text="Enter the number of people:")
label.pack(side=tk.LEFT, padx=5)

entry = tk.Entry(input_frame, width=20)
entry.pack(side=tk.LEFT, padx=5)

button = tk.Button(input_frame, text="Calculate", command=calculate)
button.pack(side=tk.LEFT, padx=5)

# Create a frame for the result section
result_frame = tk.Frame(root, bg="lightgray")
result_frame.pack(padx=10, pady=10)

result_label = tk.Label(result_frame, text="", font=("Arial", 18))
result_label.pack(pady=10)

root.mainloop()
