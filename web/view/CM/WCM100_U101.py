from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM100_U101VO = dict()
WCM100_U101VO.update(BaseVO)
WCM100_U101VO["CMS_CD"] = ""
WCM100_U101VO["CMS_NM"] = ""
WCM100_U101VO["CMS_ENM"] = ""
WCM100_U101VO["CONTRACT_YN"] = ""
WCM100_U101VO["OFFICE_NO"] = ""
WCM100_U101VO["CMS_HOTELCODE"] = ""
WCM100_U101VO["TEL_NO"] = ""
WCM100_U101VO["FAX_NO"] = ""
WCM100_U101VO["INCHARGE_NM"] = ""
WCM100_U101VO["CMS_SYSID"] = ""
WCM100_U101VO["CMS_USERID"] = ""
WCM100_U101VO["CMS_USERPWD"] = ""
WCM100_U101VO["CMS_USE_YN"] = ""
WCM100_U101VO["DENY_MODIFY_DAY"] = ""
WCM100_U101VO["DENY_CANCEL_DAY"] = ""
WCM100_U101VO["DEFAULT_RMTYPE"] = ""
WCM100_U101VO["DEFAULT_RMTYPE_YN"] = ""
WCM100_U101VO["remark"] = ""
WCM100_U101VO["strSql"] = ""
WCM100_U101VO["tproc"] = ""
WCM100_U101VO["Input_User"] = ""
WCM100_U101VO["Update_User"] = ""


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
        logger.debug(f'/CM/WCM100_U101 main, GET')

        paramVO = WCM100_U101VO
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
                paramVO["tproc"] = "EDIT"
                paramVO["CMS_CD"] = rs["CMS_CD"]
                paramVO["CMS_NM"] = rs["CMS_NM"]
                paramVO["CMS_ENM"] = rs["CMS_ENM"]
                paramVO["OFFICE_NO"] = rs["OFFICE_NO"]
                paramVO["CMS_HOTELCODE"] = rs["CMS_HOTELCODE"]
                paramVO["CMS_SYSID"] = rs["CMS_SYSID"]
                paramVO["CMS_USERID"] = rs["CMS_USERID"]
                paramVO["CMS_USERPWD"] = rs["CMS_USERPWD"]
                paramVO["DENY_MODIFY_DAY"] = rs["DENY_MODIFY_DAY"]
                paramVO["DENY_CANCEL_DAY"] = rs["DENY_CANCEL_DAY"]
                paramVO["DEFAULT_RMTYPE"] = rs["DEFAULT_RMTYPE"]
                paramVO["CMS_USE_YN"] = rs["CMS_USE_YN"]
                paramVO["remark"] = rs["REMARK"]
                paramVO["Input_User"] = rs["insert_id"] + "/" + rs["insert_date"]
                paramVO["Update_User"] = rs["update_id"] + "/" + rs["UPDATE_DATE"]
        else:
            paramVO["tproc"] = "ADD"

        paramVO["strSql"] = f"SELECT DEFAULT_RMTYPE_YN fROM DBO.T_TO_107 WHERE OFFICE_NO = '{ViewData['sessionInfo']['OfficeNo']}'"
        rs2 = procSelect(paramVO["strSql"])

        if rs2:
            paramVO["DEFAULT_RMTYPE_YN"] = rs2["DEFAULT_RMTYPE_YN"]

        ViewData["resultVO"] = paramVO
        return render(request, 'CM/WCM100_U101.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM100_U101 main, POST')

        paramVO = WCM100_U101VO

        if paramVO:
            paramVO["CMS_CD"] = RqChk("CMS_CD", request)
            paramVO["CMS_USE_YN"] = RqChk("CMS_USE_YN", request)
            paramVO["remark"] = RqChk("remark", request)
            paramVO["tproc"] = RqChk("tproc", request)
            paramVO["OFFICE_NO"] = RqChk("OFFICE_NO", request)
            paramVO["CMS_HOTELCODE"] = RqChk("CMS_HOTELCODE", request)
            paramVO["CMS_SYSID"] = RqChk("CMS_SYSID", request)
            paramVO["CMS_USERID"] = RqChk("CMS_USERID", request)
            paramVO["CMS_USERPWD"] = RqChk("CMS_USERPWD", request)
            paramVO["DENY_MODIFY_DAY"] = RqChk("DENY_MODIFY_DAY", request)
            paramVO["DENY_CANCEL_DAY"] = RqChk("DENY_CANCEL_DAY", request)
            paramVO["DEFAULT_RMTYPE"] = RqChk("DEFAULT_RMTYPE", request)

            strSql = f"SCM100_T101 '{paramVO['tproc']}','{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}','{paramVO['CMS_HOTELCODE']}','{paramVO['CMS_SYSID']}','{paramVO['CMS_USERID']}','{paramVO['CMS_USERPWD']}','{paramVO['remark']}','{paramVO['CMS_USE_YN']}','{ViewData['sessionInfo']['LoginId']}','{paramVO['DENY_MODIFY_DAY']}','{paramVO['DENY_CANCEL_DAY']}','{paramVO['DEFAULT_RMTYPE']}'"
            rs = procTran(strSql)

            strOpenerUrl = "/CM/WCM100_S101"
            intResult = rs[0]
            strResult = rs[1]

            if intResult == 1:
                return HttpResponse(alertParentDialogCloseMsg2("" + strResult + "", "location.reload(true)"))
            else:
                return HttpResponse(alertMsg(strResult, ""))

        return render(request, 'CM/WCM100_U101.html', ViewData)


    return redirect('/')


def procSelect(strSql):
    return dbexecuteQuery(strSql,'')[0]

def procTran(strSql):
    return dbexecute(strSql)
    