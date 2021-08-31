from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM100_S101VO = dict()
WCM100_S101VO.update(BaseVO)
WCM100_S101VO["strSql"] = ""
WCM100_S101VO["recordcount"] = ""
WCM100_S101VO["recnum"] = ""
WCM100_S101VO["pagecount"] = ""
WCM100_S101VO["pagesize"] = ""
WCM100_S101VO["Gotopage"] = ""
WCM100_S101VO["CMS_USE_YN"] = ""
WCM100_S101VO["reservedUrlssl"] = ""
WCM100_S101VO["CMS_CD"] = ""
WCM100_S101VO["CMS_NM"] = ""
WCM100_S101VO["ex_sql"] = ""
WCM100_S101VO["ex_cond"] = ""
WCM100_S101VO["ex_title"] = ""
WCM100_S101VO["ex_head"] = ""
WCM100_S101VO["ex_datatype"] = ""
WCM100_S101VO["ex_column"] = ""
WCM100_S101VO["ex_page"] = ""
WCM100_S101VO["strTemp"] = ""
WCM100_S101VO["arrIdx"] = ""
WCM100_S101VO["intBound"] = ""
WCM100_S101VO["tProc"] = ""
WCM100_S101VO["strResult"] = ""
WCM100_S101VO["strOpenerUrl"] = ""
WCM100_S101VO["intResult"] = ""


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
        logger.debug(f'/CM/WCM100_S101 main, GET')

        paramVO = WCM100_S101VO
        paramVO["CMS_CD"] = RqChk("CMS_CD", request)

        if not paramVO["CMS_CD"]:
            paramVO["CMS_CD"] = ""

        paramVO["Gotopage"] = RqChk("gotopage", request)
        paramVO["pagesize"] = RqChk("pagesize", request)

        if not paramVO["pagesize"]:
            paramVO["pagesize"] = 20
        if not paramVO["Gotopage"]:
            paramVO["Gotopage"] = 1
        
        ViewData["strParam"] = "&CMS_CD=" + paramVO["CMS_CD"]

        ViewData["resultrs"] = procSelect(paramVO, ViewData)
        ViewData["resultVO"] = paramVO

        return render(request, 'CM/WCM100_S101.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM100_S101 main, POST')

        paramVO = WCM100_S101VO

        if paramVO:
            paramVO["strOpenerUrl"] = "/CM/WCM100_S101"
            paramVO["strTemp"] = RqChk("userIdx", request).replace(" ", "")
            paramVO["arrIdx"] = paramVO["strTemp"].split(",")
            paramVO["intBound"] = len(paramVO["arrIdx"])
            paramVO["tProc"] = "DEL"
            if paramVO["intBound"] >= 0:
                procTran(paramVO)
            else:
                paramVO["strResult"] = "선택하신 자료가 없습니다."
            return HttpResponse(alertMsg(paramVO["strResult"], paramVO["strOpenerUrl"]))

        return render(request, 'CM/WCM100_S101.html', ViewData)


    return redirect('/')


def procSelect(paramVO, ViewData):
    if paramVO:
        paramVO["strSql"] = f"SCM100_S101 {0},'{paramVO['Gotopage']}','{paramVO['pagesize']}','{ViewData['G_OFFICE_NO']}','{paramVO['CMS_CD']}'"
        rs = dbexecute(paramVO["strSql"])
        paramVO["recordcount"] = rs[0]
        paramVO["strSql"] = f"SCM100_S101 {1},'{paramVO['Gotopage']}','{paramVO['pagesize']}','{ViewData['G_OFFICE_NO']}','{paramVO['CMS_CD']}'"
        rs = dbexecute(paramVO["strSql"])

        paramVO["pagecount"] = (int(paramVO["recordcount"] - 1) /paramVO["pagesize"]) + 1
        paramVO["recnum"] = (paramVO["Gotopage"] - 1) * paramVO["pagesize"]

        # excel용 변수 정의 시작  (ex_sql에서 pagesize를 excel 최대한도인 65535 라인 설정 top 65535)===================================
        paramVO["ex_sql"] = f"SCM100_S101 {2},'{paramVO['Gotopage']}','{paramVO['pagesize']}','{ViewData['G_OFFICE_NO']}','{paramVO['CMS_CD']}'"
        paramVO["ex_sql"] = paramVO["ex_sql"].replace("'", "@^@")

        # 조회조건 적용을 위해 commonfunction1에 selectValue / selectValue1 정의됨.
        paramVO["ex_title"] = "Channel Code"   #'제목 , 없으면 프로그램명이 표시됨
        paramVO["ex_cond"] = "" #'검색조건 표시줄
        paramVO["ex_head"] = "Property@CMS Name@Hotel Code@Sys ID@User ID@Use@Insert@Insert Date"
        paramVO["ex_column"] = "OFFICE_NM@CMS_NM@CMS_HOTELCODE@CMS_SYSID@CMS_USERID@CMS_USE_YN@insert_id@insert_date"
        paramVO["ex_datatype"] = "0@0@0@0@0@0@0@0"  #'' 0:문자열 / 1:숫자(excel에서 합계에 사용)
        # excel용 변수 정의 끝============================================================================================================
        return rs
    return ""

def procTran(paramVO, ViewData):
    if paramVO:
        for i in range(0, len(paramVO["intBound"])):
            arrData = paramVO["arrIdx"][i].split("|")
            strSql = f"SCM100_T101 '{paramVO['tProc']}','{arrData[0]}','{arrData[1]}','','','','','','N','{ViewData['sessionInfo']['LoginId']}'"
            rs = dbexecute(paramVO["strSql"])

        paramVO["intResult"] = 1
        paramVO["strResult"] = "Data is deleted"
    return ""