from web.view.base.baseController import *

def alertMsg(Msg, goUrl):
    if goUrl == "":
        return "<script language='javascript'>alert('" + Msg + "');history.back();</script>"
    else:
        return "<script language='javascript'>alert('" + Msg + "');location.replace('" + goUrl + "');</script>"

def alertCloseMsg(Msg):
    if Msg == "":
        return "<script language='javascript'>self.close();</script>"
    else:
        return "<script language='javascript'>alert('" + Msg + "');self.close();</script>"

def alertParentDialogCloseMsg2(Msg, func):
    if Msg == "":
        return "<script language='javascript'>parent.$('#dialog').dialog('close');</script>"
    else:
        return "<script language='javascript'>alert('" + Msg + "');parent.$('#dialog').dialog('close');parent." + func + "</script>"

def GetCms_CD():
    GetCms_CD = ""
    strSql = "SELECT Top 1 A.CMS_CD FROM T_CM_100 A JOIN T_CM_010 B ON B.CMS_CD = A.CMS_CD WHERE CMS_USE_YN = 'Y' AND office_no= '" + G_OFFICE_NO + "' ORDER BY B.SORT_SEQ ASC, CMS_NM DESC "
    tmpRs = dbexecute(strSql)
    if tmpRs:
        GetCms_CD = str(tmpRs[0])
    return GetCms_CD

def checkSort(pSort, strSort):
    checkSort = pSort
    if pSort == strSort:
        strFirst = pSort[0:strSort.find(" ")-1]
        strSecond = pSort[strSort.find(" ")+1]
        if strSecond == "asc":
            strSecond = "desc"
        else:
            strSecond = "asc"
        checkSort = strFirst + " " + strSecond
    return checkSort

def ChkWordIn(CheckValue):
    CheckValue = CheckValue.replace("&", "&amp;")
    CheckValue = CheckValue.replace("<", "&lt;")
    CheckValue = CheckValue.replace(">", "&gt;")
    CheckValue = CheckValue.replace("'", "&rsquo;")
    CheckValue = CheckValue.replace("\"\"", "&quot;")
    CheckValue = CheckValue.replace("&", "&amp;")
    CheckValue = CheckValue.replace("/n", "<br>")
    return CheckValue

def setMultiLang(multi_lang):
    if multi_lang.strip() == "":
        return ""
    MultiLang = ""
    for i in range(1, len(multi_lang) + 1):
        MultiLang = MultiLang + "'" + multi_lang[i:i+1] + "',"
    MultiLang = MultiLang[1:len(MultiLang)]
    return MultiLang

