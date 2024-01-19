def desc(f):
    def wrapper():
        print("study")
        f()
    return wrapper
@desc
def something():
    print("do something~")

# s = desc(something)
# s()
something()