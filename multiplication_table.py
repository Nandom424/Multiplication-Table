import tkinter as tk

def show_table():
    output.delete('1.0', tk.END)  # Clear previous output
    name = name_entry.get()
    try:
        table = int(table_entry.get())
        output.insert(tk.END, f"Hello, {name}! Here's the {table} times table:\n\n")
        for x in range(1, 11):
            output.insert(tk.END, f"{table} x {x} = {table * x}\n")
    except ValueError:
        output.insert(tk.END, "Please enter a valid number.\n")

# Create the main window
root = tk.Tk()
root.title("Multiplication Table")

# Name input
tk.Label(root, text="What is your name?").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Table input
tk.Label(root, text="Which multiplication table do you want?").pack()
table_entry = tk.Entry(root)
table_entry.pack()

# Show table button
tk.Button(root, text="Show Table", command=show_table).pack()

# Output display
output = tk.Text(root, height=15, width=40)
output.pack()

# Run the GUI
root.mainloop()
