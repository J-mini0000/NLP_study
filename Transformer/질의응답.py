from transformers import TFBertForQuestionAnswering #트랜스 질의응답 유형(Question Answering)임포트
model = TFBertForQuestionAnswering.from_pretrained('모델 이름')
