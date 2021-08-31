from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM021_S101VO = dict()
WCM021_S101VO.update(BaseVO)
WCM021_S101VO["strSql"] = ""
WCM021_S101VO["recordcount"] = ""
WCM021_S101VO["recnum"] = ""
WCM021_S101VO["pagecount"] = ""
WCM021_S101VO["pagesize"] = ""
WCM021_S101VO["Gotopage"] = ""
WCM021_S101VO["use_flag"] = ""
WCM021_S101VO["reservedUrlssl"] = ""
WCM021_S101VO["CMS_CD"] = ""
WCM021_S101VO["OFFICE_NO"] = ""
WCM021_S101VO["ASSIGN"] = ""
WCM021_S101VO["OTA_CD"] = ""
WCM021_S101VO["OTA_NM"] = ""
WCM021_S101VO["strSort"] = ""
WCM021_S101VO["ex_sql"] = ""
WCM021_S101VO["ex_cond"] = ""
WCM021_S101VO["ex_title"] = ""
WCM021_S101VO["ex_head"] = ""
WCM021_S101VO["ex_datatype"] = ""
WCM021_S101VO["ex_column"] = ""
WCM021_S101VO["ex_page"] = ""
WCM021_S101VO["strTemp"] = ""
WCM021_S101VO["arrIdx"] = ""
WCM021_S101VO["intBound"] = ""
WCM021_S101VO["tProc"] = ""
WCM021_S101VO["strResult"] = ""
WCM021_S101VO["strOpenerUrl"] = ""
WCM021_S101VO["intResult"] = ""
WCM021_S101VO["TL_SOCC"] = ""


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
        logger.debug(f'/CM/WCM021_S101 main, GET')

        paramVO = WCM021_S101VO
        paramVO["CMS_CD"] = RqChk("CMS_CD", request)
        paramVO["OFFICE_NO"] = RqChk("OFFICE_NO", request)


        if not paramVO["CMS_CD"]:
            paramVO["CMS_CD"] = ""
        if paramVO["CMS_CD"] == "":
            paramVO["CMS_CD"] = GetCms_CD()

        if not paramVO["OFFICE_NO"]:
            paramVO["OFFICE_NO"] = ViewData["G_OFFICE_NO"]

        paramVO["ASSIGN"] = RqChk("ASSIGN", request)
        if not paramVO["ASSIGN"]:
            paramVO["ASSIGN"] = "1"

        paramVO["OTA_CD"] = RqChk("OTA_CD", request)
        paramVO["OTA_NM"] = RqChk("OTA_NM", request)
        paramVO["strSort"] = RqChk("strSort", request)
        paramVO["Gotopage"] = RqChk("gotopage", request)
        paramVO["pagesize"] = RqChk("pagesize", request)
        paramVO["TL_SOCC"] = RqChk("TL_SOCC", request)

        if not paramVO["pagesize"]:
            paramVO["pagesize"] = 50
        if not paramVO["Gotopage"]:
            paramVO["Gotopage"] = 1

        ViewData["OTA_CD"] = checkSort("OTA_CD desc", paramVO["strSort"])
        ViewData["OTA_NM"] = checkSort("OTA_NM desc", paramVO["strSort"])
        ViewData["TL_SOCC"] = checkSort("TL_SOCC desc", paramVO["strSort"])
        ViewData["COMP_NO"] = checkSort("COMP_NO desc", paramVO["strSort"])
        ViewData["COMP_NM"] = checkSort("COMP_NM desc", paramVO["strSort"])
        ViewData["COMP_DIRECTPAY"] = checkSort("COMP_DIRECTPAY desc", paramVO["strSort"])
        ViewData["COMP_SPECIAL"] = checkSort("COMP_SPECIAL desc", paramVO["strSort"])
        ViewData["AMT_FLAG"] = checkSort("AMT_FLAG desc", paramVO["strSort"])
        ViewData["entry_date"] = checkSort("entry_date desc", paramVO["strSort"])
        
        ViewData["strParam"] = "&CMS_CD=" + paramVO["CMS_CD"] + "&OFFICE_NO=" + paramVO["OFFICE_NO"] + "&ASSIGN=" + paramVO["ASSIGN"] + "&OTA_CD=" + paramVO["OTA_CD"] + "&OTA_NM=" + paramVO["OTA_NM"] + "&TL_SOCC=" + paramVO["TL_SOCC"]

        ViewData["resultrs"] = procSelect(paramVO)
        ViewData["resultVO"] = paramVO

        return render(request, 'CM/WCM021_S101.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM021_S101 main, POST')

        paramVO = WCM021_S101VO

        if paramVO:
            paramVO["strOpenerUrl"] = "/CM/WCM021_S101"
            paramVO["strTemp"] = RqChk("userIdx", request).replace(" ", "")
            paramVO["arrIdx"] = paramVO["strTemp"].split(",")
            paramVO["intBound"] = len(paramVO["arrIdx"])
            paramVO["tProc"] = "DEL"
            if paramVO["intBound"] >= 0:
            	procTran(paramVO)
            else:
            	paramVO["strResult"] = "There is no data."
            return HttpResponse(alertMsg(paramVO["strResult"], paramVO["strOpenerUrl"]))

        return render(request, 'CM/WCM021_S101.html', ViewData)


    return redirect('/')


