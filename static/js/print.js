var authorId = "E4FD8E78-A576-416A-9F7E-FF618ABE3EE0";
var pageOrientation = "0";
var topMargin = "0.5";
var bottomMargin = "0.5";
var leftMargin = "0.5";
var rightMargin = "0.5";




function Installed() {

    if (typeof (document.all("IEPageSetupX")) != "undefined" && document.all("IEPageSetupX") != null)
        return true;
    else
        return false;
}
function Installed2() {
    try {
        return (new ActiveXObject('IEPageSetupX.IEPageSetup'));
    }
    catch (e) {
        return false;
    }
}


function printWindow(header, footer, lm, rm, tm, bm, or, pf) {
    //��üȭ�������� ���
    //����    

    $('#divContents').jqprint("10");        // 20210116 

    //PopupPrint()        // 20210105     by Fred
}

function PopupPrint() {     // 20210105     by Fred
    var data = document.getElementById("divContents");//.innerHTML;
    
    var mywin = window.open();  //("", "", "height=400,width=600");    
    mywin.document.write("<html><body>");        //mywin.document.write(document.getElementById('divContents').innerHTML);
    mywin.document.write(data.innerHTML);
    mywin.document.write("</body></html>");
    mywin.document.close()
    mywin.focus();
    mywin.print();
    mywin.close();    //return true;
}

//
function printWindow2(header, footer, lm, rm, tm, bm, or, pf) {
    //����˾����̾ ���
    $('#print_div').jqprint();
}


//����˾�â�� �ƴ� �Ϲ��˾�â�� ��¸�� (2012.10.24 �������߰�)
function PrintPopWin(header, footer, lm, rm, tm, bm, or, pf) {
    
}

function backup_printWindow(header, footer, lm, rm, tm, bm, or, pf) {
    if (Installed()) {

        //IEPageSetupX.clear();
        //alert(or);
        IEPageSetupX.Orientation = or; 	// ���� �μ���� ����(1:����, 0:����)
        IEPageSetupX.header = header;
        IEPageSetupX.footer = footer;

        IEPageSetupX.leftMargin = lm;
        IEPageSetupX.rightMargin = rm;
        IEPageSetupX.topMargin = tm;
        IEPageSetupX.bottomMargin = bm;

        IEPageSetupX.PaperSize = "A4";

        IEPageSetupX.PrintBackground = true; 	// ���� �� �̹��� �μ�

        if (pf == "p") {
            IEPageSetupX.Preview(); 				// �̸�����
        }
        else {
            //IEPageSetupX.Print();					// �μ�
            IEPageSetupX.Print(true); 		// �μ�(�μ� ��ȭ���� ǥ��)
        }
        //IEPageSetupX.RollBack();			// ���� ���� ������
        //IEPageSetupX.SetDefault();    // �⺻������ ����(���� ���: 0.75mm, �Ӹ���:&w&b������ &p / &P, �ٴڱ�:&u&b&d, ���� �� �̹��� �μ�: ����)
    }
    else
        alert("�μ� ��Ʈ���� ��ġ���� �ʾҽ��ϴ�.\n\n�ùٸ� �μ⸦ ���� �μ� ��Ʈ���� ��ġ�� �ֽʽÿ�.");
}

function printWindowX(header, footer, lm, rm, tm, bm, or, pf) {
    factory.printing.header = header; // �Ӹ����� �����մϴ�.
    factory.printing.footer = footer; // �������� �����մϴ�.
    factory.printing.portrait = or; // ���η� ����Ұ����� ���η� ����Ұ����� �����մϴ�. true:���� false:����
    factory.printing.leftMargin = lm;   // ��������
    factory.printing.rightMargin = rm;   // ��������
    factory.printing.topMargin = tm;   // ��ܿ���
    factory.printing.bottomMargin = bm;   // �ϴܿ���
    //factory.printing.copies          = 1;     // ���常 ���
    //factory.printing.printBackground = true;  // ��׶������ ���
    factory.printing.Print(true, window);     // ���������� ����Ʈ�ϴ¶�(window��ſ� frame�� �������ָ� �ش� �������� ����մϴ�.)
}

