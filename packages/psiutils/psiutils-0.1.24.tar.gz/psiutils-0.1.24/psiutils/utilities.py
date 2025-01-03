"""Common methods for psiutils."""
from pathlib import Path
import tkinter as tk
from typing import Any

import psiutils.text as text


class Enum():
    def __init__(self, values: dict) -> None:
        self.values = invert(values)


def confirm_delete(parent: Any) -> str:
    question = text.DELETE_THESE_ITEMS
    return tk.messagebox.askquestion(
        'Delete items', question, icon='warning', parent=parent)


def create_directories(path: str | Path) -> bool:
    """Create directories recursively."""
    create_parts = []
    create_path = Path(path)
    for part in create_path.parts:
        create_parts.append(part)
        new_path = Path(*create_parts)
        if not Path(new_path).is_dir():
            try:
                Path(new_path).mkdir()
            except PermissionError:
                print(f'Invalid file path: {new_path}')
                return False
    return True


def invert(enum: dict) -> dict:
    """Add the inverse items to a dictionary."""
    output = {}
    for key, item in enum.items():
        output[key] = item
        output[item] = key
    return output


def display_icon(root, path: str,
                 ignore_error: bool = True) -> None:
    try:
        root.iconphoto(False, tk.PhotoImage(file=path))
    except tk.TclError as err:
        if ignore_error and text.NO_SUCH_FILE in str(err):
            return
        print(f'Cannot find icon file: {path}')


def enable_frame(parent: tk.Frame, enable: bool = True) -> None:
    state = tk.NORMAL if enable else tk.DISABLED
    for child in parent.winfo_children():
        w_type = child.winfo_class()
        if w_type in ('Frame', 'Labelframe', 'TFrame', 'TLabelframe'):
            enable_frame(child, enable)
        else:
            child.configure(state=state)
