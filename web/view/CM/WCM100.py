from django.shortcuts import render, redirect
import json
import logging
from web.view.base.baseController import *
from web.view.base.commonFunction import *
from web.view.base.FileUtil import *
import requests
from django.http import StreamingHttpResponse

logger = logging.getLogger(__name__)


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
        logger.debug(f'/CM/WCM100 main, GET')

        base_url = f"{request.scheme}://{request.get_host()}/"
        fileName = RqChk("PDSNM", request)
        filePath = base_url + Config.reservedPath + "/" + ViewData["G_OFFICE_NO"]
        strPathFileName = filePath + "/" + fileName

        print(strPathFileName)
        r = requests.get(strPathFileName, stream=True)
        response = StreamingHttpResponse(streaming_content=r)
        response['Content-Disposition'] = f'attachement; filename="{fileName}"'
        return response

    return redirect('/')



