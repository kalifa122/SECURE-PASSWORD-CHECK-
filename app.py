# app.py
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

# import functions from your modules
from password_checker import check_password_strength, is_strong_password
from pwned_check import check_pwned_api  # ensure your function is named check_pwned_api
from password_generator import generate_password

# ---------- GUI ----------

class PasswordApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secure Password Tool")
        self.geometry("740x460")
        self.resizable(False, False)
        self._pw_visible = False  # internal flag for visibility
        self.create_widgets()

    def create_widgets(self):
        pad = 12

        # Title
        title = ttk.Label(self, text="🔐 Secure Password Tool", font=("Segoe UI", 16, "bold"))
        title.pack(pady=(12, 0))

        frame = ttk.Frame(self)
        frame.pack(fill="both", expand=True, padx=pad, pady=pad)

        # Input label
        lbl = ttk.Label(frame, text="Enter password to evaluate:")
        lbl.grid(row=0, column=0, sticky="w")

        # Entry + eye button container
        entry_frame = ttk.Frame(frame)
        entry_frame.grid(row=1, column=0, sticky="w")

        self.pw_var = tk.StringVar()
        self.entry = ttk.Entry(entry_frame, textvariable=self.pw_var, width=50, show="*")
        self.entry.grid(row=0, column=0, sticky="w")
        self.entry.focus()

        # Eye button to toggle visibility (uses emoji)
        self.eye_btn = ttk.Button(entry_frame, text="👁️", width=3, command=self.toggle_password_visibility)
        self.eye_btn.grid(row=0, column=1, padx=(6,0))

        # Buttons (Check / Check Pwned / Generate)
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=1, column=1, padx=(16,0), sticky="n")

        self.check_btn = ttk.Button(btn_frame, text="Check", command=self.on_check, width=16)
        self.check_btn.pack(fill="x", pady=(0,6))

        self.pwned_btn = ttk.Button(btn_frame, text="Check Pwned", command=self.on_check_pwned, width=16)
        self.pwned_btn.pack(fill="x", pady=(0,6))

        self.generate_btn = ttk.Button(btn_frame, text="Generate Password", command=self.on_generate, width=16)
        self.generate_btn.pack(fill="x")

        # Criteria box
        criteria_frame = ttk.LabelFrame(frame, text="Password criteria")
        criteria_frame.grid(row=2, column=0, columnspan=2, pady=(14,0), sticky="ew")

        self.criteria_vars = {}
        criteria_list = [
            "Length ≥ 8 characters",
            "Contains an uppercase letter",
            "Contains a lowercase letter",
            "Contains a digit",
            "Contains a special character"
        ]
        for i, crit in enumerate(criteria_list):
            v = tk.StringVar(value="❌")
            lbl = ttk.Label(criteria_frame, text=f"{crit}", width=44)
            lbl.grid(row=i, column=0, sticky="w", padx=8, pady=2)
            val = ttk.Label(criteria_frame, textvariable=v, width=3, anchor="center")
            val.grid(row=i, column=1, sticky="e", padx=8)
            self.criteria_vars[crit] = v

        # Strength label and pwned result
        self.strength_var = tk.StringVar(value="Strength: -")
        self.strength_lbl = ttk.Label(frame, textvariable=self.strength_var, font=("Segoe UI", 11, "bold"))
        self.strength_lbl.grid(row=3, column=0, sticky="w", pady=(12,0))

        self.pwned_var = tk.StringVar(value="Pwned: -")
        self.pwned_lbl = ttk.Label(frame, textvariable=self.pwned_var, font=("Segoe UI", 10))
        self.pwned_lbl.grid(row=3, column=1, sticky="e", pady=(12,0))

        # Generated password display
        gen_frame = ttk.LabelFrame(self, text="Generated password")
        gen_frame.pack(fill="x", padx=pad, pady=(12,14))
        self.generated_var = tk.StringVar(value="")
        gen_entry = ttk.Entry(gen_frame, textvariable=self.generated_var, width=60)
        gen_entry.grid(row=0, column=0, padx=8, pady=8)
        copy_btn = ttk.Button(gen_frame, text="Copy", command=self.copy_generated, width=10)
        copy_btn.grid(row=0, column=1, padx=6)

    # ---------- Actions ----------
    def on_check(self):
        pw = self.pw_var.get().strip()
        if not pw:
            messagebox.showwarning("Warning", "Please enter a password.")
            return
        # update criteria
        results = check_password_strength(pw)
        for crit, val in results.items():
            self.criteria_vars[crit].set("✅" if val else "❌")

        strong = is_strong_password(pw)
        self.strength_var.set(f"Strength: {'Strong' if strong else 'Weak'} ({sum(results.values())}/5)")

        # reset pwned label (user must explicitly click Check Pwned)
        self.pwned_var.set("Pwned: -")

    def on_check_pwned(self):
        pw = self.pw_var.get().strip()
        if not pw:
            messagebox.showwarning("Warning", "Please enter a password.")
            return

        self.pwned_var.set("Pwned: Checking...")
        # run network call in background thread
        thread = threading.Thread(target=self._check_pwned_thread, args=(pw,), daemon=True)
        thread.start()

    def _check_pwned_thread(self, pw):
        try:
            count = check_pwned_api(pw)
        except Exception as e:
            self.pwned_var.set("Pwned: Error")
            messagebox.showerror("Error", f"Pwned check failed: {e}")
            return

        if count == 0:
            self.pwned_var.set("Pwned: Not found")
            messagebox.showinfo("Pwned", "Password not found in known breaches.")
        else:
            self.pwned_var.set(f"Pwned: Found {count} times")
            messagebox.showwarning("Pwned", f"Password found {count} times in breaches. Change it!")

    def on_generate(self):
        pwd = generate_password(length=14, use_digits=True, use_specials=True)
        self.generated_var.set(pwd)
        # also fill the input so user can re-check if wanted
        self.pw_var.set(pwd)
        # show the generated password automatically
        if not self._pw_visible:
            self._pw_visible = True
            self.entry.config(show="")
            self.eye_btn.config(text="🙈")  # change icon to indicate hide
        self.on_check()

    def copy_generated(self):
        val = self.generated_var.get()
        if val:
            pyperclip.copy(val)
            messagebox.showinfo("Copied", "Generated password copied to clipboard.")
        else:
            messagebox.showwarning("Nothing", "No generated password to copy.")

    def toggle_password_visibility(self):
        # flip visibility flag
        self._pw_visible = not self._pw_visible
        if self._pw_visible:
            self.entry.config(show="")  # Show text
            self.eye_btn.config(text="🙈")  # closed-eye icon
        else:
            self.entry.config(show="*")  # Mask text
            self.eye_btn.config(text="👁️")  # open-eye icon

if __name__ == "__main__":
    try:
        app = PasswordApp()
        app.mainloop()
    except Exception as e:
        print("Fatal error:", e)