def setCommonQuery(cFlag, strSelValue, strSelMent, strOption1, strOption2, sessionInfoVo, G_OFFICE_NO):
    strSql = ""
    selcolumnName = "code_nm"
    selcolumnName2 = "DEPT_NM"
    selcolumnName5 = ""

    if cFlag == "PMS_LANG":
        if sessionInfoVo.multi_lang == "":
            strSql = " select code, " + selcolumnName + " from DBO.FN_CODE010('" + G_OFFICE_NO + "','" + sessionInfoVo.LoginId + "') where CODE_GRP = 'H19' AND CODE <> '00' AND CODE IN ('K','E') and use_flag <> 'N' ORDER BY SORT_SEQ "
        else:
            strSql = " select code, " + selcolumnName + " from DBO.FN_CODE010('" + G_OFFICE_NO + "','" + sessionInfoVo.LoginId + "') where CODE_GRP = 'H19' AND CODE <> '00' AND CODE IN (" + setMultiLang(sessionInfoVo.multi_lang) + ")  and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "YN_FLAG":    # Yes/No 구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '00' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "SYSTEM_SW":  # 시스템 구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '05' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "CUST_GRADE": # 고객등급 구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '06' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "TD_SVC_CD":  # TD 서비스 구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '07' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "ASSETS_TYPE":    # 자산구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '08' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "DUTY_CD":    # 직책 구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '09' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "WORK_PROC_CD":   # 업무 진행 구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '10' AND CODE > '00' AND CODE <= '10' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "LGOIN_LEVEL":    # 회원 구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '12' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "PAY_CD": # 지급시 지급방법
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '54' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "COMP_DUTY_CD":   # 직급구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '16' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"

    elif cFlag == "Gubun01":    # 업무관련구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '20' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "AR_Category":
        strSql = " select code, code_enm as 'code_nm' from T_CD_010 where CODE_GRP = 'H04' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "VAN_TYPE":
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = 'H08' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ, CODE"
    elif cFlag == "DOOR_TYPE":
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = 'H34' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ, CODE "

    elif cFlag == "SZON_RATETYPE":
        strSql = f" select rate_type as code, rate_enm as code_nm from V_TH_107 where use_flag = 'Y' and OFFICE_NO = '{0}'", G_OFFICE_NO
    elif cFlag == "KIOSK_TYPE":
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = 'H35' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"

    elif cFlag == "SCD":
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '100' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "HEADER_HOTEL":
        sb = []
        sb.append(" select 'Total' as code, 'Total' as code_nm union all ")
        sb.append(" select to100.office_no as code, to100.office_snm as code_nm ")
        sb.append("   from T_TO_100 to100 ")
        sb.append("        join V_TO_010 to010 on to100.head_office_no = to010.head_office_no ")
        sb.append(f" where to010.office_no = '{0}'", G_OFFICE_NO)

        if strSelValue == "":
            sb.append(f"   and to100.hotel_grade in (select * from dbo.fn_Split2('', ','))")
        else:
            sb.append(f"   and to100.hotel_grade in (select * from dbo.fn_Split2('{0}', ','))", strSelValue.replace(", ", ","))
        strSql = ''.join(sb)

    elif cFlag == "HOTEL_GRADE":    # 호텔등급 (오피스전용 T_CD_100:GRP_CD = '20')
        strSql = " select code, code_enm as code_nm from T_CD_100 "
        strSql = strSql + " where OFFICE_NO = '" + G_OFFICE_NO + "' and CODE_GRP = '20' AND CODE <> '00' and use_flag <> 'N'  ORDER BY SORT_SEQ, CODE_NM "
    elif cFlag == "JOB_CD_OFFICE":  # 업무관련구분 (오피스전용 T_CD_100:GRP_CD = 'W1')
        strSql = " select code, code_nm from T_CD_100 "
        strSql = strSql + " where OFFICE_NO = '" + G_OFFICE_NO + "' and CODE_GRP = 'W1' AND CODE <> '00' and use_flag <> 'N'  ORDER BY SORT_SEQ, CODE_NM "
    elif cFlag == "CLAIM_CLIENT":   # 클레임관리업체  (오피스전용 T_CD_100:GRP_CD = 'W7')
        strSql = " select code, code_nm from T_CD_100 "
        strSql = strSql + " where OFFICE_NO = '" + G_OFFICE_NO + "' and CODE_GRP = 'W7' AND CODE <> '00' and use_flag <> 'N'  ORDER BY SORT_SEQ, CODE "
    elif cFlag == "CLAIM_CD":   # 클레임구분     (오피스전용 T_CD_100:GRP_CD = 'W8')
        strSql = " select code, code_nm from T_CD_100 "
        strSql = strSql + " where OFFICE_NO = '" + G_OFFICE_NO + "' and CODE_GRP = 'W8' AND CODE <> '00' and use_flag <> 'N'  ORDER BY SORT_SEQ, CODE "

    elif cFlag == "VISIT_CD":   # 방문 구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '21' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "DUTY_COMP_CD":   # 업체 직책 구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '24' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"

    elif cFlag == "TXD_APP_METHOD": # 가입 등록 구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '28' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "OFFICE_POINT_GEN":   # 포인트 구분
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '29' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"

    elif cFlag == "SCH_MINUTE":
        strSql = " select code_nm as code, code_nm from T_CD_010 where CODE_GRP = '33' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "SVC_PAY_TYPE":   # 서비스 결제수단
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = '34' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"

    elif cFlag == "UNIT_CODE":  # 단위
        strSql = " select code, code+' : '+code_nm as code_nm from T_CD_010 where CODE_GRP = '108' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"

    elif cFlag == "SALES_MKT_ID":   # MKT 영업코드 (평가원, 삼일...)
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = 'X4' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"

    elif cFlag == "OFFICE_DEPT":    # 부서
        strSql = " select dept_cd as code, dept_nm as code_nm from T_TO_108 where OFFICE_NO = '" + sessionInfoVo.OfficeNo + "' ORDER BY sort_seq "

    elif cFlag == "MEMBER_LEVEL_BTW":   # 레벨 (시스템일괄 T_CD_010:GRP_CD = 'X1')
        strSql = " select code, code_nm from T_CD_010 "
        strSql = strSql + " where CODE_GRP = 'X1' AND CODE <> '00' AND CODE >= '" + strOption1 + "' and CODE <= '" + strOption2 + "' and use_flag <> 'N' "
        # response.write strsql
        strSql = strSql + " ORDER BY code"

    elif cFlag == "MEMBER_LEVEL_OFFICE":
        strSql = " select code, code_nm from T_CD_100 "
        strSql = strSql + " where OFFICE_NO = 'RLINK' and CODE_GRP = 'X1' AND CODE <> '00' and use_flag <> 'N' "

        if sessionInfoVo.LoginLevel >= "SA" and sessionInfoVo.LoginLevel <= "ZZ":
            strSql = strSql + " Union select 'SA' CODE, 'SA' CODE_NM "
            strSql = strSql + " Union select 'SB' CODE, 'SB' CODE_NM "
            strSql = strSql + " Union select 'SS' CODE, 'SS' CODE_NM "
            strSql = strSql + " Union select 'SZ' CODE, 'SZ' CODE_NM "
        strSql = strSql + " ORDER BY code"
    elif cFlag == "TRUE_FALSE":
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = 'XA' AND CODE <> '00' ORDER BY code desc"

        # Case "MEMBER_ROLE"
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = 'X2' AND CODE <> '00' and use_flag <> 'N' ORDER BY code"
    elif cFlag == "MEMBER_ROLE_BTW":    # 역할(시스템일괄용 T_CD_010: CODE_GRP="X2")
        strSql = " select code, code_nm from T_CD_010 "
        strSql = strSql + " where CODE_GRP = 'X2' AND CODE <> '00' AND CODE >= '" + strOption1 + "' and CODE <= '" + strOption2 + "' and use_flag <> 'N' ORDER BY code"

    elif cFlag == "MEMBER_ROLE1_BTW":   # 부가권한:본지점이용권한
        strSql = " select code, code_nm from T_CD_010 "
        strSql = strSql + " where CODE_GRP = 'X3' AND CODE <> '00' AND CODE >= '" + strOption1 + "' and CODE <= '" + strOption2 + "' and use_flag <> 'N' ORDER BY code"

    elif cFlag == "ACCT_AUTH":  # 상단 예약대메뉴권한
        strSql = " select code, code_nm from T_CD_010 a join t_to_100 ON office_no = '" + G_OFFICE_NO + "' and use_acct = 'Y'  where CODE_GRP = '36' AND CODE <> '00' and a.use_flag <> 'N' ORDER BY code"
    elif cFlag == "HR_AUTH":    # 상단 투숙/정산대메뉴권한
        strSql = " select code, code_nm from T_CD_010 a join t_to_100 ON office_no = '" + G_OFFICE_NO + "' and use_hr = 'Y'  where CODE_GRP = '106' AND CODE <> '00' and a.use_flag <> 'N' ORDER BY code"
    elif cFlag == "INVENTORY_AUTH": # 상단 H/K메뉴권한
        strSql = " select code, code_nm from T_CD_010 a join t_to_100 ON office_no = '" + G_OFFICE_NO + "' and use_inventory = 'Y' where CODE_GRP = '107' AND CODE <> '00' and a.use_flag <> 'N' ORDER BY code"
    elif cFlag == "PRODUCTION_AUTH":    # 상단 관리대메뉴권한 (CONFIG)
        strSql = " select code, code_nm from T_CD_010 a join t_to_100 ON office_no = '" + G_OFFICE_NO + "' and use_production = 'Y' where CODE_GRP = '109' AND CODE <> '00' and a.use_flag <> 'N' ORDER BY code"

    elif cFlag == "AR_AUTH":    # 상단 관리대메뉴권한 (후불관리 Account Receivable)
        strSql = " select code, code_nm from T_CD_010 a join t_to_100 ON office_no = '" + G_OFFICE_NO + "' and use_ar = 'Y' where CODE_GRP = '111' AND CODE <> '00' and a.use_flag <> 'N' ORDER BY code"
    elif cFlag == "EVENT_AUTH": # 상단 관리대메뉴권한 (행사(연회) EVENT/BANQUET)
        strSql = " select code, code_nm from T_CD_010 a join t_to_100 ON office_no = '" + G_OFFICE_NO + "' and use_event = 'Y' where CODE_GRP = '112' AND CODE <> '00' and a.use_flag <> 'N' ORDER BY code"
    elif cFlag == "REPORT_AUTH":    # 상단 관리대메뉴권한 (REPORT)
        strSql = " select code, code_nm from T_CD_010 a join t_to_100 ON office_no = '" + G_OFFICE_NO + "' and use_report = 'Y' where CODE_GRP = '113' AND CODE <> '00' and a.use_flag <> 'N' ORDER BY code"
    elif cFlag == "MANAGE_AUTH":    # 상단 관리대메뉴권한 (MANAGE)
        strSql = " select code, code_nm from T_CD_010 a join t_to_100 ON office_no = '" + G_OFFICE_NO + "' and use_manage = 'Y' where CODE_GRP = '114' AND CODE <> '00' and a.use_flag <> 'N' ORDER BY code"

    elif cFlag == "UGRP_NO":    # 이용자그룹 (이용자권한그룹)
        strSql = " select ugrp_no as code, ugrp_nm as code_nm from T_MB_101 WHERE office_no = '" + G_OFFICE_NO + "' and use_flag <> 'Y' ORDER BY ugrp_nm"

    elif cFlag == "OFFICE_STAFF":   # 이용자 조회
        strSql = " select OSTAFF_ID AS code, STAFF_NM AS code_nm from T_MB_100 "
        if strOption1 == "":
            strSql = strSql + " where OFFICE_NO IN (SELECT office_no FROM T_TO_100 WHERE head_office_no = dbo.GetHeadOffice('" + G_OFFICE_NO + "')) and use_flag = 'Y' "

        else:   # 그룹호텔에서 그룹내 타호텔의 자료 검색
            strSql = strSql + " where OFFICE_NO IN (SELECT office_no FROM T_TO_100 WHERE head_office_no = dbo.GetHeadOffice('" + strOption1 + "')) and use_flag = 'Y' "

        if strOption2 != "":
            strSql = strSql + "   and DUTY_CD = '" + strOption2 + "'  "
        strSql = strSql + " order by staff_nm "

    elif cFlag == "OFFICE_STAFF_upper": # 이용자 조회
        strSql = " select OSTAFF_ID AS code, STAFF_NM AS code_nm from T_MB_100 "
        strSql = strSql + " where OFFICE_NO IN (SELECT office_no FROM T_TO_100 WHERE head_office_no = dbo.GetHeadOffice('" + G_OFFICE_NO + "')) and use_flag = 'Y' "
        if strOption2 != "":
            strSql = strSql + "   and DUTY_CD >= '" + strOption2 + "'  "
        strSql = strSql + " order by staff_nm "

    elif cFlag == "OFFICE_STAFF_under": # 이용자 조회
        strSql = " select OSTAFF_ID AS code, STAFF_NM AS code_nm from T_MB_100 "
        strSql = strSql + " where OFFICE_NO IN (SELECT office_no FROM T_TO_100 WHERE head_office_no = dbo.GetHeadOffice('" + G_OFFICE_NO + "')) and use_flag = 'Y' "
        if strOption2 != "":
            strSql = strSql + "   and DUTY_CD <= '" + strOption2 + "'  "
        strSql = strSql + " order by staff_nm "
    elif cFlag == "OFFICE_STAFF_all":   # 이용자 조회 (퇴사자 포함)
        strSql = " select OSTAFF_ID AS code, STAFF_NM AS code_nm from T_MB_100 "
        strSql = strSql + " where OFFICE_NO IN (SELECT office_no FROM T_TO_100 WHERE head_office_no = dbo.GetHeadOffice('" + G_OFFICE_NO + "'))  "
        if strOption2 != "":
            strSql = strSql + "   and DUTY_CD = '" + strOption2 + "'  "
        strSql = strSql + " order by staff_nm "

    elif cFlag == "OFFICE_EMP": # 인사정보에 등록된 직원리스트
        strSql = " select emp_id AS code, emp_nm AS code_nm from T_MB_600 "
        strSql = strSql + " where OFFICE_NO = '" + G_OFFICE_NO + "' and use_flag = 'Y' and retire_flag <> 'Y'  "
        strSql = strSql + " order by emp_nm "

    elif cFlag == "OFFICE_EMP_all": # 인사정보에 등록된 전체직원리스트 (퇴사자포함)
        strSql = " select emp_id AS code, emp_nm AS code_nm from T_MB_600 "
        strSql = strSql + " where OFFICE_NO = '" + G_OFFICE_NO + "' and use_flag = 'Y'    "
        strSql = strSql + " order by emp_nm "

    elif cFlag == "CONTRACT_TYPE":  # 계약 구분 매출계약, 매입계약
        strSql = " select code as code, code_nm from T_CD_010 where CODE_GRP = '59' AND CODE <> '00' and use_flag <> 'N' ORDER BY CODE "
    elif cFlag == "ROOM_Type_CD":   # 숙소구분 코드     (오피스전용 T_CD_100:GRP_CD = 'W5')
        strSql = " select code, code_nm from T_CD_100 "
        strSql = strSql + " where OFFICE_NO = '" + G_OFFICE_NO + "' and CODE_GRP = '11' AND CODE <> '00'   ORDER BY SORT_SEQ, CODE_NM " # and use_flag <> 'N'
    elif cFlag == "RoomTypeCode":   # 숙소타입코드
        strSql = f" SELECT DISTINCT(ROOM_TYPE) AS code, RTYPE_NM AS code_nm FROM T_RM_010   WHERE USE_FLAG = 'Y' OFFICE_NO = '{0}'", G_OFFICE_NO
    elif cFlag == "RoomTypeName":   # 숙소타입명
        strSql = f" SELECT DISTINCT(ROOM_TYPE) AS code, ROOM_TYPE  + ' ' + RTYPE_NM AS CODE_NM FROM T_RM_010 WHERE USE_FLAG = 'Y' AND OFFICE_NO = '{0}'", G_OFFICE_NO
    elif cFlag == "RoomTypeName1":  # 숙소타입명
        strSql = f" SELECT DISTINCT(ROOM_TYPE) AS code, ROOM_TYPE  + ' ' + RTYPE_NM AS CODE_NM FROM T_RM_010 WHERE USE_FLAG = 'Y' AND OFFICE_NO = '{0}' AND RTYPE_FLAG = '02'", G_OFFICE_NO
    elif cFlag == "staffType":  # 직원구분
        strSql = f" SELECT CODE, CODE_NM FROM T_CD_100 WHERE CODE_GRP = '16' AND CODE <> '00'AND USE_FLAG = 'Y' AND OFFICE_NO = '{0}' order by code asc", G_OFFICE_NO
    elif cFlag == "staff_FLAG": # 직원구분
        strSql = f" SELECT CODE, CODE_NM FROM T_CD_100 WHERE CODE_GRP = '16' AND CODE <> '00'AND OFFICE_NO = '{0}' order by code asc", G_OFFICE_NO

    elif cFlag == "cusLevel":   # 고객등급
        strSql = f" SELECT CODE, CODE_NM FROM T_CD_100 WHERE CODE_GRP = '14' AND CODE <> '00' AND OFFICE_NO = '{0}'", G_OFFICE_NO

    elif cFlag == "clean_status":   # 숙소상태
        strSql = f" SELECT CODE, CODE_NM FROM T_CD_100 WHERE CODE_GRP = '15' AND CODE <> '00' AND OFFICE_NO = '{0}'", G_OFFICE_NO

    elif cFlag == "Loan_Status":    # 물품대여 상태
        strSql = f" SELECT CODE, CODE_NM, CODE_ENM FROM T_CD_100 WHERE CODE_GRP = '10' AND CODE <> '00' AND OFFICE_NO = '{0}'", G_OFFICE_NO


    elif cFlag == "room_floor": # 숙소층수
        strSql = f" select distinct(rm_floor) as code, rm_floor as code_nm from T_RM_100 where use_flag = 'Y' and OFFICE_NO = '{0}'", G_OFFICE_NO

    elif cFlag == "room_Type":  # 숙소타입
        strSql = f" select  Room_Type as code, RTYPE_NM as code_nm from t_rm_010 where use_flag = 'Y' and OFFICE_NO = '{0}'", G_OFFICE_NO
    elif cFlag == "Bed_Type":   # 배드타입
        strSql = f" select CODE, code_nm from t_cd_100 where code_grp='05' AND CODE <> '00' and use_flag = 'Y' and OFFICE_NO = '{0}'", G_OFFICE_NO
    elif cFlag == "rmview": # 뷰
        strSql = f" select CODE, code_nm from t_cd_100 where code_grp='04' and use_flag = 'Y' and code <> '00' and OFFICE_NO = '{0}'", G_OFFICE_NO
    elif cFlag == "Status": # RooM Sataus
        strSql = f" select CODE, code_nm from t_cd_100 where code_grp='07'AND CODE <> '00' and use_flag = 'Y' and OFFICE_NO = '{0}'", G_OFFICE_NO
    elif cFlag == "Hk": # 뷰
        strSql = f" select CODE, code_nm from t_cd_100 where code_grp='15' and use_flag = 'Y' AND CODE <> '00' and OFFICE_NO = '{0}'", G_OFFICE_NO
    elif cFlag == "RM_FLOOR":   # 층(Floor)
        strSql = f" select  distinct RM_FLOOR as CODE, RM_FLOOR as code_nm from t_rm_100 where OFFICE_NO = '{0}' and RM_FLOOR is not null and RM_FLOOR <> '' order  by RM_FLOOR ASC   ", G_OFFICE_NO

    elif cFlag == "item_type":  # Item Type
        strSql = f" select CODE, code_nm from t_cd_100 where code_grp='40' and use_flag = 'Y' AND CODE <> '00' and OFFICE_NO = '{0}'", G_OFFICE_NO

    elif cFlag == "tax_gubun":  # Tax Gubun
        strSql = f" select CODE, code_nm from t_cd_100 where code_grp='22' and use_flag = 'Y' AND CODE <> '00' and OFFICE_NO = '{0}'", G_OFFICE_NO

    elif cFlag == "maid_id":    # 메이드 정보 (로그인이용없을 경우 사용 : 등록된 직원정보에서 검색)
        strSql = f"select emp_id as code, emp_nm as code_nm from t_mb_600 where staff_flag = '03' AND office_no= '{0}' ", G_OFFICE_NO
    elif cFlag == "maid_id2":   # 메이드 정보 (로그인하는 경우 이용자로 등록하고 구분코드로 분류)
        strSql = f"select ostaff_id as code, staff_nm as code_nm from t_mb_100 where staff_flag = '03' AND office_no= '{0}' ", G_OFFICE_NO

    elif cFlag == "COMP_TYPE":  # 거래처타입
        strSql = f"SELECT comp_no as code , comp_nm as code_nm  FROM T_CP_200 WHERE use_flag = 'Y' AND office_no= dbo.GetHeadOffice('{0}') ", G_OFFICE_NO
    elif cFlag == "CHARGE_ID":  # 담당자 정보
        strSql = f"select OSTAFF_ID AS code, STAFF_NM AS code_nm from T_MB_100 WHERE DEPT_CD = '05' and use_flag = 'Y' AND office_no= '{0}' ", G_OFFICE_NO
    elif cFlag == "TCDGRP110":  # 숙소 위치
        strSql = "select code, code_nm from T_CD_010 WHERE CODE_GRP = '110' and use_flag = 'Y' and code  <> '00'"
    elif cFlag == "outlet_nm":  # outlet_no
        strSql = f"SELECT outlet_no as code , outlet_no+ ' ' + outlet_nm as code_nm from [dbo].[T_TH_100] WHERE  use_flag = 'Y' AND office_no= '{0}' and outlet_type <> '00' ", G_OFFICE_NO

    elif cFlag == "CREDIT_CARD":
        if strOption1 == "":
            strSql = f"SELECT cc_cd as code , cc_cd + ' ' + cc_nm as code_nm from [dbo].[v_th_110] WHERE  use_flag = 'Y' AND office_no= '{0}' ORDER BY CC_NM ASC ", G_OFFICE_NO
        else:   # 그룹호텔에서 그룹내 타호텔자료 검색
            strSql = f"SELECT cc_cd as code , cc_cd + ' ' + cc_nm as code_nm from [dbo].[v_th_110] WHERE  use_flag = 'Y' AND office_no= '{0}' ORDER BY CC_NM ASC ", strOption1
    elif cFlag == "CREDIT_CARD2":
        strSql = f"SELECT cc_cd as code ,  cc_cd + ' ' + cc_enm as code_nm from [dbo].[v_th_110] WHERE  use_flag = 'Y' AND office_no= '{0}' ORDER BY CC_ENM ASC ", G_OFFICE_NO


    elif cFlag == "MAEIP_CD":   # 카드매입사 (초기이용자료)
        strSql = f"SELECT CASE SUBSTRING(B.VAN_TYPE,1,3) WHEN 'KIC' THEN A.KICC_CD WHEN 'NIC' THEN A.NICE_CD ELSE '' END as code , cc_nm as code_nm from [dbo].[v_th_110] A JOIN T_TO_107 B ON B.OFFICE_NO = A.OFFICE_NO WHERE  A.use_flag = 'Y' AND a.office_no= '{0}' ORDER BY CC_NM ASC ", G_OFFICE_NO


    elif cFlag == "MAEIP_CD2":  # 카드매입사(수정된 자료)
        strSql = f"SELECT DISTINCT A.COMP_NO as code , COMP_NM as code_nm from [dbo].[v_th_110] A JOIN T_TO_107 B ON B.OFFICE_NO = A.OFFICE_NO JOIN T_CP_200 C ON C.OFFICE_NO = dbo.GetHeadOffice(A.OFFICE_NO AND C.COMP_NO = A.COMP_NO WHERE  a.use_flag = 'Y' AND a.office_no= '{0}' ORDER BY COMP_NM ASC ", G_OFFICE_NO


    elif cFlag == "outlet_cd":  # outlet_cd
        strSql = f"SELECT outlet_no as code , outlet_no + ' ' + outlet_nm as code_nm from [dbo].[T_TH_100] WHERE  use_flag = 'Y' AND office_no= '{0}' ", G_OFFICE_NO
    elif cFlag == "outlet_cd2": # outlet_cd '후불등록가능 업장
        strSql = f"SELECT outlet_no as code , outlet_no + ' ' + outlet_nm as code_nm from [dbo].[T_TH_100] WHERE  use_flag = 'Y' AND office_no= '{0}' and ar_yn = 'Y' ", G_OFFICE_NO
    elif cFlag == "outlet_cd3": # outlet_cd '수동 포스팅 업장 대상 (80. ROOM AUTO, 20 BREAKFAST AUTO 만 제외)
        strSql = f"SELECT outlet_no as code , outlet_no + ' ' + outlet_nm as code_nm from [dbo].[T_TH_100] WHERE  use_flag = 'Y' AND office_no= '{0}' and outlet_no NOT IN ('80','20')  ", G_OFFICE_NO

    elif cFlag == "outlet_cd_ITEM": # outlet_cd '업장상품관리 업장 (식당,커피숍 등 주문상품메뉴 관리용)
        strSql = f"SELECT outlet_no as code , outlet_no + ' ' + outlet_nm as code_nm from [dbo].[T_TH_100] WHERE  use_flag = 'Y' AND office_no= '{0}' and item_entry_yn = 'Y' ", G_OFFICE_NO

    elif cFlag == "outlet_cd_pos":  # outlet_cd '상품판매용 업장 (POS와 연동이 될 수 있는 업장 : 30번대)
        strSql = f"SELECT outlet_no as code , outlet_no + ' ' + outlet_nm as code_nm from [dbo].[T_TH_100] WHERE  use_flag = 'Y' AND office_no= '{0}' and outlet_no like '3%' ", G_OFFICE_NO

    elif cFlag == "minibar_cd_pos": # minibar '상품판매용 업장 (POS와 연동이 될 수 있는 업장 : 00번대)
        strSql = f"SELECT outlet_no as code , outlet_no + ' ' + outlet_nm as code_nm from [dbo].[T_TH_100] WHERE  use_flag = 'Y' AND office_no= '{0}' and outlet_no like '01' ", G_OFFICE_NO

    elif cFlag == "CompType":   # CompType
        strSql = f" SELECT code AS code, code_nm FROM [dbo].[T_CD_100] where code_grp='21' AND CODE <> '00' AND office_no= '{0}' order by code ", G_OFFICE_NO

    elif cFlag == "OutletType": # CompType
        strSql = f" SELECT code AS code, code_nm FROM [dbo].[T_CD_100] where code_grp='25' AND CODE <> '00' AND office_no= '{0}' order by code ", G_OFFICE_NO

    elif cFlag == "WEEK_GUBUN": # WEEK구분 : 2W, 4W
        strSql = f" SELECT code AS code, code_enm as code_nm FROM [dbo].[T_CD_100] where code_grp='26' AND CODE <> '00' AND office_no= '{0}' order by code ", G_OFFICE_NO


    elif cFlag == "MarcketType":    # 마켓타입
        if strOption1 == "":
            strSql = f" SELECT code AS code, code+' '+ code_nm as code_nm FROM [dbo].[T_CD_100]  where code_grp='01' AND CODE <> '00' AND USE_FLAG = 'Y' AND office_no= '{0}' order by SORT_SEQ, code ", G_OFFICE_NO
        else:   # 그룹호텔에서 다른호텔의 정보검색하는 경우에 적용
            strSql = f" SELECT code AS code, code+' '+ code_nm as code_nm FROM [dbo].[T_CD_100]  where code_grp='01' AND CODE <> '00' AND USE_FLAG = 'Y' AND office_no= '{0}' order by SORT_SEQ, code ", strOption1
    elif cFlag == "MarcketType2":   # 마켓타입2 (TGA (Travel Agent Group)코드가 2개이상일경우 Agent 통합으로 검색하기 위한 코드
        if strOption1 == "":
            strSql = f" SELECT code AS code, code+' '+ code_nm as code_nm,sort_seq FROM [dbo].[T_CD_100]  where code_grp='01' AND CODE <> '00' AND USE_FLAG = 'Y' AND office_no= '{0}' UNION select 'XAG', 'XAG Agent Group', 9999 as sort_seq order by SORT_SEQ, code ", G_OFFICE_NO
        else:   # 그룹호텔에서 다른호텔의 정보검색하는 경우에 적용
            strSql = f" SELECT code AS code, code+' '+ code_nm as code_nm,sort_seq FROM [dbo].[T_CD_100]  where code_grp='01' AND CODE <> '00' AND USE_FLAG = 'Y' AND office_no= '{0}' UNION select 'XAG', 'XAG Agent Group', 9999 as sort_seq order by SORT_SEQ, code ", strOption1
    elif cFlag == "SourceType": # 소스타입
        if strOption1 == "":
            strSql = f" SELECT code AS code, code+' '+ code_nm as code_nm  FROM [dbo].[T_CD_100] where code_grp='02' AND CODE <> '00' AND USE_FLAG = 'Y' AND office_no= '{0}' order by SORT_SEQ, code ", G_OFFICE_NO
        else:   # 그룹호텔에서 다른호텔의 정보검색하는 경우에 적용
            strSql = f" SELECT code AS code, code+' '+ code_nm as code_nm  FROM [dbo].[T_CD_100] where code_grp='02' AND CODE <> '00' AND USE_FLAG = 'Y' AND office_no= '{0}' order by SORT_SEQ, code ", strOption1
    elif cFlag == "PersonInCharge": # 호텔담당자 (BUT WCP200_U101에서의 PERSON IN CHARGE는 거래처의 담당자를 의미함) 본 코드는 이용할 필요 없음 (SALES_EMP, OFFICE_STAFF 이용)
        strSql = f" SELECT staff_nm as code , staff_nm as code_nm FROM [dbo].[T_MB_100] where office_no= '{0}' ", G_OFFICE_NO
    elif cFlag == "nationality":    # nationality
        strSql = "SELECT COUNTRY_cd AS code , COUNTRY_NM AS code_nm FROM [dbo].[T_CD_081] where use_flag= 'Y' "
    elif cFlag == "GENDER_DBO": # 성별
        strSql = " select code, code_nm from T_CD_010 where CODE_GRP = 'H02' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "Cancel_Reason":  # 취소사유
        strSql = " select code, code_nm from DBO.T_CD_100 WHERE OFFICE_NO = '" + G_OFFICE_NO + "' AND CODE_GRP = '06' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "VIP_CODE":   # VIP
        if strOption1 == "":
            strSql = " SELECT code, code_nm FROM DBO.T_CD_100 WHERE OFFICE_NO = '" + G_OFFICE_NO + "' AND CODE_GRP = '03' AND CODE <> '00' AND USE_FLAG = 'Y' ORDER BY code "
        else:   # 그룹호텔에서 다른호텔의 정보검색하는 경우에 적용
            strSql = " SELECT code, code_nm FROM DBO.T_CD_100 WHERE OFFICE_NO = '" + strOption1 + "' AND CODE_GRP = '03' AND CODE <> '00' AND USE_FLAG = 'Y' ORDER BY code "
    elif cFlag == "LANGUAGE":   # LANGUAGE
        strSql = " SELECT LANGUAGE_CD code, LANGUAGE_NM code_nm FROM DBO.V_CD_084 WHERE USE_FLAG = 'Y' ORDER BY LANGUAGE_NM "
    elif cFlag == "SERVICE_CD": # SERVICE_CD
        strSql = f" SELECT SERVICE_CD as code , SERVICE_NM as code_nm FROM dbo.V_TH_102 WHERE OFFICE_NO= '{0}' AND USE_FLAG = 'Y' ORDER BY SERVICE_NM ASC", G_OFFICE_NO
    elif cFlag == "PAYMENT_CD": # 선수금용 지불코드 (현금+신용카드사)
        strSql = f" SELECT PAYMENT_CD as code , case when TYPE = 'C' then '카드-' +PAYMENT_NM else PAYMENT_NM	end as code_nm FROM dbo.V_TH_105 WHERE OFFICE_NO= '{0}' AND DEPOSIT_PAY = '1' ORDER BY type desc, sort_seq asc, PAYMENT_NM asc  ", G_OFFICE_NO
    elif cFlag == "PAYMENT_CD2":    # 지불코드전체 (지불방식 + 신용카드사)
        strSql = f" SELECT PAYMENT_CD as code , case when TYPE = 'C' then '카드-' +PAYMENT_NM else PAYMENT_NM	end as code_nm FROM dbo.V_TH_105 WHERE OFFICE_NO= '{0}' ORDER BY type desc, sort_seq asc, PAYMENT_NM asc  ", G_OFFICE_NO
    elif cFlag == "PAYMENT_CD3":    # 지불코드대분류 (지불방식 + 신용카드구분)
        strSql = f" select DISTINCT case WHEN TYPE = 'C' THEN 'AA' ELSE PAYMENT_CD END AS CODE, CASE WHEN TYPE = 'C' THEN 'AA 신용카드' ELSE PAYMENT_CD + ' ' + PAYMENT_NM END as code_nm FROM V_TH_105 WHERE OFFICE_NO= '{0}' ORDER BY CODE ASC ", G_OFFICE_NO
    elif cFlag == "PAYMENT_CD4":    # 지불코드대분류 (지불방식 + 신용카드구분 - (DP,EM,PO,RF)  <<< CASH, CASH in Online, Credit Card 포함됨)
        strSql = f" select DISTINCT case WHEN TYPE = 'C' THEN 'AA' ELSE PAYMENT_CD END AS CODE, CASE WHEN TYPE = 'C' THEN 'AA 신용카드' ELSE PAYMENT_CD + ' ' + PAYMENT_NM END as code_nm FROM V_TH_105 WHERE OFFICE_NO= '{0}' and PAYMENT_CD NOT IN ('DP','EM','PO','RF','CL') ORDER BY CODE ASC ", G_OFFICE_NO


    elif cFlag == "PAYMENT_CD_ONLY":    # PAYMENT_CD ONLY
        strSql = f" SELECT PAYMENT_CD AS CODE, PAYMENT_NM AS CODE_NM FROM DBO.T_TH_105 WHERE OFFICE_NO = '{0}' AND USE_FLAG = 'Y' ORDER BY CD1 DESC ", G_OFFICE_NO
    elif cFlag == "FOLIO_TYPE": # FOLIO TYPE
        strSql = f" SELECT code, code_nm FROM [dbo].[T_CD_100] where code_grp='00' AND CODE <> '00' AND office_no= '{0}' order by code ", G_OFFICE_NO
    elif cFlag == "FOLIO_TYPE_ENM": # FOLIO TYPE
        strSql = f" SELECT code, code_enm code_nm FROM [dbo].[T_CD_100] where code_grp='00' AND CODE <> '00' AND office_no= '{0}' order by code ", G_OFFICE_NO
    elif cFlag == "Sales_Emp":  # 호텔의 영업담당자를 의미 (호텔이용자아이디)
        strSql = f" SELECT staff_nm as code , staff_nm as code_nm FROM [dbo].[T_MB_100] where office_no= '{0}' ", G_OFFICE_NO


    elif cFlag == "ACCOUNT":
        strSql = f"SELECT    ACCT_NO as code , (AR_FLAG + ':' + ACCT_NM) as  code_nm FROM DBO.V_AR_000 WHERE office_no= dbo.GetHeadOffice('{0}') ", G_OFFICE_NO
    elif cFlag == "COLLECT_CD":
        strSql = f"SELECT COLLECT_CD CODE, COLLECT_NM CODE_NM FROM V_AR_201 WHERE OFFICE_NO = '{0}' ", G_OFFICE_NO
    elif cFlag == "sell_type":
        strSql = f"SELECT code, code_nm FROM t_cd_100 WHERE OFFICE_NO = '" + G_OFFICE_NO + "' and code_grp='34' and use_flag='y' order by code"
    elif cFlag == "guide_nm":
        strSql = f"SELECT guide_nm as code, guide_nm as code_nm FROM v_rv_100 WHERE OFFICE_NO = '" + G_OFFICE_NO + "' and guide_nm <>'' group by guide_nm"
    elif cFlag == "MOP_CD": # MOP
        if strOption1 == "":
            strSql = f" SELECT code AS code, code+' '+ code_nm as code_nm  FROM [dbo].[T_CD_100] where code_grp='37' AND CODE <> '00' AND USE_FLAG = 'Y' AND office_no= '{0}' order by code ", G_OFFICE_NO
        else:   # 그룹호텔에서 다른호텔의 정보검색하는 경우에 적용
            strSql = f" SELECT code AS code, code+' '+ code_nm as code_nm  FROM [dbo].[T_CD_100] where code_grp='37' AND CODE <> '00' AND USE_FLAG = 'Y' AND office_no= '{0}' order by code ", strOption1
    elif cFlag == "LAYOUT_TYPE22":  # 행사장 배치 타입xxxxx 42 번 이용
        strSql = f" SELECT code AS code, code+' '+ code_nm as code_nm  FROM [dbo].[T_CD_100] where code_grp='38' AND CODE <> '00' AND USE_FLAG = 'Y' AND office_no= '{0}' order by sort_seq asc, code asc ", G_OFFICE_NO

    elif cFlag == "EVENT_TYPE": # 행사진행타입 (기업,관공서, 학교,종료단체 등...)
        strSql = f" SELECT code AS code, code+' '+ code_nm as code_nm  FROM [dbo].[T_CD_100] where code_grp='39' AND CODE <> '00' AND USE_FLAG = 'Y' AND office_no= '{0}' order by sort_seq asc, code asc ", G_OFFICE_NO

    elif cFlag == "OOO_CD": # OOO코드 (고장코드 OUT OF ORDER)
        strSql = f" SELECT ooo_no AS code, ooo_nm as code_nm  FROM [T_TH_119] where USE_FLAG = 'Y' AND office_no= '{0}' order by SORT_SEQ, OOO_NM ASC ", G_OFFICE_NO

    elif cFlag == "LF_FLAG":    # lf_flag
        strSql = f" SELECT code, code_nm  FROM T_CD_100 where USE_FLAG = 'Y' AND CODE_GRP='08' and code<>'00' AND office_no= '" + G_OFFICE_NO + "' order by code ASC "

    elif cFlag == "LF_STATUS":  # 분실물 상황(LF_STATUS)
        strSql = f" SELECT code, code_nm  FROM T_CD_100 where USE_FLAG = 'Y' AND CODE_GRP='09' and code<>'00' AND office_no= '" + G_OFFICE_NO + "' order by code ASC "

    elif cFlag == "HOTEL_GRAGE_SELECT":
        strSql = "select '" + G_OFFICE_NO + "' + 'ALL' as code, 'ALL' as code_nm "
        strSql = strSql + "union "
        strSql = strSql + "SELECT '" + G_OFFICE_NO + "' + 'ALL' + A.HOTEL_GRADE AS CODE, B.CODE_ENM AS CODE_NM "
        strSql = strSql + "FROM T_TO_100 A "
        strSql = strSql + "LEFT OUTER JOIN T_CD_100 B ON B.OFFICE_NO = dbo.GetHeadOffice('" + G_OFFICE_NO + "') AND A.HOTEL_GRADE = CODE AND CODE_GRP='20' "
        strSql = strSql + "WHERE HEAD_OFFICE_NO = dbo.GetHeadOffice('" + G_OFFICE_NO + "') "
        strSql = strSql + "union ALL "
        strSql = strSql + "SELECT A.OFFICE_NO AS CODE,OFFICE_NM AS CODE_NM "
        strSql = strSql + "FROM T_TO_100 A "
        strSql = strSql + "WHERE HEAD_OFFICE_NO = dbo.GetHeadOffice('" + G_OFFICE_NO + "') "

    elif cFlag == "RSV_QUERY_STATUS":
        strSql = f" select code, code_enm as code_nm from t_cd_010 where use_flag = 'Y' and code_grp = 'H10' and code <> '00' order by sort_seq"

    elif cFlag == "TRACE_STATUS":
        strSql = f" select code, code_enm as code_nm from t_cd_010 where use_flag = 'Y' and code_grp = '71' and code <> '00' order by sort_seq"

    elif cFlag == "MARKET_GROUP":   # 마켓타입그룹구분 (매출목표관리시 이용)
        strSql = f" SELECT code, code_nm  FROM T_CD_100 where USE_FLAG = 'Y' AND CODE_GRP='43' and code<>'00' AND office_no= '" + G_OFFICE_NO + "' order by code ASC "

    elif cFlag == "CMS_CD": # CMS_CD마스터가 아닌 CMS-HOTEL 코드등록 대상에 한함.
        strSql = " SELECT DISTINCT A.CMS_CD code, B.CMS_NM code_nm, B.SORT_SEQ AS SEQ FROM T_CM_100 A JOIN T_CM_010 B ON B.CMS_CD = A.CMS_CD WHERE office_no= '" + G_OFFICE_NO + "' AND A.CMS_USE_YN = 'Y' AND A.USE_YN = 'Y' ORDER BY B.SORT_SEQ ASC, B.CMS_NM ASC "

    elif cFlag == "CMS_CD_TLLC":    # 티엘린칸 전용
        strSql = " SELECT DISTINCT A.CMS_CD code, B.CMS_NM code_nm, B.SORT_SEQ AS SEQ FROM T_CM_100 A JOIN T_CM_010 B ON B.CMS_CD = A.CMS_CD WHERE office_no= '" + G_OFFICE_NO + "' AND A.CMS_CD = 'TLLC' AND A.CMS_USE_YN = 'Y' AND A.USE_YN = 'Y' ORDER BY B.SORT_SEQ ASC, B.CMS_NM ASC "

    elif cFlag == "CMS_CD2":    # 티엘린칸제외하고 모두
        strSql = " SELECT DISTINCT A.CMS_CD code, B.CMS_NM code_nm, B.SORT_SEQ AS SEQ FROM T_CM_100 A JOIN T_CM_010 B ON B.CMS_CD = A.CMS_CD WHERE office_no= '" + G_OFFICE_NO + "' AND A.CMS_CD <> 'TLLC' AND A.CMS_USE_YN = 'Y' AND A.USE_YN = 'Y' ORDER BY B.SORT_SEQ ASC, B.CMS_NM ASC "

    elif cFlag == "CMS_ALL":    # CMS_CD마스터
        if strOption1 == "":
            strSql = " SELECT CMS_CD code, CMS_NM code_nm FROM T_CM_010  WHERE USE_FLAG = 'Y' ORDER BY SORT_SEQ ASC, CMS_NM ASC "
        else:   # 그룹호텔에서 다른호텔의 정보검색하는 경우에 적용
            strSql = f" SELECT CMS_CD code, CMS_NM code_nm FROM T_CM_010  WHERE USE_FLAG = 'Y' AND code = '{0}' ORDER BY SORT_SEQ ASC, CMS_NM ASC ", strOption1

    elif cFlag == "API_CD":
        strSql = f" select code, code_nm as code_nm from t_cd_010 where use_flag = 'Y' and code_grp = 'C02' and code <> '00' order by sort_seq"

    elif cFlag == "API_CD2":
        strSql = f" select code, code + ' ' + code_enm as code_nm from t_cd_010 where use_flag = 'Y' and code_grp = 'C02' and code <> '00' order by sort_seq"

    elif cFlag == "AMT_FLAG":   # Amount Flag (전체,  NET, SELL, NET/SELL)
        strSql = f" select code, code_nm as code_nm from t_cd_010 where use_flag = 'Y' and code_grp = 'C03' and code <> '00' order by sort_seq"

    elif cFlag == "AMT_FLAG2":  # Amount Flag  (NET + SELL,    NET/SELL은 사용안함)
        strSql = f" select code, code_nm as code_nm from t_cd_010 where use_flag = 'Y' and code_grp = 'C03' and code <> '00' and value1 = 1 order by sort_seq"

    elif cFlag == "OTA_TYPE":   # Amount Type
        strSql = f" select code, code_nm as code_nm from t_cd_010 where use_flag = 'Y' and code_grp = 'C01' and code <> '00' order by sort_seq"

    elif cFlag == "USE_CD":
        strSql = f" select code, code_nm as code_nm from t_cd_010 where use_flag = 'Y' and code_grp = 'E27' and code <> '00' order by sort_seq"

    elif cFlag == "AMT_FLAG3":  # Amount Flag (SELL ONLY = TL Lincoln용)
        strSql = f" select code, code_nm as code_nm from t_cd_010 where use_flag = 'Y' and code_grp = 'C03' and code = '02' order by sort_seq"

    elif cFlag == "CHNL_NO":    # 채널번호
        strSql = " SELECT DISTINCT  CHNL_NO code,  CHNL_NM code_nm FROM T_CM_130 WHERE office_no= '" + G_OFFICE_NO + "' AND CMS_CD = '" + strOption2 + "' ORDER BY CHNL_NM ASC "

    elif cFlag == "ROOMTYPE_API":
        strSql = " select code, code_nm from t_cd_010 where CODE_GRP = 'H18' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "SSKIN_TYPE":
        strSql = " select code, code_nm from t_cd_010 where CODE_GRP = 'H32' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ"
    elif cFlag == "CLDCD":
        strSql = " select code, code_nm from t_cd_010 where CODE_GRP = 'C04' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ, CODE "
    elif cFlag == "CMS_SEND_SRC":
        strSql = " select code, code_nm from t_cd_010 where CODE_GRP = 'C05' AND CODE <> '00' and use_flag <> 'N' ORDER BY SORT_SEQ, CODE "

    return strSql