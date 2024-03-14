import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI is: {bmi:.2f}")
    except ValueError:
        result_label.config(text="Please enter you values for weight and height.")

#  main window
root = tk.Tk()
root.title("BMI Calculator")

# Create widgets
weight_label = tk.Label(root, text="Enter your weight in kg:")
weight_label.grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

height_label = tk.Label(root, text="Enter your height (cm):")
height_label.grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Run event loop
root.mainloop()
