from subprocess import call
import certsettings

def createCommand(command, params):
    commandFormatted = replaceSettings(command)
    commandFormatted = replaceParams(command, params)
    verif = verifyCommand(command)
    if verif is None:
        return command
    else:
        if verif is "%":
            print("Missing Setting (This shouldn't happen)")
        elif verif is "#":
            print("Missing Param (This shouldn't happen)")

def replaceSettings(command):
    settings = certsettings.getsettings()
    for setting in settings:
        command = command.replace("%" + setting + "%", settings[setting].replace("\"", "\\\""))
    return command

def replaceParams(command, params):
    for param in params:
        command = command.replace("#" + param + "#", params[param].replace("\"", "\\\""))
    return command

def verifyCommand(command):
    if "%" in command:
        return "%"
    elif "#" in command:
        return "#"
    return ""
    

# Commands
cd                  = "cd %certRootDir%"

generateKey         = "openssl genrsa -out %certPrivateKeysDir%/#cn#.key.pem" # Include -aes256 for encryption
generateKeyPerms    = "chmod 400 %certPrivateKeysDir%/#cert#.key.pem"

generateCSR         = "openssl req -config %certRootDir%/openssl.cnf -key %certPrivateKeysDir%/#cn#.key.pem -new -sha256 -out %certCSRDir%/#cn#.csr.pem -subj \"/C=#c#/ST=#st#/L=#l#/O=#o#/OU=#ou#/CN=#cn#\""

# type = server_cert or user_cert
signCSR             = "openssl ca -config %certRootDir%/openssl.cnf -extensions #type# -days %serverDays% -notext -md sha256 -in %certCSRDir%/#cn#.csr.pem -out %certSignedFilesDir%/#cn#.cert.pem"
signCSRPerms        = "chmod 444 %certSignedFilesDir%/#cn#.cert.pem"