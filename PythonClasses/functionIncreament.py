def increament(n):
    print("id = {}, value = {}".format(id(n), n))
    n += 1
    print("id = {}, value = {}".format(id(n), n))

def main():
    n = 1
    print("id = {}, value = {}".format(id(n), n))
    increament(n)
    print("id = {}, value = {}".format(id(n), n))

main()