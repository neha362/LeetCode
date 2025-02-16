-- Replace Employee ID With The Unique Identifier, Jan 13 2025
SELECT unique_id, name FROM Employees LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id
