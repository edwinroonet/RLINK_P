from django.shortcuts import render, redirect
import json, os
import logging
from django.core.files.storage import FileSystemStorage
from web.view.base.baseController import *
from web.view.base.commonFunction import *
from web.view.base.param_filter import *
from web.view.base.Config import Config

logger = logging.getLogger(__name__)

FileUtilVO = dict()
FileUtilVO.update(BaseVO)
FileUtilVO["NewFileName"] = ""
FileUtilVO["OriginFileName"] = ""
FileUtilVO["FileSize"] = ""
FileUtilVO["FileType"] = ""


def fnUpload(request, fileFieldName, db_method):
	if fileFieldName in request.FILES:
		_file = request.FILES[fileFieldName]
		#request.FILES.getlist('files')
	return fileUpload(request, _file, db_method, "")

def fileUpload(request, _file, db_method, oldFile):
	_fileUtilVO = FileUtilVO
	_sessionInfo = getSession(request, "LoginInfo")
	countFileName = 1


	if not _sessionInfo:
		return _fileUtilVO

	if len(_file) > 0:
		filename = _file.name
		filename = filename.replace("!", "-")
		filename = filename.replace("@", "-")
		filename = filename.replace("#", "-")
		filename = filename.replace("$", "-")
		filename = filename.replace("%", "-")
		filename = filename.replace("^", "-")
		filename = filename.replace("&", "-")
		filename = filename.replace("*", "-")

		fs = FileSystemStorage()
		parts = os.path.splitext(filename)
		strName = parts[0] # 파일명
		strExt = parts[1] #확장자

		path = os.path.join('', Config.reservedPath)
		_dPath = path + "/" + _sessionInfo["OfficeNo"]
		
		_fileUtilVO["errCode"] = "0"

		# 필터 적용 업로드가능 확장자 추가
		if fnFileCheck(filename) == False:
			_fileUtilVO["errCode"] = "1"
			_fileUtilVO["errMsg"] = alertMsg("허가되지 않은 파일 양식 입니다.", "")
			return _fileUtilVO
		# 파일용량 체크
		if _file._size > 102400000:
			_fileUtilVO["errCode"] = "1"
			_fileUtilVO["errMsg"] = ("<script language=javascript>"
								   + "alert(formatnumber(10240000/1024000,1) & 'M 이상의 사이즈인 파일은 업로드하실 수 없습니다');"
								   + "history.back();"
								   + "</script>")
		else:
			# 폴더 존재 여부 체크
			if not os.path.isdir(_dPath):
				os.mkdir(path)
			# 파일 경로 생성
			_path = os.path.join(_dPath, filename)
			# db_method가 수정(EDIT)일경우 해당 pFileNm 파일명이 존재할 경우 삭제 처리
			if db_method.upper() == "EDIT":
				if not (oldFile == "" or not oldFile):
					dFile = os.path.join(_dPath, oldFile)
					if os.path.isfile(dFile):
						try:
							os.remove(dFile)
						except Exception as e:
							logger.exception(f'fileUpload {dFile} removefile error : {e}')
			# 같은이름의 파일 여부 체크
			file_list = os.listdir(_dPath)
			for f in file_list:
				if f == os.path.isfile(_path):
					filename = strName + "(" + countFileName + ")" + strExt
					_path = os.path.join(_dPath, filename)
					countFileName = countFileName + 1

			# 파일 저장
			savefilename = fs.save(_path, _file)
			uploaded_file_url = fs.url(savefilename)

			# 처리 여부 설정
			_fileUtilVO["errMsg"] = "성공"
			_fileUtilVO["FileSize"] = _file._size
			_fileUtilVO["FileType"] = strExt
			_fileUtilVO["OriginFileName"] = _file.name
			_fileUtilVO["NewFileName"] = filename

	else:
		# 첨부파일이 없을겨우에는 오류가 아니므로 fileUtilVO.errCode = 0 으로 설정
		# 첨부파일이 없고 기존에 업로드한 파일이 있을 경우 기존 파일명으로 대체
		_fileUtilVO["errCode"] = "0"
		_fileUtilVO["errMsg"] = "첨부파일 없음"
		_fileUtilVO["FileType"] = oldFile.split(".")[-1]
		_fileUtilVO["OriginFileName"] = oldFile
		_fileUtilVO["NewFileName"] = oldFile

	return _fileUtilVO








