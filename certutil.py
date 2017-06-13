import OpenSSL.crypto
from OpenSSL.crypto import load_certificate_request, FILETYPE_PEM

import certconfig
import certsettings

def createKey(params):
    command = certconfig.cd + "; " + certconfig.generateKey + "; " + certconfig.generateKeyPerms
    fcommand = certconfig.createCommand(command, params)
    stream = execute(fcommand)

def genCSR(params):
    command = certconfig.cd + "; " + certconfig.generateCSR
    fcommand = certconfig.createCommand(command, params)
    stream = execute(fcommand)
    
def signCSR(cn):
    csr = open(certsettings.settings['crlRequestsDir'] + cn + ".csr.pem")
    req = load_certificate_request(FILETYPE_PEM, csr)
    params = genCSRParams(req)
    
    command = certconfig.cd + "; " + certconfig.signCSR + "; " + certconfig.signCSRPerms
    fcommand = certconfig.createCommand(command, params)
    stream = execute(fcommand)

def importCSR(csrText):
    req = load_certificate_request(FILETYPE_PEM, csrText)
    key_type = 'RSA' if key.type() == OpenSSL.crypto.TYPE_RSA else 'DSA'
    components = getCSRParams(req)
    
    filename = components['CN'] + ".csr.pem"
    file = open(filename)
    file.write(csrText)
    
    return components['cn']
    
def getCSRParams(cn):
    subject = req.get_subject()
    components = dict(subject.get_components())
    return components

def execute(command):
    return os.popen(command)