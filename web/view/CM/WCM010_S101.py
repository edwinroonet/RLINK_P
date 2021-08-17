from django.shortcuts import render, redirect
import json
import logging
from web.view.base import baseController

logger = logging.getLogger(__name__)

def main(request):
    baseController.basemain()

    if request.method == 'GET':
        logger.debug(f'main, GET')
        return render(request, 'CM/WCM010_S101.html', {'u_no': ''})

    return redirect('/')