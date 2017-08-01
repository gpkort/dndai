from sklearn.linear_model import LinearRegression
from Game.Characters.Attributes import Attributes
import pandas as pd

FEATURES = ['strength', 'intelligence', 'wisdom', 'dexterity', 'constitution', 'charisma', 'score']


def get_training_dataset():
    return pd.DataFrame(columns=FEATURES)


def get_coeff(battles):
    X = battles[FEATURES]
    y = battles['score']
    linreg = LinearRegression()
    linreg.fit(X, y)
    coeff = {}

    for name, val in zip(FEATURES, linreg.coef_):
        coeff[name] = val

    return coeff


def adjust_attributes(coeff, attribs: Attributes):
    most = 0
    least = 1.0
    target_name = ''
    source_name = ''

    for key, val in coeff.items():
        if val > most:
            most = val
            target_name = key

    coeff.pop(target_name)

    for key, val in coeff.items():
        if val < least:
            least = val
            source_name = key

    coeff.pop(source_name)
    attribs.reallocate(source_name, target_name)

    return coeff


def smart_adjust(character, coeff):
    adjust_attributes(coeff, character.attributes)

