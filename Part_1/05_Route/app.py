from flask import Flask, request, Response

app = Flask(__name__)

# 기본 경로에 대한 라우트 
@app.route('/')
def home():
    return 'Hello, this is the home page!'

# 다른 경로에 대한 라우트
# 127.0.0.1:5000/about
@app.route('/about')
def about():
    return 'This is the about page.'

# 127.0.0.1:5000/project
@app.route('/project')
def project():
    return 'The project page'

# 동적인 URL 파라미터 사용
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

@app.route('/number/<int:number>')
def number(number):
    return f'Number: {number}'

# post 요청 날리는 법
# (1) postman
# (2) requests

import requests
# pip install requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)

    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")

    if request.method == 'POST':
        print("***POST method***", request.data)
    
    return Response("success", status=200)

# URL에 변수 및 타입 지정
@app.route('/post<int:post_id>')
def show_post(post_id):
    return f'Post ID : {post_id}'


