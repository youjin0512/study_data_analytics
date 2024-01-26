<details >
<summary>Titanic From Disaster_타이타닉 참사</summary>

### DDA 분석
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | ---|
<!-- | PassengerId |  | | unique id의 경우 데이터로 사용 불가 판단 | 
| survival | Survival | 0 = No, 1 = Yes | 범주형(명목형), 생존과 죽음의 두가지 종류이기 때문에 범주형으로 판단됨| -->
<!-- | pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 범주형(순서형), 등급이 부여된 티켓이기 때문에 범주형으로 판단됨 |
| sex | Sex | | 범주형(명목형) |
| Age | Age in years | | 수치형(이산형) | 
| sibsp | # of siblings / spouses aboard the Titanic | | 범주형(순서형), 형제자매의 특정 수치이며 범주별 빈도를 분석해야 함  |
| parch | # of parents / children aboard the Titanic | |범주형(순서형), 범주형으로 빈도를 파악해야 함 |
| ticket | Ticket number | | 범주형(순서형) |
| fare | Passenger fare | | 수치형(이산형), 각 요금별 승객의 수를 파악하는데 사용할 수 있음 |
| cabin | Cabin number | | 범주형(순서형)|
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton | 범주형(명목형) | -->
| PassengerId | Passenger_id |   | 수치형 |
| Pclass | Cabin class | 1, 2, 3 | 범주형(순서형) |
| Name | Passenger name |    | 범주형(명목형)|
| Sex | Sex | male, female | 범주형(명목형) |
| Age | Age || 수치형(이산형) |
| SibSp | 함께 탑승한 형제와 배우자의 수 | 0, 1, 2, 3, 4, 5, 8 | 수치형(연속형) |
| Parch | 함께 탑승한 부모, 아이의 수 | 0, 1, 3, 2, 4, 6, 5, 9 | 수치형(연속형) |
| Ticket | The number of ticket|| 범주형(명목형) |
| Fare | Bording fare || 수치형(이산형) |
| Cabin | 객실번호 || 범주형(순서형) |
| Embarked | 탑승항구 | 'Q', 'S', 'C' | 범주형(명목형) |


</details>