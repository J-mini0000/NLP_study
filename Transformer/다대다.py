from transformers import TFBertForTokenClassification #트랜스포머다대다 유형(many-to-many)임포트
model = TFBertForTokenClassification.from_pretrained("모델 이름", num_labels=분류할 레이블의 개수)#다대다 유형(many-to-many)
