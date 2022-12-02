from transformers import TFBertForSequenceClassification #트랜스포머 다대일 유형(many-to-one)임포트
model = TFBertForSequenceClassification.from_pretrained("모델 이름", num_labels=분류할 레이블의 개수)#다대일 유형(many-to-one)
