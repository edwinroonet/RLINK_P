from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import translation
import json, logging, datetime

from web.models import *

BaseVO = dict()
BaseVO["errCode"] = ''
BaseVO["errMsg"] = ''
BaseVO["pp"] = ''
BaseVO["salesDate"] = ''

SessionInfoVO = dict()
SessionInfoVO.update(BaseVO)
SessionInfoVO["LoginId"] = ''
SessionInfoVO["LoginLevel"] = ''
SessionInfoVO["LoginRole"] = ''
SessionInfoVO["LoginName"] = ''
SessionInfoVO["OfficeNo"] = ''
SessionInfoVO["OfficeNm"] = ''
SessionInfoVO["CompNo"] = ''
SessionInfoVO["CompNm"] = ''
SessionInfoVO["LoginFlag"] = ''
SessionInfoVO["OfficeTel"] = ''
SessionInfoVO["LoginRole1"] = ''
SessionInfoVO["AcctAuth"] = ''
SessionInfoVO["CtaxType"] = ''
SessionInfoVO["MemberType"] = ''
SessionInfoVO["CoopCd"] = ''
SessionInfoVO["OMailUrl"] = ''
SessionInfoVO["MMailUrl"] = ''
SessionInfoVO["PositionNm"] = ''
SessionInfoVO["DeptCd"] = ''
SessionInfoVO["HrAuth"] = ''
SessionInfoVO["InventoryAuth"] = ''
SessionInfoVO["ProductionAuth"] = ''
SessionInfoVO["ArAuth"] = ''
SessionInfoVO["EventAuth"] = ''
SessionInfoVO["EventSave"] = ''
SessionInfoVO["ReportAuth"] = ''
SessionInfoVO["ManageAuth"] = ''
SessionInfoVO["GUEST_NM_KOR"] = ''
SessionInfoVO["HTLGRP_AUTHCD"] = ''
SessionInfoVO["NoReadChangeEvent"] = ''
SessionInfoVO["BBiLOGIN_LEVEL"] = ''
SessionInfoVO["Corp_type"] = ''
SessionInfoVO["W_LOGIN_ID"] = ''
SessionInfoVO["W_LOGIN_NAME"] = ''
SessionInfoVO["W_LOGIN_LEVEL"] = ''
SessionInfoVO["W_OFFICE_NO"] = ''
SessionInfoVO["W_OFFICE_NM"] = ''
SessionInfoVO["G_PGM_ID"] = ''
SessionInfoVO["TLLC_YN"] = ''
SessionInfoVO["OFFICE_NO"] = ''
SessionInfoVO["HTML_WWW_TITLE"] = ''
SessionInfoVO["ADDRESS1"] = ''
SessionInfoVO["BOOKING_NO"] = ''
SessionInfoVO["TEL_NO"] = ''
SessionInfoVO["ZIPCODE"] = ''
SessionInfoVO["ADDRESS2"] = ''
SessionInfoVO["G_MOBILE_YN"] = ''
SessionInfoVO["Mobile_YN"] = ''
SessionInfoVO["Hcn"] = ''
SessionInfoVO["PG_ID"] = ''
SessionInfoVO["PG_KEY"] = ''
SessionInfoVO["TOT_AMT"] = ''
SessionInfoVO["FOLIO_NO"] = ''
SessionInfoVO["BKCODE"] = ''
SessionInfoVO["PG_LiveYN"] = ''
SessionInfoVO["Pms_lang"] = ''
SessionInfoVO["Multi_lang"] = ''


G_SALESDATE = ''

