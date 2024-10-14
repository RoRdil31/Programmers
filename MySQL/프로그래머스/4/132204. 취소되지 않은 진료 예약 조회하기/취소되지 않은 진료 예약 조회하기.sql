#   진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
SELECT APNT_NO, PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME, APNT_YMD
    FROM PATIENT P
    JOIN APPOINTMENT A
      ON P.PT_NO = A.PT_NO
    JOIN DOCTOR D
      ON D.DR_ID = A.MDDR_ID AND D.MCDP_CD = A.MCDP_CD
    WHERE A.MCDP_CD = 'CS' AND APNT_YMD LIKE '2022-04-13%' AND APNT_CNCL_YN = 'N'
      
    
    ORDER BY 6
# '환자번호', 환자이름, 성별코드, 나이, 전화번호
# 의사이름, 의사ID, 면허번호, 고용일자, 진료과코드, 전화번호
# 진료 예약일시, 진료예약번호, '환자번호', 진료과코드, 의사ID, 예약취소여부, 예약취소날짜

