//***********************************************************************//
//***********************************************************************//
//	Title		: include javascript file								 //
//	Author		: Karl Lee (SangHyuk Lee)								 //
//	Date		: May 7, 2000											 //
//  Modify      : July 3, 2003											 //
//	Description : This page is for include in asp page which 			 //
//				  have text field or some of necessarily validate		 //		
//				  from client side										 //
//***********************************************************************//
//***********************************************************************//

//문자열 , 숫자, 날짜 유효성 검사 관련
//==========================================================================================================================================
//function checkEmpty(karl,name)
//function checkETC(karl,name)
//function checkETC_with_trim(karl,name)
//function checkETC_spece(karl,name)
//function checkEmail(karl)
//function checkDate(karl,name)
//function checkNaString(karl,name)
//function checkEnglish_withOut_trim(karl,name)
//function checkEnglish_withOut_trim_bar(karl,name)
//function checkEnglish_with_comma(karl,name)
//function checkEnglish_space_comma_bar(karl,name)
//function checkEnglish(karl,name)

//function checkNaN(karl,name)
//function checkNaN_with_bar(karl,name)
//function checkDigit(karl,name,digit)
//==========================================================================================================================================


//메일관련
//==========================================================================================================================================
//function sendMail(Amail,Aname)
//==========================================================================================================================================

//시작페이지 관련
//==========================================================================================================================================
//function setStartPage()
//==========================================================================================================================================


//주민 & 사업자 번호 관련
//==========================================================================================================================================
//function JuminValid(j1, j2)
//function f_is_saup(textObj)
//function f_is_jumin(newValue)
//==========================================================================================================================================

//새창 관련
//==========================================================================================================================================
//function open_window(width,height,title,URL,param)
//function open_window_popupHtml(width,height,title,URL,param)
//==========================================================================================================================================

//키보드 관련
//==========================================================================================================================================
//function CheckKeyPress()
//==========================================================================================================================================



//달력관련(관리자페이지용)
//==========================================================================================================================================
//function LeapYear (yy)
//function LastDay(yy, mm)
//function ChkDate(elm)  
//function InitDate(elm)	
//function ShowCal(ename, add_bit)
//function reCal(sw, add_top)
//function dayCho(d)
//==========================================================================================================================================


//프린터관련(컴포넌트 Object사용 필)
//==========================================================================================================================================
//function printWindow()
//==========================================================================================================================================


//컬러관련
//==========================================================================================================================================
//function OverColor(elm,c)
//function OutColor(elm,c)
//==========================================================================================================================================



//검색관련
//==========================================================================================================================================
//function find()
//==========================================================================================================================================



//팝업공지 관련
//==========================================================================================================================================
//function findNoticeCookies(name)
//function setCookie_and_closeWin() 
//function setCookie(name, value, expiredays)
//==========================================================================================================================================


//기타 개별 함수
//==========================================================================================================================================
//function checkValid_write(a,aa,b,bb,c,cc,d,dd,e,ee,f,ff)
//==========================================================================================================================================








//##########################################################################################################################################
//##########################################################################################################################################
//##########################################################################################################################################









function checkEmpty(karl,name)
{
	var str = karl.value;
		
	if (str==null || str=="" || str.length==0)
	{
		alert(name + " 항목이 비어있습니다.\n\n값을 넣어주십시오");		
			karl.focus();
				return false;
	}
	if (str.substring(0,1)==" " || str.substring(0,1)==null)
	{
		alert(name + " 항목은 빈칸 혹은 공백으로 시작될 수 없습니다..\n\n다시 입력하여 주십시오");
			karl.focus();
				return false;
	}
	
	return true;
}

function checkETC(karl,name)
{
	var str = karl.value;
	for (i=0;i<=(str.length);i++)
	{
		var cha = str.substring(i,i+1);
			if((cha=="'") || (cha==",") || (cha==".") || (cha=="=") || (cha=="+") || (cha=="_") || (cha=="*") || (cha=="&") || (cha=="^") || (cha=="%") || (cha=="$") || (cha=="#") || (cha=="@") || (cha=="!") || (cha=="`") || (cha=="~") || (cha=="<") || (cha==">") || (cha=="/") || (cha==":") || (cha==";"))
			{
				alert(""+ name +"란은 특수문자를 허용하지 않습니다.\n\n다시 입력하여 주십시오");
						karl.focus();
							return false;
			}
	}
	return true;
}

