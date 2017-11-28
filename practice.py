# import bluetooth
# print("performing inquiry...")
#
# nearby_devices = bluetooth.discover_devices(lookup_names = True)
#
# print("found %d devices" % len(nearby_devices))
#
# for addr, name in nearby_devices:
#
#     print("address : %s - name : %s" % (addr, name))


import time
import bluetooth

def search():
    devices = bluetooth.discover_devices(duration = 10, lookup_names = True)
    return devices

if __name__ == "__main__":
    while True:
        print("performing inquiry...")
        results = search()
        if (results != None) :
            print("found %d devices" % len(results))
            for addr, name in results:
                print("name : %s ------ address : %s" % (name, addr))
        print("sleeping for 5 seconds")
        time.sleep(5)
