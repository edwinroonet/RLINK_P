from django.shortcuts import render, redirect
import json, os
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM100_U103VO = dict()
WCM100_U103VO.update(BaseVO)
WCM100_U103VO["IMG_NM1"] = ""
WCM100_U103VO["IMG_NM2"] = ""
WCM100_U103VO["IMG_NM3"] = ""
WCM100_U103VO["CMS_CD"] = ""
WCM100_U103VO["OFFICE_NO"] = ""
WCM100_U103VO["DESC_KOR"] = ""
WCM100_U103VO["DESC_ENG"] = ""
WCM100_U103VO["DESC_JPN"] = ""
WCM100_U103VO["DESC_CHN"] = ""
WCM100_U103VO["DESC_BUN"] = ""
WCM100_U103VO["strFileName"] = ""
WCM100_U103VO["strFileName2"] = ""
WCM100_U103VO["strFileName3"] = ""
WCM100_U103VO["strSql"] = ""



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
        logger.debug(f'/CM/WCM100_U103 main, GET')

        paramVO = WCM100_U103VO
        paramVO["CMS_CD"] = RqChk("CMS_CD", request)

        if paramVO["CMS_CD"]:
            paramVO["strTemp"] = RqChk("CMS_CD", request).replace(" ", "")
            paramVO["arrIdx"] = paramVO["strTemp"].split("|")
            paramVO["CMS_CD"] = paramVO["arrIdx"][0]
            paramVO["OFFICE_NO"] = paramVO["arrIdx"][1]

        if not paramVO["OFFICE_NO"]:
            paramVO["OFFICE_NO"] = ViewData["G_OFFICE_NO"]

        if paramVO["CMS_CD"]:
            paramVO["strSql"] = f"SCM100_U101 'Select','{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}'"
            rs = procSelect(paramVO["strSql"])

            if not rs:
                return HttpResponse(alertCloseMsg("No Select Data."))
            else:
                ViewData["resultrs"] = rs
                paramVO["DESC_KOR"] = rs["DESC_KOR"]
                paramVO["DESC_ENG"] = rs["DESC_ENG"]
                paramVO["DESC_JPN"] = rs["DESC_JPN"]
                paramVO["DESC_CHN"] = rs["DESC_CHN"]
                paramVO["DESC_BUN"] = rs["DESC_BUN"]
                paramVO["IMG_NM1"] = rs["IMG_NM1"]
                paramVO["IMG_NM2"] = rs["IMG_NM2"]
                paramVO["IMG_NM3"] = rs["IMG_NM3"]

        ViewData["resultVO"] = paramVO
        return render(request, 'CM/WCM100_U103.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM100_U103 main, POST')

        paramVO = WCM100_U103VO

        if paramVO:
            paramVO["CMS_CD"] = RqChk("CMS_CD", request)
            paramVO["OFFICE_NO"] = RqChk("OFFICE_NO", request)

            strReturn = procDelete(paramVO, request, ViewData)

            return HttpResponse(alertMsg(strReturn, "/CM/WCM100_U101/?pp=Y&CMS_CD=" + paramVO["CMS_CD"] + "&OFFICE_NO=" + paramVO["OFFICE_NO"]))

    return redirect('/')


def procSelect(strSql):
    return dbexecuteQuery(strSql,'')[0]

def procDelete(paramVO, request, ViewData):
    DirectoryPath = "Data/EData/" + ViewData["G_OFFICE_NO"]
    strReturn = ""

    fsq = RqChk("fsq", request)
    if fsq == "1":
        strSql = " SELECT IMG_NM1 "
    elif fsq == "2":
        strSql = " SELECT IMG_NM2 "
    else:
        strSql = " SELECT IMG_NM3 "
    strSql = strSql + " FROM T_CM_100 "
    strSql = strSql + " WHERE OFFICE_NO = '" + ViewData["G_OFFICE_NO"] + "' and CMS_CD = '" + paramVO["CMS_CD"] + "' "
    rs = dbexecute(strSql)

    if rs:
        DeleteFile = rs[0]
        if DeleteFile:
            if os.path.isfile(DirectoryPath + "/" + DeleteFile):
                try:
                    os.remove(DirectoryPath + "/" + DeleteFile)
                    strSql = " UPDATE T_CM_100 "

                    if fsq == "1":
                        strSql = " SET IMG_NM1 = ''"
                    elif fsq == "2":
                        strSql = " SET IMG_NM2 = ''"
                    else:
                        strSql = " SET IMG_NM3 = ''"
                    strSql = strSql + " WHERE OFFICE_NO = '" + ViewData["G_OFFICE_NO"] + "' and CMS_CD = '" + paramVO["CMS_CD"] + "' "
                    rs = dbexecute(strSql)
                    strReturn = "Files have been deleted."

                except Exception as e:
                    strReturn = "During deleting files, error occured."
                    logger.exception(f'WCM100_U103 {strReturn} error : {e}')
    return strReturn