function checkETC_with_trim(karl,name)
{
	var str = karl.value;
	for (i=0;i<=(str.length);i++)
	{
		var cha = str.substring(i,i+1);
			if((cha=="    ") || (cha=="'") || (cha==",") || (cha==".") || (cha=="=") || (cha=="+") || (cha=="_") || (cha==")") || (cha=="(") || (cha=="*") || (cha=="&") || (cha=="^") || (cha=="%") || (cha=="$") || (cha=="#") || (cha=="@") || (cha=="!") || (cha=="`") || (cha=="~") || (cha=="<") || (cha==">") || (cha=="/") || (cha==":") || (cha==";"))
			{
				alert(""+ name +"란은 특수문자를 허용하지 않습니다.\n\n다시 입력하여 주십시오");
						karl.focus();
							return false;
			}
	}
	return true;
}

function checkETC_spece(karl,name)
{
	var str = karl.value;
	for (i=0;i<=(str.length);i++)
	{
		var cha = str.substring(i,i+1);
			if((cha=="'") || (cha=='"') || (cha==" ") || (cha==",") || (cha==".") || (cha=="=") || (cha=="+") || (cha=="_") || (cha==")") || (cha=="(") || (cha=="*") || (cha=="&") || (cha=="^") || (cha=="%") || (cha=="$") || (cha=="#") || (cha=="@") || (cha=="!") || (cha=="`") || (cha=="~") || (cha=="<") || (cha==">") || (cha=="/") || (cha==":") || (cha==";"))
			{
				alert(""+ name +"란은 특수문자 및 공백을 허용하지 않습니다.\n\n다시 입력하여 주십시오");
						karl.focus();
							return false;
			}
	}
	return true;
}

function checkNaN(karl,name)
{
	var str = karl.value;
	if (isNaN(str))
	{
		alert(""+ name +"란은 숫자입력만을 허용합니다..\n\n다시 입력하여 주십시오");
			karl.value = "";
				karl.focus();
					return false;
	}
	return true;
}

function checkNaN_with_bar(karl,name)
{
	var str = karl.value;
	if (isNaN(str))
	{
		alert(""+ name +"란은 숫자입력만을 허용합니다..\n\n다시 입력하여 주십시오");
			karl.value = "";
				karl.focus();
					return false;
	}
	return true;
}

function checkNaString(karl,name)
{
	var str = karl.value;
	for (i=0;i<=str.length;i++)
	{
		var char = str.charCodeAt(i);
		if ((char < 65) || ((char > 90) && (char < 97)))
		{
			alert(""+ name +"란은 문자입력만을 허용합니다.\n\n다시 입력하여 주십시오.");
				karl.value = "";
					karl.focus();
						return false;
		}
	}
	return true;
}

function checkEmail(karl)
{
	var str = karl.value;
	if (str.indexOf('@')==-1 || str.indexOf('.')==-1)
	{
		alert("메일주소 형식이 잘못되었습니다.\n\n다시 입력하여 주십시오.");
			karl.value="";
				karl.focus();
					return false;
	}

	for (i=0;i<=(str.length);i++)
	{
		var cha = str.substring(i,i+1);
			if((cha=="'") || (cha==" ") || (cha==",") || (cha=="=") || (cha=="+") || (cha==")") || (cha=="(") || (cha=="*") || (cha=="&") || (cha=="^") || (cha=="%") || (cha=="$") || (cha=="#") || (cha=="!") || (cha=="`") || (cha=="~") || (cha=="<") || (cha==">") || (cha=="/") || (cha==":") || (cha==";"))
			{
				alert("email란에 특수문자 혹은 공백이 포함 되었습니다..\n\n다시 입력하여 주십시오");
						karl.focus();
							return false;
			}
	}
	
  return true;	
}

