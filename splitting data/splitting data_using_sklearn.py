import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#np.arange(0부터 10개).reshape((5행 *2열)), range(5)
X, y = np.arange(10).reshape((5, 2)), range(5)
print('X 전체 데이터 :')
print(X)
print('y 전체 데이터 :')
print(list(y))

#train : test 를 6:4로 분리 randoms_state는 데이터를 섞는 결과를 고정하기위해 난수지정(아무숫자나)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=7)

print("X_train\n",X_train, "\nX_test\n", X_test, "\ny_train\n", y_train, "\ny_test\n", y_test)


#아래와 같이 수동으로 분리시 데이터 누락이 생길 수 있음
num_of_train = int(len(X) * 0.8) # 데이터의 전체 길이의 80%에 해당하는 길이값을 구한다.
num_of_test = int(len(X) - num_of_train) # 전체 길이에서 80%에 해당하는 길이를 뺀다.
print('훈련 데이터의 크기 :',num_of_train)
print('테스트 데이터의 크기 :',num_of_test)

#수동으로 분리시 아래와 같이 변수를 사용하여 분리 한다면 데이터 누락 문제를 해결 가능.
X_test = X[num_of_train:] # 전체 데이터 중에서 20%만큼 뒤의 데이터 저장
y_test = y[num_of_train:] # 전체 데이터 중에서 20%만큼 뒤의 데이터 저장
X_train = X[:num_of_train] # 전체 데이터 중에서 80%만큼 앞의 데이터 저장
y_train = y[:num_of_train] # 전체 데이터 중에서 80%만큼 앞의 데이터 저장