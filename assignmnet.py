import pandas as pd

def read_data_from_csv(csv_path='data.csv'):
	df = pd.read_csv(csv_path)
	print(df.head())
	print(df.columns)
	print(df.shape)

if __name__ == '__main__':
	print("Assignment started")
	read_data_from_csv()
	print("Assignment ended")