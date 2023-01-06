def who(root):
        root = {{'labs'}:{'lab1.txt':223,
                        'lab2.txt':251,
                        'lab3.txt':317,},
                'hws':{},
                'plans':{'vacation.txt':636,
                        'evil':{'world_domination.txt':766}},
                'resume.txt':607,
                'cat.jpg':607}
        for x in root:
                print(x)

who({{'labs'}:{'lab1.txt':223,
                        'lab2.txt':251,
                        'lab3.txt':317,},
                'hws':{},
                'plans':{'vacation.txt':636,
                        'evil':{'world_domination.txt':766}},
                'resume.txt':607,
                'cat.jpg':607})