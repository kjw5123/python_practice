from flask import Flask, Response, request
from markupsafe import escape
import json
import requests

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False



attendance = [0]
attendance_total = []
password = {}
articles = {}


def calculate_level(name):
    return attendance.index(name)

# url = 'http://localhost:5000/'

@app.route('/')
def main():
     return '방문해주셔서 감사합니다. 강의실 입니다. 학생들은 주소에 자신의 성명을 기입해주시길 바랍니다.'


@app.route('/students/<name>', methods = ['POST', 'GET'])
def show_students_name(name): 

     if request.method == 'POST':   
          # body 값은 "password": "123123" 이런 형태
          if name in attendance: # 학생이 GET으로 사이트에 출석 한 경우,
               if name in password: #이미 학생에 비밀번호가 입력 된 경우,
                    data = request.json
                    pw = data['password']
                    password.setdefault(name)
                    password[name] = pw
                    print(password)
                    return '비밀번호가 재입력 되었습니다.'
               else: #학생이 처음으로 비밀번호 입력하는 경우
                    data = request.json
                    pw = data['password']
                    password.setdefault(name)
                    password[name] = pw
                    print(password)
                    return '비밀번호를 입력받았습니다.'
          else:
               return '존재하지 않는 학생 입니다.'
          
     if name in attendance:
          return '반복입력하지 마세요.'
     elif name not in attendance:
          attendance.append(name)
          a_int = calculate_level(name)
          return 'students %s, 당신은 %s 번째로 출석하셨습니다.' %(name, a_int)


@app.route('/students')
def show_students_attendance():
     attendance_total.clear()                
     attendance2 = attendance.copy()
     attendance2.remove(0)

     for i , name in enumerate(attendance2):
          attendance_total.append('%s: %d등' %(name, i + 1))
          
     if attendance_total == []:
          return '아무도 출석하지 않았습니다.'
     else: 
          return json.dumps(attendance_total, ensure_ascii=False).encode('utf8')


@app.route('/students/<name>/panty-run')
def remove_students_information(name):
    attendance.remove(name)
    return '"%s"... 전우애 실시 ! 악 !! ' %escape(name)


@app.route('/students/<name>/articles', methods = ["GET", "POST", "DELETE"])
def edit_article(name):
     if request.method == "POST":

          data = request.json # '<name>':'(하고 싶은 말)' 이런 형태로 post
          print(data)

          if (name) not in password:
               return '학생정보 혹은 비밀번호부터 입력하시오.'

          elif name in password:
               article = data[name]
               articles.setdefault(name)

               if articles[name] == None:
                    articles[name] = []               
               
               articles[name].append(article)
               print(articles)
               return '문장이 입력되었습니다.'
     
     if request.method == "DELETE":
          if request.args.get('no') == None: 
               if articles[name] == None: #학생의 이름에 관련된 게시물이 없을 경우
                    return '존재하지 않는 학생입니다.'
               else: #젠부 샤쓰
                    del articles[name] 
                    print(articles)
                    return Response("", status=204, mimetype='application/json')
          else:
               if articles[name] == None: # 학생의 이름에 관련된 게시물이 없을 경우
                    return '존재하지 않는 학생입니다.'
               else: #입력 된 쿼리 스트링에 따른, 학생의 게시물을 없애버림
                    del (articles[name][int(request.args.get('no')) - 1])
                    print(articles)
                    return Response("", status = 204, mimetype = 'application/json')
          
     if name not in password:
          return '학생정보 혹은 비밀번호부터 입력하시오.'
     else:
          if request.args.get('no') == None: #여지껏 학생이 작성한 게시글 전부 사이트에 노출
               return articles[name]
          else: #쿼리 스트링에 따른 특정 게시글만 사이트에 노출
               a = articles[name][int(request.args.get('no')) - 1]
               print(a)
               return a


if __name__ == '__main__':
    app.run()