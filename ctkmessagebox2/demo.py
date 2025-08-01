import customtkinter as ctk
import ctkmessagebox as messagebox

class AppTest(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.minsize(400, 200)
        self.title("CTkMessageBox 2 Demo")

        buttons = ctk.CTkFrame(self)
        buttons.pack(side=ctk.LEFT)
        self.button_1 = ctk.CTkButton(buttons, text="showinfo", command=self.showinfo)
        self.button_2 = ctk.CTkButton(buttons, text="showsuccess", command=self.showsuccess)
        self.button_3 = ctk.CTkButton(buttons, text="showwarning", command=self.showwarning)
        self.button_4 = ctk.CTkButton(buttons, text="showerror", command=self.showerror)
        self.button_5 = ctk.CTkButton(buttons, text="askokcancel", command=self.askokcancel)
        self.button_6 = ctk.CTkButton(buttons, text="askyesno", command=self.askyesno)
        self.button_7 = ctk.CTkButton(buttons, text="askyesnocancel", command=self.askyesnocancel)
        self.button_8 = ctk.CTkButton(buttons, text="askretrycancel", command=self.askretrycancel)
        self.button_9 = ctk.CTkButton(buttons, text="askabortignore", command=self.askabortignore)
        self.button_10 = ctk.CTkButton(buttons, text="custom", command=self.custom)
        
        self.button_1.pack(side="top", padx=10, pady=10)
        self.button_2.pack(side="top", padx=10, pady=10)
        self.button_3.pack(side="top", padx=10, pady=10)
        self.button_4.pack(side="top", padx=10, pady=10)
        self.button_5.pack(side="top", padx=10, pady=10)
        self.button_6.pack(side="top", padx=10, pady=10)
        self.button_7.pack(side="top", padx=10, pady=10)
        self.button_8.pack(side="top", padx=10, pady=10)
        self.button_9.pack(side="top", padx=10, pady=10)
        self.button_10.pack(side="top", padx=10, pady=10)

        details = ctk.CTkFrame(self)
        details.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=5)

        self._result = ctk.StringVar(value='Clicked: ')
        self._title = ctk.StringVar(value='CTkMessageBox 2 Demo')

        ctk.CTkLabel(details, textvariable=self._result).pack()
        ctk.CTkLabel(details, text='Title').pack()
        ctk.CTkEntry(details, textvariable=self._title).pack(fill=ctk.X)
        ctk.CTkLabel(details, text='Message').pack()
        self._msg = ctk.CTkTextbox(details)
        self._msg.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5)

        self.toplevel_window = None

    def custom(self):
        msg = self._msg.get(0.0, ctk.END).strip('\n')
        if not msg:
            msg = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

        buttons = ['CTk', 'MessageBox 2', 'is', 'awesome!']
        icon = messagebox.SUCCESS
        self.toplevel_window = messagebox.showcustom(self, self._title.get(), msg, icon, *buttons)
        self._result.set(value=f"Clicked: {self.toplevel_window}")

    def showsuccess(self):
        msg = self._msg.get(0.0, ctk.END).strip('\n')
        if not msg:
            msg = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
        self.toplevel_window = messagebox.showsuccess(self, self._title.get(), msg)
        self._result.set(value=f"Clicked: {self.toplevel_window}")

    def askyesno(self):
        msg = self._msg.get(0.0, ctk.END).strip('\n')
        if not msg:
            msg = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        self.toplevel_window = messagebox.askyesno(self, self._title.get(), msg)
        self._result.set(value=f"Clicked: {self.toplevel_window}")

    def askyesnocancel(self):
        msg = self._msg.get(0.0, ctk.END).strip('\n')
        if not msg:
            msg = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."  #
        self.toplevel_window = messagebox.askyesnocancel(self, self._title.get(), msg)
        self._result.set(value=f"Clicked: {self.toplevel_window}")

    def askretrycancel(self):
        msg = self._msg.get(0.0, ctk.END).strip('\n')
        if not msg:
            msg = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
        self.toplevel_window = messagebox.askretrycancel(self, self._title.get(), msg)
        self._result.set(value=f"Clicked: {self.toplevel_window}")

    def showinfo(self):
        msg = self._msg.get(0.0, ctk.END).strip('\n')
        if not msg:
            msg = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
        self.toplevel_window = messagebox.showinfo(self, self._title.get(), msg)
        self._result.set(value=f"Clicked: {self.toplevel_window}")

    def showwarning(self):
        msg = self._msg.get(0.0, ctk.END).strip('\n')
        if not msg:
            msg = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
        self.toplevel_window = messagebox.showwarning(self, self._title.get(), msg)
        self._result.set(value=f"Clicked: {self.toplevel_window}")

    def showerror(self):
        msg = self._msg.get(0.0, ctk.END).strip('\n')
        if not msg:
            msg = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
        self.toplevel_window = messagebox.showerror(self, self._title.get(), msg)
        self._result.set(value=f"Clicked: {self.toplevel_window}")

    def askokcancel(self):
        msg = self._msg.get(0.0, ctk.END).strip('\n')
        if not msg:
            msg = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."  #
        self.toplevel_window = messagebox.askokcancel(self, self._title.get(), msg)
        self._result.set(value=f"Clicked: {self.toplevel_window}")

    def askabortignore(self):
        msg = self._msg.get(0.0, ctk.END).strip('\n')
        if not msg:
            msg = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."  #
        self.toplevel_window = messagebox.askabortignore(self, self._title.get(), msg)
        self._result.set(value=f"Clicked: {self.toplevel_window}")


if __name__ == "__main__":
    app = AppTest()
    app.mainloop()

