#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()
import sqlite3 # 데이터베이스 접근
import sys # 종료
import configparser # 설정파일 읽기

def _fail_response(user_id, user_mac):
    """등록 실패 응답
    """
    print("<html>")
    print("<head>")
    print("  <title>DNLab 출석부</title>")
    print("</head>")
    print("<body>")
    print("  <h1>MAC주소 등록에 실패했습니다.</h1>")
    print("  <h1>개발자에게 알려주세요.</h1>")
    print("  <h2>입력된 정보: {0} {1}</h2>".format(user_id, user_mac))
    print("  <a href='/index.html'>메인페이지로 가기</a>")
    print("</body>")
    print("</html>")


def _success_response(user_id, user_mac):
    """등록 성공 응답
    """
    print("<html>")
    print("<head>")
    print("  <title>DNLab 출석부</title>")
    print("</head>")
    print("<body>")
    print("  <h1>MAC주소가 등록되었습니다.</h1>")
    print("  <h2>안녕하세요. {0} {1}</h2>".format(user_id, user_mac))
    print("  <a href='/index.html'>메인페이지로 가기</a>")
    print("</body>")
    print("</html>")


# 응답 헤더
print("Content-type:text/html\r\n\r\n")
# 유저 학번 / MAC 주소
form = cgi.FieldStorage()
user_id = form.getvalue('id')
if user_id == None:
    user_id = ' '
user_mac  = form.getvalue('mac')
if user_mac == None:
    user_mac = ' '
user_mac = user_mac.upper()
# 유저 아이디 확인
if not user_id.isdigit():
    _fail_response(user_id, user_mac)
    sys.exit(0)
# ini 파일 읽어오기
config_file = 'class_server.ini' # 하드 코딩
config = configparser.ConfigParser()
config.read(config_file)
# 변수 생성
user_db = config['server']['user_db']
# 데이터베이스 연결
connector = sqlite3.connect(user_db)
cursor = connector.cursor()
try:
    cursor.executescript('''
            UPDATE OR IGNORE user
            SET '''
            + 'id="' + user_id + '", '
            + 'mac="' + user_mac + '" '
            + '''WHERE '''
            + 'id="' + user_id + '";'
            + '\n'
            + 'INSERT OR IGNORE INTO user '
            + '(id, mac) VALUES ('
            + '"' + user_id + '", '
            + '"' + user_mac + '");')
    connector.commit()
    _success_response(user_id, user_mac)
except Exception as err:
    _fail_response(user_id, user_mac)
    print(err)
