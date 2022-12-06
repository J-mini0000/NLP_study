import pandas as pd
import numpy as np

#zip()함수는 동일한 개수를 가지는 시퀀스 자료형에서 각 순서에 등장하는 원소들끼리 묶어주는 역할을 한다. 결과는 튜플로 나온다.
X, y = zip(['a', 1], ['b', 2], ['c', 3])
print('X 데이터 :',X)
print('y 데이터 :',y)

# 리스트 앞에 별표(*)가 붙는 이유는 파라미터로 1차원 시퀀스 자료형 여러개를 입력받기 때문에 다차원 자료형일 경우 바깥 리스트를 벗겨내는 언팩(unpack)을 해주는 것이다.
sequences = [['a', 1], ['b', 2], ['c', 3]]
X, y = zip(*sequences)
print('X 데이터 :',X)
print('y 데이터 :',y)

#pandas DataFrame을 통해 표로 정리하기
values = [['당신에게 드리는 마지막 혜택!', 1],
['내일 뵐 수 있을지 확인 부탁드...', 0],
['도연씨. 잘 지내시죠? 오랜만입...', 0],
['(광고) AI로 주가를 예측할 수 있다!', 1]]
columns = ['메일 본문', '스팸 메일 유무']

df = pd.DataFrame(values, columns=columns)
print(df)

# df[columns1] 을 통해 columns1에 해당하는 열의 내용을 확인 가능
X = df['메일 본문']
y = df['스팸 메일 유무']
print('X 데이터 :',X.to_list())
print('y 데이터 :',y.to_list())

#numpy를 통해 슬라이싱 np.arange(0부터 15까지).reshape((4*4형태로))
np_array = np.arange(0,16).reshape((4,4))
print('전체 데이터 :')
print(np_array)

#[행:열] 슬라이싱
#int = a,b,c,d =>index
#array1[a:b, c:d] 행은 a부터 b-1까지, 열은 c부터, d-1까지

#EX)


#[:, :3] 모든행의 처음부터 index가 2(3-1)인 열까지
X = np_array[:, :3]

#[:, 3] 모든행의 index가 3인 열
y = np_array[:, 3]

#[2,:] index가 2인 행의 모든 열
Z = np_array[2,:]

print('X 데이터 :')
print(X)
print('y 데이터 :',y)
print('Z 데이터 :')
print(Z)
