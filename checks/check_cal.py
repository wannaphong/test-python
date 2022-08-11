import os
import sys
import config
ans = 42

for teamname in config.list_students():
    sys.path.insert(1, teamname)
    # Add try except?
    import cal
    print(teamname)
    print(cal.plus(40,2)==ans)
    del cal
    sys.modules.pop('cal')
    sys.path.remove(teamname)
    print('--------------------------------------------')