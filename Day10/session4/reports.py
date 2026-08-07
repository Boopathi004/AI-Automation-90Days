from database import get_connection


def highest_salary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM employees_details
        ORDER BY salary DESC
        LIMIT 1
    """)

    print(cursor.fetchone())
    conn.close()


def lowest_salary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM employees_details
        ORDER BY salary
        LIMIT 1
    """)

    print(cursor.fetchone())
    conn.close()


def average_salary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT AVG(salary)
        FROM employees_details
    """)

    print("Average Salary :", cursor.fetchone()[0])
    conn.close()


def total_salary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(salary)
        FROM employees_details
    """)

    print("Total Salary :", cursor.fetchone()[0])
    conn.close()


def total_employee():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM employees_details
    """)

    print("Total Employees :", cursor.fetchone()[0])
    conn.close()


def department_report():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT department,COUNT(*)
        FROM employees_details
        GROUP BY department
    """)

    rows = cursor.fetchall()

    for row in rows:
        print(row[0], ":", row[1])

    conn.close()


def salary_filter(amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM employees_details
        WHERE salary > ?
    """,(amount,))

    for row in cursor.fetchall():
        print(row)

    conn.close()


def sort_salary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM employees_details
        ORDER BY salary DESC
    """)

    for row in cursor.fetchall():
        print(row)

    conn.close()