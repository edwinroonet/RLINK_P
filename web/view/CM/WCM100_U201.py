from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM100_U201VO = dict()
WCM100_U201VO.update(BaseVO)
WCM100_U201VO["CMS_CD"] = ""
WCM100_U201VO["CMS_NM"] = ""
WCM100_U201VO["CMS_ENM"] = ""
WCM100_U201VO["CONTRACT_YN"] = ""
WCM100_U201VO["CCINFO_TYPE"] = ""
WCM100_U201VO["OFFICE_NO"] = ""
WCM100_U201VO["CMS_HOTELCODE"] = ""
WCM100_U201VO["TEL_NO"] = ""
WCM100_U201VO["FAX_NO"] = ""
WCM100_U201VO["INCHARGE_NM"] = ""
WCM100_U201VO["CMS_SYSID"] = ""
WCM100_U201VO["CMS_USERID"] = ""
WCM100_U201VO["CMS_USERPWD"] = ""
WCM100_U201VO["CMS_USE_YN"] = ""
WCM100_U201VO["remark"] = ""
WCM100_U201VO["strSql"] = ""
WCM100_U201VO["tproc"] = ""
WCM100_U201VO["Input_User"] = ""
WCM100_U201VO["Update_User"] = ""
WCM100_U201VO["DENY_MODIFY_DAY"] = ""
WCM100_U201VO["DENY_CANCEL_DAY"] = ""
WCM100_U201VO["RSVN_ADD"] = ""
WCM100_U201VO["RSVN_UPDATE"] = ""
WCM100_U201VO["RSVN_CANCEL"] = ""
WCM100_U201VO["CMS_UPD_TYPE"] = ""
WCM100_U201VO["API_AUTOBATCH"] = ""
WCM100_U201VO["PMS_RATETYPE"] = ""


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
        logger.debug(f'/CM/WCM100_U201 main, GET')

        paramVO = WCM100_U201VO
        paramVO["CMS_CD"] = RqChk("CMS_CD", request)

        if paramVO["CMS_CD"]:
            paramVO["strTemp"] = RqChk("CMS_CD", request).replace(" ", "")
            paramVO["arrIdx"] = paramVO["strTemp"].split("|")
            paramVO["CMS_CD"] = paramVO["arrIdx"][0]
            paramVO["OFFICE_NO"] = paramVO["arrIdx"][1]

        if not paramVO["OFFICE_NO"]:
            paramVO["OFFICE_NO"] = ViewData["G_OFFICE_NO"]

        if paramVO["CMS_CD"]:
            paramVO["strSql"] = f"SCM100_U201 'Select','{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}'"
            rs = procSelect(paramVO["strSql"])

            if not rs:
                #return HttpResponse(alertCloseMsg("No Select Data."))
                paramVO["tproc"] = "ADD"
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
                paramVO["RSVN_ADD"] = rs["RSVN_ADD"]
                paramVO["RSVN_UPDATE"] = rs["RSVN_UPDATE"]
                paramVO["RSVN_CANCEL"] = rs["RSVN_CANCEL"]
                paramVO["API_AUTOBATCH"] = rs["API_AUTOBATCH"]
                paramVO["PMS_RATETYPE"] = rs["PMS_RATETYPE"]
                paramVO["CMS_USE_YN"] = rs["CMS_USE_YN"]
                paramVO["USE_YN"] = rs["USE_YN"]
                paramVO["CMS_UPD_TYPE"] = rs["CMS_UPD_TYPE"]
                paramVO["remark"] = rs["REMARK"]
                paramVO["Input_User"] = rs["INSERT_ID"] + "/" + rs["INSERT_DATE"]
                paramVO["Update_User"] = rs["UPDATE_ID"] + "/" + rs["UPDATE_DATE"]
                paramVO["CCINFO_TYPE"] = rs["CCINFO_TYPE"]
        else:
            paramVO["tproc"] = "ADD"

        ViewData["resultVO"] = paramVO
        return render(request, 'CM/WCM100_U201.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM100_U201 main, POST')

        paramVO = WCM100_U201VO

        if paramVO:
            paramVO["CMS_CD"] = RqChk("CMS_CD", request)
            paramVO["CMS_USE_YN"] = RqChk("CMS_USE_YN", request)
            paramVO["USE_YN"] = RqChk("USE_YN", request)
            paramVO["remark"] = RqChk("remark", request)
            paramVO["tproc"] = RqChk("tproc", request)
            paramVO["OFFICE_NO"] = RqChk("OFFICE_NO", request)
            paramVO["CMS_HOTELCODE"] = RqChk("CMS_HOTELCODE", request)
            paramVO["CMS_SYSID"] = RqChk("CMS_SYSID", request)
            paramVO["CMS_USERID"] = RqChk("CMS_USERID", request)
            paramVO["CMS_USERPWD"] = RqChk("CMS_USERPWD", request)
            paramVO["DENY_MODIFY_DAY"] = RqChk("DENY_MODIFY_DAY", request)
            paramVO["DENY_CANCEL_DAY"] = RqChk("DENY_CANCEL_DAY", request)
            paramVO["RSVN_ADD"] = RqChk("RSVN_ADD", request)
            paramVO["RSVN_UPDATE"] = RqChk("RSVN_UPDATE", request)
            paramVO["RSVN_CANCEL"] = RqChk("RSVN_CANCEL", request)
            paramVO["API_AUTOBATCH"] = RqChk("API_AUTOBATCH", request)
            paramVO["PMS_RATETYPE"] = RqChk("PMS_RATETYPE", request)
            paramVO["CMS_UPD_TYPE"] = RqChk("CMS_UPD_TYPE", request)
            paramVO["CCINFO_TYPE"] = RqChk("CCINFO_TYPE", request)

            strSql = f"SCM100_T201 '{paramVO['tproc']}','{paramVO['CMS_CD']}','{paramVO['OFFICE_NO']}','{paramVO['CMS_HOTELCODE']}','{paramVO['CMS_SYSID']}','{paramVO['CMS_USERID']}','{paramVO['CMS_USERPWD']}','{paramVO['remark']}','{paramVO['CMS_USE_YN']}','{ViewData['sessionInfo']['LoginId']}','{paramVO['DENY_MODIFY_DAY']}','{paramVO['DENY_CANCEL_DAY']}','{paramVO['RSVN_ADD']}','{paramVO['RSVN_UPDATE']}','{paramVO['RSVN_CANCEL']}','{paramVO['API_AUTOBATCH']}','{paramVO['PMS_RATETYPE']}','{paramVO['USE_YN']}','{paramVO['CMS_UPD_TYPE']}','{paramVO['CCINFO_TYPE']}'"
            rs = procTran(strSql)

            strOpenerUrl = "/CM/WCM100_S201?CMS_CD=" + paramVO['CMS_CD'] + "&OFFICE_NO=" + paramVO['OFFICE_NO']
            intResult = rs[0]
            strResult = rs[1]

            if intResult == 1:
                return HttpResponse(alertParentDialogCloseMsg2("" + strResult + "", "location.reload(true)"))
            else:
                return HttpResponse(alertMsg(strResult, ""))

        return render(request, 'CM/WCM100_U201.html', ViewData)


    return redirect('/')


def procSelect(strSql):
    return dbexecute(strSql)

def procTran(strSql):
    return dbexecute(strSql)
    