from django.shortcuts import render, redirect
import json, logging, datetime

from django.utils import translation

from web.view.base.baseController import *
from django.http import JsonResponse

logger = logging.getLogger(__name__)

def procPmsLang(request):
    if request.method == "POST":
        try:
            print(request.POST)
            data = request.POST
            logger.debug(f'procPmsLang, POST')
            fcn = data.get("fcn", None)
            if fcn == "procPmsLang":
                pms_lang = data.get("pms_lang", "")
                if pms_lang == "":
                    pms_lang = "E"

                strSql = []
                strSql.append(" update t_mb_100 ")
                strSql.append("    set PMS_LANG = '" + pms_lang + "' ")
                strSql.append("  where ostaff_id = '" + getSession(request, "LoginInfo")["LoginId"] + "' ")

                dbexecute(''.join(strSql))
                getSession(request, "LoginInfo")["Pms_lang"] = pms_lang

                ViewData = basemain(request)
                ViewData["sessionInfo"]["Pms_lang"] = pms_lang

                return JsonResponse({"success": True, "message": "정상"}, status=200)
            else:
                return JsonResponse({"success": False, "message": "실패", "rst": {}}, status=200)
        except Exception as e:
            logger.error(f'join search error : {e}')
            return JsonResponse({"success": False, "message": "회원가입 실패", "rst": {}}, status=200)

    return redirect('/')