function checkDate(karl,name)
{
	var str = karl.value;
	for (i=0;i<=str.length;i++)
	{
		var char = str.charCodeAt(i);
		if (char > 57 || (char < 48 && char!==45))
		{
			alert(""+ name +"란은 날짜와 부호(-)만을 허용합니다.\n\n다시 입력하여 주십시오");
					karl.focus();
						return false;
		}
	}
	

	if ((str.length !== 10) || (str.substring(4,5) !=="-") || (str.substring(7,8) !=="-") || (str.substring(0,4) < 1600) || (str.substring(5,7) > 13) || (str.substring(8,10) > 31))
	{
		alert("" + name + "란은 다음과 같은 형식이어야 합니다. ex:yyyy-mm-dd  \n\n다시 입력하여 주십시오.");
			karl.value = "";
					karl.focus();
						return false;
	}
	return true;
}

function checkEnglish_withOut_trim(karl,name)
{
	var str = karl.value;
	for(i=0;i<=str.length;i++)
	{
		var char = str.charCodeAt(i);
		if ((char < 65 && char != 32) || (char > 90 && char < 97) || (char > 122))
		{
			alert("" + name + "란은 알파벳만을 허용합니다. \n\n다시 입력하여 주십시오.");
				karl.value="";
					karl.focus();
						return false;
		}
	}
	return true;
}

function checkEnglish_withOut_trim_bar(karl,name)
{
	var str = karl.value;
	for(i=0;i<=str.length;i++)
	{
		var char = str.charCodeAt(i);
		if ((char < 65 && char != 32 && char !=45) || (char > 90 && char < 97) || (char > 122))
		{
			alert("" + name + "란은 알파벳과 - 기호만을 허용합니다. \n\n다시 입력하여 주십시오.");
				karl.value="";
					karl.focus();
						return false;
		}
	}
	return true;
}

function checkEnglish_with_comma(karl,name)
{
	var str = karl.value;
	for(i=0;i<=str.length;i++)
	{
		var char = str.charCodeAt(i);
		if ((char < 65 && char != 44 && char != 46) || (char > 90 && char < 97) || (char > 122))
		{
			alert("" + name + "란은 알파벳만을 허용합니다. \n\n다시 입력하여 주십시오.");
				karl.value="";
					karl.focus();
						return false;
		}
	}
	return true;
}

function checkEnglish_space_comma_bar(karl,name)
{
	var str = karl.value;
	for(i=0;i<=str.length;i++)
	{
		var char = str.charCodeAt(i);
		if ((char < 65 && char != 32 && char !=45 && char != 44 && char != 46) || (char > 90 && char < 97) || (char > 122))
		{
			alert("" + name + "란은 알파벳과 \",\" -와 공백만을 허용합니다. \n\n다시 입력하여 주십시오.");
				karl.value="";
					karl.focus();
						return false;
		}
	}
	return true;
}

function checkEnglish(karl,name)
{
	var str = karl.value;
	for(i=0;i<=str.length;i++)
	{
		var char = str.charCodeAt(i);
		if ((char < 65) || (char > 90 && char < 97) || (char > 122))
		{
			alert("" + name + "란은 알파벳만을 허용합니다. \n\n다시 입력하여 주십시오.");
				karl.value="";
					karl.focus();
						return false;
		}
	}
	return true;
}

function checkDigit(karl,name,digit)
{
	var str = karl.value;
	if(str.length < digit)
	{
		alert("" + name + "란이 올바르게(숫자가 모자랍니다.) 입력되지 않았습니다. \n\n다시 입력하여 주십시오");
			karl.value="";
				karl.focus();
					return false;
	}
	return true;
}

