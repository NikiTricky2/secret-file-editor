import tkinter as tk
from tkinter.filedialog import askopenfilename

window = tk.Tk()
window.title("Secret File Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

filepath = None
 
class popupWindow(object):
    def __init__(self,master):
        top=self.top=tk.Toplevel(master)
        self.l=tk.Label(top,text="Enter secret path")
        self.l.pack(pady=10)
        
        self.e=tk.Entry(top, width=50)
        self.e.pack(padx=5)
        
        self.b=tk.Button(top,text='Ok',command=self.cleanup)
        self.b.pack(pady=10)
        
        self.value = ""
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

def open_file():
    global filepath
    filepath = askopenfilename(
        filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")]
    )
    if not filepath:
        return
    popup = popupWindow(window)
    while popup.value == "":
        window.update()
    txt_edit.delete(1.0, tk.END)
    try:
        with open(filepath + ":" + popup.value, "r", encoding='utf-8') as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
    except OSError:
        with open(filepath + ":" + popup.value, "w+", encoding='utf-8') as save_file:
            save_file.write("")
        with open(filepath + ":" + popup.value, "r", encoding='utf-8') as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
    filepath = filepath + ":" + popup.value
    window.title(f"Secret File Editor - {filepath}")

def save_file():
    global filepath
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")

txt_edit = tk.Text(window)
scrollbar = tk.Scrollbar(window ,orient="vertical")

scrollbar.config(command=txt_edit.yview)
txt_edit.config()

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
scrollbar.grid(row=0, column=2, sticky="nsew")

window.mainloop()
