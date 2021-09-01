from django import template
from django.utils.safestring import mark_safe

from web.models import *

register = template.Library()

@register.simple_tag
def SetSelectBox2(cFlag, strSelValue, strSelMent, QUERY_OFFICE, strOption1, _hcb, _G_OFFICE_NO):

    _httpContextBase = _hcb
    G_OFFICE_NO = _G_OFFICE_NO
    sessionInfoVo = _httpContextBase.session.get("LoginInfo")

    rtnValue = ""
    strSql = ""

    if cFlag == "Comp_No":  # 업체
        strSql = " select 	a.office_no + a.comp_no as comp_no, 	a.comp_nm "
        strSql = strSql + "  from T_CP_200 a "
        strSql = strSql + " 			left join T_TO_100 b  on a.office_no = b.office_no "
        strSql = strSql + " where a.use_flag = 'Y' "
        strSql = strSql + "   and a.office_no = dbo.GetHeadOffice('" + G_OFFICE_NO + "') "
        strSql = strSql + " ORDER BY a.comp_nm"
    elif cFlag == "Comp_No1":   # 업체
        strSql = " select 	a.comp_no, 	a.comp_nm "
        strSql = strSql + "  from T_CP_200 a "
        strSql = strSql + " 			left join T_TO_100 b  on a.office_no = b.office_no "
        strSql = strSql + " where a.use_flag = 'Y' "
        strSql = strSql + "   and a.office_no = dbo.GetHeadOffice('" + G_OFFICE_NO + "') "
        strSql = strSql + " ORDER BY a.comp_nm"
    elif cFlag == "Office_No_ALL":  # 사이트 (오리지날, 관리지용 전체 다 보기)
        strSql = " 	select office_no comp_no, office_nm comp_nm "
        strSql = strSql + "  from t_to_100  "
        strSql = strSql + " where use_flag = 'Y' "
        strSql = strSql + " ORDER BY office_nm "
    elif cFlag == "Office_No":      # 사이트의 그룹내 사이트만 표시
        strSql = " 	select office_no comp_no, office_nm comp_nm "
        strSql = strSql + "  from V_TO_010  "
        strSql = strSql + " where head_office_no = dbo.GetHeadOffice('" + G_OFFICE_NO + "') "
        strSql = strSql + " ORDER BY office_no "
    elif cFlag == "CMS_OFFICE":     # 사이트의 그룹내 사이트만 표시
        strSql = " 	select office_no comp_no, office_nm comp_nm "
        strSql = strSql + "  from T_TO_200  "
        # strSql = strSql + " where cms_use_yn = 'Y' "
        strSql = strSql + " ORDER BY office_nm "
    elif cFlag == "FDESK_OFFICE_NO":    # 모든 OFFICE 표시
        strSql = " 	select office_no AS comp_no, office_no + ' '  + office_nm  AS comp_nm "
        strSql = strSql + "  from V_TO_101  "
        strSql = strSql + " ORDER BY office_nm "
    elif cFlag == "HQ_OFFICE":  # 사이트
        strSql = " select  b.office_no comp_no, b.office_nm comp_nm "
        strSql = strSql + "  from	t_mb_100 mb  "
        strSql = strSql + "  		join  t_to_100 a  on mb.office_no = a.office_no "
        strSql = strSql + "  		join  t_to_100 b  on a.office_no = b.head_office_no "
        strSql = strSql + " where mb.ostaff_id ='" + sessionInfoVo.LoginId + "' "
        # response.write strSql
    elif cFlag == "Country_Cd":     # 국가코드
        strSql = " select country_cd comp_no, country_cd+ ' - ' + country_nm comp_nm from t_cd_081 where use_flag = 'Y' order by country_CD "

    elif cFlag == "Rv_Status":      # 예약상태
        strSql = " select code comp_no, code_nm comp_nm from dbo.t_cd_100 where office_no = '" + G_OFFICE_NO + "' and code_grp = '18' and code <> '00' and use_flag = 'Y' order by sort_seq asc "

    elif cFlag == "Rv_Status_Enm":  # 예약상태
        strSql = " select code comp_no, code_enm comp_nm from dbo.t_cd_100 where office_no = '" + G_OFFICE_NO + "' and code_grp = '18' and code <> '00' and use_flag = 'Y' order by sort_seq asc "

    elif cFlag == "Agent":          # Agent
        strSql = " select comp_no, comp_nm  from dbo.t_cp_200 where office_no = dbo.GetHeadOffice('" + G_OFFICE_NO + "') and comp_type = '02' and use_flag = 'Y' order by comp_nm "

    elif cFlag == "Company":        # Company
        strSql = " select comp_no, comp_nm  from dbo.t_cp_200 where office_no = dbo.GetHeadOffice('" + G_OFFICE_NO + "') and contract_yn = 'Y' and use_flag = 'Y' order by comp_nm "

    elif cFlag == "Company2":       # Company over 9000000. (일반거래처)
        strSql = " select comp_no, comp_nm  from dbo.t_cp_200 where office_no = dbo.GetHeadOffice('" + G_OFFICE_NO + "') and contract_yn = 'Y' and use_flag = 'Y' and comp_no > '9000000' order by comp_nm "

    elif cFlag == "Company_All":    # Company
        strSql = " select comp_no, comp_nm  from dbo.t_cp_200 where office_no = dbo.GetHeadOffice('" + G_OFFICE_NO + "') and use_flag = 'Y' order by comp_nm "

    elif cFlag == "Rv_Type":        # 예약구분(확정,잠정, 대기, 블럭)
        strSql = " select code comp_no, code_nm comp_nm from dbo.t_cd_100 where office_no = '" + G_OFFICE_NO + "' and code_grp = '19' and code <> '00' and use_flag = 'Y' and value1 = 1 order by sort_seq asc "

    elif cFlag == "Rv_Type_Enm":    # 예약상태
        if QUERY_OFFICE == "":
            strSql = " select code comp_no, code_enm comp_nm from dbo.t_cd_100 where office_no = '" + G_OFFICE_NO + "' and code_grp = '19' and code <> '00' and use_flag = 'Y' and value1 = 1 order by sort_seq asc "
        else:
            strSql = " select code comp_no, code_enm comp_nm from dbo.t_cd_100 where office_no = '" + QUERY_OFFICE + "' and code_grp = '19' and code <> '00' and use_flag = 'Y' and value1 = 1 order by sort_seq asc "
    elif cFlag == "Travel_CD":      # 업체 직책 구분
        if QUERY_OFFICE == "":
            strSql = " select code comp_no, code_enm comp_nm from dbo.t_cd_100 where office_no = '" + G_OFFICE_NO + "' and code_grp = '24' and code <> '00' and use_flag = 'Y' "
        else:
            strSql = " select code comp_no, code_enm comp_nm from dbo.t_cd_100 where office_no = '" + QUERY_OFFICE + "' and code_grp = '24' and code <> '00' and use_flag = 'Y' "
    elif cFlag == "RATE_TYPE":      # Rate Type
        if QUERY_OFFICE == "":
            strSql = " select rate_type as comp_no, rate_type +'   '+ rate_nm as comp_nm  from v_th_107 where office_no = '" + G_OFFICE_NO + "' and use_flag = 'Y' ORDER BY SORT_SEQ, RATE_TYPE "
        else:   # 그룹호텔에서 그룹내 타호텔검색
            strSql = " select rate_type as comp_no, rate_type +'   '+ rate_nm as comp_nm  from v_th_107 where office_no = '" + QUERY_OFFICE + "' and use_flag = 'Y' ORDER BY SORT_SEQ, RATE_TYPE "
    elif cFlag == "RM_PAC_TYPE":    # RM / PAC
        strSql = "select code comp_no, code + ' ' + name comp_nm from dbo.v_rm_010 where office_no = '" + G_OFFICE_NO + "' and use_flag = 'Y' "

    elif cFlag == "RM_PAC_TYPE_HOUSE":  # (룸타입/패키지) + House_Account(ZZZ)
        # strSql = "select code comp_no, name comp_nm from dbo.v_rm_010 where office_no = '" + G_OFFICE_NO + "' and (use_flag = 'Y' or code = 'ZZZ') "

        if QUERY_OFFICE == "":
            strSql = "select code comp_no, code + ' ' + name comp_nm from dbo.v_rm_010 where office_no = '" + G_OFFICE_NO + "' and (use_flag = 'Y' or code = 'ZZZ' or code = 'YYY') order by sort_seq, code asc"   # ZZZ: 하우스어카운트  YYY: NP,CP 카운트용 룸
        else:   # 그룹호텔에서 그룹내 타호텔검색
            strSql = "select code comp_no, code + ' ' + name comp_nm from dbo.v_rm_010 where office_no = '" + QUERY_OFFICE + "' and (use_flag = 'Y' or code = 'ZZZ' or code = 'YYY') order by sort_seq, code asc " # 그룹내호텔에서 타호텔검색
    elif cFlag == "RM_TYPE":    # RM / PAC
        if QUERY_OFFICE == "":
            strSql = "select ROOM_TYPE comp_no, RTYPE_NM comp_nm from dbo.v_rm_010F where office_no = '" + G_OFFICE_NO + "'  "  # V_RM_010F <-- FDESK 룸타입
        else:
            strSql = "select ROOM_TYPE comp_no, RTYPE_NM comp_nm from dbo.v_rm_010F where office_no = '" + QUERY_OFFICE + "'  "  # V_RM_010F <-- FDESK 룸타입
    elif cFlag == "RM_TYPE2":   # RM / PAC
        if QUERY_OFFICE == "":
            strSql = "select ROOM_TYPE comp_no, (ROOM_TYPE + ' - ' + RTYPE_NM) comp_nm from dbo.v_rm_010F where office_no = '" + G_OFFICE_NO + "'  "
        else:
            strSql = "select ROOM_TYPE comp_no, (ROOM_TYPE + ' - ' + RTYPE_NM) comp_nm from dbo.v_rm_010F where office_no = '" + QUERY_OFFICE + "'  "
        # strSql = "select ROOM_TYPE comp_no, ROOM_TYPE comp_nm from dbo.v_rm_010   "

    elif cFlag == "RM_PAC_TYPE_CD":     # CODE_NAME RM / PAC
        if QUERY_OFFICE == "":
            strSql = "select code comp_no, code + ' ' + name comp_nm from dbo.v_rm_010 where office_no = '" + G_OFFICE_NO + "' and use_flag = 'Y' "
        else:   # 그룹호텔에서 그룹내 타호텔검색
            strSql = "select code comp_no, code + ' ' + name comp_nm from dbo.v_rm_010 where office_no = '" + QUERY_OFFICE + "' and use_flag = 'Y' "
    elif cFlag == "COMPLAINT_TYPE":     # 불평타입
        strSql = " select COMPLAINT_CD comp_no, COMPLAINT_NM comp_nm from dbo.t_th_117 where office_no = '" + G_OFFICE_NO + "' and use_flag = 'Y' order by SORT_SEQ, COMPLAINT_CD asc "

    elif cFlag == "COMPLAINT_STATUS":   # 불평상태
        strSql = " select code comp_no, code_nm comp_nm from dbo.t_cd_100 where office_no = '" + G_OFFICE_NO + "' and code_grp='36' and use_flag = 'Y' and code != '00' "

    elif cFlag == "room_floor":     # 층수정보
        strSql = " select distinct(rm_floor) comp_no, rm_floor comp_nm from dbo.t_rm_100 where use_flag = 'Y' and office_no = '" + G_OFFICE_NO + "'  "

    elif cFlag == "PMS_SVCCD":      # 부가서비스 정보
        strSql = "SELECT SERVICE_CD comp_no, SERVICE_NM comp_nm FROM V_TH_102 WHERE OFFICE_NO = '" + G_OFFICE_NO + "' AND USE_FLAG = 'Y'"

    elif cFlag == "PMS_RATETYPE":   # 레이트 타입 정보
        strSql = "SELECT RATE_TYPE comp_no, RATE_NM comp_nm FROM V_TH_107 WHERE OFFICE_NO = '" + G_OFFICE_NO + "' AND USE_FLAG = 'Y' order by sort_seq asc, rate_nm asc"

    elif cFlag == "PMS_PKGCD":      # 레이트 플랜 정보
        strSql = "SELECT PKG_CD comp_no, PKG_NM comp_nm FROM V_RM_020 WHERE OFFICE_NO = '" + G_OFFICE_NO + "' AND USE_FLAG = 'Y' ORDER BY PKG_NM ASC"

    elif cFlag == "RDESK_PKGCD":    # 레이트 플랜 정보
        strSql = "SELECT PKG_CD comp_no, PKG_NM comp_nm FROM V_RM_02R WHERE OFFICE_NO = '" + G_OFFICE_NO + "' AND USE_FLAG = 'Y' ORDER BY PKG_NM ASC"

    elif cFlag == "RLINK_PKGCD":    # XXXXX 정리해야함..
        strSql = "SELECT PKG_CD comp_no, PKG_NM comp_nm FROM V_RM_020 WHERE OFFICE_NO = '" + G_OFFICE_NO + "' AND USE_FLAG = 'Y' ORDER BY PKG_NM ASC"

    else:
        return ""
    tmpRs = dbexecuteQuery(strSql, '')
    print(tmpRs)
    if strSelMent != "":
        rtnValue = "<option	value=''>" + strSelMent + "</option>"
    # response.write tmpRs.RecordCount

    if not tmpRs:
        return rtnValue

    strSel = ""
    for t in tmpRs:
        if t["comp_no"] == strSelValue:
            strSel = " selected"
        else:
            strSel = ""

        rtnValue = rtnValue + "<option  value='" + t["comp_no"] + "'" + strSel + ">" + t["comp_nm"] + "</option>"

    return mark_safe(rtnValue)
