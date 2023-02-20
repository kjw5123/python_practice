from flask import Flask, Response
from markupsafe import escape
import json
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


attendance = [0]
attendance_total = []

def calculate_level(name):
    return attendance.index(name)


@app.route('/')
def main():
     return '방문해주셔서 감사합니다. 강의실 입니다. 학생들은 주소에 자신의 성명을 기입해주시길 바랍니다.'


@app.route('/students/<name>')
def show_students_name(name):
     
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


if __name__ == '__main__':
    app.run()