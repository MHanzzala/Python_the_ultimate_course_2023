# creating the custom Exceptions

class customException(Exception):
    pass
class ElementDoesNotExist(customException):
    pass
class firstElementIsSmallarThanSecond(customException):
    pass


l = [1,2,3,4,5]

try:
    if not 3 in l:
        raise ElementDoesNotExist
    elif l[0]<l[1]:
        raise firstElementIsSmallarThanSecond

except firstElementIsSmallarThanSecond:
    print("1st element is smaller. raising an Exception")

except ElementDoesNotExist:
    print("Element does not exist, Raising an exception")

else:
    print("Success element exists")