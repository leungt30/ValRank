import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import main

input = ""
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return

    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
    global path 
    path = filepath
    window.title(f"{filepath}")


# def runbtn(self):
#     run(self.input)

def btnpress():
    print("Button pressed")
    print(path)
    #main.run()
    
path = ""




window = tk.Tk()
window.title("Simple Text Editor")







frm = tk.Frame(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
text = tk.Entry(frm)

btn_run = tk.Button(frm_buttons, text="Run", command=btnpress)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_run.grid(row=1, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")

frm.grid(row=1, column=0)

window.mainloop()
