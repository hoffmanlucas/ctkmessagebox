import os
import customtkinter as ctk
from PIL import Image
from functools import partial


__all__ = ["showinfo", "showwarning", "showerror", "showcustom",
           "showsuccess", "askokcancel", "askyesno",
           "askyesnocancel", "askretrycancel", "askabortignore",
           "ERROR", "INFO", "QUESTION", "WARNING", "SUCCESS"]


def resource_path(relative_path) -> str:
    """Returns the absolute path of the resource using the current file path"""
    base_path = os.path.dirname(__file__)
    path = str(os.path.join(base_path, relative_path))
    return path


# icons
ERROR = resource_path("icons/error-icon.png")
INFO = resource_path("icons/info-icon.png")
QUESTION = resource_path("icons/ask-icon.png")
WARNING = resource_path("icons/alert-icon.png")
SUCCESS = resource_path("icons/ok-icon.png")

# types
ABORTRETRYIGNORE = "abortretryignore"
# OK = "Ok"
OKCANCEL = "okcancel"
RETRYCANCEL = "retrycancel"
YESNO = "yesno"
YESNOCANCEL = "yesnocancel"
CUSTOM = "custom"

# replies
ABORT = "Abort"
RETRY = "Retry"
CANCEL = "Cancel"
OK = 'Ok'
YES = 'Yes'
NO = 'No'



def showinfo(master, title:str, message:str) -> str:
    """Show an info message;  return the button pressed."""
    return MessageBox(master, title, message, INFO, OK).get()


def showsuccess(master, title:str, message:str) -> str:
    """Show an info message;"""
    return MessageBox(master, title, message, SUCCESS, OK).get()


def showwarning(master, title:str, message:str) -> str:
    """Show a warning message;  return the button pressed."""
    return MessageBox(master, title, message, WARNING, OK).get()


def showerror(master, title:str, message:str) -> str:
    """Show an error message; return the button pressed."""
    return MessageBox(master, title, message, ERROR, OK).get()


def askokcancel(master, title:str, message:str) -> str:
    """Ask if operation should proceed;  return the button pressed."""
    return MessageBox(master, title, message, QUESTION, OKCANCEL).get()


def askyesno(master, title:str, message:str) -> str:
    """Ask a question;  return the button pressed."""
    return MessageBox(master, title, message, QUESTION, YESNO).get()


def askyesnocancel(master, title:str, message:str) -> str:
    """Ask a question; return the button pressed."""
    return MessageBox(master, title, message, QUESTION, YESNOCANCEL).get()


def askretrycancel(master, title:str, message:str) -> str:
    """Ask if operation should be retried; return the button pressed."""
    return MessageBox(master, title, message, WARNING, RETRYCANCEL).get()


def askabortignore(master, title:str, message:str) -> str:
    """Ask if operation should be retried or ignored; return the button pressed."""
    return MessageBox(master, title, message, WARNING, ABORTRETRYIGNORE).get()


def showcustom(master, title:str, message:str, icon:str=INFO, *buttons) -> str:
    """Show a messagebox with custom buttons

    icon: str. Options available:
        ctkmessagebox2.ERROR, ctkmessagebox2.INFO, ctkmessagebox2.QUESTION, ctkmessagebox2.WARNING, ctkmessagebox2.SUCCESS
        """
    return MessageBox(master, title, message, WARNING, CUSTOM, *buttons).get()


class MessageBox(ctk.CTkToplevel):
    """A customtkinter message box"""
    def __init__(self, master, title:str, message: str, _icon:str, _type:str, *buttons):
        n_lines = len(message) // 40
        n_lines += message.count('\n')
        super().__init__(master)

        # Definindo o tamanho da janela
        width = 300
        height = 150+9*n_lines

        if master is None:
            # place the window to center of screen
            position_x = int((self.winfo_screenwidth()-width)/2)
            position_y = int((self.winfo_screenheight()-height)/2)
        else:
            # place the window to center of master window
            position_x = int(master.winfo_width() * .5 + master.winfo_x() - .5 * width + 7)
            position_y = int(master.winfo_height() * .5 + master.winfo_y() - .5 * height + 20)

        # Layout
        self.geometry(f"450x{height}+{position_x}+{position_y}")
        self.title(title)
        self.resizable(False, False)
        self.attributes('-topmost', True)

        msg_frame = ctk.CTkFrame(self, fg_color='transparent')
        msg_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=(20,0))

        image = ctk.CTkImage(Image.open(_icon), size=(50, 50))
        ctk.CTkLabel(msg_frame, text='', image=image).pack(side=ctk.LEFT, padx=5)

        text = ctk.CTkTextbox(msg_frame, wrap='word', fg_color='transparent', height=20)
        text.pack(fill=ctk.BOTH, expand=True, side=ctk.LEFT, padx=5)
        text.insert(0.0, message)
        text.configure(state='disabled')

        buttons_frame = ctk.CTkFrame(self, fg_color='transparent')
        buttons_frame.pack(padx=20, pady=20, anchor=ctk.CENTER)

        self.result = None
        self.buttons = buttons

        _pack = dict(side=ctk.LEFT, padx=5, pady=5)

        if _type == OK:
            ctk.CTkButton(buttons_frame, text='OK', width=100, command=self._ok).pack(**_pack)
        elif _type == OKCANCEL:
            ctk.CTkButton(buttons_frame, text='OK', width=100, command=self._ok).pack(**_pack)
            ctk.CTkButton(buttons_frame, text='Cancel', width=100, command=self._cancel).pack(**_pack)
        elif _type == RETRYCANCEL:
            ctk.CTkButton(buttons_frame, text='Retry', width=100, command=self._retry).pack(**_pack)
            ctk.CTkButton(buttons_frame, text='Cancel', width=100, command=self._cancel).pack(**_pack)
        elif _type == YESNO:
            ctk.CTkButton(buttons_frame, text='Yes', width=100, command=self._yes).pack(**_pack)
            ctk.CTkButton(buttons_frame, text='No', width=100, command=self._no).pack(**_pack)
        elif _type == YESNOCANCEL:
            ctk.CTkButton(buttons_frame, text='Yes', width=100, command=self._yes).pack(**_pack)
            ctk.CTkButton(buttons_frame, text='No', width=100, command=self._no).pack(**_pack)
            ctk.CTkButton(buttons_frame, text='Cancel', width=100, command=self._cancel).pack(**_pack)
        elif _type == ABORTRETRYIGNORE:
            ctk.CTkButton(buttons_frame, text='Abort', width=100, command=self._abort).pack(**_pack)
            ctk.CTkButton(buttons_frame, text='Retry', width=100, command=self._retry).pack(**_pack)
            ctk.CTkButton(buttons_frame, text='Cancel', width=100, command=self._cancel).pack(**_pack)
        elif _type == CUSTOM:
            for button in self.buttons:
                ctk.CTkButton(buttons_frame, text=button, width=100, command=partial(self._custom_btn, button)).pack(**_pack)

        self.after(150, self._make_modal)

    def _make_modal(self):
        self.grab_set()
        self.focus_force()

    def _custom_btn(self, button:str):
        self.result = button
        self.close()

    def _ok(self):
        self.result = OK
        self.close()

    def _yes(self):
        self.result = YES
        self.close()

    def _no(self):
        self.result = NO
        self.close()

    def _retry(self):
        self.result = RETRY
        self.close()

    def _abort(self):
        self.result = ABORT
        self.close()

    def _cancel(self):
        self.result = CANCEL
        self.close()

    def close(self):
        self.grab_release()
        self.destroy()

    def get(self):
        self.wait_window()
        return self.result
