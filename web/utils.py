from django.utils.crypto import get_random_string
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from string import Template
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
from rlink.settings import SECRET_KEY, ALGORITHM, CERTIFIED_MAIL, CERTIFIED_PW, BASE_PATH, FIREBASE_API_KEY
import os, math, random, re
import copy, requests, json
import smtplib, logging, hashlib
from datetime import datetime
import threading


logger = logging.getLogger("web")

cntperpage = 10
ChatURL = 'http://175.207.29.133:8080'


def genPageOjb(request, listdata):
    paginator = Paginator(listdata, cntperpage)
    if 'page' in request.GET:
        page = request.GET["page"]
        try:
            pdata = paginator.page(page)
        except PageNotAnInteger:
            pdata = paginator.page(1)
        except EmptyPage:
            pdata = paginator.page(paginator.num_pages)
        return pdata
    else:
        return paginator.get_page(1)

def genPageOjbPost(request, listdata):
    paginator = Paginator(listdata, cntperpage)
    if 'page' in request.POST:
        page = request.POST["page"]
        try:
            pdata = paginator.page(page)
        except PageNotAnInteger:
            pdata = paginator.page(1)
        except EmptyPage:
            pdata = paginator.page(paginator.num_pages)
        return pdata
    else:
        return paginator.get_page(1)

def genPageInfo(request, pageOjb):
    pagelist = ''
    if request.method == 'GET':
        pagelist = genPageOjb(request, pageOjb)
    elif request.method == 'POST':
        pagelist = genPageOjbPost(request, pageOjb)
    ntcrange = []
    for i in pagelist.paginator.page_range:
        ntcrange.append(i)

    pageinfo = {"has_previous": pagelist.has_previous(), "num_pages": ntcrange, "number": pagelist.number, "has_next": pagelist.has_next()}
    return pageinfo

def loopCounter(listdata):
    count = (listdata.number - 1) * 10
    return count

def funcCodeValue(codelist, keyval):
    for c in codelist:
        if c["key"] == keyval:
            return c["value"]
    return None


def checkLogin(request, pagename):
    u_no = request.session.get("u_no", '')
    u_access = request.session.get("u_access", '')
    access = ""
    if u_access == 1 and ("/com_" in request.path or "/admin_" in request.path):
        access = "/"
    elif u_access == 2 and "/com_" not in request.path:
        access = "/com_req_list"
    elif u_access == 3 and "/admin_" not in request.path:
        access = "/admin_req_list"
    logger.debug(f'checkLogin : {pagename},{request.method}, u_no : {u_no}')
    if not u_no:
        return False, False
    else:
        return u_no, access


def postPageOjb(request, listdata):
    paginator = Paginator(listdata, cntperpage)
    if 'page' in request.POST:
        page = request.POST["page"]
        try:
            pdata = paginator.page(page)
        except PageNotAnInteger:
            pdata = paginator.page(1)
        except EmptyPage:
            pdata = paginator.page(paginator.num_pages)
        return pdata
    else:
        return paginator.get_page(1)

# 게시판
def chgBoardTitle(c_name):
    title = c_name + "의 업체정보가 변경되었습니다."
    return title

def chgBoardText(c_name):
    text = '<p>안녕하세요. 세공입니다.</p><p>' + c_name + '의 업체정보가 변경되었습니다.</p><a "javascript:void(0)" onclick="compDetail()" ' \
                                                'style="cursor: pointer; display: inline-block; color: black; text-decoration: underline; margin: 20px 0; text-underline-position: under;">업체정보 확인하기 ></a><br><p>감사합니다.</p>'
    return text

def makeBoardTitle(c_name):
    title = c_name + "이(가) 제휴업체로 등록되었습니다."
    return title

def makeBoardText(c_name):
    text = '<p>안녕하세요. 세공입니다.</p><p>' + c_name + '이(가) 세공의 제휴업체로 새롭게 등록되었습니다.</p><a "javascript:void(0)" onclick="compDetail()" ' \
                                                'style="cursor: pointer; display: inline-block; color: black; text-decoration: underline; margin: 20px 0; text-underline-position: under;">업체정보 확인하기 ></a><br><p>감사합니다.</p>'
    return text

