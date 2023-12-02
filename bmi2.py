import tkinter as tk
from tkinter import messagebox
import json


class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.label_weight = tk.Label(self.root, text="Weight (pounds):")
        self.label_weight.grid(row=0, column=0)
        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.grid(row=0, column=1)

        self.label_height = tk.Label(self.root, text="Height (inches):")
        self.label_height.grid(row=1, column=0)
        self.entry_height = tk.Entry(self.root)
        self.entry_height.grid(row=1, column=1)

        self.calculate_button = tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height should be positive numbers.")
            bmi = (weight * 703) / (height * height)
            self.result_label.config(text=f"Your BMI is: {bmi:.2f}")
            self.store_data(weight, height, bmi)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def store_data(self, weight, height, bmi):
        data = {"Weight": weight, "Height": height, "BMI": bmi}
        with open("bmi_data.json", "a") as f:
            json.dump(data, f)
            f.write("\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
