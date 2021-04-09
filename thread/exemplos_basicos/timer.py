from threading import Timer


def hello():
    print('Hello timer!')


t = Timer(2, hello)
t.start()
