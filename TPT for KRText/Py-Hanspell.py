#pip install git+https://github.com/ssut/py-hanspell.git
#위의 명령어를 터미널에 입력하여 패키지 설치

#네이버 한글 맞춤법 검사기를 바탕으로 만들어진 패키지

from hanspell import spell_checker

sent = "맞춤법 틀리면 외 않되? 쓰고싶은대로쓰면돼지 "
spelled_sent = spell_checker.check(sent)

hanspell_sent = spelled_sent.checked
print(hanspell_sent)


#hanspell은 띄어쓰기 또한 보정합니다.
sent = '전희원님이 개발한 PyKoSpacing은 띄어쓰기가 안된 문장을 띄어쓰기를 한 문장으로 변환해주는 패키지'
# 띄어쓰기가 없는 문장 임의로 만들기
new_sent = sent.replace(" ", '')

spelled_sent = spell_checker.check(new_sent)

hanspell_sent = spelled_sent.checked
print(hanspell_sent)
