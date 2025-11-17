import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path,encoding='utf-8')
    return df[['Sentence','Label']]

if __name__ == "__main__":
    file_path = './SQLiV3.csv'
    data = load_data(file_path)
    print(data)
