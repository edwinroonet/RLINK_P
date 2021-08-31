from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM031_U101VO = dict()
WCM031_U101VO.update(BaseVO)
WCM031_U101VO["RTYPE_IMGS"] = ""
WCM031_U101VO["RTYPE_IMGL"] = ""
WCM031_U101VO["smallImgName"] = ""
WCM031_U101VO["strExt"] = ""
WCM031_U101VO["largeImgName"] = ""
WCM031_U101VO["CMS_PLANCD"] = ""
WCM031_U101VO["RDESK_RMCD"] = ""
WCM031_U101VO["CMS_CD"] = ""
WCM031_U101VO["CMS_NM"] = ""
WCM031_U101VO["CMS_ENM"] = ""
WCM031_U101VO["OFFICE_NO"] = ""
WCM031_U101VO["CMS_SVCCD"] = ""
WCM031_U101VO["UNIT_AMT"] = ""
WCM031_U101VO["INCHARGE_NM"] = ""
WCM031_U101VO["CMS_SVCNM"] = ""
WCM031_U101VO["SERVICE_CD"] = ""
WCM031_U101VO["USE_FLAG"] = ""
WCM031_U101VO["remark"] = ""
WCM031_U101VO["strSql"] = ""
WCM031_U101VO["tproc"] = ""
WCM031_U101VO["Input_User"] = ""
WCM031_U101VO["Update_User"] = ""

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
        logger.debug(f'/CM/WCM031_U101 main, GET')

        paramVO = WCM031_U101VO
        paramVO["CMS_CD"] = RqChk("CMS_CD", request)
        if paramVO["CMS_CD"]:
            arrData = paramVO["CMS_CD"].split("|")
            paramVO["CMS_CD"] = arrData[0]
            paramVO["OFFICE_NO"] = arrData[1]
            paramVO["CMS_SVCCD"] = arrData[2]

        if not paramVO["OFFICE_NO"]:
            paramVO["OFFICE_NO"] = ViewData["G_OFFICE_NO"]

        if paramVO["CMS_SVCCD"]:
            paramVO["strSql"] = f"SCM031_U101 'Select','{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}','{paramVO['CMS_SVCCD']}'"
            rs = procSelect(paramVO["strSql"])

            if not rs:
                paramVO["tproc"] = "ADD"
                return HttpResponse(alertCloseMsg("No Select Data."))
            else:
                paramVO["tproc"] = "EDIT"
                paramVO["CMS_CD"] = rs["CMS_CD"]
                paramVO["CMS_ENM"] = rs["CMS_ENM"]
                paramVO["OFFICE_NO"] = rs["OFFICE_NO"]
                paramVO["CMS_SVCCD"] = rs["CMS_SVCCD"]
                paramVO["CMS_SVCNM"] = rs["CMS_SVCNM"]
                paramVO["UNIT_AMT"] = rs["UNIT_AMT"]
                paramVO["SERVICE_CD"] = rs["SERVICE_CD"]
                paramVO["USE_FLAG"] = rs["USE_FLAG"]
                paramVO["remark"] = rs["remark"]
                paramVO["Input_User"] = rs["INSERT_ID"] + "/" + rs["INSERT_DATE"]
                paramVO["Update_User"] = rs["UPDATE_ID"] + "/" + rs["UPDATE_DATE"]

        else:
            paramVO["tproc"] = "ADD"

        ViewData["resultVO"] = paramVO
        return render(request, 'CM/WCM031_U101.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM031_U101 main, POST')

        paramVO = WCM031_U101VO

        if paramVO:
            paramVO["CMS_CD"] = RqChk("CMS_CD", request)
            paramVO["USE_FLAG"] = RqChk("USE_FLAG", request)
            paramVO["remark"] = RqChk("remark", request)
            paramVO["tproc"] = RqChk("tproc", request)
            paramVO["OFFICE_NO"] = RqChk("OFFICE_NO", request)
            paramVO["CMS_SVCCD"] = RqChk("CMS_SVCCD", request)
            paramVO["CMS_SVCNM"] = RqChk("CMS_SVCNM", request)
            paramVO["SERVICE_CD"] = RqChk("SERVICE_CD", request)
            paramVO["UNIT_AMT"] = RqChk("UNIT_AMT", request).replace(",", "")

            strSql = f"SCM031_T101 '{paramVO['tproc']}','{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}','{paramVO['CMS_SVCCD']}','{paramVO['CMS_SVCNM']}','{paramVO['SERVICE_CD']}','{paramVO['remark']}','{paramVO['USE_FLAG']}','{ViewData['sessionInfo']['LoginId']}','{paramVO['UNIT_AMT']}'"
            rs = procTran(strSql)

            strOpenerUrl = "/CM/WCM031_S101"
            intResult = rs[0]
            strResult = rs[1]

            if intResult == 1:
                return HttpResponse(alertParentDialogCloseMsg2("" + strResult + "", "location.reload(true)"))
            else:
                return HttpResponse(alertMsg(strResult, ""))

        return render(request, 'CM/WCM031_U101.html', ViewData)

    return redirect('/')


def procSelect(strSql):
    return dbexecute(strSql)

def procTran(strSql):
    return dbexecute(strSql)
    