def chatUserReg(username):
    try:
        URL = ChatURL + "/signup?username="+username
        headers = {'content-type': 'application/x-www-form-urlencoded; charset=utf-8'}
        # data = {'username': username}
        # res = requests.post(URL, headers=headers, data=json.dumps(data))
        response = requests.get(URL, headers=headers)
        jsonrst = json.loads(response.text)
        print(f'chatUserReg rst=> {jsonrst}')
        if jsonrst["success"]:
            return jsonrst["u_no"]
        else:
            return False
    except Exception as e:
            logger.error(f'chatUserReg error : {e}')
            return False

def chatUserList(uid):
    try:
        URL = ChatURL + "/api/v1/user?uid="+str(uid)
        headers = {'content-type': 'application/x-www-form-urlencoded; charset=utf-8'}
        # data = {'username': username}
        # res = requests.post(URL, headers=headers, data=json.dumps(data))
        response = requests.get(URL, headers=headers)
        jsonrst = json.loads(response.text)
        print(f'chatUserList rst=> {jsonrst}')
        if jsonrst:
            return jsonrst
        else:
            return []
    except Exception as e:
            logger.error(f'chatUserList error : {e}')
            return False


def chatUserChatList(chat_uno):
    try:
        URL = ChatURL + "/recent_chat_history?u_no="+str(chat_uno)
        headers = {'content-type': 'application/x-www-form-urlencoded; charset=utf-8'}
        # data = {'username': username}
        # res = requests.post(URL, headers=headers, data=json.dumps(data))
        response = requests.get(URL, headers=headers)
        jsonrst = json.loads(response.text)
        print(f'chatUserChatList rst=> {jsonrst}')
        if jsonrst["success"]:
            return jsonrst["rst"]
        else:
            return False
    except Exception as e:
            logger.error(f'chatUserChatList error : {e}')
            return False

def _createHash(val):
    """This function generate 10 character long hash"""
    hash = hashlib.sha3_256()
    hash.update(val.encode(encoding="utf-8"))
    return  hash.hexdigest()[:-10]

def makeFileHashName(filename):
    try:
        parts = os.path.splitext(filename)
        return _createHash(parts[0])+parts[1]
    except Exception as e:
        print(e)
        return False

def saveFileServer(u_no, filename, file, path=None):
    try:
        uploadpath = ''
        try:
            uploadpath = os.path.join('', str(u_no))
            if path:
                uploadpath = os.path.join(uploadpath, path)
            os.mkdir(uploadpath)
        except Exception as e:
            pass

        fs = FileSystemStorage()
        parts = os.path.splitext(filename)
        savefilename = fs.save(uploadpath + '/' + _createHash(parts[0])+parts[1], file)
        uploaded_file_url = fs.url(savefilename)
        print('uploaded_file_url:', uploaded_file_url)
        return uploaded_file_url
    except Exception as e:
        print(e)
        return False


