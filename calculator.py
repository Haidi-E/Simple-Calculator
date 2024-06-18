import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid( columnspan=5, padx=10, pady=10)


# These variables are used to keep track of the current row and column numbers
# when placing buttons in the grid layout.
row_num = 1
col_num = 0

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C" 
]
def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)     # tk. END refers to the position after the existing text
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")   
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=10)
    button.grid(row=row_num, column=col_num, padx=5, pady=5)
    button.bind("<Button-1>", button_click)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()
