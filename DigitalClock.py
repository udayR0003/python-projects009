import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.resizable(False, False)

# Clock label
clock_label = tk.Label(
    root,
    font=("Arial", 50),
    padx=20,
    pady=40
)

clock_label.pack()


def update_clock():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)


# Start clock
update_clock()

# Run application
root.mainloop()