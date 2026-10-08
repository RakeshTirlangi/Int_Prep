# QualiZeal Interview Preparation Material

## 1. Object-Oriented Programming (OOPs)
OOP is a programming paradigm based on the concept of "objects", which can contain data and code. 

### The Four Pillars of OOP
1. **Encapsulation:** Wrapping data (variables) and code (methods) together into a single unit (Class). It hides internal state and requires all interaction to be performed through an object's methods.
   - *Example:* A `BankAccount` class where the `balance` is private, and you can only change it using `deposit()` or `withdraw()` methods.
2. **Abstraction:** Hiding complex implementation details and showing only the essential features of the object.
   - *Example:* A coffee machine. You just press a button (essential feature) without knowing how the internal circuits boil the water (implementation detail).
3. **Inheritance:** A mechanism where a new class acquires the properties and behavior of an existing class. It promotes code reusability.
   - *Example:* `Vehicle` is a base class. `Car` and `Bike` are derived classes that inherit from `Vehicle`.
4. **Polymorphism:** The ability of different classes to respond to the same method call in their own way. 
   - **Compile-time (Method Overloading):** Multiple methods in the same class with the same name but different parameters.
   - **Run-time (Method Overriding):** A child class provides a specific implementation of a method that is already provided by its parent class.

### SOLID Principles (Bonus)
- **S**ingle Responsibility: A class should have only one reason to change.
- **O**pen/Closed: Open for extension, closed for modification.
- **L**iskov Substitution: Subclasses should be substitutable for their base classes.
- **I**nterface Segregation: Many client-specific interfaces are better than one general-purpose interface.
- **D**ependency Inversion: Depend on abstractions, not on concretions.

---

## 2. Database & SQL Concepts

### Relational Database Basics
- **Table:** A collection of related data held in a structured format (rows and columns).
- **Primary Key (PK):** A unique identifier for a record in a table. Cannot be NULL.
- **Foreign Key (FK):** A field in one table that uniquely identifies a row of another table, establishing a relationship.

### SQL Commands Categorization
- **DDL (Data Definition Language):** Defines structure. `CREATE`, `ALTER`, `DROP`, `TRUNCATE`.
- **DML (Data Manipulation Language):** Manipulates data. `INSERT`, `UPDATE`, `DELETE`.
- **DQL (Data Query Language):** Queries data. `SELECT`.
- **DCL (Data Control Language):** Controls access. `GRANT`, `REVOKE`.

### Important SQL Queries (Practice these!)
1. **Joins:** 
   - `INNER JOIN`: Returns records with matching values in both tables.
   - `LEFT JOIN`: Returns all records from the left table, and matched records from the right.
   - `RIGHT JOIN`: Returns all records from the right table, and matched records from the left.
   - `FULL JOIN`: Returns all records when there is a match in either left or right table.
2. **Group By & Having:** Used with aggregate functions (`COUNT`, `MAX`, `MIN`, `SUM`, `AVG`) to group the result-set.
   ```sql
   SELECT department, COUNT(employee_id) 
   FROM Employees 
   GROUP BY department 
   HAVING COUNT(employee_id) > 5;
   ```

### ACID Properties (Important for Transactions)
- **Atomicity:** All or nothing. If one part of a transaction fails, the entire transaction fails.
- **Consistency:** The database must remain in a valid state after any transaction.
- **Isolation:** Concurrent transactions don't interfere with each other.
- **Durability:** Once a transaction is committed, it remains saved even in case of a system failure.

---

## 3. APIs (Application Programming Interfaces)

An API allows two applications to talk to each other. For web development, we use **REST** (Representational State Transfer).

### HTTP Methods (CRUD Operations)
- **GET:** Retrieve data from a server (Read).
- **POST:** Send data to the server to create a new resource (Create).
- **PUT:** Update an existing resource entirely (Update).
- **PATCH:** Update a resource partially (Update).
- **DELETE:** Remove a resource from the server (Delete).

### Common HTTP Status Codes
- **200 OK:** Successful request.
- **201 Created:** Successful request and a resource was created.
- **400 Bad Request:** The server could not understand the request due to invalid syntax.
- **401 Unauthorized:** Authentication is required and has failed or not been provided.
- **403 Forbidden:** The client does not have access rights to the content.
- **404 Not Found:** The server cannot find the requested resource.
- **500 Internal Server Error:** The server encountered a situation it doesn't know how to handle.

---

## 4. Programming Languages (Java / C#)

### Java Focus Areas:
- **Collections Framework:** Know the difference between `ArrayList` (dynamic array, fast retrieval) and `LinkedList` (fast insertion/deletion). Know `HashMap` (key-value pairs, O(1) retrieval) and `HashSet` (unique elements).
- **Exception Handling:** `try`, `catch`, `finally`, `throw`, `throws`. Difference between Checked and Unchecked exceptions.
- **Java 8 Features:** Understand how to use `Streams` (filter, map, reduce) and `Lambda Expressions` for cleaner code.
- **Strings:** Why are strings immutable in Java? Difference between `String`, `StringBuilder`, and `StringBuffer`.

### C# / .NET Focus Areas:
- **Value Types vs. Reference Types:** Value types (int, struct) are stored on the Stack. Reference types (classes, strings) are stored on the Heap.
- **LINQ (Language Integrated Query):** Used for querying collections cleanly.
- **Delegates and Events:** A delegate is a type that safely encapsulates a method. Used heavily in event-driven programming.
- **Garbage Collection:** How memory is automatically managed in .NET.

---

## 5. Aptitude & Logical Reasoning (For Online Test)

**Topics to Practice (Use IndiaBix.com or similar sites):**
- **Quant:** Time and Work, Speed/Distance/Time, Percentages, Profit and Loss, Ratios.
- **Logical:** Number and Letter Series, Coding-Decoding, Blood Relations, Seating Arrangements.
- **Technical MCQs:** Output of loops (especially tricky nested loops or post/pre-increment operators), debugging basic OOP structures.

---

## 6. HR & Group Discussion Prep

### Group Discussion (GD) Topics to Read About:
- Impact of AI (ChatGPT, GenAI) on IT Jobs.
- Work from Home vs. Work from Office.
- Cloud Computing vs. On-Premise Servers.

### HR Interview Questions:
- **"Tell me about yourself."** -> Keep it professional. (Current degree -> Skills -> 1 Major Project -> Why you want this job).
- **"Why QualiZeal?"** -> Mention their focus on Quality Engineering and digital transformation. Mention you want to learn under their structured training program (AI, Cloud).
- **"Where do you see yourself in 3 years?"** -> Talk about mastering .NET/Java and becoming a reliable full-stack or backend engineer.
- **"Are you willing to commit to the 2-year bond?"** -> Yes, because you are looking for long-term learning and stability to start your career.
