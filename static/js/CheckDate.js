 
function funcCheckDate(strDate)	
{	
	var bIsDateOk;
	
	bIsDayOk = true;
	
	//��ü���ڿ��� ���� üũ
//	alert(strDate);
	if (strDate.length != 8)
	{	
		alert("��¥�� 8�ڸ��� �Է��ϼž� �մϴ�.\n\n���� ������ YYYYMMDD �Դϴ�.");
		return false;
	}
	
	//�������� üũ
	if (!funcAreTheyDigits(strDate))
	{
		alert("��¥���� ���ڸ� �Է°����մϴ�.");
		return false;
	}
		
	var nYear = parseInt(strDate.substring(0, 4), 10);	
	var nMonth = strDate.substring(4, 6)
	var nDay = parseInt(strDate.substring(6, 8), 10);	
	
	//�⵵ �˻�
	if (nYear < 1900 || nYear > 2078)
	{
		alert("�⵵�� 1900����� 2078������� �����մϴ�.");
		return false;
	}
	
	//���˻�
	if (nMonth < 1 || nMonth > 12)
	{
		alert("���� �Է��� �߸��Ǿ����ϴ�.");
		return false;	
	}
	
	//�ϰ˻�
	// 31���� �ִ´�    
    if (((nMonth > 7) && !(nMonth % 2)) || ((nMonth < 8) && (nMonth % 2)))
    {
		if (nDay > 31 )
			bIsDayOk = false;
    // 2����
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
    // 30�ϸ� �ִ´�
    } else {
        if (nDay > 30)
        {
			bIsDayOk = false;
		}
    }  
  
	if (!bIsDayOk) 
	{
		alert("�Է��Ͻ� ���ڴ� ���� �����Դϴ�.");
	}
	
	return bIsDayOk
}


function funcCheckHour(strDate)	
{
	bIsDayOk = true;
	
	//��ü���ڿ��� ���� üũ
	if (strDate.length != 2)
	{	
		alert("�ð��� 2�ڸ��� �Է��ϼž� �մϴ�.");
		return false;
	}
	
	//�������� üũ
	if (!funcAreTheyDigits(strDate))
	{
		alert("�ð����� ���ڸ� �Է°����մϴ�.");
		return false;
	}
		
	//�⵵ �˻�
	if (strDate < 0 || strDate > 24)
	{
		alert("�ð��� 00�ú��� 24�ñ����� �����մϴ�.");
		return false;
	}
	
	
	return bIsDayOk
}

function funcCheckMin(strDate)	
{
	bIsDayOk = true;
	//��ü���ڿ��� ���� üũ
	if (strDate.length != 2)
	{	
		alert("�ð��� 2�ڸ��� �Է��ϼž� �մϴ�.");
		return false;
	}
	
	//�������� üũ
	if (!funcAreTheyDigits(strDate))
	{
		alert("�п��� ���ڸ� �Է°����մϴ�.");
		return false;
	}
		
	//�⵵ �˻�
	if (strDate < 0 || strDate > 59)
	{
		alert("���� 00�к��� 59�б����� �����մϴ�.");
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