def basemain(request):
	ViewData = dict()
	_masterPage = ''
	G_OFFICE_NO = RqChk("G_OFFICE_NO", request)
	G_COMP_NO = RqChk("G_COMP_NO", request)
	G_EMP_ID = RqChk("G_EMP_ID", request)
	G_SALESDATE = RqChk("G_SALESDATE", request)

	ViewData["Title"] = "RLink"
	ViewData["pp"] = RqChk("pp", request)
	ViewData["G_OFFICE_NO"] = G_OFFICE_NO or getSession(request, "G_OFFICE_NO")
	ViewData["G_COMP_NO"] = G_COMP_NO or getSession(request, "G_COMP_NO")
	ViewData["G_EMP_ID"] = G_EMP_ID or getSession(request, "G_EMP_ID")
	ViewData["G_SALESDATE"] = G_SALESDATE or getSession(request, "G_SALESDATE")


	if ViewData["pp"] == "Y":
		_masterPage = 'CMM/_Layout.Master'
	else:
		if "WMB_100" in request.path:
			_masterPage = 'CMM/_Layout.Master'
		elif "WRG" in request.path:
			_masterPage = 'CMM/_LayoutRG.Master'
		else:
			_masterPage = 'CMM/_LayoutMain.Master'

	wcm = RqChk("wcm", request)
	swcm = getSession(request, "WCM")
	if (not wcm) and (not swcm):
		setSession(request, "WCM", "001")
	else:
		if wcm == swcm or not wcm:
			setSession(request, "WCM", swcm)
		else:
			setSession(request, "WCM", wcm)
	ViewData["wcm"] = swcm

	ViewData["sessionInfo"] = SessionInfoVO
	setSession(request, "LoginInfo", SessionInfoVO)

	if ViewData["sessionInfo"]["Pms_lang"] == "K":
		if translation.LANGUAGE_SESSION_KEY in request.session:
			del (request.session[translation.LANGUAGE_SESSION_KEY])
		translation.activate('ko')
		request.session[translation.LANGUAGE_SESSION_KEY] = 'ko'
	elif ViewData["sessionInfo"]["Pms_lang"] == "E" or ViewData["sessionInfo"]["Pms_lang"] == "":
		if translation.LANGUAGE_SESSION_KEY in request.session:
			del (request.session[translation.LANGUAGE_SESSION_KEY])
		translation.activate('en')
		request.session[translation.LANGUAGE_SESSION_KEY] = 'en'

	print('basemain')
	print(ViewData)

	return ViewData


# request 함수
def RqChk(str, request):
	strRq = ''
	if request.method == 'GET':
		strRq = request.GET.get(str, '')
	elif request.method == 'POST':
		strRq = request.POST.get(str, '')
	if type(strRq) is not int:
		strRq = fnReplace(strRq)
	if type(strRq) is str:
		strRq = strRq.strip()
	return strRq

# 인젝션 처리
def fnReplace(str):
	if str:
		str = str.replace("'", "''")
		return str
	return str

# 세션등록
def setSession(request, key, val):
	request.session[key] = val
	return True

# 세션조회
def getSession(request, key):
	return request.session.get(key)


# 권한체크
def auth_fnChecking(request, G_OFFICE_NO, G_COMP_NO, G_EMP_ID, G_SALESDATE, ViewData):
	print("auth_fnChecking start")
	sessionInfoVO = getSession(request, "LoginInfo")
	controllerName = ''
	actionName = ''

	# 로그인 되어있을 경우 로그인 페이지 접근시 Redirect 설정
	if sessionInfoVO and "WMB_100" in request.path:
		if sessionInfoVO["LoginLevel"] >= "OA":
			return {"resp":"redirect", "data":'/CMM/WCM_110'}
		else:
			if "WMB_100" in request.path:
				if sessionInfoVO:
					sessionInfoVO = SessionInfoVO
				else:
					return {"resp": "redirect", "data": '/BD/WBD310_S201?BD_CD=01'}

	if not "WMB_100" in request.path or "WMB_102" in request.path or "WMB_102" in request.path \
			or "excel_0" in request.path or "WWC_912" in request.path or "zip_" in request.path \
			or "WST_" in request.path or "WPI" in request.path or "WRG" in request.path \
			or "WCM_201" in request.path or "WCM_200" in request.path or "blank" in request.path \
			or "sample" in request.path or "test" in request.path:

		if not sessionInfoVO:
			return {"resp": "redirect", "data": '/MB/WMB_100'}
		else:
			if sessionInfoVO["LoginId"] == "":
				return {"resp": "redirect", "data": '/MB/WMB_100'}

		if sessionInfoVO["LoginId"] >= "OA": # 전체이용자 레벨에 대해 Request를 받아 처리 120816
			G_OFFICE_NO = RqChk("G_OFFICE_NO", request)
			if G_OFFICE_NO and len(G_OFFICE_NO) > 5 and G_OFFICE_NO != "Nothing":
				return {"resp": "HttpResponse", "data": "<script language='javascript'>alert('SYSTEM FAULT. TRY AGAIN. \n\n재시도 바랍니다.');history.back();</script>"}

		if sessionInfoVO["LoginLevel"] >= "OA" or sessionInfoVO["BBiLOGIN_LEVEL"] >= "OA": # 회사이용자 레벨이상 Request를 받아 처리
			G_COMP_NO = RqChk("G_COMP_NO", request)
			if G_COMP_NO and len(G_COMP_NO) > 10 and G_COMP_NO != "Nothing":
				return {"resp": "HttpResponse", "data": "<script language='javascript'>alert('SYSTEM FAULT. TRY AGAIN. \n\n재시도 바랍니다.');history.back();</script>"}

		if G_COMP_NO == "":
			G_COMP_NO = sessionInfoVO["CompNo"]

		if G_OFFICE_NO == "":
			G_OFFICE_NO = sessionInfoVO["OfficeNo"]

		G_EMP_ID = RqChk("G_EMP_ID", request)
		sessionInfoVO["G_PGM_ID"] = request.path

		if (G_OFFICE_NO and len(G_OFFICE_NO) > 5) or (G_COMP_NO and len(G_COMP_NO) > 10): # length 체크로 sql injection 차단
			return {"resp": "HttpResponse", "data": "<script language='javascript'>alert('SYSTEM FAULT. TRY AGAIN. \n\n재시도 바랍니다.');history.back();</script>"}


