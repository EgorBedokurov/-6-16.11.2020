import time

def countdown(m_f):
    def inner():
        m_f()
        time.sleep(1)
        print(time.strftime('%H:%M'))
    return inner


@countdown
def what_time():
    print('What time is now?')
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)

what_time()