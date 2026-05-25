from tkinter import *
from tkinter import messagebox

sex = ["Male", "Female"]
status = ["Single", "Married", "Divorced", "Widowed", "Separated"]

window = Tk()
window.title("DATA ENTRY FORM")
window.geometry("400x600")

icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)

# FUNCTIONS 

def submit():
    name = nameEntry.get()
    age = ageEntry.get()
    selected_sex = sex[x.get()]
    bdate = bdateEntry.get()
    bplace = bplaceEntry.get()
    occu = occuEntry.get()
    address = addEntry.get()
    number = numEntry.get()
    selected_status = status[y.get()]

    if (name == "" or
        age == "" or
        bdate == "" or
        bplace == "" or
        occu == "" or
        address == "" or
        number == "" or
        x.get() == -1 or
        y.get() == -1):
        messagebox.showwarning("Error", "Please fill up the whole form before submitting.")
        return

    with open("records.txt", "a") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Sex: {selected_sex}\n")
        f.write(f"Birthdate: {bdate}\n")
        f.write(f"Birthplace: {bplace}\n")
        f.write(f"Occupation: {occu}\n")
        f.write(f"Address: {address}\n")
        f.write(f"Contact: {number}\n")
        f.write(f"Status: {selected_status}\n")
        f.write("-" * 30 + "\n")

    messagebox.showinfo("Success", "Record saved!")
    clear_fields()


def view_records():
    try:
        with open("records.txt", "r") as f:
            data = f.read()
    except FileNotFoundError:
        data = "No records found."

    view_window = Toplevel(window)
    view_window.title("All Records")

    text = Text(view_window, width=60, height=25)
    text.pack()
    text.insert(END, data)


def search_record():
    keyword = nameEntry.get()

    if keyword == "":
        messagebox.showwarning("Error", "Enter a name to search.")
        return

    try:
        with open("records.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        messagebox.showinfo("Search", "No records found.")
        return

    result = ""
    temp = ""

    for line in lines:
        temp += line
        if line.strip() == "------------------------------":
            if keyword.lower() in temp.lower():
                result += temp + "\n"
            temp = ""

    if result == "":
        result = "No matching record found."

    search_window = Toplevel(window)
    search_window.title("Search Result")

    text = Text(search_window, width=60, height=25)
    text.pack()
    text.insert(END, result)


def clear_fields():
    nameEntry.delete(0, END)
    ageEntry.delete(0, END)
    bdateEntry.delete(0, END)
    bplaceEntry.delete(0, END)
    occuEntry.delete(0, END)
    addEntry.delete(0, END)
    numEntry.delete(0, END)

    x.set(-1)
    y.set(-1)


# FORM UI

nameLabel = Label(window, text="Name :")
nameLabel.grid(row=0, column=0, sticky=W, pady=5)

nameEntry = Entry(window, width=40)
nameEntry.grid(row=0, column=1, pady=5)

ageLabel = Label(window, text="Age :")
ageLabel.grid(row=1, column=0, sticky=W, pady=5)

ageEntry = Entry(window, width=40)
ageEntry.grid(row=1, column=1, pady=5)

x = IntVar()
x.set(-1)

sexLabel = Label(window, text="Sex :")
sexLabel.grid(row=2, column=0, sticky=W, pady=5)

for i in range(len(sex)):
    Radiobutton(window, text=sex[i], variable=x, value=i)\
        .grid(row=2 + i, column=1, sticky=W, pady=5)

bdateLabel = Label(window, text="Birthdate :")
bdateLabel.grid(row=4, column=0, sticky=W, pady=5)

bdateEntry = Entry(window, width=40)
bdateEntry.grid(row=4, column=1, pady=5)

bplaceLabel = Label(window, text="Birthplace :")
bplaceLabel.grid(row=5, column=0, sticky=W, pady=5)

bplaceEntry = Entry(window, width=40)
bplaceEntry.grid(row=5, column=1, pady=5)

occuLabel = Label(window, text="Occupation :")
occuLabel.grid(row=6, column=0, sticky=W, pady=5)

occuEntry = Entry(window, width=40)
occuEntry.grid(row=6, column=1, pady=5)

addLabel = Label(window, text="Address :")
addLabel.grid(row=7, column=0, sticky=W, pady=5)

addEntry = Entry(window, width=40)
addEntry.grid(row=7, column=1, pady=5)

numLabel = Label(window, text="Contact Number :")
numLabel.grid(row=8, column=0, sticky=W, pady=5)

numEntry = Entry(window, width=40)
numEntry.grid(row=8, column=1, pady=5)

y = IntVar()
y.set(-1)

statLabel = Label(window, text="Status :")
statLabel.grid(row=9, column=0, sticky=W, pady=5)

for i in range(len(status)):
    Radiobutton(window, text=status[i], variable=y, value=i)\
        .grid(row=9 + i, column=1, sticky=W)

# BUTTONS

Button(window, text="Submit", command=submit)\
    .grid(row=15, column=1, pady=5)

Button(window, text="View Records", command=view_records)\
    .grid(row=16, column=1, pady=5)

Button(window, text="Search", command=search_record)\
    .grid(row=17, column=1, pady=5)

Button(window, text="Clear", command=clear_fields)\
    .grid(row=18, column=1, pady=5)

window.mainloop()
