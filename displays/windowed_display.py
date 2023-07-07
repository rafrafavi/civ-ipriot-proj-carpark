import tkinter as tk
from typing import Iterable

class WindowedDisplay:
    DISPLAY_INIT = '– – –'
    SEP = ':'

    def __init__(self, title: str, display_fields: Iterable[str]):
        """
        Initializes the WindowedDisplay class.

        Args:
            title (str): The title of the window.
            display_fields (Iterable[str]): The fields to be displayed in the window.
        """
        # Create the main window
        self.window = tk.Tk()
        self.window.title(f'{title}: Parking')
        self.window.geometry('800x400')
        self.window.resizable(False, False)

        # Store the display fields
        self.display_fields = display_fields

        # Create the GUI elements dictionary
        self.gui_elements = {}

        # Create labels for each display field
        for i, field in enumerate(self.display_fields):
            self.gui_elements[f'lbl_field_{i}'] = tk.Label(
                self.window, text=field + self.SEP, font=('Arial', 50))
            self.gui_elements[f'lbl_value_{i}'] = tk.Label(
                self.window, text=self.DISPLAY_INIT, font=('Arial', 50))

            self.gui_elements[f'lbl_field_{i}'].grid(
                row=i, column=0, sticky=tk.E, padx=5, pady=5)
            self.gui_elements[f'lbl_value_{i}'].grid(
                row=i, column=2, sticky=tk.W, padx=10)

    def show(self):
        """
        Displays the window.

        Starts the main window event loop.
        """
        self.window.mainloop()

    def update(self, updated_values: dict):
        """
        Updates the values of the display fields.

        Args:
            updated_values (dict): A dictionary containing the updated values for the display fields.
        """
        for field in self.gui_elements:
            if field.startswith('lbl_field'):
                field_value = field.replace('field', 'value')
                index = int(field.split('_')[2])
                self.gui_elements[field_value].config(
                    text=updated_values[self.display_fields[index]])
