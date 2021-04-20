from matplotlib import pyplot
from openpyxl import load_workbook
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

# years = sheet['A'][1:]
# temperature = sheet['C'][1:]
# activity = sheet['D'][1:]

def getvalue(x):
    return x.value

# years = map(getvalue, sheet['A'][1:])
# temperature = map(getvalue, sheet['C'][1:])
# activity = map(getvalue, sheet['D'][1:])

years = list(map(getvalue, sheet['A'][1:]))
temperature = list(map(getvalue, sheet['C'][1:]))
activity = list(map(getvalue, sheet['D'][1:]))

# print (activity)

pyplot.plot(years, temperature, label='temperature', color='orange')
pyplot.plot(years, activity, label='activity', color='red')
pyplot.xlabel('Years')
pyplot.ylabel(r'temerature\activity')
pyplot.title('температура и активность солнца', fontsize=15)
# pyplot.title('активность солнца', fontsize=15, color='red')
# pyplot.title('температура', fontsize=15, color='orange'+"+"+'активность солнца', fontsize=15, color='red')
pyplot.legend()
pyplot.grid(True)
pyplot.show()