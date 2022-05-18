import ftplib
import os

# send file to FTP server
def send2ftp(filename):
    # FTP server info
    ip = 'xxx.xx.xxx.xx'
    port = 9999
    username = 'xxxxxxxx'
    password = 'xxxxxxxx'
    
    # Connecting to FTP
    ftp = ftplib.FTP()
    ftp.connect(ip, port)
    ftp.login(username, password)
    
    # getting local path
    localpath = os.getcwd()
    print('localpath:', localpath)
    
    mypath = '/yourdir'                                         # folder name (Remote site)
    
    ftp.cwd(mypath)                                             # cwd : change working directory
    
    files = ftp.nlst()                                          # list all file and directory in path
    print('before:', files)
    
    filepath = os.path.join(localpath, filename)
    fileupload = open(filepath, 'rb')                           # rb : read-binary
    
    result = ftp.storbinary('STOR ' + filename, fileupload)
    print('result:', result)
    
    files = ftp.nlst()                                          # list all file and directory in path
    print('after:', files)
    ftp.close()
   
   
# List all file and directory in desktop    
def listDesktop(upload=False):
    # getting desktop path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    desktop_list = os.listdir(desktop)
    print('desktop:', desktop)

    # list path of all file in desktop to text
    for d in desktop_list:
        folder = os.path.join(desktop, d)
        filename = 'desktop-{}.txt'.format(os.getenv('username').replace(' ', '-'))
        with open(filename, 'a', encoding='utf-8') as file:
            t = '{}\n'.format(folder)
            file.write(t)
    
    # Upload list to FTP server
    if upload:
        send2ftp(filename)
    

send2ftp('hello.txt')
listDesktop()
    
    

    




