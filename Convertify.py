import tkinter as tk
from tkinter import ttk

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meter": 1,
        "kilometer": 0.001,
        "inches": 39.3701,
        "feet": 3.28084
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def convert_unit():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        category = combo_category.get()

        if category == "Length":
            result = length_converter(value, from_unit, to_unit)
            label_result.config(text=f"Result: {result:.2f} {to_unit}")
        else:
            label_result.config(text="Unsupported Category")
    except ValueError:
        label_result.config(text="Please enter a valid number.")

# Main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x350")

# Category dropdown
tk.Label(root, text="Select Category:").pack(pady=5)
combo_category = ttk.Combobox(root, values=["Length"], state="readonly")
combo_category.current(0)
combo_category.pack(pady=5)

# From unit dropdown
tk.Label(root, text="Convert from:").pack(pady=5)
combo_from = ttk.Combobox(root, values=["meter", "kilometer", "inches", "feet"], state="readonly")
combo_from.current(0)
combo_from.pack(pady=5)

# To unit dropdown
tk.Label(root, text="Convert to:").pack(pady=5)
combo_to = ttk.Combobox(root, values=["meter", "kilometer", "inches", "feet"], state="readonly")
combo_to.current(1)
combo_to.pack(pady=5)

# Value entry
tk.Label(root, text="Enter Value:").pack(pady=5)
entry_value = tk.Entry(root)
entry_value.pack(pady=5)

# Convert button
tk.Button(root, text="Convert", command=convert_unit).pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result:", font=("Arial", 14))
label_result.pack(pady=20)

# Run the app
root.mainloop()