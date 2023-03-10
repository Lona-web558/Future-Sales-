import statsmodels.api as sm
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/advertising.csv")
print(data.head())

import plotly.express as px
import plotly.graph_objects as go
figure = px.scatter(data_frame=data, x="Sales", y="TV", size="TV", trendline="ols")

figure.show()

#future sales prediction model

x = np.array(data.drop(["Sales"], 1))
y = np.array(data["Sales"])
xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                           test_size=0.2,
                           random_state=42)
                           
 #train the model
model = LinearRegression()
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))

#input values

features = np.array([[230.1, 37.8, 69.2]])
print(model.predict(features))