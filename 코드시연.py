import pandas as pd
import matplotlib.pyplot as plt

df_covid = pd.read_csv('latestdata.csv')
parse_dates=['date_onset_syptoms','date_admission_hospital','date_confirmation','date_death_or_discharge',].low_memory=False)