function JuminValid(j1, j2)
{
	if	(j1.value == "" )
	{
		alert("주민등록번호 6자리를 입력해주세요.");
		j1.focus();
		return false; ;
           
	} 
	if (j2.value == "" )
	{
		alert("주민등록번호 7자리를 입력해주세요.");
		j2.focus();       
		return false; ;
           
	} 
	
	if (j1.value.length < 6 )
	{
		alert("주민등록번호 입력이 잘못되었습니다.");
		j1.focus();
		return false; ;
	}
	
	if (j2.value.length < 7 )
	{
		alert("주민등록번호 입력이 잘못되었습니다.");
		j2.focus();
		return false; ;
	} 
	
	var str_serial1 = j1.value;
	var str_serial2 = j2.value;
	var digit=0;
	for (var i=0; i<str_serial1.length; i++)
	{
		var str_dig=str_serial1.substring(i,i+1);
		if (str_dig<'0' || str_dig>'9')
			digit=digit+1 ;
	}

	if ((str_serial1 == '') || ( digit != 0 ))
	{
 	  	alert('잘못된 주민등록번호입니다.\n\n다시 확인하시고 입력해 주세요.');
	  	j1.focus();
		return false; ; 
	}
	
	var digit1=0
	for (var i=0;i<str_serial2.length;i++)
	{
		var str_dig1=str_serial2.substring(i,i+1);
		if (str_dig1<'0' || str_dig1>'9')
			digit1=digit1+1; 
	}
	
	if ((str_serial2 == '') || ( digit1 != 0 ))
	{
		alert('잘못된 주민등록번호입니다.\n\n다시 확인하시고 입력해 주세요.');
		j2.focus();
		return false;;  
	}
	
	if (str_serial1.substring(2,3) > 1)
	{
		alert('잘못된 주민등록번호입니다.\n\n다시 확인하시고 입력해 주세요.');
		j1.focus();
		return false; ; 
	}

	if (str_serial1.substring(4,5) > 3)
	{
		alert('잘못된 주민등록번호입니다.\n\n다시 확인하시고 입력해 주세요.');
		j1.focus();
		return false;;
	} 
	
	if (str_serial2.substring(0,1) > 4 || str_serial2.substring(0,1) == 0)
	{
		alert('잘못된 주민등록번호입니다.\n\n다시 확인하시고 입력해 주세요.');
		j2.focus();
		return false;;
	}
	
	var a1=str_serial1.substring(0,1);
	var a2=str_serial1.substring(1,2);
	var a3=str_serial1.substring(2,3);
	var a4=str_serial1.substring(3,4);
	var a5=str_serial1.substring(4,5);
	var a6=str_serial1.substring(5,6);
	var check_digit=a1*2+a2*3+a3*4+a4*5+a5*6+a6*7;

	var b1=str_serial2.substring(0,1);
	var b2=str_serial2.substring(1,2);
	var b3=str_serial2.substring(2,3);
	var b4=str_serial2.substring(3,4);
	var b5=str_serial2.substring(4,5);
	var b6=str_serial2.substring(5,6);
	var b7=str_serial2.substring(6,7);
	var check_digit=check_digit+b1*8+b2*9+b3*2+b4*3+b5*4+b6*5 ;
		
	check_digit = check_digit%11;
	check_digit = 11 - check_digit;
	check_digit = check_digit%10;
	
	if (check_digit != b7)
	{
		alert('잘못된 주민등록번호입니다.');
		j2.focus();
		return false;
	}
	return true;
}  

//function printWindow(strHeader,strFooter)
function printWindow() {
    
//	factory.printing.header = strHeader
//	factory.printing.footer = strFooter
	factory.printing.portrait = false //좌우
	factory.printing.leftMargin = 15.0
	factory.printing.topMargin = 0.0
	factory.printing.rightMargin = 15.0
	factory.printing.bottomMargin = 0.0
	factory.printing.Print(false, window)
	self.close();
}

function OverColor(elm,c)
{
	elm.style.backgroundColor = c;
}

function OutColor(elm,c)			
{
	elm.style.backgroundColor = c;
}

function LeapYear (yy)
{
	if (((yy % 4)==0) && ((yy % 100)!=0) || ((yy % 400)==0))
		return 1;
	else
		return 0;
}

function LastDay(yy, mm)
{
	if	(mm == 1)
		return 31;
	else
		if	(mm == 2)
			return 28+LeapYear(yy);
		else
			if	(mm == 3)
				return 31;
			else
				if	(mm == 4)
					return 30;
				else
					if	(mm == 5)
						return 31;
					else
						if	(mm == 6)
							return 30;
						else
							if	(mm == 7)
								return 31;
							else
								if	(mm == 8)
									return 31;
								else
									if	(mm == 9)
										return 30;
									else
										if	(mm == 10)
											return 31;
										else
											if	(mm == 11)
												return 30;
											else
												if	(mm == 12)
													return 31;
}

