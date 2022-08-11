import os
import sys
import config
import pandas as pd

def getteamname(team_path):
    data = team_path.split("\\")
    return data[-1]

teams = []
questionA = []
questionB = []
questionC = []
questionD = []

for team_path in config.list_students():
    sys.path.insert(1, team_path)
    teams.append(getteamname(team_path))

    # question A ----------------------------------------------
    try:
        import question_a
        score = 0
        
        data = [1,2,3,4]
        if(question_a.summation(data)==10):score+=1
        data = [1,2,3,4,5]
        if(question_a.summation(data)==15):score+=1
        data = [10,20,30,40]
        if(question_a.summation(data)==100):score+=1
        data = [-1,-2,-3,-4]
        if(question_a.summation(data)==-10):score+=1
        data = [-1,2,-3,4]
        if(question_a.summation(data)==2):score+=1

        questionA.append(score)
        del question_a
        sys.modules.pop('question_a')
    except ModuleNotFoundError:
        questionA.append(-1)
    except:
        questionA.append(0)

    # question B ----------------------------------------------
    try:
        import question_b
        score = 0

        if(question_b.factorial(5)==120):score += 1
        if(question_b.factorial(1)==1):score += 1
        if(question_b.factorial(0)==1):score += 1
        if(question_b.factorial(10)==3628800):score += 1
        if(question_b.factorial(2)==2):score += 1
        
        questionB.append(score)
        del question_b
        sys.modules.pop('question_b')
    except ModuleNotFoundError:
        questionB.append = -1
    except:
        questionB.append = 0

    # question C ----------------------------------------------
    try:
        import question_c
        score = 0

        if(round(question_c.distance(50, 20, 30, 10),4)==22.3607):score += 1
        if(round(question_c.distance(-1, 2, 3, -1),4)==5.0):score += 1
        if(round(question_c.distance(-1, -1, 3, 7),4)==8.9443):score += 1
        if(round(question_c.distance(1.1, 2.2, 3.3, 4.4),4)==3.1113):score += 1
        if(round(question_c.distance(-1.1, -4.4, 3, 1),4)==6.7801):score += 1

        questionC.append(score)
        del question_c
        sys.modules.pop('question_c')
    except ModuleNotFoundError:
        questionC.append(-1)
    except:
        questionC.append(0)

    # question D ----------------------------------------------
    try:
        import question_d
        score = 0

        rawdata = {'record': ['ค่าขนม', 'ค่าอาหารกลางวัน', 'ค่าเดินทาง', 'เงินเดือน'], 'income': [0, 0, 0, 300], 'outcome': [40, 120, 45, 0]}
        df = pd.DataFrame(data=rawdata)
        if(question_d.netincome(df)==95):score += 1

        rawdata = {'record': ['ค่าขนม', 'ค่าอาหารกลางวัน', 'ค่าเดินทาง', 'เงินเดือน'], 'income': [400, 0, 0, 300], 'outcome': [0, 120, 145, 0]}
        df = pd.DataFrame(data=rawdata)
        if(question_d.netincome(df)==435):score += 1

        rawdata = {'record': ['ค่าขนม', 'ค่าอาหารกลางวัน', 'ค่าเดินทาง', 'เงินเดือน'], 'income': [0, 200, 0, 300], 'outcome': [40, 0, 45, 0]}
        df = pd.DataFrame(data=rawdata)
        if(question_d.netincome(df)==415):score += 1

        rawdata = {'record': ['ค่าขนม', 'ค่าอาหารกลางวัน', 'ค่าเดินทาง', 'เงินเดือน'], 'income': [100, 20, 20, 300], 'outcome': [0, 0, 0, 0]}
        df = pd.DataFrame(data=rawdata)
        if(question_d.netincome(df)==440):score += 1

        rawdata = {'record': ['ค่าขนม', 'ค่าอาหารกลางวัน', 'ค่าเดินทาง', 'เงินเดือน'], 'income': [0, 0, 0, 0], 'outcome': [40, 120, 45, 50]}
        df = pd.DataFrame(data=rawdata)
        if(question_d.netincome(df)==-255):score += 1

        questionD.append(score)

        del question_d
        sys.modules.pop('question_d')
    except ModuleNotFoundError:
        questionD.append(-1)
    except:
        questionD.append(0)

    sys.path.remove(team_path)    

print('Save to excel')
scoreDF = pd.DataFrame([teams, questionA, questionB, questionC, questionD])
scoreDF = scoreDF.transpose()
scoreDF.columns = ['team', 'A', 'B', 'C', 'D']
scoreDF.to_excel('score.xlsx', encoding='utf-8', index=False)