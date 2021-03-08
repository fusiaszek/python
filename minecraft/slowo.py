def oblicz(*argument):
    najwiecej = 0
    najmniej = 10
    for i in argument:
        if i > najwiecej:
            najwiecej = i
        if i < najmniej:
            najmniej = i
    print(najwiecej - najmniej)


oblicz(4.2, 3.9, 4, 1.004, 9.104, 2.81, 8)
