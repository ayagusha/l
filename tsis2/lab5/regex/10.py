import re

def f(mObject):
    return mObject.group("g1")+ "_" + mObject.group("g2").lower()
x="mySuperVar" 
y="(?P<g1>[a-z])(?P<g2>[A-Z])+"
print(re.sub(y, f, x))