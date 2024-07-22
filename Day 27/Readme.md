# Miles to Kilometers Converter

This project is a simple graphical user interface (GUI) application built using 
Python's Tkinter library. It converts a given distance in miles to kilometers. 
The application features an input field for the user to enter a value in miles 
and a button to trigger the conversion. The result is displayed in kilometers.

## Features

- **User Input Field:** Allows the user to enter the distance in miles.
- **Conversion Button:** When clicked, it converts the entered value from miles 
to kilometers.
- **Result Display:** Shows the converted distance in kilometers.

## Installation

1. Ensure you have Python installed on your system. If not, download and install
it from [Python's official website](https://www.python.org/).
2. Tkinter is included with standard Python installations. If you have
Python installed, you should already have Tkinter. If you encounter any issues, you can install Tkinter using pip:
    ```bash
    pip install tk
    ```

## Usage

1. Save the provided code in a Python file, for example, `mile_to_km_converter.py`.
2. Run the Python file:
    ```bash
    python mile_to_km_converter.py
    ```

## Code Explanation

Here is a breakdown of the code:

### Importing Tkinter

```python
import tkinter
```

### Function to Convert Miles to Kilometers

```python
def Miles_to_Km():
    mile_float = float(user_input.get())
    ans = round(mile_float * 1.609344)
    value_Km.config(text=f"{ans}")
```

- **Miles_to_Km Function:** This function is called when the "Calculate" button
is clicked. It retrieves the value entered by the user, converts it from miles to
kilometers, and updates the label to display the result.

### Setting Up the Tkinter Window

```python
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=50, height=50)
```

- **window:** Creates the main application window.
- **window.title:** Sets the title of the window.
- **window.minsize:** Sets the minimum size of the window.

### Adding Widgets

```python
miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)
```

- **miles:** Creates a label widget with the text "Miles".
- **grid:** Places the label in the specified grid position.

```python
user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)
```

- **user_input:** Creates an entry widget for user input.
- **grid:** Places the entry widget in the specified grid position.

```python
meaning = tkinter.Label(text="is equal to")
meaning.grid(column=0, row=1)
```

- **meaning:** Creates a label widget with the text "is equal to".
- **grid:** Places the label in the specified grid position.

```python
value_Km = tkinter.Label(text="0")
value_Km.grid(column=1, row=1)
```

- **value_Km:** Creates a label widget to display the conversion result.
- **grid:** Places the label in the specified grid position.

```python
Km = tkinter.Label(text="Km")
Km.grid(column=2, row=1)
```

- **Km:** Creates a label widget with the text "Km".
- **grid:** Places the label in the specified grid position.

```python
cal = tkinter.Button(text="Calculate", command=Miles_to_Km)
cal.grid(column=1, row=2)
```

- **cal:** Creates a button widget with the text "Calculate". When clicked,
it calls the `Miles_to_Km` function.
- **grid:** Places the button in the specified grid position.

### Running the Tkinter Event Loop

```python
window.mainloop()
```

- **window.mainloop:** Starts the Tkinter event loop, allowing the window to
be displayed and user interaction to be handled.

## Conclusion

This simple Tkinter application effectively demonstrates how to create a basic 
GUI for converting miles to kilometers. It serves as a good starting point for
learning more about Tkinter and GUI development in Python.