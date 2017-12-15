import pandas as pd
import numpy as np

# def computing_skills(seed):
#   return 2.5*seed
#
def data_skills(computing):
  data_skills = computing-np.random.random_sample(1)[0]
  if data_skills > 5.0:
    return 5.0
  elif data_skills < 0:
    return 0
  return data_skills

def student_id(index):
  return 'student_%02d' % (index,)

# No data for now, let's create a hypothetical set
seeds = np.random.random_sample(40)
# computing =
df_students = pd.DataFrame(seeds, columns=['seeds'])
df_students['normal'] = np.random.normal(loc=2.3, scale=.6, size=40)
df_students['student_id'] = df_students.index
df_students['student_id'] = df_students.student_id.apply(student_id)
# df_students['computing_skills'] = df_students.seeds*5
df_students['computing_skills'] = df_students['normal']
df_students['computing_skills'] = df_students.computing_skills.round(decimals=1)

# print(df_students)
# error = np.random.normal(loc=.3, scale=.2, size=40)
df_students['data_skills'] = df_students.computing_skills.apply(data_skills)
df_students['data_skills'] = df_students.data_skills.round(decimals=1)

print(df_students)
# df_students['computing'] = df.seeds.apply(computing_skills)
df_students.to_csv('skills-at-start.csv', encoding='utf-8')
