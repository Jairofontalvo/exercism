from datetime import timedelta

def add(moment):
    gigasegundo = 10 ** 9
    x = timedelta(seconds=gigasegundo)
    return moment + x
