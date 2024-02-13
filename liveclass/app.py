from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print("message was recevied!!")
    # DB에다가 채팅 데이터 저장

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print(f'데이터 수신 완료: {json}')
    socketio.emit('my response', json, callback=messageReceived)
    
if __name__ == "__main__":
    socketio.run(app, debug=True)