function ChkDate(elm)
{
	if	(elm.value == '')
		return;
	if	(!IsNumber(elm))
	{
		alert ('숫자가 아닌 값이 입력되었습니다.');
		return;
	}
		
	elmstr = '';
	for (i=0; i < elm.value.length; i++)
	{
		if	(elm.value.charAt(i) != '.')
			elmstr = elmstr + elm.value.charAt(i);
	}

	if	(elmstr.length != 8)		//  입력된 숫자가 8자리(YYYYMMDD)인지 검사
	{
		alert('날짜는 20010101 형태로 입력하십시오.');
		elm.focus();
		return false;
	}
	
	y	= elmstr.substring(0,4);
	m	= elmstr.substring(4,6);
	d	= elmstr.substring(6,8);
	yy = parseInt(y);
	mm = parseInt(m);
	dd = parseInt(d);
	if	(dd > LastDay(yy,mm))
	{
		alert( y+'.'+m+'.'+d+'는 올바른 날짜가 아닙니다.');
		elm.focus();
		return false;
	}

	elm.value = y + '.' + m + '.' + d;
	return true;
}
  
  
function InitDate(elm)	
{
	if	(elm.value == '')
		return;
	elmstr = '';
	for (i=0; i < elm.value.length; i++)
	{
		if	((elm.value.charCodeAt(i) >= 48) && (elm.value.charCodeAt(i) <= 57))
			elmstr += elm.value.charAt(i);
	}
	elm.value = elmstr;
	return;
}


function ShowCal(ename, add_bit)
{
	document.all.caldate.value = ename;	// caldate에 달력을 Call한 입력항목명 설정
	if	(add_bit)
		reCal(-1, 26);
	else
		reCal(-1, -6);
}



function dayCho(d)		// 사용자가 선택한 날짜를 날짜입력 항목에 설정하고 달력 숨기기
{
	var s;
	s = document.all("cal_year").value + ".";
	m = parseInt(document.all("cal_month").value);
	if	(m < 10)
		s = s + '0' + m;
	else
		s = s + m;
	s = s + "."
	if	(d < 10)
		s = s + '0' + d;
	else
		s = s + d;
	document.all(document.all.caldate.value).value = s;
	document.all(document.all.caldate.value).focus();
	document.all.cal.style.display = 'none';
}

function checkValid_write(a,aa,b,bb,c,cc,d,dd,e,ee,f,ff)
{	
	if (aa!="")
	{
		if (checkEmpty(a,aa)==false)
			return false;
	}
	if (bb!="")
	{
		if (checkEmpty(b,bb)==false)
			return false;
				if (checkNaString(b,bb)==false)
					return false;
	}
	if (cc!="")
	{
		if (checkEmpty(c,cc)==false)
			return false;
	}
	if (dd!="")
	{
		if (checkEmpty(d,dd)==false)
			return false;
				if (checkEmail(d)==false)
						return false;				
	}
	if (ee!="")
	{
		if (checkEmpty(e,ee)==false)
			return false;
	}
		
	return true;
}


function find()
{
	if(checkEmpty(karl.search,"검색항목")==false)
		return false;
	if(checkETC(karl.search,"검색항목")==false)
		return false;			
	
		karl.submit();
	return true;
}



function sendMail(Amail,Aname)
{
	window.open("/mail/mail.asp?email="+Amail+"&name="+Aname,"karlmail","width=500,height=600");
}
function noMail()
{
	alert("메일주소를 입력하지 않아 메일을 발송할 수 없습니다.");
}

//키보드 event key값 알아내기 함수
function CheckKeyPress() {
 var ekey = event.keyCode ? event.keyCode : event.which ? event.which : event.charCode;
 alert (ekey);
}



