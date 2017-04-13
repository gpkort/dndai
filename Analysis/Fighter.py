import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn import metrics
import numpy as np
from sklearn.cross_validation import train_test_split

"""
'strength',
'intelligence',
'wisdom',
'dexterity',
'constitution',
'charisma',
'score'
"""


def analyze():
    battles = pd.read_pickle('battles')
    # print(battles.describe())
    # features = ['strength', 'dexterity', 'constitution']
    features = ['strength', 'intelligence', 'wisdom', 'dexterity', 'constitution', 'charisma']
    X = battles[features]
    y = battles['score']
    # linreg = LinearRegression()
    # linreg.fit(X, y)
    #
    # coeff = zip(features, linreg.coef_)
    #
    # for co in coeff:
    #     print(co)

    # sns.pairplot(battles, x_vars=features, y_vars='score', kind='reg')
    # sns.plt.show()

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    linreg = LinearRegression()
    linreg.fit(X_train, y_train)
    coeff = zip(features, linreg.coef_)

    for co in coeff:
        print(co)

    y_pred = linreg.predict(X_test)
    # predict our testing set

    print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    print(y_train.mean())
    print(y_pred.mean())


def compare():
    battles = pd.read_pickle('battles')
    smart_battles = pd.read_pickle('battles_attrib')

    print(battles['score'].describe())
    print(smart_battles['score'].describe())











if __name__ == '__main__':
    compare()