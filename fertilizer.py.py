import tkinter as tk
from tkinter import messagebox

# Example nutrient requirements per crop type
crop_nutrient_requirements = {
    "Wheat": {"N": 120, "P": 60, "K": 40},
    "Rice": {"N": 150, "P": 70, "K": 50}
}

# Function to calculate fertilizer recommendation
def calculate_fertilizer():
    crop = crop_var.get().strip()  # Get and strip whitespace
    if crop == "":
        messagebox.showerror("Error", "Please enter a crop type")
        return

    if crop not in crop_nutrient_requirements:
        messagebox.showerror("Error", "Unsupported crop type")
        return

    soil_type = soil_type_var.get()
    soil_factor = 1.0 if soil_type == "Loamy" else 1.2 if soil_type == "Sandy" else 0.8

    requirements = crop_nutrient_requirements[crop]
    n = requirements["N"] * soil_factor
    p = requirements["P"] * soil_factor
    k = requirements["K"] * soil_factor

    result_var.set(f"N: {n:.2f} kg/ha, P: {p:.2f} kg/ha, K: {k:.2f} kg/ha")

# GUI Setup
root = tk.Tk()
root.title("Fertilizer Recommendation System")

# Function to handle Enter key press (optional)
def on_enter(event):
    calculate_fertilizer()

# Labels and Entry for Crop Type
tk.Label(root, text="Crop Type:").pack()
crop_var = tk.StringVar()
crop_entry = tk.Entry(root, textvariable=crop_var)
crop_entry.pack()

# Labels and OptionMenu for Soil Type
tk.Label(root, text="Soil Type:").pack()
soil_type_var = tk.StringVar(value="Loamy")
soil_option_menu = tk.OptionMenu(root, soil_type_var, "Loamy", "Sandy", "Clay")
soil_option_menu.pack()

# Button to trigger calculation
calculate_button = tk.Button(root, text="Calculate Fertilizer", command=calculate_fertilizer)
calculate_button.pack()

# Bind Enter key to calculate function (optional)
root.bind('<Return>', on_enter)

# Label to display result
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

root.mainloop()
