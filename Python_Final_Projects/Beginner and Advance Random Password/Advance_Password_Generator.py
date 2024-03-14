import tkinter as tk
import random
import string

class Password_Builder_App:
    def __init__(self, master):
        self.master = master
        master.title("Random Password Builder")

        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = tk.Button(master, text="Create Password", command=self.builder_password)
        self.generate_button.grid(row=1, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=2, columnspan=2, padx=10, pady=10)

    def builder_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Password length must be greater than 0.")
        except ValueError as e:
            self.result_label.config(text=str(e), fg="red")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.result_label.config(text="Create Password: " + password, fg="Blue")


def main():
    root = tk.Tk()
    app = Password_Builder_App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
