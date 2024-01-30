# - from dataset, readme
# - apply() 적용 BMI 컬럼 생성
# - BMI = 체중(kg) / (키(m), 신장)^2
# - option) 수술시간 -> 시분 표시 컬럼 생성

import pandas as pd
df_surgerylist = pd.read_csv('docs\quests\DDA\SpineSurgeryList.csv')
print(df_surgerylist)


# 체중
weight = df_surgerylist['체중']
print(weight)
# 키(cm -> m으로 변환)
height = df_surgerylist['신장']/100
height_m = height**2  # m으로 변환
print(height_m)

BMI = weight / height_m
print(BMI)

# option) 수술시간 -> 시분 표시 컬럼 생성
surgerytime = df_surgerylist['수술시간']
pd.DataFrame(data=surgerytime)
pass
