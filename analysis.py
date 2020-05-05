import pandas as pd

path_to_data_files = '../files/fake-news-kaggle-corpus/'
submit = pd.read_csv(path_to_data_files+'submit.csv')
test = pd.read_csv(path_to_data_files+'test.csv')
train = pd.read_csv(path_to_data_files+'train.csv')

print(train)