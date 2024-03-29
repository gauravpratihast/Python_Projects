import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style


data = pd.read_csv('student-mat.csv', sep=';')
# print(data.head())
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]


predict = "G3"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
# best = 0
# for _ in range(30):
#     x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
#     linear = linear_model.LinearRegression()
#
#     linear.fit(x_train,y_train)
#     acc = linear.score(x_test,y_test)
#
#
#     if acc > best:
#         best = acc
#         with open('Studentmodel.pickle', 'wb') as f:
#             pickle.dump(linear, f)

# print(best)
pickle_in = open('Studentmodel.pickle', 'rb')
linear = pickle.load(pickle_in)

# print("Co: \n", linear.coef_)
# print('Intercept: \n', linear.intercept_)


# prediction= linear.predict(x_test)

# for x in range(len(prediction)):
#     print(prediction[x], x_test[x], y_test[x])

# acc = linear.score(x_test,y_test)
# print(acc)
print(linear.score(x_test, y_test))
# p = 'absences'
# style.use('ggplot')
# pyplot.scatter(data[p], data["G3"])
# pyplot.xlabel(p)
# pyplot.ylabel("final Grade")
# pyplot.show()
print('Task Done')