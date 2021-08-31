from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *

logger = logging.getLogger(__name__)

WCM010_S101VO = dict()
WCM010_S101VO.update(BaseVO)
WCM010_S101VO["strSql"] = ""
WCM010_S101VO["recordcount"] = ""
WCM010_S101VO["recnum"] = ""
WCM010_S101VO["pagecount"] = ""
WCM010_S101VO["pagesize"] = ""
WCM010_S101VO["Gotopage"] = ""
WCM010_S101VO["use_flag"] = ""
WCM010_S101VO["reservedUrlssl"] = ""
WCM010_S101VO["CMS_NM"] = ""
WCM010_S101VO["ex_sql"] = ""
WCM010_S101VO["ex_cond"] = ""
WCM010_S101VO["ex_title"] = ""
WCM010_S101VO["ex_head"] = ""
WCM010_S101VO["ex_datatype"] = ""
WCM010_S101VO["ex_column"] = ""
WCM010_S101VO["ex_page"] = ""
WCM010_S101VO["strTemp"] = ""
WCM010_S101VO["arrIdx"] = ""
WCM010_S101VO["intBound"] = ""
WCM010_S101VO["tProc"] = ""
WCM010_S101VO["strResult"] = ""
WCM010_S101VO["strOpenerUrl"] = ""
WCM010_S101VO["intResult"] = ""



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
        logger.debug(f'/CM/WCM010_S101VO main, GET')

        paramVO = WCM010_S101VO
        paramVO["CMS_NM"] = RqChk("CMS_NM", request)
        paramVO["Gotopage"] = RqChk("gotopage", request)
        paramVO["pagesize"] = RqChk("pagesize", request)

        if not paramVO["pagesize"]:
            paramVO["pagesize"] = 20
        if not paramVO["Gotopage"]:
            paramVO["Gotopage"] = 1

        ViewData["strParam"] = "&CMS_NM=" + str(paramVO["CMS_NM"])

        ViewData["resultrs"] = procSelect(paramVO)
        ViewData["resultVO"] = paramVO

        return render(request, 'CM/WCM010_S101.html', ViewData)

    elif request.method == 'POST':
        logger.debug(f'/CM/WCM010_S101VO main, POST')

        paramVO = WCM010_S101VO
        rst = mainTran(request, paramVO, ViewData)
        return HttpResponse(rst)

    return redirect('/')

def mainTran(request, paramVO, ViewData):
    paramVO["strOpenerUrl"] = "/CM/WCM010_S101"
    paramVO["strTemp"] = RqChk("userIdx", request).replace(" ", "")
    paramVO["arrIdx"] = paramVO["strTemp"].split(",")
    paramVO["intBound"] = len(paramVO["arrIdx"])
    paramVO["tProc"] = "DEL"

    if paramVO["intBound"] >= 0:
        procTran(paramVO, ViewData)
    else:
        paramVO["strResult"] = "선택하신 자료가 없습니다."

    return alertMsg(paramVO["strResult"], paramVO["strOpenerUrl"])

def procSelect(paramVO):
    if paramVO:
        paramVO["strSql"] = f"SCM010_S101 {0},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_NM']}'"
        rs = dbexecute(paramVO["strSql"])

        paramVO["recordcount"] = rs[0]
        paramVO["strSql"] =f"SCM010_S101 {1},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_NM']}'"

        paramVO["pagecount"] = (int(paramVO["recordcount"][0] - 1) /paramVO["pagesize"]) + 1
        paramVO["recnum"] = (paramVO["Gotopage"] - 1) * paramVO["pagesize"]

        # excel용 변수 정의 시작  (ex_sql에서 pagesize를 excel 최대한도인 65535 라인 설정 top 65535)===================================
        paramVO["ex_sql"] = f"SCM010_S101 {2},{paramVO['Gotopage']},{paramVO['pagesize']},'{paramVO['CMS_NM']}'"
        paramVO["ex_sql"] = paramVO["ex_sql"].replace("'", "@^@")

        # 조회조건 적용을 위해 commonfunction1에 selectValue / selectValue1 정의됨.
        paramVO["ex_title"] = "채널코드"   #'제목 , 없으면 프로그램명이 표시됨
        paramVO["ex_cond"] = "" #'검색조건 표시줄
        paramVO["ex_head"] = "Code@CMS Name@Contarct@Use@Insert@Insert Date"
        paramVO["ex_column"] = "CMS_CD@CMS_NM@CONTRACT_YN@USE_FLAG@insert_id@insert_date"
        paramVO["ex_datatype"] = "0@0@0@0@0@0"  #''0: 문자열 / 1:숫자(excel에서 합계에 사용)
        # excel용 변수 정의 끝============================================================================================================
        return rs
    return ""

def procTran(paramVO, ViewData):
    for i in paramVO["intBound"]:
        strSql = f"SCM010_T101 '{paramVO['tProc']}','{paramVO['arrIdx'][i]}','','','','','','','','','','','','','N','{ViewData['sessionInfo']['LoginId']}'"
        rs = dbexecute(paramVO["strSql"])

    paramVO["intResult"]= 1
    paramVO["strResult"]= "선택하신 자료가 삭제 되었습니다."





    