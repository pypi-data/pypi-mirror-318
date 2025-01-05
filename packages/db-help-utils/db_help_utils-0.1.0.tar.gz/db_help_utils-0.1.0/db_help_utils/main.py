import sqlite3
import psycopg2
from tkinter import ttk, Frame, Toplevel
from tkinter.messagebox import askyesno, showerror
# Database Connection Class
class DBConnector:
    def __init__(self, db_type, **kwargs):
        self.db_type = db_type
        self.connection = self.connect_to_db(**kwargs)

    def connect_to_db(self, **kwargs):
        if self.db_type == 'sqlite':
            return sqlite3.connect(kwargs['database'])
        elif self.db_type == 'postgresql':
            return psycopg2.connect(**kwargs)

        else:
            raise ValueError("Unsupported database type!")

    def close_connection(self):
        if self.connection:
            self.connection.close()

# Query Execution Class
class QueryExecutor:
    def __init__(self, connection):
        self.connection = connection

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def execute_non_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        self.connection.commit()
        cursor.close()

# UI Utility Functions
def create_buttons_from_data(frame, data, column_names, command_func):
    for row in data:
        button_text = "\n".join(f"{col}: {row[idx]}" for idx, col in enumerate(column_names))
        btn = ttk.Button(frame, text=button_text, command=lambda r=row: command_func(r))
        btn.pack(pady=5, anchor='n')

def show_table_in_window(data, headers, title="Table View"):
    win = Toplevel()
    win.title(title)
    frame = Frame(win)
    frame.pack(fill='both', expand=True)
    tree = ttk.Treeview(frame, columns=headers, show='headings')

    for header in headers:
        tree.heading(header, text=header)
        tree.column(header, width=150, anchor="center")

    for row in data:
        tree.insert('', 'end', values=row)

    tree.pack(fill='both', expand=True)

def show_details_in_window(row_data, detail_query_func):
    """Opens a new window and displays details based on the given row data."""
    detail_data = detail_query_func(row_data)
    if not detail_data:
        detail_data = [["No details available"]]
        headers = ["Message"]
    else:
        headers = [f"Column {i+1}" for i in range(len(detail_data[0]))]

    show_table_in_window(detail_data, headers, title="Details View")


def create_add_record_form(frame, headers, submit_func):
    """Generates a form for adding records to the database."""
    entries = {}
    for idx, header in enumerate(headers):
        lbl = ttk.Label(frame, text=f"{header}:")
        lbl.grid(row=idx, column=0, padx=5, pady=5, sticky='e')
        entry = ttk.Entry(frame)
        entry.grid(row=idx, column=1, padx=5, pady=5, sticky='w')
        entries[header] = entry

    def submit():
        record = {key: entry.get() for key, entry in entries.items()}
        submit_func(record)

    submit_btn = ttk.Button(frame, text="Submit", command=submit)
    submit_btn.grid(row=len(headers), columnspan=2, pady=10)

def delete_record(confirm_message, delete_func):
    """Asks for confirmation and deletes a record."""
    if askyesno("Confirm Deletion", confirm_message):
        delete_func()





#example

"""
from db_main_utils import create_buttons_from_data, show_table_in_window, show_details_in_window, DBConnector, QueryExecutor, create_add_record_form, delete_record
from tkinter import ttk, Frame, Toplevel

if __name__ == "__main__":
    # Connect to a PostgreSQL database (modify parameters as needed)
    conn = DBConnector(
        'postgresql',
        user='postgres',
        password='1234',
        host='localhost',
        database='work'
    )

    executor = QueryExecutor(conn.connection)

    # Example query
    query = "SELECT Код_обслед, Дата_Обслед FROM Обследованные"
    data = executor.execute_query(query)

    headers = ["Код_Обслед", "Дата_обслед"]  # Example headers
    headers2 = ["Код_Обслед", "Квартал"] 
    import tkinter as tk
    root = tk.Tk()
    root.title("Database UI Example")
    root.geometry("800x600")

    # Frame for buttons
    content_frame = Frame(root)
    content_frame.pack(fill='both', expand=True)
    def fetch_details(row):
        detail_query = "SELECT Квартал FROM Обследованные WHERE Код_обслед = %s"
        return executor.execute_query(detail_query, params=(row[0],))
    
    # Function to add a record
    def add_record(record):
        insert_query = "INSERT INTO Обследованные (Код_обслед, Квартал) VALUES (%s, %s)"
        executor.execute_non_query(insert_query, params=(record["Код_Обслед"], record["Квартал"]))
        print("Record added successfully.")

    # Function to delete a record
    def delete_selected_record():
        delete_query = "DELETE FROM Обследованные WHERE Код_обслед = %s"
        executor.execute_non_query(delete_query, params=("Код_обслед",))
        print("Record deleted successfully.")

    create_buttons_from_data(content_frame, data, headers, lambda row: show_details_in_window(row, fetch_details))

    # Frame for adding records
    add_frame = Frame(root)
    add_frame.pack(pady=5, anchor='n')
    create_add_record_form(add_frame, headers2, add_record)

    # Button for deleting records
    delete_btn = ttk.Button(root, text="Delete Record", command=lambda: delete_record("Are you sure?", delete_selected_record))
    delete_btn.pack(pady=5, anchor='n')

    table_show_btn = ttk.Button(
        root, 
        command=lambda: show_table_in_window(data, headers, title="Example Table View"), 
        text="Просмотр таблицы"
    )
    table_show_btn.pack(pady=5, anchor='n')
    # Show data in a table
    

    root.mainloop()

    conn.close_connection()

    conn.close_connection()
"""