#pip install git+https://github.com/haven-jeon/PyKoSpacing.git
#위의 명령어를 터미널에 입력하여 패키지 설치

#전희원님이 개발한 PyKoSpacing은 띄어쓰기가 안된 문장을 띄어쓰기를 한 문장으로 변환해주는 패키지

from pykospacing import Spacing
sent = '전희원님이 개발한 PyKoSpacing은 띄어쓰기가 안된 문장을 띄어쓰기를 한 문장으로 변환해주는 패키지'
# 띄어쓰기가 없는 문장 임의로 만들기
new_sent = sent.replace(" ", '')
print(new_sent)

#Spacing을 통해 띄어쓰기를 없앤 new_sent 문자열 띄어쓰기 다시하기
spacing = Spacing()
kospacing_sent = spacing(new_sent)

print("sent: ",sent)
print("sent using Spacing: ",kospacing_sent)