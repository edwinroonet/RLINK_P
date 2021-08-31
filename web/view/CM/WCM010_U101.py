from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM010_U101VO = dict()
WCM010_U101VO.update(BaseVO)
WCM010_U101VO["CMS_CD"] = ""
WCM010_U101VO["CMS_NM"] = ""
WCM010_U101VO["CMS_ENM"] = ""
WCM010_U101VO["CONTRACT_YN"] = ""
WCM010_U101VO["CONTRACT_START"] = ""
WCM010_U101VO["CONTRACT_END"] = ""
WCM010_U101VO["TEL_NO"] = ""
WCM010_U101VO["FAX_NO"] = ""
WCM010_U101VO["INCHARGE_NM"] = ""
WCM010_U101VO["INCHARGE_TEL"] = ""
WCM010_U101VO["INCHARGE_FAX"] = ""
WCM010_U101VO["INCHARGE_EMAIL"] = ""
WCM010_U101VO["use_flag"] = ""
WCM010_U101VO["remark"] = ""
WCM010_U101VO["strSql"] = ""
WCM010_U101VO["tproc"] = ""
WCM010_U101VO["Input_User"] = ""
WCM010_U101VO["Update_User"] = ""
WCM010_U101VO["ROOMTYPE_API"] = ""
WCM010_U101VO["SERVER_IP"] = ""
WCM010_U101VO["SERVER_PORT"] = ""
WCM010_U101VO["CATALOG"] = ""
WCM010_U101VO["USER_ID2"] = ""
WCM010_U101VO["USER_PWD"] = ""
WCM010_U101VO["API_URL"] = ""



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
        logger.debug(f'/CM/WCM010_U101 main, GET')

        paramVO = WCM010_U101VO
        paramVO["CMS_CD"] = RqChk("CMS_CD", request)

        if paramVO["CMS_CD"]:
            paramVO["strSql"] = f"SCM010_U101 '{'Select'}','{paramVO['CMS_CD']}'"
            rs = procSelect(paramVO["strSql"])

            if not rs:
                return HttpResponse(alertCloseMsg("No Select Data."))
            else:
                paramVO["tproc"] = "EDIT"
                paramVO["CMS_NM"] = rs["CMS_NM"]
                paramVO["CONTRACT_YN"] = rs["CONTRACT_YN"]
                paramVO["CMS_ENM"] = rs["CMS_ENM"]
                paramVO["CONTRACT_START"] = rs["CONTRACT_START"]
                paramVO["CONTRACT_END"] = rs["CONTRACT_END"]
                paramVO["TEL_NO"] = rs["TEL_NO"]
                paramVO["FAX_NO"] = rs["FAX_NO"]
                paramVO["INCHARGE_NM"] = rs["INCHARGE_NM"]
                paramVO["INCHARGE_TEL"] = rs["INCHARGE_TEL"]
                paramVO["INCHARGE_FAX"] = rs["INCHARGE_FAX"]
                paramVO["INCHARGE_EMAIL"] = rs["INCHARGE_EMAIL"]

                paramVO["ROOMTYPE_API"] = rs["ROOMTYPE_API"]
                paramVO["SERVER_IP"] = rs["SERVER_IP"]
                paramVO["SERVER_PORT"] = rs["SERVER_PORT"]
                paramVO["CATALOG"] = rs["CATALOG"]
                paramVO["USER_ID2"] = rs["USER_ID"]
                paramVO["USER_PWD"] = rs["USER_PWD"]
                paramVO["API_URL"] = rs["API_URL"]
                paramVO["use_flag"] = rs["USE_FLAG"]
                paramVO["remark"] = rs["REMARK"]
                paramVO["Input_User"] = rs["INSERT_ID"] + "/" + rs["INSERT_DATE"]
                paramVO["Update_User"] = rs["UPDATE_ID"] + "/" + rs["UPDATE_DATE"]
        else:
            paramVO["tproc"] = "ADD"


        ViewData["resultVO"] = paramVO

        return render(request, 'CM/WCM010_U101.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM010_U101 main, POST')

        paramVO = WCM010_U101VO

        if paramVO:

            paramVO["CMS_CD"] = RqChk("CMS_CD", request)
            paramVO["CMS_NM"] = RqChk("CMS_NM", request)
            paramVO["CONTRACT_YN"] = RqChk("CONTRACT_YN", request)
            paramVO["use_flag"] = RqChk("use_flag", request)
            paramVO["remark"] = RqChk("remark", request)
            paramVO["tproc"] = RqChk("tproc", request)
            paramVO["CMS_ENM"] = RqChk("CMS_ENM", request)
            paramVO["CONTRACT_START"] = RqChk("CONTRACT_START", request)
            paramVO["CONTRACT_END"] = RqChk("CONTRACT_END", request)
            paramVO["TEL_NO"] = RqChk("TEL_NO", request)
            paramVO["FAX_NO"] = RqChk("FAX_NO", request)
            paramVO["INCHARGE_NM"] = RqChk("INCHARGE_NM", request)
            paramVO["INCHARGE_TEL"] = RqChk("INCHARGE_TEL", request)
            paramVO["INCHARGE_FAX"] = RqChk("INCHARGE_FAX", request)
            paramVO["INCHARGE_EMAIL"] = RqChk("INCHARGE_EMAIL", request)
            paramVO["ROOMTYPE_API"] = RqChk("ROOMTYPE_API", request)
            paramVO["SERVER_IP"] = RqChk("SERVER_IP", request)
            paramVO["SERVER_PORT"] = RqChk("SERVER_PORT", request)
            paramVO["CATALOG"] = RqChk("CATALOG", request)
            paramVO["USER_ID2"] = RqChk("USER_ID2", request)
            paramVO["USER_PWD"] = RqChk("USER_PWD", request)
            paramVO["API_URL"] = RqChk("API_URL", request)

            LoginId = ViewData["sessionInfo"]["LoginId"]

            strSql = f"SCM010_T101 '{paramVO['tproc']}','{paramVO['CMS_CD']}','{paramVO['CMS_NM']}','{paramVO['CMS_ENM']}','{paramVO['CONTRACT_YN']}','{paramVO['CONTRACT_START']}','{paramVO['CONTRACT_END']}','{paramVO['TEL_NO']}','{paramVO['FAX_NO']}','{paramVO['INCHARGE_NM']}','{paramVO['INCHARGE_TEL']}','{paramVO['INCHARGE_FAX']}','{paramVO['INCHARGE_EMAIL']}','{paramVO['remark']}','{paramVO['use_flag']}','{LoginId}','{paramVO['ROOMTYPE_API']}','{paramVO['SERVER_IP']}','{paramVO['SERVER_PORT']}','{paramVO['CATALOG']}','{paramVO['USER_ID2']}','{paramVO['USER_PWD']}','{paramVO['API_URL']}'"
            rs = procTran(strSql)
            strOpenerUrl = "/CM/WCM010_S101"
            intResult = rs[0]
            strResult = rs[1]

            if intResult == 1:
                return HttpResponse(alertParentDialogCloseMsg2("" + strResult + "", "location.reload(true)"))
            else:
                return HttpResponse(alertMsg(strResult, ""))

        return render(request, 'CM/WCM010_U101.html', ViewData)


    return redirect('/')


def procSelect(strSql):
    return dbexecute(strSql)

def procTran(strSql):
    return dbexecute(strSql)