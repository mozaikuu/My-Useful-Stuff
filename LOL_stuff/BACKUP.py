import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from tkinter import messagebox

# Create the GUI window
window = tk.Tk()
window.title("League of Legends Data")
window.configure(bg="#f2f2f2")  # Set background color
window.geometry("800x400")  # Set window size

# Connect to the MySQL database
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="LOLdb",
        charset="utf8"
    )
except mysql.connector.Error as error:
    messagebox.showerror("Error", "Failed to connect to the database: {}".format(error))

# Function to display all data from the database
def display_data():
    try:
        cursor = mydb.cursor()
        cursor.execute("SELECT Name, PENTAKILLL, `No Death`, `S+ Rank`, `Mastery 7`, Ai, `S+ ARAM`, WINS, `1M Mastery`, ARENA FROM loldb.lol_data")
        rows = cursor.fetchall()

        # Create a new window to display the table
        table_window = tk.Toplevel(window)
        table_window.title("League of Legends Data")

        # Create a Treeview widget to display the table
        table_treeview = ttk.Treeview(table_window)
        table_treeview.pack()

        # Configure the columns
        table_treeview["columns"] = ("Name", "PENTAKILLL", "No Death", "S+ Rank", "Mastery 7", "Ai", "S+ ARAM", "WINS", "1M Mastery", "ARENA")
        for col in table_treeview["columns"]:
            table_treeview.column(col, width=100)
            table_treeview.heading(col, text=col.capitalize())

        # Insert the table data into the Treeview
        for row in rows:
            table_treeview.insert("", tk.END, values=row)

    except mysql.connector.Error as error:
        messagebox.showerror("Error", "Failed to fetch data: {}".format(error))

# Call the display_data function to show the table data instantly
display_data()

# Run the GUI main loop
window.mainloop()
