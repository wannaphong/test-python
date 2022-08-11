import os
import sys
import config
ans = "fail"

for i in config.list_students():
    sys.path.insert(1, i)
    # Add try except?
    import exam_pass
    print(i)
    print(exam_pass.check(50)==ans)
    del exam_pass
    sys.modules.pop('exam_pass')
    sys.path.remove(i)