function printWindow_test() {
    factory.printing.header = ""
    factory.printing.footer = ""
    factory.printing.portrait = true  //false = ���� ��� , true = ���� ��� 
    factory.printing.leftMargin = 1.0   //  ��������
    factory.printing.topMargin = 1.0   // �� ����
    factory.printing.rightMargin = 0.0  // ��������
    factory.printing.bottomMargin = 3.0  // �Ʒ�����    
    factory.printing.Print(false, window)     //  false = ����Ʈ ��ȭâ�ȿ��� , true = ��ȭâ ����
    location.href = "/NsmdG/BL/WBL210_p102/main"
    //    window = ������ ��ü ��� , �Ǵ� �����Ӹ��� �־ �������� ����Ѵ�.
}

function printWindow_test2() {
    factory.printing.header = ""
    factory.printing.footer = ""
    factory.printing.portrait = true  //false = ���� ��� , true = ���� ��� 
    factory.printing.leftMargin = 0.0   //  ��������
    factory.printing.topMargin = 1.0   // �� ����
    factory.printing.rightMargin = 0.0  // ��������
    factory.printing.bottomMargin = 3.0  // �Ʒ�����    
    //factory.printing.Print(true, window)     //  false = ����Ʈ ��ȭâ�ȿ��� , true = ��ȭâ ����
    
    //    window = ������ ��ü ��� , �Ǵ� �����Ӹ��� �־ �������� ����Ѵ�.
}

function printWindow_base() {
    factory.printing.header = ""
    factory.printing.footer = ""
    factory.printing.portrait = true  //false = ���� ��� , true = ���� ��� 
    factory.printing.leftMargin = 0.0   //  ��������
    factory.printing.topMargin = 1.0   // �� ����
    factory.printing.rightMargin = 0.0  // ��������
    factory.printing.bottomMargin = 3.0  // �Ʒ�����    
    //factory.printing.Print(true, window)     //  false = ����Ʈ ��ȭâ�ȿ��� , true = ��ȭâ ����

    //    window = ������ ��ü ��� , �Ǵ� �����Ӹ��� �־ �������� ����Ѵ�.
}



function ActiveX_print() {
    IEPageSetupX.header = ""; // �������
    IEPageSetupX.footer = ""; // Ǫ�ͼ���
    IEPageSetupX.leftMargin = 10; // ���ʿ��鼳��
    IEPageSetupX.rightMargin = 10; // �����ʿ��� ����
    IEPageSetupX.topMargin = 4; // ���ʿ��� ����
    IEPageSetupX.bottomMargin = 10; // �Ʒ��� ���鼳��
    IEPageSetupX.PrintBackground = true; // ���� �� �̹��� �μ�
    IEPageSetupX.Orientation = 1; // ���� ����� ���Ͻø� 0�� ������ �˴ϴ�. ��������� 1�Դϴ�.

    IEPageSetupX.paper = "A4"; // ���������Դϴ�.
    // IEPageSetupX.Print(); // �μ��ϱ�
    IEPageSetupX.Print(true); // �μ��ȭ���� ����
    // PrintTest(); // ��Ʈ�Ѽ�ġ���� �׽�Ʈ
    // IEPageSetupX.RollBack(); // ���� ���� ������ �ǵ���(�� �ܰ� ������ ����)
    // IEPageSetupX.Clear(); // ������ 0����, �Ӹ���/�ٴڱ��� ��� ����, ���� �� �̹��� �μ� ����
    // IEPageSetupX.SetDefault(); // �⺻������ �ǵ���
    // IEPageSetupX.SetDefault(); // �⺻������ ����(���� ���: 0.75mm, �Ӹ���:&w&b������ &p / &P, �ٴڱ�:&u&b&d, ���� �� �̹��� �μ�: ����)
    // IEPageSetupX.Preview(); // �̸�����
    // IEPageSetupX.SetupPage(); // ����������â ����
}


