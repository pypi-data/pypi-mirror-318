import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys
import time
import threading
import logging
import fcntl

from utils import monitor_file_for_external_modification

WINDOW_TITLE = "Uniteditor"
Global_current_file_path = ""
Global_last_internal_modification_time = None
# Keep cursor at same text position between saves/loads
Global_last_cursor_pos = None

def load_file():
    global Global_last_internal_modification_time
    global Global_current_file_path

    if Global_current_file_path:
        try:
            with open(Global_current_file_path, "r") as file:
                fcntl.flock(file, fcntl.LOCK_SH)
                file_content = file.read()
                Global_last_internal_modification_time = get_file_modification_time(
                    Global_current_file_path
                )
                fcntl.flock(file, fcntl.LOCK_UN)

                logging.debug("Updated window contents")
                textbox.delete("1.0", tk.END)  # Clear current content
                textbox.insert(tk.END, file_content)
                if Global_last_cursor_pos:
                    textbox.mark_set(tk.INSERT, Global_last_cursor_pos)
                textbox.focus()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")


def open_file(default_file_name=""):
    global Global_current_file_path

    if default_file_name:
        file_path = default_file_name
    else:
        file_path = filedialog.askopenfilename(initialfile=default_file_name)

    if file_path:
        Global_current_file_path = file_path
        root.title(f"{WINDOW_TITLE}: {Global_current_file_path}")
        load_file()
        background_thread.start()


def save_file():
    global Global_last_internal_modification_time
    global Global_current_file_path
    global Global_last_cursor_pos

    if not Global_current_file_path:
        Global_current_file_path = filedialog.asksaveasfilename()
        if not Global_current_file_path:
            return

    Global_last_cursor_pos = textbox.index(tk.INSERT)
    file_content = textbox.get("1.0", tk.END).strip()
    try:
        with open(Global_current_file_path, "w") as file:
            fcntl.flock(file, fcntl.LOCK_EX)
            file.write(file_content)
            Global_last_internal_modification_time = get_file_modification_time(
                Global_current_file_path
            )
            fcntl.flock(file, fcntl.LOCK_UN)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")


def get_file_modification_time(filename):
    return os.stat(filename).st_mtime


# TODO: deduplicate with _wait_for_user_input()
def reload_file_when_modified():
    monitor_file_for_external_modification(
        Global_current_file_path,
        lambda: Global_last_internal_modification_time,
        load_file,
    )


def select_all(event):
    event.widget.tag_add("sel", "1.0", "end-1c")  # Select all text
    return "break"  # Prevent default behavior (if any)


background_thread = threading.Thread(target=reload_file_when_modified)
background_thread.daemon = True  # thread exits when main program exits

root = tk.Tk()
root.title(WINDOW_TITLE)

textbox = tk.Text(root, font="TkFixedFont", wrap="word", undo=True)
textbox.pack(fill="both", expand=True, padx=5, pady=5)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu, underline=0)
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O", underline=0)
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S", underline=0)
file_menu.add_command(label="Reload", command=load_file, accelerator="F5", underline=0)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=root.quit, accelerator="Ctrl+Q", underline=0)

root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-O>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-S>", lambda event: save_file())
root.bind("<F5>", lambda event: load_file())
root.bind("<Control-q>", lambda event: root.quit())
root.bind("<Control-Q>", lambda event: root.quit())
textbox.bind("<Control-a>", select_all)
textbox.bind("<Control-A>", select_all)

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] [%(levelname)s] %(message)s")


def main():
    if len(sys.argv) == 2:
        default_file_name = sys.argv[1]
        open_file(default_file_name)

    textbox.focus()
    root.geometry("1024x768")
    root.mainloop()


if __name__ == "__main__":
    main()
