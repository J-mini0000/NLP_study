from konlpy.tag import Okt

okt = Okt()
tokens = okt.morphs("나는 자연어 처리를 배운다")
print(tokens) #토큰화

#enumerate()-리스트를 딕셔너리형식으로 인덱스를 부여해주는 함수
word_to_index = {word : index for index, word in enumerate(tokens)} #각 토큰에 인덱스 부여
print('단어 집합 :',word_to_index)

word_to_index1 = {word : index for index, word in enumerate(tokens,start=3)} #인덱스 3부터 시작하여 부여
print('단어 집합 :',word_to_index1)

def one_hot_encoding(word, word_to_index):
  one_hot_vector = [0]*(len(word_to_index)) #word_to_index의 길이만큼 0으로 채워진 리스트를 생성
  index = word_to_index[word] #word_to_index에서 파라미터1인 word가 들어간 index를 가져옴
  one_hot_vector[index] = 1 #0으로 채웠던 리스트에서 index위치를 1로 변경
  return one_hot_vector #바꾼 리스트 리턴

for i in word_to_index.keys():
  print (i)
  print(one_hot_encoding(i, word_to_index))