def auth_checkAuthSp(request, G_OFFICE_NO, G_COMP_NO, G_EMP_ID, G_SALESDATE, ViewData):
	print("auth_checkAuthSp start")
	sessionInfoVO = getSession(request, "LoginInfo")
	NAVIGATION_URL = request.path
	PAGE_ID = ''
	LOGIN_LEVEL = sessionInfoVO["LoginLevel"]

	sSql = f" SCM010_110 '{sessionInfoVO['LoginId']}','{LOGIN_LEVEL}','{sessionInfoVO['LoginRole1']}','{getSession(request, 'SessionID')}','{PAGE_ID}','{G_OFFICE_NO}','{G_COMP_NO}' "
	print(sSql)
	tmpRs = dbexecute(sSql)[0]
	print(tmpRs)
	if not tmpRs:
		intRet = -1003
		strMsg = "네트워크가 불안정합니다. 잠시후 재시도 바랍니다."
	else:
		intRet = int(tmpRs[0])
		popup_flag = str(tmpRs[1])
		strMsg = str(tmpRs[2])
		G_SALESDATE = tmpRs[3]
		ViewData["G_SALESDATE"] = G_SALESDATE

	if intRet >= 1000:
		return
	else:
		# 로그인페이지 XX 메인페이지 일경우에만 클레임 연동 적용
		strScript = "<script language='javascript'> "
		strScript = strScript + "alert('"+ strMsg +"'); "

		if 0 <= intRet and intRet<1000:
			if intRet == 991: #클레임열람 연동 통제
				strScript = strScript + "location.replace('/FO/WFO100_S301'); "
			elif popup_flag == "Y":
				strScript = strScript + "self.close(); "
			else: # 이전 화면 이동시 통제 안됨.
				if sessionInfoVO["LoginLevel"] >= "OA": #회사이용자이상레벨
					strScript = strScript + "location.replace('/CMM/WCM_110'); "
				else:
					strScript = strScript + "location.replace('/BD/WBD310_S201?BD_CD=01'); "
		else: # 로그아웃
			if popup_flag == "Y":
				strScript = strScript + "opener."
			strScript = strScript + "location.replace('/MB/WMB_100');  "

		if popup_flag == "Y":
			strScript = strScript + "window.close();  "
		
		strScript = strScript + "</script>"
		return {"resp": "HttpResponse", "data": strScript}
		

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_weekday(date):
	'''
	파이썬 요일코드 (0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일) 를 ms타입으로 변환함
	:return:
	'''
	if (datetime.datetime.strptime(date, '%Y-%m-%d').weekday() + 2) == 8:
		return 1
	else:
		return datetime.datetime.strptime(date, '%Y-%m-%d').weekday() + 2