from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

text = "나는 원 핫 인코딩을 할거야 케라스로"

tokenizer = Tokenizer()
tokenizer.fit_on_texts([text]) #text에 대해 fit함
#tokenizer.fit_on_texts(text)로 실행할 시 어절이 아닌 한글자씩 분리됨
tti=tokenizer.word_index #fit한 text에 대한 인덱싱 결과
print('단어 집합 :',tti)

sub_text = "원 핫 인코딩을 케라스로 할거야 나는" #기존 text에서 어절단위로 문장을 섞음

encoded = tokenizer.texts_to_sequences([sub_text])[0] #subtext의 문장의 시퀀스에 맞게 tti의 인덱스값을 대체
print(sub_text)
print(encoded)

one_hot = to_categorical(encoded) #encoded에 대해 원 핫 인코딩
print(one_hot)

#원핫인코딩은 단어만큼 차원 수가 늘어나고 저장 공간 측면에서 비효율적임.
#또한 단어간 유사도를 표현하지 못함.

#위의 단점을 극복하기위해 카운트 기반 벡터화 LSA(잠재 의미 분석), HAL
#예측 기반으로 벡터화하는 NNLM, RNNLM, Word2Vec, FastText 등
#두 가지 방법을 모두 사용하는 방법으로 GloVe가 존재