from flask import Flask, render_template
from wakeonlan import send_magic_packet
from subprocess import check_output

# systems
dadpc2 = {'name':'dad PC 2','mac_address':'3c:1e:04:ea:a2:2e'}
def wake_up(system):
    send_magic_packet(system['mac_address'])

def get_sshtop():
    stdout = check_output(['./script.sh']).decode('utf-8')
    return stdout

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
    return '<pre>'+get_sshtop()+'</pre>'

if __name__=='__main__':
    app.run(debug=True)


