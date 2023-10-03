import pandas as pd

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTSS-TcErkXNk8KB0AlijhitwetxeHD2M3R0HJl2QPMAyFq0fxFX4PFKnzAWLDnratIz67DNL6GsZnV/pub?output=csv"

data = pd.read_csv(url)

missing_values = data.isnull().sum()
print(missing_values)

def remove_outliers_iqr(data, columns):
    for column in columns:
        if pd.api.types.is_numeric_dtype(data[column]):  
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
    return data

columns_to_check = ["show_id", "type", "title", "director", "country", "date_added", "release_year", "rating", "duration", "listed_in"]
data = remove_outliers_iqr(data, columns_to_check)

data.to_csv("cleaned_netflix.csv", index=False)
