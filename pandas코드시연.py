import pandas as pd

df = pd.read_csv("heart.csv")

df[df['bmi'].isnull()]

