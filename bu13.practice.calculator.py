def res_sum(num):
    if num.find('+') != -1:
        sumPl = num.split('+')
        resPl = float(sumPl[0])+float(sumPl[1])
        return resPl
    elif num.find('-') != -1:
        sumMi = num.split('-')
        resMi = float(sumMi[0])-float(sumpl[1])
        return resMi
    elif num.find('*') != -1:
        sumMu = num.split('*')
        resMu = float(sumMu[0])*float(sumMu[1])
        return resMu
    elif num.find('/') != -1:
        sumDi = num.split('/')
        resDi = float(sumDi[0])/float(sumDi[1])
        return resDi
    
def res_text():
    res_label.configure(text = 'result: '+str(res_sum(num0.get())))

window = Tk()
window.title('계산기')
window.geometry('350x200')

Label(window, text = 'number').grid(column = 0, row = 0)
res_label = Label(window, text = 'result: ')
res_label.grid(column = 0, row = 1)

num0 = Entry(window, width = 10)
num0.grid(column = 1, row = 0)

print(type(num0.get()))

btn = Button(window, text = 'reslutBtn', command = res_text)
btn.grid(column = 2, row = 0)

window.mainloop()
