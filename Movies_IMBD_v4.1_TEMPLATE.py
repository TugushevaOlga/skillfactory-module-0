#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter


# # Предобработка

# In[2]:


answers = {} # создадим словарь для ответов

data = pd.read_csv('movie_bd_v5.csv')

data['release_date']=pd.to_datetime(data['release_date']) # преобразуем дату в столбце release_date из str в datetime
profit = data['revenue'] - data['budget'] 
data['profit'] = profit #добавляем  в таблицу столбец со значением прибыли

data.head()


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[3]:


answers['1'] = '5.Pirates of the Caribbean: On Stranger Tides (tt1298650)'# +


# In[73]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv('movie_bd_v5.csv')

data_copy = data.copy()
data_1 = data_copy[data_copy.budget == data_copy.budget.max()] #находим максимальное значение в столбце budget
data_1['original_title']


# ВАРИАНТ 2

# In[5]:


# можно добавлять разные варианты решения


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[6]:


answers['2'] = '2.Gods and Generals (tt0279111)'# +


# In[7]:


data_copy[data_copy.runtime == data_copy.runtime.max()]['original_title'] # находим максимальное значение в столбце runtime


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[8]:


answers['3'] = 'Winnie the Pooh (tt1449283)' #+


# In[9]:


data_copy[data_copy.runtime == data_copy.runtime.min()]['original_title'] # то же, только ищем min


# # 4. Какова средняя длительность фильмов?
# 

# In[10]:


answers['4'] = 110 # +


# In[11]:


data_copy.describe()


# # 5. Каково медианное значение длительности фильмов? 

# In[12]:


answers['5'] = 107 # + 


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[77]:


profit = data['revenue'] - data['budget']
data['profit'] = profit
data_2 = data.copy()
data_6 = data_2[data_2.profit == data_2.profit.max()]
data_6['original_title']


# In[14]:


answers['6'] = '5.Avatar (tt0499549)'# +


# # 7. Какой фильм самый убыточный? 

# In[15]:


data_7 = data_2[data_2.profit == data_2.profit.min()]
data_7[['original_title','profit']]


# In[16]:


answers['7'] = '5.The Lone Ranger (tt1210819)'# +


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[17]:


data_2[(data_2.revenue - data_2.budget)>0].count()


# In[18]:


answers['8'] = 1478 # +


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[19]:


#сначала оставляем в таблице только строки,соответствующие фильмам с годом выхода 2008,затем сортируем по столбцу 'кассовый сбор'
data_9=data_2[data_2.release_year==2008].sort_values(by='revenue',ascending=False).reset_index()# в отсортированной таблице индексируем строки по порядку
data_9.loc[0]['original_title'] #вывод


# In[20]:


answers['9'] ='4.The Dark Knight (tt0468569)'# +


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[21]:


data_10 = data_2.query('release_year in [2012,2013,2014]').sort_values(by='profit').reset_index()
data_10.loc[0]['original_title']


# In[22]:


answers['10'] = '5.The Lone Ranger (tt1210819)'


# # 11. Какого жанра фильмов больше всего?

# In[23]:


data = pd.read_csv('movie_bd_v5.csv')
data_11=data.copy()

data_11['genres'] = data_11['genres'].str.split('|', expand=False)# преобразуем строку в ячейке с перечислением жанров в список
data_ans=data_11[['original_title','genres']]
ans_11=data_ans.explode('genres')# каждому жанру в таблице теперь соответствует только одна строка
ans_11['genres'].value_counts().index[0] # теперь можно посчитать количество уникальных значений


# In[24]:


answers['11'] = 'Drama'


# ВАРИАНТ 2

# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[25]:


data_11.explode('genres')
profit = data_11['revenue'] - data_11['budget']
data_11['profit'] = profit
data_12 = data_11[data_11['profit']>0].explode('genres')
data_12[['genres','profit']].groupby(by= 'genres').count().sort_values(by='profit',ascending=False).index[0]


# In[26]:


answers['12'] = 'Drama'


# # 13. У какого режиссера самые большие суммарные кассовые сборы?

# In[27]:


data_11['director'] = data_11['director'].str.split('|', expand=False)# превращаем строку в ячейке 'director' в список
data_13 = data_11.explode('director') # разделяем режиссеров, предоставляя каждому отдельную строку
data_13.groupby('director').revenue.sum().sort_values(ascending=False).index[0] #после группировки считаем суммарные сборы


# In[28]:


answers['13'] = 'Peter Jackson' #+


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[29]:


data = pd.read_csv('movie_bd_v5.csv')
data_14=data.copy()

data_14['genres'] = data_14['genres'].str.split('|', expand=False)
data_14['director'] = data_14['director'].str.split('|', expand=False)
data_14 = data_14.explode('genres').explode('director')
data_14[data_14['genres']=='Action'].groupby(['director']).count().sort_values(by = 'genres',ascending=False)


# In[30]:


answers['14'] = 'Robert Rodriguez'# +


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[31]:


