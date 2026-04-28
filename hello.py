import tkinter as tk
from tkinter import messagebox

# ---------- FUNCTION ----------
def calculate():
    try:
        marks = [
            int(e1.get()),      #takes value from the five input boxes and converts them into numbers using int
            int(e2.get()),
            int(e3.get()),
            int(e4.get()),
            int(e5.get())
        ]

        total = sum(marks)
        avg = total / 5

        # Grade
        if avg >= 90:
            grade = "A+"
        elif avg >= 75:
            grade = "A"
        elif avg >= 60:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "F"

        # Result (Pass/Fail)
        if all(m >= 40 for m in marks):
            result = "PASS"
            lbl_result.config(fg="green")
        else:
            result = "FAIL"
            lbl_result.config(fg="red")

        # Display in Result Panel
        lbl_total.config(text=str(total))
        lbl_avg.config(text=f"{avg:.2f}")
        lbl_grade.config(text=grade)
        lbl_result.config(text=result)

    except:
        messagebox.showerror("Error", "Enter valid marks")


def reset():
    for e in [e1, e2, e3, e4, e5]:
        e.delete(0, tk.END)   #removes all entered text

    lbl_total.config(text="-")      # clears result panel
    lbl_avg.config(text="-")
    lbl_grade.config(text="-")
    lbl_result.config(text="-")


# ---------- WINDOW ----------
root = tk.Tk()
root.title("Student Mark Management System")
root.geometry("750x400")

# ---------- TITLE ----------
tk.Label(root, text="Student Mark Management System",
         font=("Arial", 16, "bold"), fg="blue").pack(pady=10)

# ---------- MAIN FRAME ---------- 
frame = tk.Frame(root)
frame.pack()

left = tk.Frame(frame, bd=2, relief="groove", padx=20, pady=10)
left.grid(row=0, column=0, padx=20)

right = tk.Frame(frame, bd=2, relief="groove", padx=20, pady=10)
right.grid(row=0, column=1, padx=20)

# ---------- LEFT SIDE ----------
tk.Label(left, text="Enter Student Details",
         font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2)

tk.Label(left, text="Student Name").grid(row=1, column=0)
name = tk.Entry(left)
name.grid(row=1, column=1)

tk.Label(left, text="Enter Marks (out of 100)", fg="blue")\
    .grid(row=2, column=0, columnspan=2, pady=10)

# Subject entries
labels = ["English", "Maths", "Science", "Language", "social"]
entries = []

for i, text in enumerate(labels):
    tk.Label(left, text=text).grid(row=i+3, column=0, sticky="w")
    e = tk.Entry(left)
    e.grid(row=i+3, column=1, pady=2)
    entries.append(e)

e1, e2, e3, e4, e5 = entries

# Buttons
tk.Button(left, text="Calculate", bg="blue", fg="white",    #call calcualate() when clicked
          command=calculate).grid(row=8, column=0, pady=10)

tk.Button(left, text="Reset", bg="green", fg="white",         #call reset function when clicked 
          command=reset).grid(row=8, column=1)

tk.Button(left, text="Exit", bg="red", fg="white",            
          command=root.destroy).grid(row=9, column=0, columnspan=2)

# ---------- RIGHT SIDE (RESULT) ----------
tk.Label(right, text="Result",
         font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2)

tk.Label(right, text="Total Marks").grid(row=1, column=0, sticky="w")
lbl_total = tk.Label(right, text="-")
lbl_total.grid(row=1, column=1)

tk.Label(right, text="Average").grid(row=2, column=0, sticky="w")
lbl_avg = tk.Label(right, text="-")
lbl_avg.grid(row=2, column=1)

tk.Label(right, text="Grade").grid(row=3, column=0, sticky="w")
lbl_grade = tk.Label(right, text="-")
lbl_grade.grid(row=3, column=1)

tk.Label(right, text="Result").grid(row=4, column=0, sticky="w")
lbl_result = tk.Label(right, text="-", font=("Arial", 10, "bold"))
lbl_result.grid(row=4, column=1)

# ---------- RUN ----------
root.mainloop()