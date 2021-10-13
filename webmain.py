from flask import Flask, render_template
from wakeonlan import send_magic_packet

# systems
dadpc2 = {'name':'dad PC 2','mac_address':'3c:1e:04:ea:a2:2e'}
def wake_up(system):
    send_magic_packet(system['mac_address'])

# web interface
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dadpc1/')
def dadpc1():
    return render_template('index_1.html')

@app.route('/dadpc2/')
def dadpc2():
    return render_template('index_2.html')

@app.route('/WOL/')
def wol():
    dadpc1 = {'name':'dad PC 1','mac_address':'74:27:ea:01:cb:69'}
    wake_up(dadpc1)
    return 'Dad PC turned on!'

@app.route('/dadpc1bash/')
def dadpc1bash():
    #sshpass -p swethakvs ssh swetha@192.168.1.5 "top -b -n 1" > top_test
    return render_template('index_3.html')

if __name__=='__main__':
    app.run(debug=True)