def procSelect(paramVO):
    if paramVO:
        paramVO["strSql"] = f"SCM021_S101 {0},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}','{paramVO['ASSIGN']}','{paramVO['strSort']}','{paramVO['OTA_CD']}','{paramVO['OTA_NM']}'"
        rs = dbexecute(paramVO["strSql"])
        paramVO["recordcount"] = rs[0]
        paramVO["strSql"] = f"SCM021_S101 {1},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}','{paramVO['ASSIGN']}','{paramVO['strSort']}','{paramVO['OTA_CD']}','{paramVO['OTA_NM']}'"

        paramVO["pagecount"] = (int(paramVO["recordcount"] - 1) /paramVO["pagesize"]) + 1
        paramVO["recnum"] = (paramVO["Gotopage"] - 1) * paramVO["pagesize"]

        # excel용 변수 정의 시작  (ex_sql에서 pagesize를 excel 최대한도인 65535 라인 설정 top 65535)===================================
        paramVO["ex_sql"] = f"SCM021_S101 {2},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}','{paramVO['ASSIGN']}','{paramVO['strSort']}','{paramVO['OTA_CD']}','{paramVO['OTA_NM']}'"
        paramVO["ex_sql"] = paramVO["ex_sql"].replace("'", "@^@")

        # 조회조건 적용을 위해 commonfunction1에 selectValue / selectValue1 정의됨.
        paramVO["ex_title"] = "OTA Code"   #'제목 , 없으면 프로그램명이 표시됨
        paramVO["ex_cond"] = "" #'검색조건 표시줄
        paramVO["ex_head"] = "OTA Code@OTA Name@Account@Account Name@Account DP@Account Special@Amt Flag@Insert@Insert Date"
        paramVO["ex_column"] = "OTA_CD@OTA_NM@COMP_NO@COMP_NM@COMP_DIRECTPAY@COMP_SPECIAL@AMT_FLAG_NM@insert_id@insert_date"
        paramVO["ex_datatype"] = "0@0@0@0@0@0@0@0@0"  #'' 0:문자열 / 1:숫자(excel에서 합계에 사용)
        # excel용 변수 정의 끝============================================================================================================
        return rs
    return ""

def procTran(paramVO, ViewData):
    if paramVO:
        for i in range(0, len(paramVO["intBound"])):
            strSql = f"SCM021_T101 '{paramVO['tProc']}','','{paramVO['arrIdx'][i]}','','','','{ViewData['sessionInfo']['LoginId']}',''"
            rs = dbexecute(paramVO["strSql"])

        paramVO["intResult"]= 1
        paramVO["strResult"]= "Data is deleted."
    return ""