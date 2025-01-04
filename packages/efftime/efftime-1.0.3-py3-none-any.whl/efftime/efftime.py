import time

global_efftime = time.time()

def start():
    global global_efftime
    global_efftime = time.time()


def end():
    global global_efftime
    print("Run time:",round(time.time()-global_efftime,3))

