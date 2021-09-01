from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM020_S101VO = dict()
WCM020_S101VO.update(BaseVO)
WCM020_S101VO["strSql"] = ""
WCM020_S101VO["recordcount"] = ""
WCM020_S101VO["recnum"] = ""
WCM020_S101VO["pagecount"] = ""
WCM020_S101VO["pagesize"] = ""
WCM020_S101VO["Gotopage"] = ""
WCM020_S101VO["use_flag"] = ""
WCM020_S101VO["reservedUrlssl"] = ""
WCM020_S101VO["CMS_CD"] = ""
WCM020_S101VO["OTA_NM"] = ""
WCM020_S101VO["ex_sql"] = ""
WCM020_S101VO["ex_cond"] = ""
WCM020_S101VO["ex_title"] = ""
WCM020_S101VO["ex_head"] = ""
WCM020_S101VO["ex_datatype"] = ""
WCM020_S101VO["ex_column"] = ""
WCM020_S101VO["ex_page"] = ""
WCM020_S101VO["strTemp"] = ""
WCM020_S101VO["arrIdx"] = ""
WCM020_S101VO["intBound"] = ""
WCM020_S101VO["tProc"] = ""
WCM020_S101VO["strResult"] = ""
WCM020_S101VO["strOpenerUrl"] = ""
WCM020_S101VO["intResult"] = ""


def main(request):
    ViewData = basemain(request)

    rstAuth = auth_fnChecking(request, ViewData["G_OFFICE_NO"], ViewData["G_COMP_NO"], ViewData["G_EMP_ID"], ViewData["G_SALESDATE"], ViewData)
    print(rstAuth)
    if rstAuth and rstAuth["resp"] == "redirect":
        return redirect(rstAuth["data"])
    elif rstAuth and rstAuth["resp"] == "HttpResponse":
        return HttpResponse(rstAuth["data"])

    rstAuth2 = auth_checkAuthSp(request, ViewData["G_OFFICE_NO"], ViewData["G_COMP_NO"], ViewData["G_EMP_ID"], ViewData["G_SALESDATE"], ViewData)
    print(rstAuth2)

    if request.method == 'GET':
        logger.debug(f'/CM/WCM020_S101 main, GET')

        paramVO = WCM020_S101VO
        paramVO["CMS_CD"] = RqChk("CMS_CD", request)
        paramVO["Gotopage"] = RqChk("gotopage", request)
        paramVO["pagesize"] = RqChk("pagesize", request)
        paramVO["strSort"] = RqChk("strSort", request)


        if not paramVO["CMS_CD"]:
        	paramVO["CMS_CD"] = GetCms_CD()


        paramVO["OTA_NM"] = RqChk("OTA_NM", request)
        if not paramVO["pagesize"]:
        	paramVO["pagesize"] = 30
        if not paramVO["Gotopage"]:
        	paramVO["Gotopage"] = 1
        if not paramVO["strSort"]:
        	paramVO["strSort"] = " A.USE_FLAG DESC , A.CMS_CD ASC "

        ViewData["OTA_CD"] = checkSort("OTA_CD desc", paramVO["strSort"])
        ViewData["OTA_NM"] = checkSort("OTA_NM desc", paramVO["strSort"])
        ViewData["CONTRACT_YN"] = checkSort("CONTRACT_YN desc", paramVO["strSort"])
        ViewData["OTA_TYPE_NM"] = checkSort("OTA_TYPE_NM desc", paramVO["strSort"])
        ViewData["AMT_FLAG_NM"] = checkSort("AMT_FLAG_NM desc", paramVO["strSort"])
        ViewData["USE_FLAG"] = checkSort("USE_FLAG desc", paramVO["strSort"])
        ViewData["tl_socc"] = checkSort("tl_socc desc", paramVO["strSort"])
        ViewData["strParam"] = "&CMS_CD=" + paramVO["CMS_CD"] + "&OTA_NM=" + paramVO["OTA_NM"]


        ViewData["resultrs"] = procSelect(paramVO)
        ViewData["resultVO"] = paramVO

        return render(request, 'CM/WCM020_S101.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM020_S101 main, POST')

        paramVO = WCM020_S101VO

        if paramVO:
            paramVO["strOpenerUrl"] = "/CM/WCM020_S101"
            paramVO["strTemp"] = RqChk("userIdx", request).replace(" ", "")
            paramVO["arrIdx"] = paramVO["strTemp"].split(",")
            paramVO["intBound"] = len(paramVO["arrIdx"])
            paramVO["tProc"] = "DEL"
            if paramVO["intBound"] >= 0:
            	procTran(paramVO)
            else:
            	paramVO["strResult"] = "선택하신 자료가 없습니다."
            return HttpResponse(alertMsg(paramVO["strResult"], paramVO["strOpenerUrl"]))

        return render(request, 'CM/WCM020_S101.html', ViewData)


    return redirect('/')


def procSelect(paramVO):
    if paramVO:
        paramVO["strSql"] = f"SCM020_S101 {0},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_CD']}','{paramVO['OTA_NM']}','{paramVO['strSort']}'"
        rs = dbexecute(paramVO["strSql"])
        paramVO["recordcount"] = rs[0]
        paramVO["strSql"] = f"SCM020_S101 {1},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_CD']}','{paramVO['OTA_NM']}','{paramVO['strSort']}'"
        rs = dbexecuteQuery(paramVO["strSql"], '')

        paramVO["pagecount"] = (int(paramVO["recordcount"] - 1) /paramVO["pagesize"]) + 1
        paramVO["recnum"] = (paramVO["Gotopage"] - 1) * paramVO["pagesize"]

        # excel용 변수 정의 시작  (ex_sql에서 pagesize를 excel 최대한도인 65535 라인 설정 top 65535)===================================
        paramVO["ex_sql"] = f"SCM020_S101 {2},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_CD']}','{paramVO['OTA_NM']}','{paramVO['strSort']}'"
        paramVO["ex_sql"] = paramVO["ex_sql"].replace("'", "@^@")

        # 조회조건 적용을 위해 commonfunction1에 selectValue / selectValue1 정의됨.
        paramVO["ex_title"] = "채널코드"   #'제목 , 없으면 프로그램명이 표시됨
        paramVO["ex_cond"] = "" #'검색조건 표시줄
        paramVO["ex_head"] = "OTA Code@OTA Name@Contarct@Type@Amt Flag@Use@Insert@Insert Date"
        paramVO["ex_column"] = "OTA_CD@OTA_NM@CONTRACT_YN@OTA_TYPE_NM@AMT_FLAG_NM@USE_FLAG@insert_id@insert_date"
        paramVO["ex_datatype"] = "0@0@0@0@0@0@0@0"  #'' 0:문자열 / 1:숫자(excel에서 합계에 사용)
        # excel용 변수 정의 끝============================================================================================================
        return rs
    return ""

def procTran(paramVO, ViewData):
    if paramVO:
        for i in range(0, len(paramVO["intBound"])):
            arrData = paramVO["arrIdx"][i].split("|")
            strSql = f"SCM020_T101 '{paramVO['tProc']}','{arrData[0]}','{arrData[1]}','','','','','','','','','','','','','N','','','','','','','{ViewData['sessionInfo']['LoginId']}'"
            rs = dbexecute(paramVO["strSql"])

        paramVO["intResult"]= 1
        paramVO["strResult"]= "선택하신 자료가 삭제 되었습니다."
    return ""
    