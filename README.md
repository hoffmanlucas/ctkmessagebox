# CustomTkinter Messagebox

CustomTkinter Messagebox is an implementation of the `tkinter.messagebox` functionalities using the `customtkinter` package. It replicates the same functions available in `tkinter.messagebox`, but with support for CustomTkinter's modernized interface.

## Features

This package offers the following functionalities, replicating the behavior of `tkinter.messagebox`:

- **showinfo**: Displays a dialog with an informational message.
- **showwarning**: Displays a dialog with a warning message.
- **showerror**: Displays a dialog with an error message.
- **askquestion**: Displays a question and returns the user's response (`Yes/No`).
- **askokcancel**: Displays a question and returns `OK` or `Cancel`.
- **askyesno**: Displays a question and returns `Yes` or `No`.
- **askretrycancel**: Displays an error message and asks the user to choose `Retry` or `Cancel`.

## Installation

Install the package via pip:

```bash
pip install ctkmessagebox
```

## Project Structure
The project follows the same functional structure as tkinter.messagebox, allowing easy migration of code and adaptation to more modern interfaces with customtkinter.

Unlikely Tkinter messagebox, ctkmessagebox requires the master as the first argument for all messages.

## Usage
Here’s a basic example of how to use the CustomTkinter Messagebox:

```python
import customtkinter as ctk
import ctkmessagebox

app = ctk.CTk()
app.geometry("400x200")

def show_info():
    ctkmessagebox.showinfo(app, "Information", "This is an informational message.")

button = ctk.CTkButton(app, text="Show Info", command=show_info)
button.pack(pady=20)

app.mainloop()
```

## Contributions
Contributions are welcome! If you want to improve the project, feel free to open an issue or submit a pull request.

### Fork the repository
- Create a branch (git checkout -b feature/new-feature)
- Commit your changes (git commit -m 'Add new feature')
- Push to the branch (git push origin feature/new-feature)
- Open a Pull Request

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

