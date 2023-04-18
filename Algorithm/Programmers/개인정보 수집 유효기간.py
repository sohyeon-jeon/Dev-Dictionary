class Test1:
    def date2day(date):
        y,m,d=date.split('.')
        return (28*12*int(y))+(28*int(m))+int(d)

    def solution(today, terms, privacies):
        answer = []
        today2day=date2day(today)
        for idx,privacy in enumerate(privacies):
            s_d,type=privacy.split()
            start2day=date2day(s_d)
            for term in terms:
                if type==term.split()[0]:
                    end2day=start2day+int(term.split()[1])*28
                    print(today2day,end2day)
                    if today2day>=end2day:
                        answer.append(idx+1)

        return answer

    solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])

# map 함수로 쓰니까 깔끔!
def date2day(date):
    y,m,d=map(int,date.split('.'))
    return y*28*12+m*28+d

def solution(today, terms, privacies):
    answer = []
    today2day=date2day(today)
    for idx,privacy in enumerate(privacies):
        s_d,type=privacy.split()
        start2day=date2day(s_d)
        for term in terms:
            if type==term.split()[0]:
                end2day=start2day+int(term.split()[1])*28
                print(today2day,end2day)
                if today2day>=end2day:
                    answer.append(idx+1)

    return answer

solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])