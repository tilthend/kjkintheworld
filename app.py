from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return '<button>나는 버튼이다 눌러라!</button>'

@app.route('/mypage')
def mypage():
   return 'mypage 입니다!'

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)