---
title: "CRUD Query Collection"
date: 2019-01-14T13:44:38+09:00
slug: "8-CRUD-쿼리-모음"
original_url: "https://memoryhub.tistory.com/8"
tistory_id: 8
draft: false
categories: ["Dev Database"]
tags: ["Oracle Database"]
---

ORACLE QUERY

**Essential Queries (CRUD)**

Create Table

create table member(

  IDX NUMBER UNIQUE NOT NULL,

  ID VARCHAR2(20) PRIMARY KEY,

  NAME VARCHAR2(30) NOT NULL,

  PWD VARCHAR2(15) NOT NULL,

  MMS_CHK NUMBER(1) DEFAULT 0,

  PHONE VARCHAR2(20),

  EMAIL VARCHAR2(30),

  ADDR VARCHAR2(100) NOT NULL,

  ADDR_GPS VARCHAR2(50) NOT NULL,

  HEIGHT NUMBER(5),

  WEIGHT NUMBER(5),

  B_TYPE VARCHAR2(2),

  BANK_NO VARCHAR2(25),

  JUMIN VARCHAR2(20),

  JOINDATE DATE,

  LOGINDATE DATE,

  ID_IMG VARCHAR2(100),

  ID_SESSIONK VARCHAR2(30),

  ID_SESSIONL DATE,

  DEL_CHK NUMBER(1) DEFAULT 0

  );

Create Sequence

CREATE SEQUENCE SEQ_MEMBER_IDX

START WITH 1

INCREMENT BY 1

NOMAXVALUE

NOCACHE;



To be added

select

update

update

**Additional Queries**

Modify Column

ALTER TABLE MEMBER MODIFY(BANK_NO VARCHAR2(20));

ALTER TABLE MEMBER ADD DEL_CHK NUMBER(1) DEFAULT 0;

ALTER TABLE MEMBER DROP COLUMN DEL_CHK;

ALTER TABLE MEMBER MODIFY (mycol NULL);

Generate Random Data

BEGIN

    FOR i IN startNumb..endNumb LOOP

    INSERT INTO tableName(  IDX, Column1, Column2, HIT_CNT, DEL_GB, CREA_DTM, CREA_ID) VALUES(SEQ_TB_BOARD_IDX.NEXTVAL, 'Title '||i, 'Content '||i, 0, 'N', SYSDATE, 'Admin');

    END LOOP;

END;

Pagination Query

SELECT

    AAA.*

FROM(

    SELECT

        COUNT(*) OVER() AS TOTAL_COUNT,

        AA.*

    FROM(

        SELECT

            ROW_NUMBER() OVER (ORDER BY IDX DESC) RNUM,

            IDX,

            Column1,

            HIT_CNT,

            CREA_DTM

        FROM

            tableName

    ) AA

) AAA

WHERE

    AAA.RNUM BETWEEN 0 AND 20

Add COMMENT to Column Name

COMMENT ON COLUMN MEMBER.MMS_CHK IS 'SMS notification';

COMMENT ON COLUMN MEMBER.B_TYPE IS 'Blood type';

COMMENT ON COLUMN MEMBER.JOINDATE IS 'Member join date';
