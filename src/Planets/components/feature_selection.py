from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd

X_train = pd.read_csv("X_train.csv")
y_train = pd.read_csv("y_train.csv")

### Apply SelectKBest Algorithm
ordered_rank_features=SelectKBest(score_func=chi2,k=20)
ordered_feature=ordered_rank_features.fit(X_train,y_train)

dfscores=pd.DataFrame(ordered_feature.scores_,columns=["Score"])
dfcolumns=pd.DataFrame(X_train.columns)

# Q: A column in the dataset unturned into integer, what is the column name?

# Select columns with string data (object dtype)
string_columns = X_train.select_dtypes(include=['object'])

# Print the string columns
print(string_columns)

# A: The column named "Spectral Type" unturned into integer.

# After:

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd

X_train = pd.read_csv("X_train.csv")
y_train = pd.read_csv("y_train.csv")

# Select columns with string data (object dtype)
string_columns = X_train.select_dtypes(include=['object'])

# Print the string columns
print(string_columns) # Fixed

threshold=0.7

# find and remove correlated features
def correlation(dataset, threshold):
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold: # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
    return col_corr

correlation_list = list(correlation(X_train,threshold))

correlation_list

file_path = "correlation_list.txt"  # Change the path as needed

# Open the file in write mode and write the list items to it
with open(file_path, 'w') as file:
    for item in correlation_list:
        file.write(item + '\n')

# Confirm that the file has been created
print(f"The list has been written to {file_path}")