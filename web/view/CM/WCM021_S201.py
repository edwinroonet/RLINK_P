from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM021_S201VO = dict()
WCM021_S201VO.update(BaseVO)
WCM021_S201VO["strSql"] = ""
WCM021_S201VO["recordcount"] = ""
WCM021_S201VO["recnum"] = ""
WCM021_S201VO["pagecount"] = ""
WCM021_S201VO["pagesize"] = ""
WCM021_S201VO["Gotopage"] = ""
WCM021_S201VO["use_flag"] = ""
WCM021_S201VO["reservedUrlssl"] = ""
WCM021_S201VO["CMS_CD"] = ""
WCM021_S201VO["OFFICE_NO"] = ""
WCM021_S201VO["OTA_CD"] = ""
WCM021_S201VO["OTA_NM"] = ""
WCM021_S201VO["ASSIGN"] = ""
WCM021_S201VO["OPEN_URL"] = ""
WCM021_S201VO["ex_sql"] = ""
WCM021_S201VO["ex_cond"] = ""
WCM021_S201VO["ex_title"] = ""
WCM021_S201VO["ex_head"] = ""
WCM021_S201VO["ex_datatype"] = ""
WCM021_S201VO["ex_column"] = ""
WCM021_S201VO["ex_page"] = ""
WCM021_S201VO["strTemp"] = ""
WCM021_S201VO["arrIdx"] = ""
WCM021_S201VO["intBound"] = ""
WCM021_S201VO["tProc"] = ""
WCM021_S201VO["strResult"] = ""
WCM021_S201VO["strOpenerUrl"] = ""
WCM021_S201VO["intResult"] = ""


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
        logger.debug(f'/CM/WCM021_S201 main, GET')

        paramVO = WCM021_S201VO
        paramVO["CMS_CD"] = RqChk("CMS_CD", request)
        paramVO["OFFICE_NO"] = RqChk("OFFICE_NO", request)

        if not paramVO["CMS_CD"]:
            paramVO["CMS_CD"] = ""
        if paramVO["CMS_CD"] == "":
            paramVO["CMS_CD"] = GetCms_CD()

        if not paramVO["OFFICE_NO"]:
            paramVO["OFFICE_NO"] = ViewData["G_OFFICE_NO"]

        paramVO["pp"] = RqChk("pp", request)
        paramVO["OPEN_URL"] = RqChk("OPEN_URL", request)
        paramVO["OTA_CD"] = RqChk("OTA_CD", request)
        paramVO["OTA_NM"] = RqChk("OTA_NM", request)
        paramVO["ASSIGN"] = RqChk("ASSIGN", request)
        paramVO["Gotopage"] = RqChk("gotopage", request)
        paramVO["pagesize"] = RqChk("pagesize", request)

        if not paramVO["pagesize"]:
            paramVO["pagesize"] = 50
        if not paramVO["Gotopage"]:
            paramVO["Gotopage"] = 1

        ViewData["strParam"] = "&CMS_CD=" + paramVO["CMS_CD"] + "&OFFICE_NO=" + paramVO["OFFICE_NO"] + "&ASSIGN=" + paramVO["ASSIGN"] + "&OTA_CD=" + paramVO["OTA_CD"] + "&OTA_NM=" + paramVO["OTA_NM"] + "&OPEN_URL=" + paramVO["OPEN_URL"] +  "&pp=Y"

        ViewData["resultrs"] = procSelect(paramVO)
        ViewData["resultVO"] = paramVO

        return render(request, 'CM/WCM021_S201.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM021_S201 main, POST')

        paramVO = WCM021_S201VO

        if paramVO:
            paramVO["strOpenerUrl"] = "/CM/WCM021_S201"
            paramVO["strTemp"] = RqChk("userIdx", request).replace(" ", "")
            paramVO["arrIdx"] = paramVO["strTemp"].split(",")
            paramVO["intBound"] = len(paramVO["arrIdx"])
            paramVO["tProc"] = "DEL"
            if paramVO["intBound"] >= 0:
            	procTran(paramVO)
            else:
            	paramVO["strResult"] = "선택하신 자료가 없습니다."
            return HttpResponse(alertMsg(paramVO["strResult"], paramVO["strOpenerUrl"]))

        return render(request, 'CM/WCM021_S201.html', ViewData)


    return redirect('/')


def procSelect(paramVO):
    if paramVO:

        if paramVO["OPEN_URL"] == "WCM120_S101":
            paramVO["strSql"] = f"SCM021_S201 {10},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}','{paramVO['ASSIGN']}','{paramVO['OTA_CD']}','{paramVO['OTA_NM']}'"
        else:
            paramVO["strSql"] = f"SCM021_S201 {0},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}','{paramVO['ASSIGN']}','{paramVO['OTA_CD']}','{paramVO['OTA_NM']}'"
        rs = dbexecute(paramVO["strSql"])
        paramVO["recordcount"] = rs[0]

        if paramVO["OPEN_URL"] == "WCM120_S101":
            paramVO["strSql"] = f"SCM021_S201 {11},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}','{paramVO['ASSIGN']}','{paramVO['OTA_CD']}','{paramVO['OTA_NM']}'"
        else:
            paramVO["strSql"] = f"SCM021_S201 {1},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}','{paramVO['ASSIGN']}','{paramVO['OTA_CD']}','{paramVO['OTA_NM']}'"
        
        paramVO["pagecount"] = (int(paramVO["recordcount"] - 1) /paramVO["pagesize"]) + 1
        paramVO["recnum"] = (paramVO["Gotopage"] - 1) * paramVO["pagesize"]

        return rs
    return ""

def procTran(paramVO, ViewData):
    if paramVO:
        for i in range(0, len(paramVO["intBound"])):
            strSql = f"SCM021_T201 '{paramVO['tProc']}','','{paramVO['arrIdx'][i]}','','','','{ViewData['sessionInfo']['LoginId']}'"
            rs = dbexecute(paramVO["strSql"])

        paramVO["intResult"]= 1
        paramVO["strResult"]= "선택하신 자료가 삭제 되었습니다."
    return ""
    