---
title: "Oracle Cursor"
date: 2024-05-25T17:54:15+09:00
slug: "79-Oracle-Cursor"
original_url: "https://memoryhub.tistory.com/79"
tistory_id: 79
draft: false
categories: ["데브 데이터베이스"]
tags: ["Oracle"]
---

## 정의

쿼리문의 처리 결과가 저장되어 있는 메모리 공간을 가리키는 포인터

## 사용방법

1 변수 선언 (테이블 속성을 갖고 있는 값(  
2 커서 선언  
3 커서에 사용할 쿼리 선언  
4 트렌젝션 시작과 커서 열기  
5 쿼리 실행  
6 데이터를 선언된 변수에 저장  
7 루프로 실행했으면 루프 닫기, 필요한 액션 수행 및 예외 처리  
8 커서 닫기

## 해설 +

```
DECLARE
    --테이블의 name 속성의 자료형과 동일한 변수 P_name을 선언
    p_name exmployee.name%TYPE;
    --전달받은 값을 ff에 저장 후 커서 cur_name을 선언.
    CURSOR cur_name(ff INT)
    IS
    --선언된 커서가 OPEN될 때 수행할 SELECT문 정의. 
    SELECT name FROM employee WHERE id >=ff;

    BEGIN
      --cur_name 커서를 연다. SELECT의 조회문을 실행하고 cur_name에는 결과가 저장된 메모리의 시작 위치가 저장된다. 
      OPEN cur_name(20);
      LOOP
        --cur_name에서 데이터를 가져와 p_name에 저장
      	FETCH cur_name INTO p_name;
        --cur_name의 %NOTFOUND 속성은 TRUE 반환. 
        --더 불러올 값이 없으면 LOOP를 빠져아간다.
        EXIT WHEN cur_name%NOTFOUND;
        --p_name을 화면에 출력
        DBMS_OUTPUT.PUT_LINE(p_name);
      END LOOP;
      --커서를 닫는다
      CLOSE cur_name
    END;
```

### 묵시적 커서

쿼리 정보 열람시 사용.  
DBMS 자체적으로 open - fetch되어 사용이 끝나면 close됨.

- SQL%ROWCOUNT : 해당 SQL 문에 영향을 받는 행의 수
- SQL%FOUND : 해당 SQL 영향을 받는 행의 수가 한 개 이상일 경우 TRUE
- SQL%NOTFOUND : 해당 SQL 문에 영향을 받는 행의 수가 없을 경우 TRUE
- SQL%ISOPEN : 항상 FALSE, 암시적 커서가 열려 있는지의 여부 검색

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
        -- 검색된 데이터가 있을경우
        IF  SQL%FOUND THEN     
            DBMS_OUTPUT.PUT_LINE('검색한 데이터가 존재합니다 : '||v_sal);
        END IF;

        UPDATE emp
        SET sal = sal*1.1
        WHERE empno = p_empno;
        -- 수정한 데이터의 카운트를 변수에 저장
        v_update_row := SQL%ROWCOUNT;
        DBMS_OUTPUT.PUT_LINE('급여가 인상된 사원 수 : '|| v_update_row);
        EXCEPTION    
           WHEN NO_DATA_FOUND THEN  
           DBMS_OUTPUT.PUT_LINE(' 검색한 데이터가 없네요... ');
    END;
    /
-- DBMS_OUTPUT.PUT_LINE을 출력하기 위해 사용
SQL> SET SERVEROUTPUT ON ;  
-- 프로시저 실행
SQL> EXECUTE Implicit_Cursor(7369);
검색한 데이터가 존재합니다 : 880
급여가 인상된 사원 수 : 1
```

### 명시적 커서

직접 정의하는 커서. 실행 순서 Declare -> Open -> Fetch -> Close

```
-- 특정 부서의 평균급여와 사원수를 출력..
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

       -- 커서를 패치하기 위한 편수 선언
       v_dname   dept.dname%TYPE;
       emp_cnt   NUMBER;
       sal_avg   NUMBER;

     BEGIN
       -- 커서의 오픈
       OPEN dept_avg;
       -- 커서의 패치 
       FETCH dept_avg INTO v_dname, emp_cnt, sal_avg;

       DBMS_OUTPUT.PUT_LINE('부서명 : ' || v_dname);
       DBMS_OUTPUT.PUT_LINE('사원수 : ' || emp_cnt);
       DBMS_OUTPUT.PUT_LINE('평균급여 : ' || sal_avg);
       -- 커서의 CLOSE
       CLOSE dept_avg;      
    EXCEPTION
      WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM||'에러 발생 ');
   END;
   /
-- DBMS_OUTPUT.PUT_LINE을 출력하기 위해 사용
SQL> SET SERVEROUTPUT ON ;
SQL> EXECUTE ExpCursor_Test(30);
부서명 : SALES
사원수 : 6
평균급여 : 1550.833
```

## 참조

<https://fmaker7.tistory.com/137> [미래를 꿈꾸는 사람들]  
<http://www.gurubee.net/lecture/1064>