function ActiveX_print2() {
    IEPageSetupX.header = ""; // �������
    IEPageSetupX.footer = ""; // Ǫ�ͼ���
    IEPageSetupX.leftMargin = 10; // ���ʿ��鼳��
    IEPageSetupX.rightMargin = 10; // �����ʿ��� ����
    IEPageSetupX.topMargin = 4; // ���ʿ��� ����
    IEPageSetupX.bottomMargin = 10; // �Ʒ��� ���鼳��
    IEPageSetupX.PrintBackground = true; // ���� �� �̹��� �μ�
    IEPageSetupX.Orientation = 0; // ���� ����� ���Ͻø� 0�� ������ �˴ϴ�. ��������� 1�Դϴ�.

    IEPageSetupX.paper = "A4"; // ���������Դϴ�.
    // IEPageSetupX.Print(); // �μ��ϱ�
    IEPageSetupX.Print(true); // �μ��ȭ���� ����
    // PrintTest(); // ��Ʈ�Ѽ�ġ���� �׽�Ʈ
    // IEPageSetupX.RollBack(); // ���� ���� ������ �ǵ���(�� �ܰ� ������ ����)
    // IEPageSetupX.Clear(); // ������ 0����, �Ӹ���/�ٴڱ��� ��� ����, ���� �� �̹��� �μ� ����
    // IEPageSetupX.SetDefault(); // �⺻������ �ǵ���
    // IEPageSetupX.SetDefault(); // �⺻������ ����(���� ���: 0.75mm, �Ӹ���:&w&b������ &p / &P, �ٴڱ�:&u&b&d, ���� �� �̹��� �μ�: ����)
    // IEPageSetupX.Preview(); // �̸�����
    // IEPageSetupX.SetupPage(); // ����������â ����
}


//2012.11.13 �� kjh �߰� ����Ʈ ���� ���� ��� ���� �� �ڵ� ���� ����
//ȣ�� �Լ����� ex) PrintPage('0','20','20','20','20','ture','false');
	    var initBody;

	    function beforePrint() {
	        initBody = document.body.innerHTML;
	        document.body.innerHTML = document.getElementById('divContents').innerHTML;
	    }

	    function afterPrint() {
	        document.body.innerHTML = initBody;
	    }

	    function printArea() {
	        window.onbeforeprint = beforePrint;
	        window.onafterprint = afterPrint;
	        window.print();
	    }

	    function PrintPage(dir, lm, rm, tm, bm, alr) {
	        //dir,       lm,    rm,      tm,     bm,                 alr,                  
	        //�μ����,   �޿���,��������,��ܿ���,�Ʒ�����,    0 �� ��� ����μ�
	        //0����1����,  ����ǥ��ex)10 or 15            ,     1 ��  ��� �μ�â����   
	        //                                                  2 ��  ��� �̸�����ȭ��      
          // ���� �뷱���� ��/������ ���� ������ �Ϸ��� �����ʿ� ���� +5�� �ϸ� �˴ϴ�.                                                                          
	           if (Installed()) {
	                
	                window.onbeforeprint = beforePrint;
	                window.onafterprint = afterPrint;
	            
	                window.focus(); //��Ŀ���� �� ����������
	                  
	                IEPageSetupX.Orientation = dir; //�μ� ���� ���� - ����0, ����1
	                IEPageSetupX.header = ''; //�Ӹ���
	                IEPageSetupX.footer = ''; //�ٴڱ�
	                IEPageSetupX.leftMargin = lm; //���ʿ���
	                IEPageSetupX.rightMargin = rm; //�����ʿ���
	                IEPageSetupX.topMargin = tm; //���ʿ���
	                IEPageSetupX.bottomMargin = bm; //�Ʒ��ʿ���
	                IEPageSetupX.PrintBackground = true;
	                IEPageSetupX.ShrinkToFit = true;
	                //IEPageSetupX.Print(true); //�μ�(�μ� ��ȭ���� ǥ��) ture ǥ��
	         
	                if (alr == "0") {
	                    
	                    IEPageSetupX.Print(false);  
	                    }
	                if (alr == "1") {
	                    IEPageSetupX.Print(true);
	                    }
	                if (alr == "2") {
	                    IEPageSetupX.Preview();
	                }
	                if (alr == "4") {
	                    IEPageSetupX.Print(false);
	                    //IEPageSetupX.CloseIE();

	                }

	            }
	            else
	                installX.style.display = 'inline';
	        
	    }		