data_15 = data.copy()
data_15['cast'] = data_15['cast'].str.split('|', expand=False)
data_15 = data_15.explode('cast')
df_2012 = data_15[data_15['release_year']==2012]
df_2012.groupby('cast').sum().sort_values(by = 'revenue',ascending=False).index[0]


# In[32]:


answers['15'] = 'Chris Hemsworth'


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[33]:


data = pd.read_csv('movie_bd_v5.csv')
data['profit'] = data['revenue']-data['budget']

data_15=data.copy()
data_15.cast = data_15.cast.str.split('|')
data_16=data_15.explode('cast')
data_16[data_16['budget']>data_16['budget'].mean()].groupby(['cast'])['original_title'].count().sort_values(ascending=False).index[0]


# In[34]:


answers['16'] = '3.Matt Damon'


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[35]:


data_17 = data.copy() 
data_17['cast'] = data_17['cast'].str.split('|', expand=False)
data_17['genres'] = data_17['genres'].str.split('|', expand=False)
data_17 = data_17.explode('cast').explode('genres')
data_17[data_17['cast']== 'Nicolas Cage'].groupby('genres').count().sort_values(by = 'imdb_id',ascending=False).index[0]


# In[36]:


answers['17'] = '2.Action'


# # 18. Самый убыточный фильм от Paramount Pictures

# In[37]:


data_18 = data.copy()
data_18[data_18.production_companies.str.contains('Paramount Pictures')].groupby(['profit']).min()['original_title'].head()


# In[38]:


answers['18'] = '1.K-19: The Widowmaker (tt0267626)'


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[39]:


data_19 = data.copy()
data_19.groupby(['release_year'])['revenue'].sum().sort_values(ascending=False).index[0]


# In[40]:


answers['19'] = '5.2015'


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[41]:


data_20 = data.copy()
data_20['profit'] = data_20['revenue'] - data_20['budget']
# студия является концерном,чтобы учесть в статистике все её подразделения, ищем с помощью функции str.contains по ключевой части названия
data_20[data_20.production_companies.str.contains('Warner')].groupby(['release_year']).sum().sort_values(by='profit',ascending=False).index[0]


# In[42]:


answers['20'] = '1.2014'


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[43]:


data = pd.read_csv('movie_bd_v5.csv')
data_21 = data.copy()
data_21['release_date']=pd.to_datetime(data_21['release_date']) 
data_21['release_date']= data_21['release_date'].dt.month # оставляем в столбце release_date только месяц
data_21.groupby(['release_date']).count().sort_values(by='imdb_id',ascending=False)#группируем, считаем уникальные значения и сортируем по убыванию


# In[44]:


answers['21'] = '4.Сентябрь'


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[45]:


data_21.query('release_date in [6,7,8]').count()# продолжаем работать с преобразованным столбцом release_date(в нём указан только месяц)


# In[46]:


answers['22'] = '2.450'


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[48]:


data['release_date']=pd.to_datetime(data['release_date'])
data_23 = data.copy()
data_23['director'] = data_23['director'].str.split('|')
data_23 = data_23.explode('director')
data_23_groupby = data_23[data_23.release_date.dt.month.isin([1,2,12])]
data_23_groupby.groupby('director')['imdb_id'].count().sort_values(ascending=False).index[0]


# In[ ]:


answers['23'] = '5.Peter Jackson'


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[52]:


data_24 = data.copy()
data_24['original_title_length'] = data_24.original_title.map(lambda x: len(x))# применяем вычисление длины названия по количеству символов к каждой ячейке
data_24['production_companies'] = data_24['production_companies'].str.split('|')
data_24 = data_24.explode('production_companies')
data_24.groupby('production_companies')['original_title_length'].mean().sort_values(ascending=False).index[0]


# In[ ]:


answers['24'] = '5.Four By Two Productions '#+


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[53]:


data_25 = data.copy()
data_25['overview_words_length'] = data_25.overview.map(lambda x: len(x.split(' '))) #узнаём длину по количеству слов
data_25['production_companies'] = data_25['production_companies'].str.split('|')
data_25 = data_25.explode('production_companies')
data_25.groupby('production_companies')['overview_words_length'].mean().sort_values(ascending=False).index[0]


# In[54]:


answers['25'] = '3.Midnight Picture Show'#+


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[55]:


data_1 = data.sort_values(by = 'vote_average',ascending = False).reset_index()# отсортируем таблицу с фильмами по рейтингу по убыванию
end = round(data_1.vote_average.count()*0.01)# узнаём количество фильмов, которые входят в 1% от этого отсортированного списка
data_1[:end]['original_title'] #это значение делаем нижней границей среза, выводим только названия


# In[64]:


answers['26'] = ['1.Inside Out, The Dark Knight, 12 Years a Slave']


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# In[65]:


import itertools as it

data['cast_comb'] = data.cast.str.split('|').apply(lambda x: tuple(it.combinations(sorted(x),2)))
Counter(data.cast_comb.values.sum()).most_common(5)


# In[66]:


answers['27'] = ['5.Daniel Radcliffe & Rupert Grint']


# ВАРИАНТ 2

# In[ ]:





# # Submission

# In[67]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[68]:


len(answers)


# In[ ]:




