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
    //전체화면페이지 출력
    //수정    

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
    //모달팝업레이어만 출력
    $('#print_div').jqprint();
}


//모달팝업창이 아닌 일반팝업창의 출력모드 (2012.10.24 서용진추가)
function PrintPopWin(header, footer, lm, rm, tm, bm, or, pf) {
    
}

function backup_printWindow(header, footer, lm, rm, tm, bm, or, pf) {
    if (Installed()) {

        //IEPageSetupX.clear();
        //alert(or);
        IEPageSetupX.Orientation = or; 	// 가로 인쇄방향 설정(1:세로, 0:가로)
        IEPageSetupX.header = header;
        IEPageSetupX.footer = footer;

        IEPageSetupX.leftMargin = lm;
        IEPageSetupX.rightMargin = rm;
        IEPageSetupX.topMargin = tm;
        IEPageSetupX.bottomMargin = bm;

        IEPageSetupX.PaperSize = "A4";

        IEPageSetupX.PrintBackground = true; 	// 배경색 및 이미지 인쇄

        if (pf == "p") {
            IEPageSetupX.Preview(); 				// 미리보기
        }
        else {
            //IEPageSetupX.Print();					// 인쇄
            IEPageSetupX.Print(true); 		// 인쇄(인쇄 대화상자 표시)
        }
        //IEPageSetupX.RollBack();			// 수정 이전 값으로
        //IEPageSetupX.SetDefault();    // 기본값으로 복원(여백 모두: 0.75mm, 머리글:&w&b페이지 &p / &P, 바닥글:&u&b&d, 배경색 및 이미지 인쇄: 안함)
    }
    else
        alert("인쇄 컨트롤을 설치하지 않았습니다.\n\n올바른 인쇄를 위해 인쇄 컨트롤을 설치해 주십시요.");
}

function printWindowX(header, footer, lm, rm, tm, bm, or, pf) {
    factory.printing.header = header; // 머리말을 설정합니다.
    factory.printing.footer = footer; // 꼬리말을 설정합니다.
    factory.printing.portrait = or; // 세로로 출력할것인지 가로로 출력할것인지 설정합니다. true:세로 false:가로
    factory.printing.leftMargin = lm;   // 좌측여백
    factory.printing.rightMargin = rm;   // 우측여백
    factory.printing.topMargin = tm;   // 상단여백
    factory.printing.bottomMargin = bm;   // 하단여백
    //factory.printing.copies          = 1;     // 한장만 출력
    //factory.printing.printBackground = true;  // 백그라운드까지 출력
    factory.printing.Print(true, window);     // 현재윈도를 프린트하는뜻(window대신에 frame을 지정해주면 해당 프레임을 출력합니다.)
}

function printWindow_test() {
    factory.printing.header = ""
    factory.printing.footer = ""
    factory.printing.portrait = true  //false = 가로 출력 , true = 세로 출력 
    factory.printing.leftMargin = 1.0   //  좌측여백
    factory.printing.topMargin = 1.0   // 위 여백
    factory.printing.rightMargin = 0.0  // 우측여백
    factory.printing.bottomMargin = 3.0  // 아래여백    
    factory.printing.Print(false, window)     //  false = 프린트 대화창안열음 , true = 대화창 열음
    location.href = "/NsmdG/BL/WBL210_p102/main"
    //    window = 윈도우 전체 출력 , 또는 프레임명을 넣어서 프레임을 출력한다.
}

function printWindow_test2() {
    factory.printing.header = ""
    factory.printing.footer = ""
    factory.printing.portrait = true  //false = 가로 출력 , true = 세로 출력 
    factory.printing.leftMargin = 0.0   //  좌측여백
    factory.printing.topMargin = 1.0   // 위 여백
    factory.printing.rightMargin = 0.0  // 우측여백
    factory.printing.bottomMargin = 3.0  // 아래여백    
    //factory.printing.Print(true, window)     //  false = 프린트 대화창안열음 , true = 대화창 열음
    
    //    window = 윈도우 전체 출력 , 또는 프레임명을 넣어서 프레임을 출력한다.
}

function printWindow_base() {
    factory.printing.header = ""
    factory.printing.footer = ""
    factory.printing.portrait = true  //false = 가로 출력 , true = 세로 출력 
    factory.printing.leftMargin = 0.0   //  좌측여백
    factory.printing.topMargin = 1.0   // 위 여백
    factory.printing.rightMargin = 0.0  // 우측여백
    factory.printing.bottomMargin = 3.0  // 아래여백    
    //factory.printing.Print(true, window)     //  false = 프린트 대화창안열음 , true = 대화창 열음

    //    window = 윈도우 전체 출력 , 또는 프레임명을 넣어서 프레임을 출력한다.
}



