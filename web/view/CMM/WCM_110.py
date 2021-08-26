from django.shortcuts import render, redirect
import json, logging, datetime

from django.utils import translation

from web.view.base.baseController import *

logger = logging.getLogger(__name__)

Wcm_110VO = dict()
Wcm_110VO.update(BaseVO)
Wcm_110VO["officeNo"] = ""
Wcm_110VO["loginId"] = ""
Wcm_110VO["loginName"] = ""
Wcm_110VO["home_sec05"] = ""
Wcm_110VO["sSignReturn"] = ""
Wcm_110VO["corp_type"] = ""
Wcm_110VO["tel_no"] = ""
Wcm_110VO["mobile_no"] = ""
Wcm_110VO["position_nm"] = ""
Wcm_110VO["dept_nm"] = ""
Wcm_110VO["pa_update"] = ""
Wcm_110VO["me_demand_amt"] = ""
Wcm_110VO["me_collect_month"] = ""
Wcm_110VO["me_cl_amt"] = ""
Wcm_110VO["me_cl_cnt"] = ""
Wcm_110VO["comp_cnt"] = ""
Wcm_110VO["mand1"] = ""
Wcm_110VO["mand2"] = ""
Wcm_110VO["mand3"] = ""
Wcm_110VO["mand8"] = ""
Wcm_110VO["mand9"] = ""
Wcm_110VO["ingRS"] = ""
Wcm_110VO["workRS"] = ""
Wcm_110VO["clRS"] = ""
Wcm_110VO["clRS2"] = ""
Wcm_110VO["cimg"] = ""
Wcm_110VO["pRS"] = ""
Wcm_110VO["oRS"] = ""
Wcm_110VO["strFr"] = ""
Wcm_110VO["strTo"] = ""
Wcm_110VO["sdate"] = ""
Wcm_110VO["edate"] = ""
Wcm_110VO["qRS"] = ""
Wcm_110VO["record_cnt"] = ""
Wcm_110VO["rRS"] = ""
Wcm_110VO["VIP_FLAG"] = ""
Wcm_110VO["FOLIO_TYPE"] = ""
Wcm_110VO["toDay"] = ""
Wcm_110VO["sRS"] = ""
Wcm_110VO["tRS"] = ""
Wcm_110VO["sReadTodayOrder"] = ""
Wcm_110VO["sReadTodayPlan"] = ""
Wcm_110VO["add_board_flag"] = ""
Wcm_110VO["strYm"] = ""



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
        logger.debug(f'/CMM/WCM_110 main, GET')

        paramVO = Wcm_110VO
        paramVO["officeNo"] = ViewData["sessionInfo"]["OfficeNo"]
        paramVO["loginId"] = ViewData["sessionInfo"]["LoginId"]
        paramVO["loginName"] = ViewData["sessionInfo"]["LoginName"]
        paramVO["sReadTodayPlan"] = "Y"
        paramVO["sReadTodayOrder"] = "Y"
        paramVO["add_board_flag"] = "N"
        paramVO["strYm"] = RqChk("strYm", request)
        if not paramVO["strYm"]:
            paramVO["strYm"] = datetime.datetime.now().strftime('%Y%m%d') + "01"

        paramVO = procSelect(paramVO)
        print(paramVO)
        print(ViewData["sessionInfo"])
        ViewData["sessionInfo"]["Corp_type"] = paramVO["corp_type"]

        ViewData["resultVO"] = paramVO
        ViewData["strCal"] = strCal(paramVO["strYm"], ViewData)

        return render(request, 'CMM/WCM_110.html', ViewData)

    return redirect('/')

def procSelect(paramVO):

    # Notice
    param = [paramVO["officeNo"]]
    strSql = "	select 	top 5 a.office_no, notice_seq, bd_cd, ISNULL(STAFF_NM,A.reg_id) reg_id, title, fr_date, to_date, content, pds_nm, pds_ext, a.insert_date "
    strSql = strSql + "	from	T_BD_110 A	"
    strSql = strSql + "	left join T_MB_100 B ON B.OSTAFF_ID = A.REG_ID 	"
    strSql = strSql + "	where 	a.office_no = %s "
    strSql = strSql + "	  and 	BD_CD = '01' and to_date >=  convert(char(8),getdate(),112) and del_flag='N'"
    strSql = strSql + "	order by a.insert_date desc "
    paramVO["ingRS"] = dbexecuteQuery(strSql, param)

    # GM Manager Message
    param = [paramVO["officeNo"]]
    strSql = "	select 	top 5 office_no, notice_seq, bd_cd, reg_id, title, fr_date, to_date, content, pds_nm, pds_ext, insert_date "
    strSql = strSql + "	from	T_BD_110 	"
    strSql = strSql + "	where 	office_no 	= %s "
    strSql = strSql + "	  and 	BD_CD = '02' "
    strSql = strSql + "	order by insert_date desc "
    paramVO["workRS"] = dbexecuteQuery(strSql, param)

    return paramVO

def strCal(strYm, ViewData):
    print(strYm)
    D_year = strYm[0:4]
    D_month = strYm[4:6]
    D_holiday = ""

    if int(D_month) + 1 > 12:
        now_day1 = D_year + "-" + D_month + "-01"
        now_day2 = int(D_year) + 1 + "-" + str(int(D_month) -11).zfill(2) + "-01"
    else:
        now_day1 = D_year + "-" + D_month + "-01"
        now_day2 = D_year + "-" + str(int(D_month) + 1).zfill(2) + "-01"

    now_day = datetime.datetime.now().strftime('%d')
    now_month = datetime.datetime.now().strftime('%m')
    D_totalday = (datetime.datetime.strptime(now_day1, '%Y-%m-%d') - datetime.datetime.strptime(now_day2, '%Y-%m-%d')).days
    F_weekly = get_weekday(now_day1)

    vbCrLf = "\n "
    strCal = "<table width=""100%"" height=""100%"" border=""0"" cellspacing=""0"" cellpadding=""0"">" + vbCrLf
    strCal = strCal + "	<tr>" + vbCrLf
    strCal = strCal + "		<td align=""center"" valign=""top"">" + vbCrLf
    strCal = strCal + "			<table width=""100%"" border=""0"" cellspacing=""0"" cellpadding=""0"" bgcolor=""#FFFFFF"">" + vbCrLf
    strCal = strCal + "				<tr height=""20"" class=""txt_text1"" bgcolor=""#f1f6f9"">" + vbCrLf
    strCal = strCal + "					<td align=""left"" width=""14%""><font color=""#e30001"">+nbsp;S</td>" + vbCrLf
    strCal = strCal + "					<td align=""left"" width=""14%""><font color=""black"">+nbsp;M</td>" + vbCrLf
    strCal = strCal + "					<td align=""left"" width=""14%""><font color=""black"">+nbsp;T</td>" + vbCrLf
    strCal = strCal + "					<td align=""left"" width=""14%""><font color=""black"">+nbsp;W</td>" + vbCrLf
    strCal = strCal + "					<td align=""left"" width=""14%""><font color=""black"">+nbsp;T</td>" + vbCrLf
    strCal = strCal + "					<td align=""left"" width=""14%""><font color=""black"">+nbsp;F</td>" + vbCrLf
    strCal = strCal + "					<td align=""left"" width=""14%""><font color=""#007fc1"">+nbsp;S</td>" + vbCrLf
    strCal = strCal + "				</tr>" + vbCrLf
    strCal = strCal + "				<tr bgcolor=""#ffffff"">" + vbCrLf

    print(strCal)
    

    # 매월 1일 이전에 생기는 앞빈공간 채우기
    if F_weekly != 1:
        for i in range(1,F_weekly- 1):
            strCal = strCal + "             <td></td>" + vbCrLf

    for i in range(1+F_weekly-1, D_totalday + (F_weekly - 1)):
        today_date = D_year + "-" + D_month.zfill(2) + "-" + str(i - (F_weekly - 1)).zfill(2)
        bgImg = ""
        if i-F_weekly-1 == now_day and D_month == now_month: #오늘날짜면 이미지 출력
            bgImg = "/static/images/to/today_bg.gif"
        day_check = i - (F_weekly - 1) + "</font>"

        if i != 1 and i % 7 == 1:
            strCal = strCal + "<tr height=""20"" bgcolor=""#ffffff"">" + vbCrLf

        strSql = "  select  msg_date, msg_seq, isnull(msg_desc,'') as msg_desc, isnull(msg_remark,'') as msg_remark "
        strSql = strSql + " from    t_to_103 "
        strSql = strSql + " where   msg_flag   = 'O' and use_flag='Y' "
        strSql = strSql + "   and   office_no = '" + ViewData["sessionInfo"]["OfficeNo"] + "' "
        strSql = strSql + "   and   msg_date   = '" + today_date.replace("-", "") + "'     "
        strSql = strSql + " order by msg_date asc, msg_seq asc                  "
        rs = dbexecuteQuery(strSql, [])
        if not rs:
            msg_date = ""
            msg_desc = ""
            msg_remark = ""
        else:
            msg_date = today_date
            inti = 1
            for i in rs:
                bMemo = bMemo + inti + ". " + i["msg_desc"] + " (" + i["msg_remark"] + ")<br>"
                inti = inti + 1

        strCal = strCal + "     <td align=""right"" class=""num"">" + vbCrLf
        strCal = strCal + "         <table width=""100%"" align=""right"" cellspacing=""0"" cellpadding=""0"" border=""0""  background=" + bgImg + ">" + vbCrLf
        strCal = strCal + "             <tr height=""20"">" + vbCrLf
        strCal = strCal + "                 <td valign=""middle"" class=""textin"">+nbsp;" + day_color(today_date, D_holiday, i) + day_check + "</td>" + vbCrLf + vbCrLf
        strCal = strCal + "                 <td align=""right"" valign=""middle"" class=""textin"" width=""13"">" + vbCrLf
        if msg_date:
            strCal = strCal + "<a href=""#"" id=""link"" context=""Y"" attr1="" " + msg_date + " "" attr2=" "" + bMemo + " ""><img src=""/static/images/icons/doc_01.gif"" width=""10"" ></a>" + vbCrLf
        
        strCal = strCal + "                 </td>" + vbCrLf
        strCal = strCal + "             </tr>" + vbCrLf
        strCal = strCal + "         </table>" + vbCrLf
        strCal = strCal + "     </td>" + vbCrLf

        if i % 7 == 0:
            strCal = strCal + "</tr>" + vbCrLf
        
        bMemo = ""

def day_color(today, holiday, wp):
    if today in holiday or (wp % 7 == 1):
        day_color = "<font color=""#e30001"">"
    elif wp % 7 == 0:
        day_color = "<font color=""#007fc2"">"
    else:
        day_color = "<font color=""#000000"">"
    return day_color







