from django.shortcuts import render, redirect
from django.http import JsonResponse
import json, logging
import datetime
from web.view.base.baseController import *

logger = logging.getLogger(__name__)
PV_TEXT1 = ''

def main(request):
    ViewData = basemain(request)

    rstAuth = auth_fnChecking(request, ViewData["G_OFFICE_NO"], ViewData["G_COMP_NO"], ViewData["G_EMP_ID"], ViewData["G_SALESDATE"], ViewData)

    if rstAuth and rstAuth["resp"] == "redirect":
        return redirect(rstAuth["data"])
    elif rstAuth and rstAuth["resp"] == "HttpResponse":
        return HttpResponse(rstAuth["data"])

    rstAuth2 = auth_checkAuthSp(request, ViewData["G_OFFICE_NO"], ViewData["G_COMP_NO"], ViewData["G_EMP_ID"], ViewData["G_SALESDATE"], ViewData)

    if request.method == 'GET':
        logger.debug(f'WMB_100 main, GET')

        print(rstAuth)
        '''
            '''

        print(rstAuth2)

        cookie_site_no = ""
        cookie_login_id = ""
        bfocus = ""

        # ssl를 적용할 도메인 목록
        ssl_domain = {}
        ssl_domain["www.rlink.info"] = "www.rlink.info"

        # 개발자 테스트 환경에서는 ssl 체크하지 않는다
        print(request.path)

        if request.COOKIES.get('RLINK'):
            cookie_relogin_dt = request.COOKIES["RLINK"]["RELOGIN_DT"].strip()
            strNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            bfocus = "txtLoginId"

            if cookie_relogin_dt > strNow:
                p_site_no = request.COOKIES["RLINK"]["SNO"].strip()
                p_login_id = request.COOKIES["RLINK"]["LID"].strip()
                #tmp_site_no = _commonFunction.DeCrypt(p_site_no, "RLINK78")
                tmp_site_no = "RLINK78"
                #tmp_login_id = _commonFunction.DeCrypt(Replace(Replace(p_login_id, "+!", "<"), "^@^", "&"), "RLINK78")
                tmp_login_id = "RLINK78"

                if tmp_site_no[4:7] == "RLINK78" and tmp_login_id[4:7] == "RLINK78":
                    cookie_site_no = tmp_site_no[11:len(tmp_site_no) - 10]
                    cookie_login_id = tmp_login_id[11:len(tmp_login_id) - 10]
                    bfocus = "txtLoginPass"

            ViewData["cookie_site_no"] = cookie_site_no
            ViewData["cookie_login_id"] = cookie_login_id

        return render(request, 'MB/WMB_100.html', ViewData)

    elif request.method == 'POST':
        try:
            data = request.POST
            print(data)
            fcn = data.get("fcn", None)
            if fcn == "procOpen":
                paramVO = dict()
                #tmpDate = DateAdd("n", 600, Now())  '' h:시간 / n:분 / m:월 / ''쿠기가용시간을 설정 
                tmpDate = datetime.datetime.now() + datetime.timedelta(minutes=600)
                strExpire = tmpDate.strftime('%Y-%m-%d %H:%M:%S')
                strExpireDt = tmpDate.strftime('%m/%d/%Y %H:%M:%S')

                paramVO["strUser"] = RqChk("txtLoginId", request)
                paramVO["strPass"] = RqChk("txtLoginPass", request)
                paramVO["strBizNo"] = RqChk("txtBizNo", request)
                paramVO["strMac"] = ""
                paramVO["sessionid"] = request.session.session_key
                paramVO["REMOTE_ADDR"] = get_client_ip(request)

                paramVO = funcLogin(paramVO, ViewData["sessionInfo"])
                print(paramVO)

                if int(paramVO["errCode"]) > 999:
                    # 세션설정
                    setSession(request, "LoginInfo", ViewData["sessionInfo"])
                    setSession(request, "salesDate", ViewData["sessionInfo"]["salesDate"])

                    if ViewData["sessionInfo"]["MemberType"] == "AS3": #준회원 AS33 for SKY.P
                        return redirect("/MA/WMA200_S102") #DAILY REPORT
                    else:
                        return redirect("/CMM/WCM_110") #정회원 = REG 홈화면

                strErrMsg = "<script>alert('" + paramVO["errMsg"]

                if int(paramVO["errCode"]) == -14: #비밀번호 오류 (오류코드"-14")
                    iWrongCnt = PV_TEXT1
                    strErrMsg = strErrMsg + "\n\n암호 확인후 재시도 하세요.(대소문자 주의)\n\n암호 오류통제 10회중, 현재 " + iWrongCnt + " 회 입력오류입니다."

                strErrMsg = strErrMsg + "');location.href='/MB/WMB_100'</script>"
                return HttpResponse(strErrMsg)

        except Exception as e:
            print(e)
            logger.exception(f'procOpen error : {e}')
            return JsonResponse({"success": False, "message": "실패", "rst": {}}, status=200)


    return redirect('/')


