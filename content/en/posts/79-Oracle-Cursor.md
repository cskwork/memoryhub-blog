---
title: "Oracle Cursor"
date: 2024-05-25T17:54:15+09:00
slug: "79-Oracle-Cursor"
original_url: "https://memoryhub.tistory.com/79"
tistory_id: 79
draft: false
categories: ["Dev Database"]
tags: ["Oracle"]
---

## Definition

A pointer that refers to a memory area where query processing results are stored.

## Usage Method

1. Variable declaration (value with table properties)
2. Cursor declaration
3. Declare the query to use with the cursor
4. Begin transaction and open cursor
5. Execute query
6. Store data in declared variables
7. Close loop if executed in loop, perform necessary actions, and handle exceptions
8. Close cursor

## Explanation +

```
DECLARE
    -- Declare variable p_name with the same data type as the name attribute of the table
    p_name exmployee.name%TYPE;
    -- Store the passed value in ff and declare cursor cur_name
    CURSOR cur_name(ff INT)
    IS
    -- Define the SELECT statement to be executed when the declared cursor is OPEN
    SELECT name FROM employee WHERE id >=ff;

    BEGIN
      -- Open the cur_name cursor. Execute the SELECT query and cur_name stores the starting position of the memory where the result is stored
      OPEN cur_name(20);
      LOOP
        -- Fetch data from cur_name and store in p_name
      	FETCH cur_name INTO p_name;
        -- The %NOTFOUND attribute of cur_name returns TRUE
        -- Exit the LOOP if there are no more values to fetch
        EXIT WHEN cur_name%NOTFOUND;
        -- Output p_name to the screen
        DBMS_OUTPUT.PUT_LINE(p_name);
      END LOOP;
      -- Close the cursor
      CLOSE cur_name
    END;
```

### Implicit Cursor

Used when viewing query information.
Automatically opened and closed by DBMS when use is complete.

- SQL%ROWCOUNT: Number of rows affected by the SQL statement
- SQL%FOUND: TRUE if one or more rows are affected by the SQL
- SQL%NOTFOUND: TRUE if no rows are affected by the SQL statement
- SQL%ISOPEN: Always FALSE, checks whether the implicit cursor is open

```
SQL> CREATE OR REPLACE PROCEDURE Implicit_Cursor
        (p_empno IN emp.empno%TYPE)
    IS
        v_sal  emp.sal%TYPE;
        v_update_row NUMBER;

    BEGIN
        SELECT sal
        INTO v_sal
        FROM emp
        WHERE empno = p_empno;
        -- If data is found
        IF  SQL%FOUND THEN     
            DBMS_OUTPUT.PUT_LINE('Found data: '||v_sal);
        END IF;

        UPDATE emp
        SET sal = sal*1.1
        WHERE empno = p_empno;
        -- Store the count of modified data in a variable
        v_update_row := SQL%ROWCOUNT;
        DBMS_OUTPUT.PUT_LINE('Number of employees with salary increase: '|| v_update_row);
        EXCEPTION    
           WHEN NO_DATA_FOUND THEN  
           DBMS_OUTPUT.PUT_LINE('No data found...');
    END;
    /
-- Used to output DBMS_OUTPUT.PUT_LINE
SQL> SET SERVEROUTPUT ON ;  
-- Execute procedure
SQL> EXECUTE Implicit_Cursor(7369);
Found data: 880
Number of employees with salary increase: 1
```

### Explicit Cursor

A cursor that you define directly. Execution sequence: Declare -> Open -> Fetch -> Close

```
-- Display average salary and number of employees in a specific department..
SQL> CREATE OR REPLACE PROCEDURE ExpCursor_Test 
       (v_deptno IN  dept.deptno%TYPE)   
     IS
       CURSOR dept_avg IS
       SELECT b.dname, COUNT(a.empno) cnt, 
               ROUND(AVG(a.sal),3) salary
       FROM emp a, dept b
       WHERE a.deptno = b.deptno
         AND b.deptno = v_deptno
       GROUP BY b.dname ;

       -- Declare parameters to fetch the cursor
       v_dname   dept.dname%TYPE;
       emp_cnt   NUMBER;
       sal_avg   NUMBER;

     BEGIN
       -- Open the cursor
       OPEN dept_avg;
       -- Fetch the cursor
       FETCH dept_avg INTO v_dname, emp_cnt, sal_avg;

       DBMS_OUTPUT.PUT_LINE('Department: ' || v_dname);
       DBMS_OUTPUT.PUT_LINE('Number of employees: ' || emp_cnt);
       DBMS_OUTPUT.PUT_LINE('Average salary: ' || sal_avg);
       -- CLOSE the cursor
       CLOSE dept_avg;      
    EXCEPTION
      WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM||'Error occurred');
   END;
   /
-- Used to output DBMS_OUTPUT.PUT_LINE
SQL> SET SERVEROUTPUT ON ;
SQL> EXECUTE ExpCursor_Test(30);
Department: SALES
Number of employees: 6
Average salary: 1550.833
```

## References

<https://fmaker7.tistory.com/137> [People Who Dream of the Future]
<http://www.gurubee.net/lecture/1064>
