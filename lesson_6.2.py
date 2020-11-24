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
    for i in range(3,0,-1):
        time.sleep(1)
        print(i)

what_time()