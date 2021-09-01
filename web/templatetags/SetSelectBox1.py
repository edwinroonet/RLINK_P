from django import template
from django.utils.safestring import mark_safe

from web.models import dbexecute
from web.view.base.commonFunction import *

register = template.Library()

@register.simple_tag
def SetSelectBox1(cFlag, strSelValue, strSelMent, strOption1, strOption2, _hcb, _G_OFFICE_NO):

    _httpContextBase = _hcb
    G_OFFICE_NO = _G_OFFICE_NO
    sessionInfoVo = _httpContextBase.session.get("LoginInfo")

    rtnValue = ""
    strSel = ""

    strSql = setCommonQuery(cFlag, strSelValue, strSelMent, strOption1, strOption2, sessionInfoVo, G_OFFICE_NO)

    tmpRs = dbexecuteQuery(strSql, '')
    print(tmpRs)
    # RV/WRV010_S201/main/

    if strSelMent.strip() != "":
        rtnValue = "<option	value=''>" + strSelMent + "</option>"
    if not tmpRs:
        return rtnValue

    for i, t in enumerate(tmpRs):
        if t["code"].strip() == strSelValue.strip():
            strSel = " selected"
        else:
            if i == 0 and strOption1 == "FIRST_SELECT":
                strSel = " selected"
            else:
                strSel = ""
        rtnValue = rtnValue + "<option	value='" + t["code"] + "'" + strSel + ">" + t["code_nm"] + "</option>"

    return mark_safe(rtnValue)
