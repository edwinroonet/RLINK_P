from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM100_T103VO = dict()
WCM100_T103VO.update(BaseVO)
WCM100_T103VO["CMS_CD"] = ""
WCM100_T103VO["OFFICE_NO"] = ""
WCM100_T103VO["DESC_KOR"] = ""
WCM100_T103VO["DESC_ENG"] = ""
WCM100_T103VO["DESC_JPN"] = ""
WCM100_T103VO["DESC_CHN"] = ""
WCM100_T103VO["DESC_BUN"] = ""
WCM100_T103VO["FDEL"] = ""
WCM100_T103VO["DirectoryPath"] = ""
WCM100_T103VO["FileType"] = ""
WCM100_T103VO["strFileName"] = ""
WCM100_T103VO["strFileName2"] = ""
WCM100_T103VO["strFileName3"] = ""
WCM100_T103VO["bExist"] = ""
WCM100_T103VO["intResult"] = ""
WCM100_T103VO["strResult"] = ""
WCM100_T103VO["IMG_NM1"] = ""
WCM100_T103VO["IMG_NM2"] = ""
WCM100_T103VO["IMG_NM3"] = ""


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
        logger.debug(f'/CM/WCM100_T103 main, GET')

        paramVO = WCM100_T103VO
        paramVO["CMS_CD"] = RqChk("CMS_CD", request)
        paramVO["OFFICE_NO"] = RqChk("OFFICE_NO", request)
        paramVO["IMG_NM1"] = RqChk("txtFileNm", request)
        paramVO["IMG_NM2"] = RqChk("txtFileNm2", request)
        paramVO["IMG_NM3"] = RqChk("txtFileNm3", request)
        paramVO["DESC_KOR"] = RqChk("txtDESC_KOR", request)
        paramVO["DESC_ENG"] = RqChk("txtDESC_ENG", request)
        paramVO["DESC_CHN"] = RqChk("txtDESC_CHN", request)
        paramVO["DESC_JPN"] = RqChk("txtDESC_JPN", request)
        paramVO["DESC_BUN"] = RqChk("txtDESC_BUN", request)
        paramVO["DESC_KOR"] = ChkWordIn(paramVO["DESC_KOR"])
        paramVO["DESC_ENG"] = ChkWordIn(paramVO["DESC_ENG"])
        paramVO["DESC_CHN"] = ChkWordIn(paramVO["DESC_CHN"])
        paramVO["DESC_JPN"] = ChkWordIn(paramVO["DESC_JPN"])
        paramVO["DESC_BUN"] = ChkWordIn(paramVO["DESC_BUN"])
        
        FileVO = fnUpload(request, "pds_file", "")
        if FileVO["errCode"] == "0":
            paramVO["strFileName"] = FileVO["NewFileName"]
            paramVO["strFileName"] = paramVO["strFileName"].replace("!", "-")
            paramVO["strFileName"] = paramVO["strFileName"].replace("@", "-")
            paramVO["strFileName"] = paramVO["strFileName"].replace("#", "-")
            paramVO["strFileName"] = paramVO["strFileName"].replace("$", "-")
            paramVO["strFileName"] = paramVO["strFileName"].replace("%", "-")
            paramVO["strFileName"] = paramVO["strFileName"].replace("^", "-")
            paramVO["strFileName"] = paramVO["strFileName"].replace("&", "-")
            paramVO["strFileName"] = paramVO["strFileName"].replace("*", "-")

        if paramVO["strFileName"] == "":
            paramVO["strFileName"] = paramVO["IMG_NM1"]

        FileVO = fnUpload(request, "pds_file2", "")
        if FileVO["errCode"] == "0":
            paramVO["strFileName2"] = FileVO["NewFileName"]
            paramVO["strFileName2"] = paramVO["strFileName2"].replace("!", "-")
            paramVO["strFileName2"] = paramVO["strFileName2"].replace("@", "-")
            paramVO["strFileName2"] = paramVO["strFileName2"].replace("#", "-")
            paramVO["strFileName2"] = paramVO["strFileName2"].replace("$", "-")
            paramVO["strFileName2"] = paramVO["strFileName2"].replace("%", "-")
            paramVO["strFileName2"] = paramVO["strFileName2"].replace("^", "-")
            paramVO["strFileName2"] = paramVO["strFileName2"].replace("&", "-")
            paramVO["strFileName2"] = paramVO["strFileName2"].replace("*", "-")

        if paramVO["strFileName2"] == "":
            paramVO["strFileName2"] = paramVO["IMG_NM2"]

        FileVO = fnUpload(request, "pds_file3", "")
        if FileVO["errCode"] == "0":
            paramVO["strFileName3"] = FileVO["NewFileName"]
            paramVO["strFileName3"] = paramVO["strFileName3"].replace("!", "-")
            paramVO["strFileName3"] = paramVO["strFileName3"].replace("@", "-")
            paramVO["strFileName3"] = paramVO["strFileName3"].replace("#", "-")
            paramVO["strFileName3"] = paramVO["strFileName3"].replace("$", "-")
            paramVO["strFileName3"] = paramVO["strFileName3"].replace("%", "-")
            paramVO["strFileName3"] = paramVO["strFileName3"].replace("^", "-")
            paramVO["strFileName3"] = paramVO["strFileName3"].replace("&", "-")
            paramVO["strFileName3"] = paramVO["strFileName3"].replace("*", "-")

        if paramVO["strFileName3"] == "":
            paramVO["strFileName3"] = paramVO["IMG_NM3"]

        strOpenerUrl = "/CM/WCM100_S101"
        rs = procTran(paramVO, getSession(request, "LoginInfo")["LoginId"])
        paramVO["intResult"] = rs[0]
        paramVO["strResult"] = rs[1]

        if paramVO["intResult"] == 1:
            return HttpResponse(goOpenerLinkNew(paramVO["strResult"], strOpenerUrl))
        else:
            return HttpResponse(alertMsg(paramVO["strResult"], ""))

        return render(request, 'CM/WCM100_U103.html', ViewData)

    return redirect('/')



def procTran(paramVO, loginid):
    if paramVO:
        strSql = ("SCM100_T103 '" + paramVO["CMS_CD"] + "','" + paramVO["OFFICE_NO"] + "',   '" + paramVO["strFileName"] + "', '" + paramVO["strFileName2"] + "',      '" 
                    + paramVO["strFileName3"] + "',    '" + paramVO["DESC_KOR"] + "',    '" + paramVO["DESC_ENG"] + "',    '" + paramVO["DESC_JPN"] + "',  '" 
                    + paramVO["DESC_CHN"] + "',    '" + paramVO["DESC_BUN"] + "',  '" + loginid + "'")
        return dbexecute(strSql)
    return ""