function setStartPage()
{
	var Massage = confirm("시작페이지를 http://www.Xromeo.com/으로 하시겠습니까?");

	if (Massage == true) 
	{
		bookmarkurl="http://www.Xromeo.com/" 
		bookmarktitle="What a nice karl " 
		if (document.all)
		window.external.AddFavorite(bookmarkurl,bookmarktitle)
	}
	else
	{
		str = ""
	}
}

function open_window(width,height,title,URL,param)
{
	if (param != "nothing")	URL = URL + "?param='"+param +"'";	
	
    var posx = (screen.width-width)/2-1;
    var posy = (screen.height-height)/2-1;

	var str = "'toolbar=no,location=no,directories=no,status=0,menubar=no,scrollbars=no,resizable=no,copyhistory=no,";
		str = str+"top="+ posy +",left="+ posx +",";
		str = str+"width="+ width +",";
		str = str+"height="+ height +"'";	
		
	var win = window.open(URL,title,str);	
	
	if (win && !win.closed) win.focus();
}

function open_window_popupHtml(width,height,title,URL,param)
{
	if (param != "nothing")	URL = URL + "?param='"+param +"'";	
	
    var posx = (screen.width-width)/2-1;
    var posy = (screen.height-height)/2-1;

	var str = "'toolbar=no,location=no,directories=no,status=0,menubar=no,scrollbars=yes,resizable=no,copyhistory=no,";
		str = str+"top="+ posy +",left="+ posx +",";
		str = str+"width="+ width +",";
		str = str+"height="+ height +"'";	
		
	var win = window.open(URL,title,str);	
	
	if (win && !win.closed) win.focus();
}



function setCookie(name, value, expiredays)
{
	var todayDate = new Date();
        
    todayDate.setDate( todayDate.getDate() + expiredays );
  
    document.cookie = name + "=" + escape( value ) + "; path=/; expires=" + todayDate.toGMTString() + ";";
}

function setCookie_and_closeWin() 
{ 
    if (document.frm_popup.checkNomore.checked) 
		setCookie("notice", "noMore" , 1);  
			this.close(); 
}

function findNoticeCookies(name)
{
	var nameOfCookie = name + "=";
	var x = 0;
	
	while (x <= document.cookie.length)
	{
		var y = (x+nameOfCookie.length);
		
		if (document.cookie.substring( x, y ) == nameOfCookie)
		{
			if ((endOfCookie=document.cookie.indexOf(";",y))== -1)
				endOfCookie = document.cookie.length;
					return unescape(document.cookie.substring(y, endOfCookie));
		}
		
		x = document.cookie.indexOf(" ", x) + 1;
		if (x == 0)
			break;
	}
	return "";
}

function goLink(p)
{
var page = p;

document.location.href=page;
}


function selectAll(frm)
{//이야기 리스트 전체선택	
	if (frm.allCheck.checked == true) 
	{
		var mode = true;
	}
	else
	{
		var mode = false;
	}
	
	if (frm.checkField)
	{//하나이상
		if (frm.checkField.length>0)
		{//배열
			for (i=0;i<frm.checkField.length;i++)
			{
				frm.checkField[i].checked = mode;	
			}
		}
		else
			frm.checkField.checked = mode;		
	}
	else
		return;
	
		
	frm.allCheck.value = mode;
}

function illegalFileFiltering_xls(path)
{
	var imgExten = path.substring(path.lastIndexOf(".")+1,path.length);
	
	var imgExten_lower = imgExten.toLowerCase();
	
	if (imgExten_lower == 'xls')
	{
		return true;
	}
	else
	{
		alert('엑셀 파일만 허용 됩니다.');
			return false;
	}	
}

function checkREP(karl,name)
{
	var str = karl.value;
	for (i=0;i<=(str.length);i++)
	{
		var cha = str.substring(i,i+1);
			if((cha=="'") || (cha=='"'))
			{
				alert(""+ name +"란은 따옴표문자를 허용하지 않습니다.\n\n다시 입력하여 주십시오");
						karl.focus();
							return false;
			}
	}
	return true;
}

function set2char(karl)
{
  var str = karl.value
  
  if(str.length==1)
  {
		str	= "0"+str;
	}
	else
	{
		str = str
	}
	return str;
}






















