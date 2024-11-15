import tkinter as tk

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())
        simple_interest = principal * rate * time / 100
        compound_interest = principal * (1 + rate / 100) ** time - principal
        simple_interest_label.config(text=f"Simple Interest: {simple_interest:.2f}")
        compound_interest_label.config(text=f"Compound Interest: {compound_interest:.2f}")
    except ValueError:
        simple_interest_label.config(text="Invalid input!")
        compound_interest_label.config(text="")

window = tk.Tk()
window.title("Interest Calculator")

# Label and Entry for Principal Amount
tk.Label(window, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
principal_entry = tk.Entry(window)
principal_entry.grid(row=0, column=1, padx=10, pady=5)

# Label and Entry for Time Period
tk.Label(window, text="Time (in years):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
time_entry = tk.Entry(window)
time_entry.grid(row=1, column=1, padx=10, pady=5)

# Label and Entry for Rate of Interest
tk.Label(window, text="Rate of Interest:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
rate_entry = tk.Entry(window)
rate_entry.grid(row=2, column=1, padx=10, pady=5)

# Calculate Button - placed in a separate row
calculate_button = tk.Button(window, text="Calculate", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Simple Interest Label
simple_interest_label = tk.Label(window, text="Simple Interest: ")
simple_interest_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

# Compound Interest Label
compound_interest_label = tk.Label(window, text="Compound Interest: ")
compound_interest_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

window.mainloop()
