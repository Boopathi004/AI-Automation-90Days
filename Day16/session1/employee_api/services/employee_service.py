from Database.connection import get_connection


def get_all_employees():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    connection.close()

    return [dict(employee) for employee in employees]

def create_employee(name, department, salary):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO employees (name, department, salary)
        VALUES (?, ?, ?)
        """,
        (name, department, salary)
    )

    connection.commit()

    employee_id = cursor.lastrowid

    connection.close()

    return {
        "id": employee_id,
        "name": name,
        "department": department,
        "salary": salary
    }
def get_employee_by_id(employee_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE id = ?",
        (employee_id,)
    )

    employee = cursor.fetchone()

    connection.close()

    if employee:
        return dict(employee)

    return None

def update_employee(employee_id, name, department, salary):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE employees
        SET name = ?, department = ?, salary = ?
        WHERE id = ?
        """,
        (name, department, salary, employee_id)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return None

    cursor.execute(
        "SELECT * FROM employees WHERE id = ?",
        (employee_id,)
    )

    employee = cursor.fetchone()

    connection.close()

    return dict(employee)

def delete_employee(employee_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,)
    )

    connection.commit()

    deleted = cursor.rowcount > 0

    connection.close()

    return deleted