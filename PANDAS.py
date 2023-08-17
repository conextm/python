import pandas as pd
# data in the form of list of tuples
data = (
        ('David', 18, 7),
        ('Carlos', 15, 6),
        ('Brayan', 17, 8),
)

# create DataFrame using data
df = pd.DataFrame(data=data, columns=('Name', 'Age', 'Score'))
df
