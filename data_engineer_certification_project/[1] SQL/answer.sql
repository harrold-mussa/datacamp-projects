-- Create the Employees table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2) CHECK (salary >= 30000 AND salary <= 100000)
);

INSERT INTO Employees (employee_id, full_name, salary) VALUES
(1, 'Employee A', 30500),
(2, 'Employee B', 32575),
(3, 'Employee C', 55000),
(4, 'Employee D', 43025),
(5, 'Employee E', 42199);

SELECT *
FROM Employees;