function ActiveX_print() {
    IEPageSetupX.header = ""; // 헤더설정
    IEPageSetupX.footer = ""; // 푸터설정
    IEPageSetupX.leftMargin = 10; // 왼쪽여백설정
    IEPageSetupX.rightMargin = 10; // 오른쪽여백 설정
    IEPageSetupX.topMargin = 4; // 윗쪽여백 설정
    IEPageSetupX.bottomMargin = 10; // 아랫쪽 여백설정
    IEPageSetupX.PrintBackground = true; // 배경색 및 이미지 인쇄
    IEPageSetupX.Orientation = 1; // 가로 출력을 원하시면 0을 넣으면 됩니다. 세로출력은 1입니다.

    IEPageSetupX.paper = "A4"; // 용지설정입니다.
    // IEPageSetupX.Print(); // 인쇄하기
    IEPageSetupX.Print(true); // 인쇄대화상자 띄우기
    // PrintTest(); // 컨트롤설치여부 테스트
    // IEPageSetupX.RollBack(); // 수정 이전 값으로 되돌림(한 단계 이전만 지원)
    // IEPageSetupX.Clear(); // 여백은 0으로, 머리글/바닥글은 모두 제거, 배경색 및 이미지 인쇄 안함
    // IEPageSetupX.SetDefault(); // 기본값으로 되돌림
    // IEPageSetupX.SetDefault(); // 기본값으로 복원(여백 모두: 0.75mm, 머리글:&w&b페이지 &p / &P, 바닥글:&u&b&d, 배경색 및 이미지 인쇄: 안함)
    // IEPageSetupX.Preview(); // 미리보기
    // IEPageSetupX.SetupPage(); // 페이지설정창 띄우기
}


function ActiveX_print2() {
    IEPageSetupX.header = ""; // 헤더설정
    IEPageSetupX.footer = ""; // 푸터설정
    IEPageSetupX.leftMargin = 10; // 왼쪽여백설정
    IEPageSetupX.rightMargin = 10; // 오른쪽여백 설정
    IEPageSetupX.topMargin = 4; // 윗쪽여백 설정
    IEPageSetupX.bottomMargin = 10; // 아랫쪽 여백설정
    IEPageSetupX.PrintBackground = true; // 배경색 및 이미지 인쇄
    IEPageSetupX.Orientation = 0; // 가로 출력을 원하시면 0을 넣으면 됩니다. 세로출력은 1입니다.

    IEPageSetupX.paper = "A4"; // 용지설정입니다.
    // IEPageSetupX.Print(); // 인쇄하기
    IEPageSetupX.Print(true); // 인쇄대화상자 띄우기
    // PrintTest(); // 컨트롤설치여부 테스트
    // IEPageSetupX.RollBack(); // 수정 이전 값으로 되돌림(한 단계 이전만 지원)
    // IEPageSetupX.Clear(); // 여백은 0으로, 머리글/바닥글은 모두 제거, 배경색 및 이미지 인쇄 안함
    // IEPageSetupX.SetDefault(); // 기본값으로 되돌림
    // IEPageSetupX.SetDefault(); // 기본값으로 복원(여백 모두: 0.75mm, 머리글:&w&b페이지 &p / &P, 바닥글:&u&b&d, 배경색 및 이미지 인쇄: 안함)
    // IEPageSetupX.Preview(); // 미리보기
    // IEPageSetupX.SetupPage(); // 페이지설정창 띄우기
}


//2012.11.13 일 kjh 추가 프린트 가로 세로 출력 가능 및 자동 비율 조절
//호출 함수명은 ex) PrintPage('0','20','20','20','20','ture','false');
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
	        //인쇄방향,   왼여백,오른여백,상단여백,아래여백,    0 일 경우 즉시인쇄
	        //0가로1세로,  숫자표시ex)10 or 15            ,     1 일  경우 인쇄창띄우기   
	        //                                                  2 일  경우 미리보기화면      
          // 여백 밸런스는 왼/오른쪽 같게 나오게 하려면 오른쪽에 여백 +5를 하면 됩니다.                                                                          
	           if (Installed()) {
	                
	                window.onbeforeprint = beforePrint;
	                window.onafterprint = afterPrint;
	            
	                window.focus(); //포커스를 이 프레임으로
	                  
	                IEPageSetupX.Orientation = dir; //인쇄 방향 설정 - 가로0, 세로1
	                IEPageSetupX.header = ''; //머리글
	                IEPageSetupX.footer = ''; //바닥글
	                IEPageSetupX.leftMargin = lm; //왼쪽여백
	                IEPageSetupX.rightMargin = rm; //오른쪽여백
	                IEPageSetupX.topMargin = tm; //위쪽여백
	                IEPageSetupX.bottomMargin = bm; //아래쪽여백
	                IEPageSetupX.PrintBackground = true;
	                IEPageSetupX.ShrinkToFit = true;
	                //IEPageSetupX.Print(true); //인쇄(인쇄 대화상자 표시) ture 표시
	         
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