def funcLogin(paramVO, sessionInfoVO):
    strSql = f"Exec SMB_100 '{paramVO['strUser']}','{paramVO['strPass']}','{paramVO['strBizNo']}','{paramVO['REMOTE_ADDR']}','{paramVO['strMac']}','{paramVO['sessionid']}' "
    print(strSql)
    rs = dbexecute(strSql)[0]
    if rs:
        sessionInfoVO["errCode"] = str(rs[0])
        sessionInfoVO["errMsg"] = str(rs[1])
        paramVO["errCode"] = sessionInfoVO["errCode"]
        paramVO["errMsg"] = sessionInfoVO["errMsg"]

        if str(rs[0])== "-14":
            PV_TEXT1 = str(rs[2]) # 암호오류시에는 오류회수가 리턴되어짐 (오류횟수 표시시에만 임시적으로 광역변수 이용)

        if (int(rs[0]) > 999):
            sessionInfoVO["LoginId"] = paramVO['strUser']
            sessionInfoVO["LoginLevel"] = str(rs[2])
            sessionInfoVO["LoginRole"] = str(rs[3])
            sessionInfoVO["LoginName"] = str(rs[4])
            sessionInfoVO["OfficeNo"] = str(rs[5])
            sessionInfoVO["OfficeNm"] = str(rs[6])
            sessionInfoVO["CompNo"] = str(rs[7])
            sessionInfoVO["CompNm"] = str(rs[8])
            sessionInfoVO["LoginFlag"] = str(rs[9])
            sessionInfoVO["OfficeTel"] = str(rs[10])
            sessionInfoVO["LoginRole1"] = str(rs[11])
            sessionInfoVO["AcctAuth"] = str(rs[12]) #대메뉴이용구분  (예약)
            sessionInfoVO["CtaxType"] = str(rs[13]) #업체과세구분코드
            sessionInfoVO["MemberType"] = str(rs[14])
            sessionInfoVO["CootCd"] = str(rs[15])
            sessionInfoVO["OMailUrl"] = str(rs[16])
            sessionInfoVO["MMailUrl"] = str(rs[17])
            sessionInfoVO["PositionNm"] = str(rs[18])
            sessionInfoVO["DeptCd"] = str(rs[19])
            sessionInfoVO["HrAuth"] = str(rs[20]) #대메뉴이용구분  (투숙/정산)
            sessionInfoVO["InventoryAuth"] = str(rs[21]) #대메뉴이용구분  (HK)
            sessionInfoVO["ProductionAuth"] = str(rs[22]) #대메뉴이용구분  (CONFIG)
            sessionInfoVO["salesDate"] = str(rs[23])
            sessionInfoVO["GUEST_NM_KOR"] = str(rs[24]) #화면 IME입력모드 기준값
            sessionInfoVO["HTLGRP_AUTHCD"] = str(rs[25]) #그룹내 사이트이용가능자
            sessionInfoVO["ArAuth"] = str(rs[26]) #대메뉴이용구분  (AR)
            sessionInfoVO["EventAuth"] = str(rs[27]) #대메뉴이용구분  (EVENT/BANQUET)
            sessionInfoVO["ReportAuth"] = str(rs[28]) #대메뉴이용구분  (REPORT)
            sessionInfoVO["ManageAuth"] = str(rs[29]) #대메뉴이용구분  (MANAGE)
            sessionInfoVO["EventSave"] = str(rs[30]) #행사화면 저장가능 여부 (YY(저장(신규+일자조정가능))/YN(저장)/NN(저장불가))
            sessionInfoVO["TLLC_YN"] = str(rs[31]) #티엘린칸이용여부 Y/N
            sessionInfoVO["Pms_lang"] = str(rs[32]) #
            sessionInfoVO["multi_lang"] = str(rs[33]) #

    return paramVO







