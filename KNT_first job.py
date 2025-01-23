import pandas as pd
import os
path = kagglehub.dataset_download("idowuadamo/students-performance-in-2024-jamb")
Path to dataset files: /root/.cache/kagglehub/datasets/idowuadamo/students-performance-in-2024-jamb/versions/1
os.listdir(path)
df = pd.read_csv(os.path.join(path, 'jamb_exam_results.csv'))
df.describe().T
df.head(3)
df.tail()
df.sample()
df.isnull()
df.isnull().sum()
df.info()
df[df['JAMB_Score'] == df['JAMB_Score'].max()]
df.columns
df.shape
df.dropna(inplace=True)
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,8))
sns.histplot(data=df, x='JAMB_Score', hue='Parent_Education_Level')
plt.show()
df.shape
df['Parent_Education_Level'].unique()
