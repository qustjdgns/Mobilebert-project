import torch
import pandas as pd
import numpy as np

from transformers import MobileBertForSequenceClassification, MobileBertTokenizer
from tqdm import tqdm

GPU = torch.cuda.is_available()
# GPU = torch.backends.mps.is_available()

device = torch.device("cuda" if GPU else "cpu")
print("Using device:", device)

data_path = "spotify_reviews_labeled_remaining.csv"
df = pd.read_csv(data_path, encoding="utf-8")

data_X = df['content'].astype(str).tolist()
labels = df['score'].values

print(len(data_X))

tokenizer = MobileBertTokenizer.from_pretrained("google/mobilebert-uncased", do_lower_case=True)
inputs = tokenizer(data_X, truncation=True, max_length=256, add_special_tokens=True, padding="max_length")

input_ids = inputs['input_ids']
attention_mask = inputs['attention_mask']

batch_size = 8

test_inputs = torch.tensor(input_ids)
test_labels = torch.tensor(labels)
test_masks = torch.tensor(attention_mask)
test_data = torch.utils.data.TensorDataset(test_inputs, test_masks, test_labels)
test_sampler = torch.utils.data.RandomSampler(test_data)
test_dataloader = torch.utils.data.DataLoader(test_data, sampler=test_sampler, batch_size=batch_size)

model = MobileBertForSequenceClassification.from_pretrained("mobilebert_model.pt")
model.to(device)

model.eval()

test_pred = []
test_true = []

for batch in tqdm(test_dataloader, desc="Inferencing Full Dataset"):
    batch_ids, batch_mask, batch_labels = batch

    batch_ids = batch_ids.to(device)
    batch_mask = batch_mask.to(device)
    batch_labels = batch_labels.to(device)

    with torch.no_grad():
        output = model(batch_ids, attention_mask=batch_mask)

    logits = output.logits
    pred = torch.argmax(logits, dim=1)

    test_pred.extend(pred.cpu().numpy())
    test_true.extend(batch_labels.cpu().numpy())

test_accuracy = np.sum(np.array(test_pred) == np.array(test_true)) / len(test_pred)
print("전체 데이터 53,132건에 대한 긍정/부정 정확도 : ", test_accuracy)

# --- 긍정/부정 비율 그래프 추가 ---
import matplotlib.pyplot as plt
import numpy as np
import platform
# ✅ 한글 폰트 설정
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')  # 윈도우: 맑은 고딕
elif platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')    # 맥: 애플 고딕
else:
    plt.rc('font', family='NanumGothic')     # 리눅스: 나눔고딕 (설치 필요)
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지



# 클래스별 예측 개수 계산
unique, counts = np.unique(np.array(test_pred), return_counts=True)

# 클래스 라벨 (0=부정, 1=긍정)
label_names = ['부정', '긍정']

# 시각화
plt.figure(figsize=(6, 4))
plt.bar(label_names, counts, color=['red', 'green'])
plt.title('긍정/부정 예측 비율')
plt.xlabel('클래스')
plt.ylabel('건수')
plt.ylim(0, max(counts) * 1.1)

# 개수 텍스트 표시
for i, count in enumerate(counts):
    plt.text(i, count + max(counts) * 0.02, str(count), ha='center', fontsize=12)

plt.tight_layout()
plt.show()