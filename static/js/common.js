//숫자 확인
function numcheck(fname) {
    var str = fname.value
    count = 0
    for (i = 0; i < str.length; i++) {
        if (str.charAt(i) < '0' || str.charAt(i) > '9') count++
    }
    if (count != 0) {
        alert("숫자만 기입하세요.")
        //fname.value=""
        fname.focus();
        return;
    }
}

function isAlphabet(value) {
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    return containsCharsOnly(value, chars);
}

function isNumber(value) {
    var chars = "0123456789";
    return containsCharsOnly(value, chars);
}
function isAlphaNum(value) {
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    return containsCharsOnly(value, chars);
}

function isAlphaNumSpecial(value) {
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*";
    return containsCharsOnly(value, chars);
}

function containsCharsOnly(value, chars) {
    for (var inx = 0; inx < value.length; inx++) {
        if (chars.indexOf(value.charAt(inx)) == -1)
            return false;
    }
    return true;
}

//이메일 확인
function email_chk(fname) {
    var t = fname.value
    var ValidFlag = false
    var atCount = 0
    var SpecialFlag
    var atLoop
    var atChr
    var BadFlag
    var tAry1
    var UserName
    var DomainName
    if (t.length > 0 && t.indexOf("@") > 0 && t.indexOf(".") > 0) {
        atCount = 0
        SpecialFlag = false
        for (atLoop = 1; atLoop <= t.length; atLoop++) {
            atChr = t.substring(atLoop, atLoop + 1)
            if (atChr == "@") atCount = atCount + 1
            if ((atChr >= 32) && (atChr <= 44)) SpecialFlag = true
            if ((atChr == 47) || (atChr == 96) || (atChr >= 123)) SpecialFlag = true
            if ((atChr >= 58) && (atChr <= 63)) SpecialFlag = true
            if ((atChr >= 91) && (atChr <= 94)) SpecialFlag = true
        }
        if ((atCount == 1) && (SpecialFlag == false)) {
            BadFlag = false
            tAry1 = t.split("@")
            UserName = tAry1[0]
            DomainName = tAry1[1]
            if ((UserName.length <= 0) || (DomainName.length <= 0)) BadFlag = true
            if (DomainName.substring(1, 2) == ".") BadFlag = true
            if (DomainName.substring(DomainName.length - 1, DomainName.length) == ".") BadFlag = true
            ValidFlag = true
        }
    }
    if (BadFlag == true) ValidFlag = false
    return ValidFlag
}
//숫자 확인
function numcheck0(fname) {
    var str = fname.value
    count = 0
    if (str.charAt(0) == '0') count++
    for (i = 0; i < str.length; i++) {
        if (str.charAt(i) < '0' || str.charAt(i) > '9') count++
    }
    if (count != 0) {
        alert("0 이상의 숫자만 기입하세요.")
        fname.value = ""
        return;
    }
}
/**************************************
파일확장자 제한
**************************************/
function chkExt(strFileName) {
    var allowSubmit;
    file = strFileName;
    if (file.length != 0) {
        allowSubmit = false;
        if (!file) return false;
        while (file.indexOf("\\") != -1)
            file = file.slice(file.indexOf("\\") + 1);
        ext = file.slice(file.lastIndexOf(".")).toLowerCase();
        if (type == 1) {
            for (var i = 0; i < extArray.length; i++) {
                if (extArray[i] == ext) { allowSubmit = true; break; }
            }
            if (allowSubmit == false) {
                alert("죄송합니다.\n\n업로드가 지원되는 파일형식은 "
					+ (extArray.join("  ")) + " 입니다."
					+ "\n\n파일형식을 확인해보시기 바랍니다.");
                return false;
            } else { return true; }
        } else if (type == 0) {
            for (var i = 0; i < extArray.length; i++) {
                if (extArray[i] == ext) { allowSubmit = true; break; }
            }
            if (allowSubmit == true) {
                alert("죄송합니다.\n\n업로드가 지원 않되는 파일형식은 "
					+ (extArray.join("  ")) + " 입니다."
					+ "\n\n파일형식을 확인해보시기 바랍니다.");
                return false;
            } else { return true; }
        } else {
            alert("파일 업로드 설정이 잘못되어있습니다.\n\n관리자에게 문의하세요.");
            return false;
        }
    } else { return true; }
}
//특수문자 확인
function chkInjection1(fname) {
    var str = fname.value
    count = 0
    for (i = 0; i < str.length; i++) {
        if (str.charCodeAt(i) == 39) count++
    }
    if (count != 0) {
        alert("특수문자 ' 는 사용하실수 없습니다.")
        fname.value = fname.value.replace(/'/gi, "");
        fname.focus();
        return;
    }
}
//특수문자 확인
function injectioncheck(fname) {
    var str = fname.value
    count = 0
    for (i = 0; i < str.length; i++) {
        if (str.charCodeAt(i) == 39) count++
    }
    if (count != 0) {
        alert("특수문자 ' 는 사용하실수 없습니다.")
        fname.value = ""
        fname.focus();
        return;
    }
}

//폼 선택시 배경색 변환
function chgFocusIn(strfrmname) {
    strfrmname.style.background = '#F5F1E2';
}
function chgFocusout(strfrmname) {
    strchstrfrmnamee.style.background = '';
}
//창 크기 옵션 및 창 가운데 띄우기
function cnjOpen(strUrl, strID, intw, inth, strs) {
    var winl = (screen.width - intw) / 2;
    var wint = (screen.height - inth) / 2;
    winprops = 'height=' + inth + ',width=' + intw + ',top=' + wint + ',left=' + winl + ',toolbar=no, location=no, directories=no, status=yes, menubar=no, resizable=yes, scrollbars=' + strs + ', copyhistory=no'
    win = window.open(strUrl, strID, winprops)
    if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
function cnjOpenShape(intw, inth, strs) {
    var winl = (screen.width - intw) / 2;
    var wint = (screen.height - inth) / 2;
    winprops = 'height=' + inth + ',width=' + intw + ',top=' + wint + ',left=' + winl + ',toolbar=no, location=no, directories=no, status=yes, menubar=no, resizable=no, scrollbars=' + strs + ', copyhistory=no'
    return winprops;
}
function cnjOpenShape1(intw, inth, strs) {
    var winl = (screen.width - intw);
    var wint = (screen.height - inth);
    winprops = 'height=' + inth + ',width=' + intw + ',top=' + wint + ',left=' + winl + ',toolbar=no, location=no, directories=no, status=yes, menubar=no, resizable=no, scrollbars=' + strs + ', copyhistory=no'
    return winprops;
}

/*********************************************************
셀선택, 체크박스 선택,체크박스 모두 선택등
*********************************************************/
var strPreSell;
function cellOver(el) {
    strPreSell = el.style.backgroundColor;
    el.style.backgroundColor = "#EFEFEF";
}

function cellOut(el) {
    el.style.backgroundColor = strPreSell;
}

var checkflag = "false";
function chkboxall() {
    var obj;
    field = eval("document.frm.userIdx");
    if (field == undefined) {
    } else {
        if (checkflag == "false") {
            if (field.length == undefined) {
                field.checked = true;
                obj = eval('tr1');
                obj.style.backgroundColor = "#E4F2F8";
            } else {
                for (i = 0; i < field.length; i++) {
                    field[i].checked = true;
                    obj = eval('tr' + (i + 1));
                    obj.style.backgroundColor = "#E4F2F8";
                }
            }
            checkflag = "true";
            return;
        } else {
            if (field.length == undefined) {
                field.checked = false;
                obj = eval('tr1');
                obj.style.backgroundColor = "";
            } else {
                for (i = 0; i < field.length; i++) {
                    field[i].checked = false;
                    obj = eval('tr' + (i + 1));
                    obj.style.backgroundColor = "";
                }
            }
            checkflag = "false";
            return;
        }
    }
}

function chkboxall1() {
    var obj;
    field = eval("document.frm.userIdx");
    if (field == undefined) {
    } else {
        if (checkflag == "false") {
            if (field.length == undefined) {
                field.checked = true;
            } else {
                for (i = 0; i < field.length; i++) {
                    field[i].checked = true;
                }
            }
            checkflag = "true";
            return;
        } else {
            if (field.length == undefined) {
                field.checked = false;
            } else {
                for (i = 0; i < field.length; i++) {
                    field[i].checked = false;
                }
            }
            checkflag = "false";
            return;
        }
    }
}

function chkboxall_wbl102_01() {
    var obj;
    field = eval("document.frm1.BILL_NO");
    if (field == undefined) {
    } else {
        if (checkflag == "false") {
            if (field.length == undefined) {
                field.checked = true;
            } else {
                for (i = 0; i < field.length; i++) {
                    field[i].checked = true;
                }
            }
            checkflag = "true";
            return;
        } else {
            if (field.length == undefined) {
                field.checked = false;
            } else {
                for (i = 0; i < field.length; i++) {
                    field[i].checked = false;
                }
            }
            checkflag = "false";
            return;
        }
    }
}

function chkboxall2() {
    var obj;
    field = eval("document.frm1.userIdx1");
    if (field == undefined) {
    } else {
        if (checkflag == "false") {
            if (field.length == undefined) {
                field.checked = true;
                obj = eval('t2r1');
                obj.style.backgroundColor = "#E4F2F8";
            } else {
                for (i = 0; i < field.length; i++) {
                    field[i].checked = true;
                    obj = eval('t2r' + (i + 1));
                    obj.style.backgroundColor = "#E4F2F8";
                }
            }
            checkflag = "true";
            return;
        } else {
            if (field.length == undefined) {
                field.checked = false;
                obj = eval('t2r1');
                obj.style.backgroundColor = "";
            } else {
                for (i = 0; i < field.length; i++) {
                    field[i].checked = false;
                    obj = eval('t2r' + (i + 1));
                    obj.style.backgroundColor = "";
                }
            }
            checkflag = "false";
            return;
        }
    }
}

function chkboxcel(strTrName, strfrmCName) {
    obj = eval(strTrName);
    if (strfrmCName.checked) {
        //obj.style.backgroundColor="#E4F2F8";
        $("#" + strTrName).css("background-color", "#E4F2F8");
    } else {
        $("#" + strTrName).css("background-color", "");
        //obj.style.backgroundColor="";
    }
    //strPreSell=obj.style.backgroundColor;
    strPreSell = $("#" + strTrName).css("background-color");
}

function chkselmulti(loc) {
    var obj;
    obj = eval("document.frm.chk" + loc)
    field = eval("document.frm.userIdx" + loc);

    if (field != undefined) {
        if (field.length != undefined) {
            if (obj.checked == true) {
                for (i = 0; i < field.length; i++) {
                    field[i].checked = true;
                }
            }
            else {
                for (i = 0; i < field.length; i++) {
                    field[i].checked = false;
                }
            }
        }
        else {
            if (obj.checked == true) {
                field.checked = true;
            }
            else {
                field.checked = false;
            }
        }
    }
    /*
    //alert (loc);
    if(field == undefined){
    }else{
    if (checkflag == "false") {
    if(field.length==undefined){
    field.checked = true;
    }else{
    for (i = 0; i < field.length; i++) {
    field[i].checked = true;
    }
    }
    checkflag = "true";
    return;
    }else{
    if(field.length==undefined){
    field.checked = false;
    }else{
    for (i = 0; i < field.length; i++) {
    field[i].checked = false;
    }
    }
    checkflag = "false";
    return;
    }
    }
    */
}

/************************************************
검색
************************************************/
function Search() {
    //alert(searchform.searchword.value);
    if (document.searchform.searchword.value == "") {
        alert("검색어를 입력해 주세요.");
        return;
    }
    document.searchform.submit();
}

function SearchNew() {
    //alert(searchform.searchword.value);
    document.searchform.submit();
}

function focus_blur() {
    if (event.srcElement.tagName == "IMG" || event.srcElement.tagName == "A")
        document.body.focus();
}
document.onfocusin = focus_blur;

/*********************************************************
입력 글자수 byte처리 및 특수문자 ' 사용금지
*********************************************************/
String.prototype.bytes = function () {
    var str = this;
    var l = 0;
    for (var i = 0; i < str.length; i++) l += (str.charCodeAt(i) > 128) ? 2 : 1;
    return l;
}

String.prototype.cut = function (len) {
    var str = this;
    var l = 0;
    for (var i = 0; i < str.length; i++) {
        l += (str.charCodeAt(i) > 128) ? 2 : 1;
        if (l > len) return str.substring(0, i);
    }
    return str;
}


function chkInjection(fname, cutNum) {
    var str = fname.value
    count = 0
    for (i = 0; i < str.length; i++) {
        if (str.charCodeAt(i) == 39) count++
    }
    if (count != 0) {
        alert("특수문자 ' 는 사용하실수 없습니다.");
        fname.value = fname.value.replace(/'/gi, "");
        fname.focus();
        return;
    }
    if (str.bytes() > cutNum) {
        alert("글자수가 초과되었습니다.")
        fname.value = str.cut(cutNum);
        fname.focus();
        return
    }
}

function funcIsFloat(c) {
    return (((c >= "0") && (c <= "9")) || (c == ".") || (c == "-"))
}

function funcThisFloats(vTemp) {
    if (vTemp.length == 0) {
        return false;
    }
    for (i = 0; (i < vTemp.length && funcIsFloat(vTemp.charAt(i))); i++) {
        ;
    }
    if (i == vTemp.length)
        return true;
    else
        return false;
}

/**************************************
롤 오버
**************************************/
function MM_swapImgRestore() { //v3.0
    var i, x, a = document.MM_sr; for (i = 0; a && i < a.length && (x = a[i]) && x.oSrc; i++) x.src = x.oSrc;
}
function MM_preloadImages() { //v3.0
    var d = document; if (d.images) {
        if (!d.MM_p) d.MM_p = new Array();
        var i, j = d.MM_p.length, a = MM_preloadImages.arguments; for (i = 0; i < a.length; i++)
            if (a[i].indexOf("#") != 0) { d.MM_p[j] = new Image; d.MM_p[j++].src = a[i]; }
    }
}
function MM_findObj(n, d) { //v4.01
    var p, i, x; if (!d) d = document; if ((p = n.indexOf("?")) > 0 && parent.frames.length) {
        d = parent.frames[n.substring(p + 1)].document; n = n.substring(0, p);
    }
    if (!(x = d[n]) && d.all) x = d.all[n]; for (i = 0; !x && i < d.forms.length; i++) x = d.forms[i][n];
    for (i = 0; !x && d.layers && i < d.layers.length; i++) x = MM_findObj(n, d.layers[i].document);
    if (!x && d.getElementById) x = d.getElementById(n); return x;
}
function MM_swapImage() { //v3.0
    var i, j = 0, x, a = MM_swapImage.arguments; document.MM_sr = new Array; for (i = 0; i < (a.length - 2); i += 3)
        if ((x = MM_findObj(a[i])) != null) { document.MM_sr[j++] = x; if (!x.oSrc) x.oSrc = x.src; x.src = a[i + 2]; }
}
function na_restore_img_src(name, nsdoc) {
    var img = eval((navigator.appName.indexOf('Netscape', 0) != -1) ? nsdoc + '.' + name : 'document.all.' + name);
    if (name == '')
        return;
    if (img && img.altsrc) {
        img.src = img.altsrc;
        img.altsrc = null;
    }
}
function na_preload_img() {
    var img_list = na_preload_img.arguments;
    if (document.preloadlist == null)
        document.preloadlist = new Array();
    var top = document.preloadlist.length;
    for (var i = 0; i < img_list.length; i++) {
        document.preloadlist[top + i] = new Image;
        document.preloadlist[top + i].src = img_list[i + 1];
    }
}
function na_change_img_src(name, nsdoc, rpath, preload) {
    var img = eval((navigator.appName.indexOf('Netscape', 0) != -1) ? nsdoc + '.' + name : 'document.all.' + name);
    if (name == '')
        return;
    if (img) {
        img.altsrc = img.src;
        img.src = rpath;
    }
}

function OnlyAlphabet(obj) {
    val = obj.value;
    re = /[^a-zA-Z]/gi;
    obj.value = val.replace(re, "");
}

function onlyNumber() {  //숫자만을 기입받게 하는 방법
    if ((event.keyCode < 48) || (event.keyCode > 57))
        event.returnValue = false;
}

function onlyNumber1(objtext1) {  //숫자만을 기입받게 하는 방법
    var inText = objtext1.value;
    var ret;

    for (var i = 0; i < inText.length; i++) {
        ret = inText.charCodeAt(i);
        if (!((ret > 47) && (ret < 58))) {
            alert("숫자만 입력 가능합니다.");
            objtext1.value = "";
            objtext1.focus();
            return false;
        }
    }
    return true;
}

/* 마우스 우측버틑 차단  시작  */
isNoMouse = document.layers ? 1 : 0;

function noContext() { return false; }

function noContextKey(e) {
    if (isNoMouse) {
        if (e.keyCode == 96) { return (false); }
    } else {
        if (event.keyCode == 96) { return (false); }
    }
}

function noClick(e) {
    if (isNoMouse) {
        if (e.which > 1) { return false; }
    } else {
        if (event.button > 1) { return false; }
    }
}

if (isNoMouse) {
    document.captureEvents(Event.MOUSEDOWN);
}

document.oncontextmenu = noContext;
document.onkeypress = noContextKey;
document.onmousedown = noClick;
document.onmouseup = noClick;
/* 마우스 우측버틑 차단  끝  */

var SimpleContextMenu = {
    // private attributes
    _menus: new Array,
    _attachedElement: null,
    _menuElement: null,
    _preventDefault: true,
    _preventForms: true,
    // public method. Sets up whole context menu stuff..
    setup: function (conf) {
        if (document.all && document.getElementById && !window.opera) {
            SimpleContextMenu.IE = true;
        }
        if (!document.all && document.getElementById && !window.opera) {
            SimpleContextMenu.FF = true;
        }
        if (document.all && document.getElementById && window.opera) {
            SimpleContextMenu.OP = true;
        }
        if (SimpleContextMenu.IE || SimpleContextMenu.FF) {
            document.oncontextmenu = SimpleContextMenu._show;
            document.onclick = SimpleContextMenu._hide;
            if (conf && typeof (conf.preventDefault) != "undefined") {
                SimpleContextMenu._preventDefault = conf.preventDefault;
            }
            if (conf && typeof (conf.preventForms) != "undefined") {
                SimpleContextMenu._preventForms = conf.preventForms;
            }
        }
    },

    // public method. Attaches context menus to specific class names
    attach: function (classNames, menuId) {
        if (typeof (classNames) == "string") {
            SimpleContextMenu._menus[classNames] = menuId;
        }
        if (typeof (classNames) == "object") {
            for (x = 0; x < classNames.length; x++) {
                SimpleContextMenu._menus[classNames[x]] = menuId;
            }
        }
    },

    // private method. Get which context menu to show
    _getMenuElementId: function (e) {
        if (SimpleContextMenu.IE) {
            SimpleContextMenu._attachedElement = event.srcElement;
        } else {
            SimpleContextMenu._attachedElement = e.target;
        }
        while (SimpleContextMenu._attachedElement != null) {
            var className = SimpleContextMenu._attachedElement.className;
            if (typeof (className) != "undefined") {
                className = className.replace(/^\s+/g, "").replace(/\s+$/g, "")
                var classArray = className.split(/[ ]+/g);
                for (i = 0; i < classArray.length; i++) {
                    if (SimpleContextMenu._menus[classArray[i]]) {
                        return SimpleContextMenu._menus[classArray[i]];
                    }
                }
            }
            if (SimpleContextMenu.IE) {
                SimpleContextMenu._attachedElement = SimpleContextMenu._attachedElement.parentElement;
            } else {
                SimpleContextMenu._attachedElement = SimpleContextMenu._attachedElement.parentNode;
            }
        }
        return null;
    },

    // private method. Shows context menu
    _getReturnValue: function (e) {
        var returnValue = true;
        var evt = SimpleContextMenu.IE ? window.event : e;
        if (evt.button != 1) {
            if (evt.target) {
                var el = evt.target;
            } else if (evt.srcElement) {
                var el = evt.srcElement;
            }
            var tname = el.tagName.toLowerCase();
            if ((tname == "input" || tname == "textarea")) {
                if (!SimpleContextMenu._preventForms) {
                    returnValue = true;
                } else {
                    returnValue = false;
                }
            } else {
                if (!SimpleContextMenu._preventDefault) {
                    returnValue = true;
                } else {
                    returnValue = false;
                }
            }
        }
        return returnValue;
    },

    // private method. Shows context menu
    _show: function (e) {
        SimpleContextMenu._hide();
        var menuElementId = SimpleContextMenu._getMenuElementId(e);
        if (menuElementId) {
            var m = SimpleContextMenu._getMousePosition(e);
            var s = SimpleContextMenu._getScrollPosition(e);
            SimpleContextMenu._menuElement = document.getElementById(menuElementId);
            SimpleContextMenu._menuElement.style.left = m.x + s.x + 'px';
            SimpleContextMenu._menuElement.style.top = m.y + s.y + 'px';
            SimpleContextMenu._menuElement.style.display = 'block';
            return false;
        }
        return SimpleContextMenu._getReturnValue(e);
    },


    // private method. Hides context menu
    _hide: function () {
        if (SimpleContextMenu._menuElement) {
            SimpleContextMenu._menuElement.style.display = 'none';
        }
    },


    // private method. Returns mouse position
    _getMousePosition: function (e) {
        e = e ? e : window.event;
        var position = {
            'x': e.clientX,
            'y': e.clientY
        }
        return position;
    },

    // private method. Get document scroll position
    _getScrollPosition: function () {
        var x = 0;
        var y = 0;
        if (typeof (window.pageYOffset) == 'number') {
            x = window.pageXOffset;
            y = window.pageYOffset;
        } else if (document.documentElement && (document.documentElement.scrollLeft || document.documentElement.scrollTop)) {
            x = document.documentElement.scrollLeft;
            y = document.documentElement.scrollTop;
        } else if (document.body && (document.body.scrollLeft || document.body.scrollTop)) {
            x = document.body.scrollLeft;
            y = document.body.scrollTop;
        }
        var position = {
            'x': x,
            'y': y
        }
        return position;
    }
}


String.prototype.replaceAll2 = function (str1, str2) {
    return this.split(str1).join(str2);
}

function funcRvDate2(val, obj) {
    var nowdate = new Date();
    var nowYear = '' + nowdate.getYear();
    var nowMonth = nowdate.getMonth();
    nowMonth = parseInt(nowMonth) + 1;
    nowMonth = '0' + nowMonth;

    var strDate = val;
    strDate = strDate.replaceAll2("-", "");
    strDate = strDate.replaceAll2("_", "");

    if (strDate.length == 2) {
        $('input[name="' + obj + '"]').val(nowYear + Right(nowMonth, 2) + strDate);
    }
    else if (strDate.length == 4) {
        $('input[name="' + obj + '"]').val(nowYear + strDate);
    }
    else if (strDate.length == 6) {
        $('input[name="' + obj + '"]').val(nowYear.substring(0, 2) + strDate);
    }
}

function ConvertCharAjax(str) {
    var result = str;

    result = result.replaceAll2("SET", "SE{@XX@}T");
    result = result.replaceAll2("set", "se{@XX@}t");

    result = result.replaceAll2("sET", "sE{@XX@}T");
    result = result.replaceAll2("SeT", "Se{@XX@}T");
    result = result.replaceAll2("SEt", "SE{@XX@}t");

    result = result.replaceAll2("Set", "Se{@XX@}t");
    result = result.replaceAll2("sEt", "sE{@XX@}t");
    result = result.replaceAll2("seT", "se{@XX@}T");

    return result;
}

function Default_area() {
    document.write("<select name='SIDO' style='width:90px;'>");
    document.write(" <option value=''>선택</option>");
    document.write("<option value='서울특별시'>서울특별시</option>");
    document.write("<option value='경기도'>경기도</option>");
    document.write("<option value='부산광역시'>부산광역시</option>");
    document.write("<option value='충청남도'>충청남도</option>");
    document.write("<option value='충청북도'>충청북도</option>");
    document.write("<option value='대구광역시'>대구광역시</option>");
    document.write("<option value='대전광역시'>대전광역시</option>");
    document.write("<option value='강원도'>강원도</option>");
    document.write("<option value='광주광역시'>광주광역시</option>");
    document.write("<option value='경상남도'>경상남도</option>");
    document.write("<option value='경상남도'>경상남도</option>");
    document.write("<option value='경상북도'>경상북도</option>");
    document.write("<option value='인천광역시'>인천광역시</option>");
    document.write("<option value='제주특별시'>제주특별시</option>");
    document.write("<option value='전라남도'>전라남도</option>");
    document.write("<option value='전라북도'>전라북도</option>");
    document.write("<option value='세종시'>세종시</option>");
    document.write("<option value='울산광역시'>울산광역시</option>");
    document.write("</select>");
}
function fnAjaxPmsLang(pms_lang2) {
    var x = document.getElementsByName("csrfmiddlewaretoken")
    const hdata = {"X-CSRFTOKEN": x[0].value}
    $.ajax({
        url: "/CMM/WCM_200",
        type: "post",
        headers: hdata,
        dataType: "json",
        data: {
            fcn: "procPmsLang",
            pms_lang: pms_lang2
        },
        success: function (req, sts, e) {
            // alert(data.errMsg);
            location.href = location.href;
        },
        error: function (req, sts, e) {
            alert("Abnormal termination/common_34");
        }
    });
}
//str = replace(str, "\n\n", """ & chr(10) & chr(13) & """ );

/* cc_on @ */
/*@if (@_win32 && @_jscript_version>=5)

function window.confirm(str)
{
//Replace(strString, """", "'")
//str = Replace(str, chr(10), "<br>" )
execScript('n = msgbox("'+str+'","292", "확인")', "VBScript");
return(n == 6);
}

@end @*/

/*	button type
0 "Ok" button
1 "Ok" AND "Cancel" buttons
2 "Abort", 'Retry", AND "Ignore" buttons
3 "Yes", 'No", AND "Cancel" buttons
4 "Yes" AND "No" button
5 "Retry" AND "Cancel" button
*/
/*	button level
Constant Rendered button(s)
0 The first button from the left is the default button
256 The second button from the left is the default button
512 The third button from the left is the default button
768 The fourth button from the left is the default button
*/
/*	icon
16 - vbCritical
32 - vbQuestion
48 - vbExclamation
64 - vbInformation
0 Blank
*/
/*	return
0 - 확인(1) -  vbOKOnly
1 - 확인/취소 - vbOKCancel
2 - 중단(3)/다시시도(4)/무시(5) - vbAbortRetryIgnore
3 - 예(6)/아니오(7)/취소(2) - vbYesNoCancel
4 - 예(6)/아니오(7) - vbYesNo
5 - 다시시도(4)/취소(2) - vbRetryCancel
*/