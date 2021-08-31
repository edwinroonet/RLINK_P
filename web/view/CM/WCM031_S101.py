from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM031_S101VO = dict()
WCM031_S101VO.update(BaseVO)
WCM031_S101VO["strSql"] = ""
WCM031_S101VO["recordcount"] = ""
WCM031_S101VO["recnum"] = ""
WCM031_S101VO["pagecount"] = ""
WCM031_S101VO["pagesize"] = ""
WCM031_S101VO["Gotopage"] = ""
WCM031_S101VO["USE_FLAG"] = ""
WCM031_S101VO["CMS_CD"] = ""
WCM031_S101VO["OFFICE_NO"] = ""
WCM031_S101VO["CMS_NM"] = ""
WCM031_S101VO["ApiLastUpdateDate"] = ""
WCM031_S101VO["ex_sql"] = ""
WCM031_S101VO["ex_cond"] = ""
WCM031_S101VO["ex_title"] = ""
WCM031_S101VO["ex_head"] = ""
WCM031_S101VO["ex_datatype"] = ""
WCM031_S101VO["ex_column"] = ""
WCM031_S101VO["ex_page"] = ""
WCM031_S101VO["strTemp"] = ""
WCM031_S101VO["arrIdx"] = ""
WCM031_S101VO["intBound"] = ""
WCM031_S101VO["tProc"] = ""
WCM031_S101VO["strResult"] = ""
WCM031_S101VO["strOpenerUrl"] = ""
WCM031_S101VO["intResult"] = ""


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
        logger.debug(f'/CM/WCM031_S101 main, GET')

        paramVO = WCM031_S101VO
        paramVO["CMS_CD"] = RqChk("CMS_CD", request)
        paramVO["OFFICE_NO"] = RqChk("OFFICE_NO", request)

        if not paramVO["CMS_CD"]:
            paramVO["CMS_CD"] = ""

        if not paramVO["OFFICE_NO"]:
            paramVO["OFFICE_NO"] = ViewData["G_OFFICE_NO"]

        paramVO["Gotopage"] = RqChk("gotopage", request)
        paramVO["pagesize"] = RqChk("pagesize", request)

        if not paramVO["pagesize"]:
            paramVO["pagesize"] = 50
        if not paramVO["Gotopage"]:
            paramVO["Gotopage"] = 1
        
        ViewData["strParam"] = "&CMS_CD=" + paramVO["CMS_CD"] + "&OFFICE_NO=" + paramVO["OFFICE_NO"]

        ViewData["resultrs"] = procSelect(paramVO)
        ViewData["resultVO"] = paramVO

        return render(request, 'CM/WCM031_S101.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM031_S101 main, POST')

        paramVO = WCM031_S101VO

        if paramVO:
            paramVO["strOpenerUrl"] = "/CM/WCM031_S101"
            paramVO["strTemp"] = RqChk("userIdx", request).replace(" ", "")
            paramVO["arrIdx"] = paramVO["strTemp"].split(",")
            paramVO["intBound"] = len(paramVO["arrIdx"])
            paramVO["tProc"] = "DEL"
            if paramVO["intBound"] >= 0:
                procTran(paramVO)
            else:
                paramVO["strResult"] = "선택하신 자료가 없습니다."
            return HttpResponse(alertMsg(paramVO["strResult"], paramVO["strOpenerUrl"]))

        return render(request, 'CM/WCM031_S101.html', ViewData)


    return redirect('/')


def procSelect(paramVO):
    if paramVO:
        paramVO["strSql"] = f"SCM031_S101 {0},'{paramVO['Gotopage']}','{paramVO['pagesize']}','{paramVO['OFFICE_NO']}','{paramVO['CMS_CD']}'"
        rs = dbexecute(paramVO["strSql"])
        paramVO["recordcount"] = rs[0]
        paramVO["strSql"] = f"SCM031_S101 {3},'{paramVO['Gotopage']}','{paramVO['pagesize']}','{paramVO['OFFICE_NO']}','{paramVO['CMS_CD']}'"
        rs = dbexecute(paramVO["strSql"])
        if rs:
            paramVO["ApiLastUpdateDate"] = rs[0]
        paramVO["strSql"] = f"SCM031_S101 {1},'{paramVO['Gotopage']}','{paramVO['pagesize']}','{paramVO['OFFICE_NO']}','{paramVO['CMS_CD']}'"

        paramVO["pagecount"] = (int(paramVO["recordcount"] - 1) /paramVO["pagesize"]) + 1
        paramVO["recnum"] = (paramVO["Gotopage"] - 1) * paramVO["pagesize"]

        # excel용 변수 정의 시작  (ex_sql에서 pagesize를 excel 최대한도인 65535 라인 설정 top 65535)===================================
        paramVO["ex_sql"] = f"SCM031_S101 {2},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}','{paramVO['CMS_CD']}'"
        paramVO["ex_sql"] = paramVO["ex_sql"].replace("'", "@^@")

        # 조회조건 적용을 위해 commonfunction1에 selectValue / selectValue1 정의됨.
        paramVO["ex_title"] = "CMS 마스터룸타입"   #'제목 , 없으면 프로그램명이 표시됨
        paramVO["ex_cond"] = "" #'검색조건 표시줄
        paramVO["ex_head"] = "CMS Master Ext.CD@Master Ext.Name@PMS Ext.CD@PMS Ext.Name@Use@Entry@Update"
        paramVO["ex_column"] = "CMS_SVCCD@CMS_SVCNM@SERVICE_CD@SERVICE_NM@USE_FLAG@insert_date@update_date"
        paramVO["ex_datatype"] = "0@0@0@0@0@0@0"  #'' 0:문자열 / 1:숫자(excel에서 합계에 사용)
        # excel용 변수 정의 끝============================================================================================================
        return rs
    return ""

def procTran(paramVO, ViewData):
    if paramVO:
        for i in range(0, len(paramVO["intBound"])):
            arrData = paramVO["arrIdx"][i].split("|")
            strSql = f"SCM031_T101 '{paramVO['tProc']}','{arrData[0]}','{arrData[1]}','{arrData[2]}','','','','','N','{ViewData['sessionInfo']['LoginId']}'"
            rs = dbexecute(paramVO["strSql"])

        paramVO["intResult"] = 1
        paramVO["strResult"] = "선택하신 자료가 삭제 되었습니다."
    return ""