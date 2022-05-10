import requests
import re
#http://admin:12345678@192.168.1.100/Set.cmd?CMD=SetPower&P60=1&P61=1&P62=1&P63=0


class cmds_jose(object):
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self, ip='localhost:5000'):#localhost:5000
        self.ip_address = ip
        self.query = {}
        self.user = 'admin'
        self.passw = '12345678'

    def form_query(self, state, cmd, port):
        port = self.get_port_no(port)
        self.query = {port: state}
        return self.query

    def get_port_no(self, port_no):
        port = 'P6' + str(port_no)
        return port

    def clean_html(self, data):
        exp = re.compile('<.*?>')
        text = re.sub(exp, "", data)
        return text.rstrip()

    def send_cmds(self, cmd, port=None, state=None):
        url = 'http://{}:{}@{}/SetCmd?CMD={}'\
              .format(self.user,
                      self.passw,
                      self.ip_address,
                      cmd)
        print (url)
        if cmd == 'SetPower':
            self.form_query(state, cmd, port)
            self.req = requests.get(url, params=self.query)
            return True
        elif cmd == 'GetPower':
            self.req = requests.get(url)
            data = self.clean_html(self.req.text)
            return data
        else:
            return False

        return self.req.text


#c = commands('localhost:5000')

#c.send_cmds('SetPower', 2, 1)
#c.send_cmds('SetPower', 3, 1)
#print (c.send_cmds('GetPower'))

"""" 
Before the 10.05, you should be able to:

* Run at least the example tests, as it seems everyone has been able to do until this day

* For ex1. After understanding the app, you could add another parameter to it, such user email address and elaborate the test rules (email should contain @, etc)

*For ex2. You could add more pins and/or define a transient state with is basically between ON and OFF state (create a delay function between On to Off and viceversa) With that you would be able to establish the transition time and develop the testing rules for checking it.
"""
