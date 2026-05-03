---
title: "CRUD 쿼리 ++ 모음"
date: 2019-01-14T13:44:38+09:00
slug: "8-CRUD-쿼리-모음"
original_url: "https://memoryhub.tistory.com/8"
tistory_id: 8
draft: false
---

ORACLE QUERY

**필수 쿼리 (CRUD)**

테이블 생성

create table member(

  IDX NUMBER UNIQUE NOT NULL,

  ID VARCHAR2(20) PRIMARY KEY,

  NAME VARCHAR2(30) NOT NULL,

  PWD VARCHAR2(15) NOT NULL,

  MMS\_CHK NUMBER(1) DEFAULT 0,

  PHONE VARCHAR2(20),

  EMAIL VARCHAR2(30),

  ADDR VARCHAR2(100) NOT NULL,

  ADDR\_GPS VARCHAR2(50) NOT NULL,

  HEIGHT NUMBER(5),

  WEIGHT NUMBER(5),

  B\_TYPE VARCHAR2(2),

  BANK\_NO VARCHAR2(25),

  JUMIN VARCHAR2(20),

  JOINDATE DATE,

  LOGINDATE DATE,

  ID\_IMG VARCHAR2(100),

  ID\_SESSIONK VARCHAR2(30),

  ID\_SESSIONL DATE,

  DEL\_CHK NUMBER(1) DEFAULT 0

  );

시퀀스 생성

CREATE SEQUENCE SEQ\_MEMBER\_IDX

START WITH 1

INCREMENT BY 1

NOMAXVALUE

NOCACHE;



추가 예정

select

update

update

**추가 쿼리**

칼럼 변경

ALTER TABLE MEMBER MODIFY(BANK\_NO VARCHAR2(20));

ALTER TABLE MEMBER ADD DEL\_CHK NUMBER(1) DEFAULT 0;

ALTER TABLE MEMBER DROP COLUMN DEL\_CHK;

ALTER TABLE MEMBER MODIFY (mycol NULL);

임의로 데이터 생성 

BEGIN

    FOR i IN startNumb..endNumb LOOP

    INSERT INTO tableName(  IDX, Column1, Column2, HIT\_CNT, DEL\_GB, CREA\_DTM, CREA\_ID) VALUES(SEQ\_TB\_BOARD\_IDX.NEXTVAL, '제목 '||i, '내용 '||i, 0, 'N', SYSDATE, 'Admin');

    END LOOP;

END;

페이징 쿼리

SELECT

    AAA.\*

FROM(

    SELECT

        COUNT(\*) OVER() AS TOTAL\_COUNT,

        AA.\*

    FROM(

        SELECT

            ROW\_NUMBER() OVER (ORDER BY IDX DESC) RNUM,

            IDX,

            Column1,

            HIT\_CNT,

            CREA\_DTM

        FROM

            tableName

    ) AA

) AAA

WHERE

    AAA.RNUM BETWEEN 0 AND 20

칼럼명에 COMMENT 넣기

COMMENT ON COLUMN MEMBER.MMS\_CHK IS '문자 메시지 수신';

COMMENT ON COLUMN MEMBER.B\_TYPE IS '혈액형';

COMMENT ON COLUMN MEMBER.JOINDATE IS '회원가입날짜';
