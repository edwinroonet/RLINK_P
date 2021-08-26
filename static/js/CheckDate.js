 
function funcCheckDate(strDate)	
{	
	var bIsDateOk;
	
	bIsDayOk = true;
	
	//전체문자열의 길이 체크
//	alert(strDate);
	if (strDate.length != 8)
	{	
		alert("날짜는 8자리로 입력하셔야 합니다.\n\n일자 형식은 YYYYMMDD 입니다.");
		return false;
	}
	
	//숫자인지 체크
	if (!funcAreTheyDigits(strDate))
	{
		alert("날짜에는 숫자만 입력가능합니다.");
		return false;
	}
		
	var nYear = parseInt(strDate.substring(0, 4), 10);	
	var nMonth = strDate.substring(4, 6)
	var nDay = parseInt(strDate.substring(6, 8), 10);	
	
	//년도 검사
	if (nYear < 1900 || nYear > 2078)
	{
		alert("년도는 1900년부터 2078년까지만 가능합니다.");
		return false;
	}
	
	//월검사
	if (nMonth < 1 || nMonth > 12)
	{
		alert("월의 입력이 잘못되었습니다.");
		return false;	
	}
	
	//일검사
	// 31일이 있는달    
    if (((nMonth > 7) && !(nMonth % 2)) || ((nMonth < 8) && (nMonth % 2)))
    {
		if (nDay > 31 )
			bIsDayOk = false;
    // 2월달
    } else if (nMonth == 2){
        if (!(nYear % 400) || (!(nYear % 4) && (nYear % 100)))
        {
			if (nDay > 29)
            {
            	bIsDayOk = false;
            }
        }
        else
        {
            if (nDay > 28)
            {
				bIsDayOk = false;
			}
        }
    // 30일만 있는달
    } else {
        if (nDay > 30)
        {
			bIsDayOk = false;
		}
    }  
  
	if (!bIsDayOk) 
	{
		alert("입력하신 일자는 없는 일자입니다.");
	}
	
	return bIsDayOk
}


function funcCheckHour(strDate)	
{
	bIsDayOk = true;
	
	//전체문자열의 길이 체크
	if (strDate.length != 2)
	{	
		alert("시간은 2자리로 입력하셔야 합니다.");
		return false;
	}
	
	//숫자인지 체크
	if (!funcAreTheyDigits(strDate))
	{
		alert("시간에는 숫자만 입력가능합니다.");
		return false;
	}
		
	//년도 검사
	if (strDate < 0 || strDate > 24)
	{
		alert("시간은 00시부터 24시까지만 가능합니다.");
		return false;
	}
	
	
	return bIsDayOk
}

function funcCheckMin(strDate)	
{
	bIsDayOk = true;
	//전체문자열의 길이 체크
	if (strDate.length != 2)
	{	
		alert("시간은 2자리로 입력하셔야 합니다.");
		return false;
	}
	
	//숫자인지 체크
	if (!funcAreTheyDigits(strDate))
	{
		alert("분에는 숫자만 입력가능합니다.");
		return false;
	}
		
	//년도 검사
	if (strDate < 0 || strDate > 59)
	{
		alert("분은 00분부터 59분까지만 가능합니다.");
		return false;
	}
	
	
	return bIsDayOk
}

function funcIsDigit (c)
{
	return ((c >= "0") && (c <= "9"))
}

function funcAreTheyDigits (vTemp)
{
	for (i = 0 ; (i < vTemp.length && funcIsDigit(vTemp.charAt(i))) ; i++)
	{
		;
	}

	if (i == vTemp.length)
		return true;
	else
		return false;
}