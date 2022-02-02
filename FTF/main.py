import pickle
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import numpy as np

with open('../FTF/Models/model_fiz.pkl', 'rb') as fid:
 model_fiz= pickle.load(fid)
with open('../FTF/Models/model_org.pkl', 'rb') as fid:
 model_org= pickle.load(fid)

file_path = '../FTF/Models/ОСНОВНЫЕ ПАРАМЕТРЫ 2015-2017 УТОЧНЕННЫЕ.xlsx'

def read_from_file(file_path):
    cols = ['Индекс потребительских цен', 'валовой региональный продукт', 'промышленность',
          'численность постоянного населения', 'Продукция сельского хозяйства во всех категориях хозяйств',
          'инвестиции', 'оборот розничной торговли', 'реальные распологаемые доходы населения', 'уровень безработицы',
          'экспорт всего', 'импорт всего']
    read = pd.read_excel(file_path)
    feed = pd.DataFrame(columns=cols, index=[2015, 2016, 2017])
    for i in range(0, 3):
        feed.iloc[i][0] = read.loc[7][5 + 2 * i]
        feed.iloc[i][1] = read.loc[10][5 + 2 * i]
        feed.iloc[i][2] = read.loc[13][5 + 2 * i]
        feed.iloc[i][3] = read.loc[4][5 + 2 * i]
        feed.iloc[i][4] = read.loc[36][5 + 2 * i]
        feed.iloc[i][5] = read.loc[46][5 + 2 * i]
        feed.iloc[i][6] = read.loc[49][5 + 2 * i]
        feed.iloc[i][7] = read.loc[54][5 + 2 * i]
        feed.iloc[i][8] = read.loc[67][5 + 2 * i]
        feed.iloc[i][9] = read.loc[63][5 + 2 * i]
        feed.iloc[i][10] = read.loc[65][5 + 2 * i]
    return feed

feed = read_from_file(file_path)

def get_predict(feed):
  predict_org = model_org.predict(feed)
  predict_fiz = model_fiz.predict(feed)

  res = [predict_org, predict_fiz]
  return res

res = get_predict(feed)
data = pd.read_csv('../FTF/Models/data.csv')
show_fiz_real=[data['Налог на доходы физических лиц'][5],data['Налог на доходы физических лиц'][6],data['Налог на доходы физических лиц'][7]]
show_fiz_expert=[11452230385.89 , 11336124717.37 ,  11304320582.21 ]
show_fiz_us=res[1]
y_sh=np.array([2015,2016,2017])
show_corp_real=[data['Налог на прибыль организаций'][5],data['Налог на прибыль организаций'][6],data['Налог на прибыль организаций'][7]]
show_corp_expert=[2950636000.00,4483000000.00,5204100000.00 ]
show_corp_us=res[0]

fiz_gr=pd.DataFrame(columns=['Анализ экспертов','Анализ модели','Действительные данные'],index=y_sh)
fiz_gr['Анализ модели']=show_fiz_us
fiz_gr['Анализ экспертов']=show_fiz_expert
fiz_gr['Действительные данные']=show_fiz_real
fiz_gr.plot(xlabel='Год',ylabel='Десятки Млрд рублей',title='Налоги на доходы физических лиц',xticks=[2015,2016,2017], figsize=(10,10))
plt.show()

corp_gr=pd.DataFrame(columns=['Анализ экспертов','Анализ модели','Действительные данные'],index=y_sh)
corp_gr['Анализ модели']=show_corp_us
corp_gr['Анализ экспертов']=show_corp_expert
corp_gr['Действительные данные']=show_corp_real
corp_gr.plot(xlabel='Год',ylabel='Млрд рублей',title='Налоги на доходы организаций',xticks=[2015,2016,2017], figsize=(10,10))
plt.show()

print("Предсказание основных доходных источников на 2015-2017гг., используя прогнозируемые данные")
print("Первые три значения - НДО, далее - НДФЛ")
for i in range (0,2):
    for j in range (0,3):
        print(res[i][j])
    print("")