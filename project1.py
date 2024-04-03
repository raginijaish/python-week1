import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import re
from datetime import datetime

def validate_email(email):
    # Simple email validation using regular expression
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def validate_phone(phone):
    # Simple phone number validation using regular expression
    pattern = r"^\d{10}$"
    return re.match(pattern, phone)

def validate_date_of_birth(dob):
    # Validate date of birth format and minimum age
    try:
        dob_obj = datetime.strptime(dob, '%d/%m/%Y')
        age = (datetime.now() - dob_obj).days // 365
        if age < 18:
            return False
    except ValueError:
        return False
    return True

def validate_form():
    # Validate form fields
    name = name_var.get()
    dob = dob_var.get()
    address = address_var.get()
    email = email_var.get()
    phone = phone_var.get()
    program = program_var.get()
    education = education_var.get()

    if not name or not re.match(r"^[a-zA-Z\s]+$", name):
        messagebox.showerror("Error", "Please enter a valid name")
        return False
    if not validate_date_of_birth(dob):
        messagebox.showerror("Error", "Please enter a valid date of birth (dd/mm/yyyy) and you should be at least 18 years old")
        return False
    if not address:
        messagebox.showerror("Error", "Please enter your address")
        return False
    if not validate_email(email):
        messagebox.showerror("Error", "Please enter a valid email address")
        return False
    if not validate_phone(phone):
        messagebox.showerror("Error", "Please enter a valid 10-digit phone number")
        return False
    if not program:
        messagebox.showerror("Error", "Please enter the program of interest")
        return False
    if not education:
        messagebox.showerror("Error", "Please enter your educational background")
        return False

    return True

def generate_pdf():
    if validate_form():
        pdf_filename = "student_registration.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.drawString(100, 800, "Student Registration Form")
        c.drawString(100, 780, f"Name: {name_var.get()}")
        c.drawString(100, 760, f"Date of Birth: {dob_var.get()}")
        c.drawString(100, 740, f"Address: {address_var.get()}")
        c.drawString(100, 720, f"Email: {email_var.get()}")
        c.drawString(100, 700, f"Phone Number: {phone_var.get()}")
        c.drawString(100, 680, f"Program of Interest: {program_var.get()}")
        c.drawString(100, 660, f"Educational Background: {education_var.get()}")
        c.save()
        messagebox.showinfo("Success", f"PDF generated successfully! File saved as {pdf_filename}")
        clear_form()

def clear_form():
    name_var.set("")
    dob_var.set("")
    address_var.set("")
    email_var.set("")
    phone_var.set("")
    program_var.set("")
    education_var.set("")

# Create the main window
root = tk.Tk()
root.title("Student Registration Form")

# Create variables to store form data
name_var = tk.StringVar()
dob_var = tk.StringVar()
address_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
program_var = tk.StringVar()
education_var = tk.StringVar()

# Create labels and entry fields for the form
tk.Label(root, text="Name:").pack()
tk.Entry(root, textvariable=name_var).pack()

tk.Label(root, text="Date of Birth (dd/mm/yyyy):").pack()
tk.Entry(root, textvariable=dob_var).pack()

tk.Label(root, text="Address:").pack()
tk.Entry(root, textvariable=address_var).pack()

tk.Label(root, text="Email:").pack()
tk.Entry(root, textvariable=email_var).pack()

tk.Label(root, text="Phone Number:").pack()
tk.Entry(root, textvariable=phone_var).pack()

tk.Label(root, text="Program of Interest:").pack()
tk.Entry(root, textvariable=program_var).pack()

tk.Label(root, text="Educational Background:").pack()
tk.Entry(root, textvariable=education_var).pack()

# Create buttons to submit the form and clear the form
tk.Button(root, text="Submit", command=generate_pdf).pack()
tk.Button(root, text="Clear", command=clear_form).pack()

# Start the tkinter event loop
root.mainloop()
