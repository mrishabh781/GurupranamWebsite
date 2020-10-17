from flask import Flask, render_template, request, url_for
from flask_socketio import SocketIO, join_room, leave_room
from database import get_message, save_message


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    x = str(request.headers.get('User-Agent'))
    print(x)
    if 'Android' in x or 'Mobile' in x:
        return render_template("mobile.html")
    return render_template('home.html')



def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@app.route('/live')
def live():
    return """<iframe width="560" height="315" src="https://www.youtube.com/embed/LvGN2iSxrJg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""

@app.route('/quiz', methods=['GET','POST'])
def group():
    print(url_for('static',filename='1.mpeg'))
    name = ''
    group_name = ''
    if request.method == 'POST':
        name = request.form['u_name']
        password = request.form['g_code']
        group_name = request.form['group']
        print(name,password,group_name)
        if name and password and group_name:
            if group_name == 'A' and password == '2018':
                return render_template('pcbot.html', name = name,group_name=group_name)
            if group_name == 'B' and password == '2020':
                return render_template('pcbot.html', name = name,group_name=group_name)
            return render_template('form.html', message = "⚠️ Login Failed Please Try Again!")
        return render_template('form.html', message = "⚠️ Please Fill The Form!")
    return render_template('form.html')

'''@app.route('/chat',methods=['GET','POST'])
def reply():
    x = url_for("static",filename='song.mp3')
    return f"""<audio controls>
  <source src="/static/1.mpeg" type="audio/mpeg">
Your browser does not support the audio element.
</audio><br>hey bro answer this question"""'''

@app.route('/admin/<passd>',methods=['GET','POST'])
def admin_view(passd):
    if passd == '12345':
        return render_template('adminbot.html',name = "Admin",group_name="Admin")
    return "<h1>Bad Access"

@socketio.on('admin_joined')
def join_admin(data):
    print("Admin  Joined ",data)
    join_room(data['room'])


@socketio.on('join_room')
def joined(data,methods=['GET','POST']):
    print("{} has joind the room {}".format(data['username'],data['room']))
    #p = get_message(data['room'],100)
    #print(p)
    join_room(data['room'])
    #socketio.emit("joined", data)
    socketio.emit('joined',data, room = data['room'])

@socketio.on('send')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    json['img'] = url_for('static',filename='logo.png')
    try:
        save_message(json['room'],json['message'],json['username'])
    except:
        pass
    if json['username'] == 'Admin':
        socketio.emit('receive', json)
    else:
        socketio.emit('receive', json,room= json['room'])
    if json['message'][0:3].lower() == 'ans':
        socketio.emit('receive', json, room = "Admin")

@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info("{} has left the room {}".format(data['username'], data['room']))
    leave_room(data['room'])
    socketio.emit('left', data, room=data['room'])








if __name__ == '__main__':
    #socketio.run(app, debug=True)
    app.run()