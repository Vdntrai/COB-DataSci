import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/vedantrai/vsc/datasci/graphs/dataset - netflix1.csv')


non_numeric_columns = df.select_dtypes(exclude=['number']).columns

for column in non_numeric_columns:
    plt.figure(figsize=(10, 6))
    plt.title(f'Plot of {column}')

    if df[column].nunique() <= 10:
        sns.countplot(data=df, x=column)
        plt.xticks(rotation=45)
    else: 
        sns.barplot(x=df[column].value_counts().head(10).index, y=df[column].value_counts().head(10))
        plt.xticks(rotation=45)

    plt.show()
