from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM021_U101VO = dict()
WCM021_U101VO.update(BaseVO)
WCM021_U101VO["CMS_CD"] = ""
WCM021_U101VO["OTA_CD"] = ""
WCM021_U101VO["OTA_NM"] = ""
WCM021_U101VO["OFFICE_NM"] = ""
WCM021_U101VO["CMS_NM"] = ""
WCM021_U101VO["CMS_ENM"] = ""
WCM021_U101VO["CONTRACT_YN"] = ""
WCM021_U101VO["OFFICE_NO"] = ""
WCM021_U101VO["COMP_NO"] = ""
WCM021_U101VO["COMP_NO2"] = ""
WCM021_U101VO["COMP_DIRECTPAY"] = ""
WCM021_U101VO["COMP_SPECIAL"] = ""
WCM021_U101VO["SPECIAL_MEMO"] = ""
WCM021_U101VO["COMP_NM"] = ""
WCM021_U101VO["COMP_NM2"] = ""
WCM021_U101VO["COMP_NM3"] = ""
WCM021_U101VO["CMS_HOTELCODE"] = ""
WCM021_U101VO["TEL_NO"] = ""
WCM021_U101VO["FAX_NO"] = ""
WCM021_U101VO["INCHARGE_NM"] = ""
WCM021_U101VO["CMS_SYSID"] = ""
WCM021_U101VO["CMS_USERID"] = ""
WCM021_U101VO["CMS_USERPWD"] = ""
WCM021_U101VO["CMS_USE_YN"] = ""
WCM021_U101VO["remark"] = ""
WCM021_U101VO["strSql"] = ""
WCM021_U101VO["AMT_FLAG"] = ""
WCM021_U101VO["AMT_FLAG2"] = ""
WCM021_U101VO["AMT_FLAG3"] = ""
WCM021_U101VO["ASSIGN"] = ""
WCM021_U101VO["tproc"] = ""
WCM021_U101VO["Input_User"] = ""
WCM021_U101VO["Update_User"] = ""
WCM021_U101VO["TL_SOCC"] = ""

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
        logger.debug(f'/CM/WCM021_U101 main, GET')

        paramVO = WCM021_U101VO
        paramVO["CMS_CD"] = RqChk("CMS_CD", request)
        paramVO["CMS_NM"] = RqChk("CMS_NM", request)
        paramVO["OFFICE_NO"] = RqChk("OFFICE_NO", request)
        paramVO["OFFICE_NM"] = RqChk("OFFICE_NM", request)
        paramVO["OTA_CD"] = RqChk("OTA_CD", request)
        paramVO["OTA_NM"] = RqChk("OTA_NM", request)
        paramVO["ASSIGN"] = RqChk("ASSIGN", request)
        paramVO["OFFICE_NO"] = RqChk("OFFICE_NO", request)

        if not paramVO["OFFICE_NO"]:
            paramVO["OFFICE_NO"] = ViewData["G_OFFICE_NO"]

        paramVO["TL_SOCC"] = RqChk("TL_SOCC", request)

        if paramVO["OTA_CD"]:
            paramVO["strSql"] = f"SCM021_U101 'Select','{paramVO['CMS_CD']}','{paramVO['OTA_CD']}','{paramVO['OFFICE_NO']}','{paramVO['TL_SOCC']}'"
            rs = procSelect(paramVO["strSql"])

            if not rs:
                paramVO["tproc"] = "ADD"
                return HttpResponse(alertCloseMsg("No Select Data."))
            else:
                paramVO["CMS_CD"] = rs["CMS_CD"]
                paramVO["CMS_NM"] = rs["CMS_NM"]
                paramVO["CMS_ENM"] = rs["CMS_ENM"]
                paramVO["COMP_NO"] = rs["COMP_NO"]
                paramVO["COMP_NM"] = rs["COMP_NM"]
                paramVO["COMP_DIRECTPAY"] = rs["COMP_DIRECTPAY"]
                paramVO["COMP_NM2"] = rs["COMP_NM2"]
                paramVO["COMP_SPECIAL"] = rs["COMP_SPECIAL"]
                paramVO["COMP_NM3"] = rs["COMP_NM3"]
                paramVO["SPECIAL_MEMO"] = rs["SPECIAL_MEMO"]
                paramVO["OTA_CD"] = rs["OTA_CD"]
                paramVO["TL_SOCC"] = rs["TL_SOCC"]

                if not paramVO["OTA_NM"]:
                    paramVO["OTA_NM"] = rs["OTA_NM"]

                paramVO["AMT_FLAG"] = rs["AMT_FLAG"]
                paramVO["AMT_FLAG2"] = rs["AMT_FLAG2"]
                paramVO["AMT_FLAG3"] = rs["AMT_FLAG3"]

                if paramVO["COMP_NO"] == "":
                    paramVO["tproc"] = "ADD"
                else:
                    paramVO["tproc"] = "EDIT"

                paramVO["remark"] = rs["REMARK"]
                paramVO["Input_User"] = rs["INSERT_ID"] + "/" + rs["INSERT_DATE"]
                paramVO["Update_User"] = rs["UPDATE_ID"] + "/" + rs["UPDATE_DATE"]

        else:
            paramVO["tproc"] = "ADD"

        ViewData["resultVO"] = paramVO
        return render(request, 'CM/WCM021_U101.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM021_U101 main, POST')

        paramVO = WCM021_U101VO

        if paramVO:
            paramVO["CMS_CD"] = RqChk("CMS_CD", request)
            paramVO["OTA_CD"] = RqChk("OTA_CD", request)
            paramVO["remark"] = RqChk("remark", request)
            paramVO["tproc"] = RqChk("tproc", request)
            paramVO["OFFICE_NO"] = RqChk("OFFICE_NO", request)
            paramVO["COMP_NO"] = RqChk("COMP_NO", request)
            paramVO["COMP_DIRECTPAY"] = RqChk("COMP_DIRECTPAY", request)
            paramVO["COMP_SPECIAL"] = RqChk("COMP_SPECIAL", request)
            paramVO["SPECIAL_MEMO"] = RqChk("SPECIAL_MEMO", request)
            paramVO["TL_SOCC"] = RqChk("TL_SOCC", request)
            paramVO["AMT_FLAG"] = RqChk("AMT_FLAG", request)
            paramVO["AMT_FLAG2"] = RqChk("AMT_FLAG2", request)
            paramVO["AMT_FLAG3"] = RqChk("AMT_FLAG3", request)
            paramVO["ASSIGN"] = RqChk("ASSIGN", request)

            strSql = f"SCM021_T101 '{paramVO['tproc']}','{paramVO['CMS_CD']}','{paramVO['OTA_CD']}','{paramVO['OFFICE_NO']}','{paramVO['COMP_NO']}','{paramVO['remark']}','{ViewData['sessionInfo']['LoginId']}','{paramVO['AMT_FLAG']}','{paramVO['COMP_DIRECTPAY']}','{paramVO['AMT_FLAG2']}','{paramVO['COMP_SPECIAL']}','{paramVO['AMT_FLAG3']}','{paramVO['SPECIAL_MEMO']}','{paramVO['TL_SOCC']}'"
            rs = procTran(strSql)

            strOpenerUrl = "/CM/WCM021_S101?CMS_CD=" + paramVO["CMS_CD"] + "&OFFICE_NO=" + paramVO["OFFICE_NO"] + "&ASSIGN=" + paramVO["ASSIGN"]
            intResult = rs[0]
            strResult = rs[1]

            if intResult == 1:
                return HttpResponse(alertParentDialogCloseMsg2("" + strResult + "", "location.reload(true)"))
            else:
                return HttpResponse(alertMsg(strResult, ""))

        return render(request, 'CM/WCM021_U101.html', ViewData)

    return redirect('/')


def procSelect(strSql):
    return dbexecute(strSql)

def procTran(strSql):
    return dbexecute(strSql)
    