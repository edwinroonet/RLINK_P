from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM020_U101VO = dict()
WCM020_U101VO.update(BaseVO)
WCM020_U101VO["CMS_CD"] = ""
WCM020_U101VO["OTA_CD"] = ""
WCM020_U101VO["OTA_NM"] = ""
WCM020_U101VO["OTA_ENM"] = ""
WCM020_U101VO["CONTRACT_YN"] = ""
WCM020_U101VO["CONTRACT_START"] = ""
WCM020_U101VO["CONTRACT_END"] = ""
WCM020_U101VO["TEL_NO"] = ""
WCM020_U101VO["FAX_NO"] = ""
WCM020_U101VO["INCHARGE_NM"] = ""
WCM020_U101VO["INCHARGE_TEL"] = ""
WCM020_U101VO["INCHARGE_FAX"] = ""
WCM020_U101VO["INCHARGE_EMAIL"] = ""
WCM020_U101VO["OTA_TYPE"] = ""
WCM020_U101VO["AMT_FLAG"] = ""
WCM020_U101VO["use_flag"] = ""
WCM020_U101VO["remark"] = ""
WCM020_U101VO["TL_SOCC"] = ""
WCM020_U101VO["TL_SUPPORT1"] = ""
WCM020_U101VO["TL_SUPPORT2"] = ""
WCM020_U101VO["TL_SUPPORT3"] = ""
WCM020_U101VO["strSql"] = ""
WCM020_U101VO["strTemp"] = ""
WCM020_U101VO["arrIdx"] = ""
WCM020_U101VO["intBound"] = ""
WCM020_U101VO["tproc"] = ""
WCM020_U101VO["Input_User"] = ""
WCM020_U101VO["Update_User"] = ""


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
        logger.debug(f'/CM/WCM020_U101 main, GET')

        paramVO = WCM020_U101VO
        paramVO["CMS_CD"] = RqChk("CMS_CD", request)

        if paramVO["CMS_CD"]:
            paramVO["strTemp"] = RqChk("CMS_CD", request).replace(" ", "")
            paramVO["arrIdx"] = paramVO["strTemp"].split("|")
            paramVO["CMS_CD"] = paramVO["arrIdx"][0]
            paramVO["OTA_CD"] = paramVO["arrIdx"][1]
            paramVO["TL_SOCC"] = paramVO["arrIdx"][2]

        if paramVO["OTA_CD"]:
            paramVO["strSql"] = f"SCM020_U101 'Select','{paramVO['CMS_CD']}','{paramVO['OTA_CD']}','{paramVO['TL_SOCC']}'"
            rs = procSelect(paramVO["strSql"])

            if not rs:
                return HttpResponse(alertCloseMsg("No Select Data."))
            else:
                paramVO["tproc"] = "EDIT"
                paramVO["CMS_CD"] = rs["CMS_CD"]
                paramVO["OTA_CD"] = rs["OTA_CD"]
                paramVO["OTA_NM"] = rs["OTA_NM"]
                paramVO["CONTRACT_YN"] = rs["CONTRACT_YN"]
                paramVO["OTA_ENM"] = rs["OTA_ENM"]
                paramVO["CONTRACT_START"] = rs["CONTRACT_START"]
                paramVO["CONTRACT_END"] = rs["CONTRACT_END"]
                paramVO["TEL_NO"] = rs["TEL_NO"]
                paramVO["FAX_NO"] = rs["FAX_NO"]
                paramVO["INCHARGE_NM"] = rs["INCHARGE_NM"]
                paramVO["INCHARGE_TEL"] = rs["INCHARGE_TEL"]
                paramVO["INCHARGE_FAX"] = rs["INCHARGE_FAX"]
                paramVO["INCHARGE_EMAIL"] = rs["INCHARGE_EMAIL"]
                paramVO["TL_SOCC"] = rs["TL_SOCC"]
                paramVO["TL_SUPPORT1"] = rs["TL_SUPPORT1"]
                paramVO["TL_SUPPORT2"] = rs["TL_SUPPORT2"]
                paramVO["TL_SUPPORT3"] = rs["TL_SUPPORT3"]
                paramVO["OTA_TYPE"] = rs["OTA_TYPE"]
                paramVO["AMT_FLAG"] = rs["AMT_FLAG"]
                paramVO["use_flag"] = rs["USE_FLAG"]
                paramVO["remark"] = rs["REMARK"]
                paramVO["Input_User"] = rs["INSERT_ID"] + "/" + rs["INSERT_DATE"]
                paramVO["Update_User"] = rs["UPDATE_ID"] + "/" + rs["UPDATE_DATE"]
        else:
            paramVO["tproc"] = "ADD"

        ViewData["resultVO"] = paramVO
        return render(request, 'CM/WCM020_U101.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM020_U101 main, POST')

        paramVO = WCM020_U101VO

        if paramVO:
            paramVO["CMS_CD"] = RqChk("CMS_CD", request)
            paramVO["OTA_CD"] = RqChk("OTA_CD", request)
            paramVO["OTA_NM"] = RqChk("OTA_NM", request)
            paramVO["CONTRACT_YN"] = RqChk("CONTRACT_YN", request)
            paramVO["use_flag"] = RqChk("use_flag", request)
            paramVO["remark"] = RqChk("remark", request)
            paramVO["tproc"] = RqChk("tproc", request)
            paramVO["OTA_ENM"] = RqChk("OTA_ENM", request)
            paramVO["CONTRACT_START"] = RqChk("CONTRACT_START", request)
            paramVO["CONTRACT_END"] = RqChk("CONTRACT_END", request)
            paramVO["TEL_NO"] = RqChk("TEL_NO", request)
            paramVO["FAX_NO"] = RqChk("FAX_NO", request)
            paramVO["INCHARGE_NM"] = RqChk("INCHARGE_NM", request)
            paramVO["INCHARGE_TEL"] = RqChk("INCHARGE_TEL", request)
            paramVO["INCHARGE_FAX"] = RqChk("INCHARGE_FAX", request)
            paramVO["INCHARGE_EMAIL"] = RqChk("INCHARGE_EMAIL", request)
            paramVO["TL_SOCC"] = RqChk("TL_SOCC", request)
            paramVO["TL_SUPPORT1"] = RqChk("TL_SUPPORT1", request)
            paramVO["TL_SUPPORT2"] = RqChk("TL_SUPPORT2", request)
            paramVO["TL_SUPPORT3"] = RqChk("TL_SUPPORT3", request)
            paramVO["OTA_TYPE"] = RqChk("OTA_TYPE", request)
            paramVO["AMT_FLAG"] = RqChk("AMT_FLAG", request)

            strSql = f"SCM020_T101 '{paramVO['tproc']}','{paramVO['CMS_CD']}','{paramVO['OTA_CD']}','{paramVO['OTA_NM']}','{paramVO['OTA_ENM']}','{paramVO['CONTRACT_YN']}','{paramVO['CONTRACT_START']}','{paramVO['CONTRACT_END']}','{paramVO['TEL_NO']}','{paramVO['FAX_NO']}','{paramVO['INCHARGE_NM']}','{paramVO['INCHARGE_TEL']}','{paramVO['INCHARGE_FAX']}','{paramVO['INCHARGE_EMAIL']}','{paramVO['remark']}','{paramVO['use_flag']}','{paramVO['TL_SOCC']}','{paramVO['TL_SUPPORT1']}','{paramVO['TL_SUPPORT2']}','{paramVO['TL_SUPPORT3']}','{paramVO['OTA_TYPE']}','{paramVO['AMT_FLAG']}','{ViewData['sessionInfo']['LoginId']}'"
            rs = procTran(strSql)

            strOpenerUrl = "/CM/WCM020_S101"
            intResult = rs[0]
            strResult = rs[1]

            if intResult == 1:
                return HttpResponse(alertParentDialogCloseMsg2("" + strResult + "", "location.reload(true)"))
            else:
                return HttpResponse(alertMsg(strResult, ""))

        return render(request, 'CM/WCM020_U101.html', ViewData)


    return redirect('/')


def procSelect(strSql):
    return dbexecute(strSql)

def procTran(strSql):
    return dbexecute(strSql)
    