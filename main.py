import psutil
import tkinter as tk
from tkinter import filedialog


def set_cpu_affinity(exe_path, cpu_limit):
    process = psutil.Popen(exe_path)
    pid = process.pid
    affinity = list(range(cpu_limit))
    psutil.Process(pid).cpu_affinity(affinity)


def browse_button_func():
    file_path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)


def run_game():
    exe_path = entry_path.get()
    cpu_limit = 2
    if exe_path:
        set_cpu_affinity(exe_path, cpu_limit)


def create_main_window():
    window = tk.Tk()
    window.resizable(False, False)
    window.title("CPU Limiter")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 250
    window_height = 135
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    return window


def create_widgets(window):
    label = tk.Label(window, text="Select the prototype game's .exe file:")
    label.pack(pady=5, padx=10)

    entry_path = tk.Entry(window)
    entry_path.pack(pady=5)

    browse_button = tk.Button(window, text="Browse", command=browse_button_func)
    browse_button.pack(pady=5)

    run_button = tk.Button(window, text="Run Game", command=run_game)
    run_button.pack(pady=5)

    return entry_path


if __name__ == "__main__":
    window = create_main_window()
    entry_path = create_widgets(window)
    window.mainloop()