class EmailHTMLImageContent:
    def __init__(self, str_subject, str_image_file_name, str_cid_name, template, template_params):
        # """이미지파일(str_image_file_name), 컨텐츠ID(str_cid_name)사용된 string template과 딕셔너리형 template_params받아 MIME 메시지를 만든다"""
        assert isinstance(template, Template)
        assert isinstance(template_params, dict)
        self.msg = MIMEMultipart()
        # e메일 제목을 설정한다
        self.msg['Subject'] = str_subject  # e메일 제목을 설정한다

        # e메일 본문을 설정한다
        str_msg = template.safe_substitute(
            **template_params)  # ${변수} 치환하며 문자열 만든다
        # MIME HTML 문자열을 만든다
        mime_msg = MIMEText(str_msg, 'html')
        self.msg.attach(mime_msg)

        '''
        # e메일 본문에 이미지를 임베딩한다
        assert os.path.isfile(
            str_image_file_name), 'image file does not exist.'
        with open(str_image_file_name, 'rb') as img_file:
            mime_img = MIMEImage(img_file.read())
            mime_img.add_header('Content-ID', '<' + str_cid_name + '>')
        self.msg.attach(mime_img)

        with open(BASE_PATH+'/static/img/back_1.png', 'rb') as a:
            back1_img = MIMEImage(a.read())
            back1_img.add_header('Content-ID', '<' + 'backimage1' + '>')
        self.msg.attach(back1_img)
        '''

    def get_message(self, str_from_email_addr, str_to_eamil_addrs):
        # """발신자, 수신자리스트를 이용하여 보낼메시지를 만든다 """
        mm = copy.deepcopy(self.msg)
        mm['From'] = str_from_email_addr          # 발신자
        mm['To'] = ",".join(str_to_eamil_addrs)  # 수신자리스트
        return mm


class EmailSender:
    # """e메일 발송자"""
    def __init__(self):
        # """호스트와 포트번호로 SMTP로 연결한다 """
        # self.str_host = str_host
        # self.num_port = num_port
        self.ss = smtplib.SMTP('smtp.gmail.com', 587)
        # SMTP인증이 필요하면 아래 주석을 해제하세요.
        self.ss.starttls()  # TLS(Transport Layer Security) 시작
        self.ss.login(CERTIFIED_MAIL, CERTIFIED_PW)  # 메일서버에 연결한 계정과 비밀번호

    def send_message(self, emailContent, str_from_email_addr, str_to_email_addrs):
        # """e메일을 발송한다 """
        cc = emailContent.get_message(str_from_email_addr, str_to_email_addrs)
        self.ss.send_message(
            cc, from_addr=str_from_email_addr, to_addrs=str_to_email_addrs)
        del cc
        self.ss.quit()

def getRandomPw():
    str = get_random_string(length=8)
    return str


def sendEmailSecretNum(email, snum):
    str_subject = '세공 비밀번호 변경확인 이메일'
    go_site = 'https://www.rlink.co.kr'
    CERTIFIED_MAIL = 'contact@rlink.co.kr'
    sendemail = EmailSender()
    template = Template(
        """
            <!DOCTYPE html>
            <html lang="ko">
            <head>
              <meta charset="utf-8" />
              <meta name="viewport" content="width=device-width, initial-scale=1">
              <title></title>
            </head>
            <body style="margin:0; padding:0; width: 100%;">
            <div class="wrap" style="width: 525px; height: auto;margin: 0 auto;border: 1px solid #ccc;">
              <div style="height: 60px; background-color: #6866F7; display: flex; align-items: center; padding: 0 50px;">
                <img src="/static/img/logo.svg" alt="">
                <span style="margin-left: 16px; color: #B3B2FB; font-size: 12px;">세탁은 세공</span>
              </div>
              <div style="padding: 60px 50px;">
                <p style="margin: 0;line-height: 21px; font-size: 14px; color: #666;">안녕하세요. <br>세공을 이용해주셔서 감사합니다.</p>
                <div style="font-size: 30px; font-family: 'Roboto', sans-serif; font-weight: 700;line-height: 36px;margin: 60px 0;">
                  """+ snum +"""
                </div>
                <p style="margin: 0;line-height: 21px; font-size: 14px; color: #666;">본 메일은 발신전용으로 회신이 불가합니다. <br>감사합니다.<br><br>세공 팀 드림</p>
              </div>
              <div style="background-color: #F2F5F6; height: 35px;display: block"></div>
            </div>
            </body>
            </html>
        """
    )

    template_params = {'NAME': email}
    emailHTMLImageContent = EmailHTMLImageContent(
        str_subject, '', '', template, template_params)

    str_from_email_addr = CERTIFIED_MAIL  # 발신자
    str_to_email_addrs = [email]  # 수신자리스트
    sendemail.send_message(emailHTMLImageContent, str_from_email_addr, str_to_email_addrs)
