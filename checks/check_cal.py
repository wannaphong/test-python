import os
import sys
import config
ans = 42

for i in config.list_students():
    sys.path.insert(1, i)
    import cal
    print(i)
    print(cal.plus(40,2)==ans)
    del cal
    sys.modules.pop('cal')
    sys.path.remove(i)