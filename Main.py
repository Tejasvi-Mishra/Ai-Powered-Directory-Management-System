import os
import shutil
import datetime
from tkinter import Tk, Label, Button, filedialog, messagebox, IntVar, DoubleVar, StringVar, Checkbutton
from tkinter import ttk
from file_organizer import categorize_files, FILE_CATEGORIES, THEMES

current_theme = "dark"

def toggle_theme(window, widgets, progress_bar, theme_label):
    global current_theme
    current_theme = "light" if current_theme == "dark" else "dark"
    theme = THEMES[current_theme]

    window.configure(bg=theme["bg"])
    theme_label.config(text=f"Theme: {current_theme.capitalize()}", fg=theme["fg"], bg=theme["bg"])

    for widget in widgets:
        widget.configure(bg=theme["btn_bg"], fg=theme["btn_fg"])
    progress_bar.configure(style=f"{current_theme}.Horizontal.TProgressbar")

def reset_interface(progress_var, file_count_var, summary_var, selected_categories, size_filter, date_filter):
    progress_var.set(0)
    file_count_var.set("Files Processed: 0/0")
    summary_var.set("Summary will appear here after organizing files.")
    for category in selected_categories:
        selected_categories[category].set(1)
    size_filter.set(0)
    date_filter.set(0)

def confirm_exit():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.destroy()

def open_folder(progress_var, file_count_var, selected_categories, summary_var, size_filter, date_filter):
    directory = filedialog.askdirectory(title="Select Directory")
    if directory:
        progress_var.set(0)
        file_count_var.set("Files Processed: 0/0")
        categorize_files(directory, progress_var, file_count_var, selected_categories, summary_var, size_filter, date_filter)
    else:
        messagebox.showwarning("Warning", "No directory selected!")

def create_gui():
    global root
    root = Tk()
    root.title("AI-Powered Directory Management System")
    root.geometry("500x800")
    root.configure(bg=THEMES[current_theme]["bg"])

    selected_categories = {category: IntVar(value=1) for category in FILE_CATEGORIES}

    progress_var = DoubleVar()
    file_count_var = StringVar(value="Files Processed: 0/0")
    summary_var = StringVar(value="Summary will appear here after organizing files.")

    size_filter = IntVar()
    date_filter = IntVar()

    label = Label(root, text="Organize Files by Type", font=("Arial", 20, "bold"), bg=THEMES[current_theme]["bg"],
                  fg=THEMES[current_theme]["fg"])
    label.pack(pady=10)

    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progress_bar.pack(pady=10, fill="x", padx=20)

    Label(root, textvariable=file_count_var, font=("Arial", 12), bg=THEMES[current_theme]["bg"],
          fg=THEMES[current_theme]["fg"]).pack()

    for category in FILE_CATEGORIES:
        Checkbutton(root, text=f"Organize {category} Files", variable=selected_categories[category], bg=THEMES[current_theme]["bg"],
                    fg=THEMES[current_theme]["fg"], selectcolor="#8D99AE").pack(anchor="w", padx=40)

    Checkbutton(root, text="Only files larger than 1MB", variable=size_filter, bg=THEMES[current_theme]["bg"],
                fg=THEMES[current_theme]["fg"], selectcolor="#8D99AE").pack(anchor="w", padx=40)

    Checkbutton(root, text="Only files modified in the last 30 days", variable=date_filter, bg=THEMES[current_theme]["bg"],
                fg=THEMES[current_theme]["fg"], selectcolor="#8D99AE").pack(anchor="w", padx=40)

    Button(root, text="Select Folder and Organize Files",
           command=lambda: open_folder(progress_var, file_count_var, selected_categories, summary_var, size_filter, date_filter),
           bg=THEMES[current_theme]["btn_bg"], fg=THEMES[current_theme]["btn_fg"]).pack(pady=10)

    Label(root, text="Keyboard Shortcuts: Ctrl+O (Open Folder), Ctrl+R (Reset), Ctrl+Q (Quit)",
          bg=THEMES[current_theme]["bg"], fg=THEMES[current_theme]["fg"]).pack(pady=5)

    Button(root, text="Reset", command=lambda: reset_interface(progress_var, file_count_var, summary_var, selected_categories, size_filter, date_filter), bg="#FFC107", fg="black").pack(pady=5)
    Button(root, text="Exit", command=confirm_exit, bg="#EF233C", fg="#EDF2F4").pack(pady=10)

    theme_label = Label(root, text=f"Theme: {current_theme.capitalize()}", font=("Arial", 12),
                        bg=THEMES[current_theme]["bg"], fg=THEMES[current_theme]["fg"])
    theme_label.pack(pady=5)

    widgets = [label, theme_label]

    Button(root, text="Toggle Theme", command=lambda: toggle_theme(root, widgets, progress_bar, theme_label),
           bg=THEMES[current_theme]["btn_bg"], fg=THEMES[current_theme]["btn_fg"]).pack(pady=5)

    Label(root, textvariable=summary_var, font=("Arial", 12), bg=THEMES[current_theme]["bg"], fg=THEMES[current_theme]["fg"]).pack(pady=10, fill="x", padx=10)

    style = ttk.Style(root)
    style.configure("dark.Horizontal.TProgressbar", troughcolor="#2B2D42", background="#8D99AE")
    style.configure("light.Horizontal.TProgressbar", troughcolor="#F7F7F7", background="#4CAF50")

    root.bind("<Control-o>", lambda event: open_folder(progress_var, file_count_var, selected_categories, summary_var, size_filter, date_filter))
    root.bind("<Control-r>", lambda event: reset_interface(progress_var, file_count_var, summary_var, selected_categories, size_filter, date_filter))
    root.bind("<Control-q>", lambda event: confirm_exit())

    root.mainloop()

if __name__ == "__main__":
    create_gui()
