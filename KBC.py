Questions=[["Which languauge is used to create facebook?", "Python", "French", "Javascript", "Php", "None", 4],
           ["Who remained ubeatean in UFC and retired?", "Conor", "Khabib", "Dustin", "Tony", "None", 2],
           ["In which year CBUM won MR.Olympia?", "2021", "2020", "2023", "2022", "None", 4],
           ["Which languauge mostly used by you?", "Python", "French", "Javascript", "Php", "None", 1],
           ["Who created facebook?", "Mirage", "Prekshya", "Mark Zuckerberg", "Bill Gates", "None", 3],
           ["Who is owner of Tesla", "Elon Musk", "Jeff Bezos", "Mirage", "Prachanda", "None", 1],
           ["Which year the WW-II ended?", "1935", "1945", "1936", "1946", "None", 2],
           ["Which year the WW-II started?", "1935", "1945", "1939", "1946", "None", 3],
           ["Mike Tyson is a:", "Footballer", "Boxer", "Cricketer", "Developer", "None", 2],
           ["Which languauge is mostly used in job?", "Python", "French", "Javascript", "Php", "None", 1],
           ["In which year Messi won the world cup?", "2021", "2022", "2023", "2020", "None", 2],
           ["Who loves you the most?", "Family", "Girlfriend", "Neighbour", "Jesus Christ", "None", 4],
           ["Which languauge is mostly used for web development?", "Python", "French", "Javascript", "Php", "None", 3],
           ["Mirage was born in:", "2004", "2003", "2002", "2001", "None", 1],
           ["Mirage is:", "18", "19", "20", "21", "None", 1]]
levels=[1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money= 0
for i in range(0, len(Questions)):
    Question=Questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(Question[0])
    print(f"1. {Question[1]}          2. {Question[2]} ")
    print(f"3. {Question[3]}          4. {Question[4]} ")
    Reply=int(input("Enter Your Answer (1-4) "))
    if Reply==Question[-1]:
        print(f"Correct answer, You have won {levels[i]}")
        if (i==4):
            money=10000
        elif i==9:
            money=320000
        elif i==14:
            money=10000000
    else:
        print("Wrong Answer")
        break
if i<4:
    print("Zero")
else:
    print(f"You have won {money}")