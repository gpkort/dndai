from Simulator import Utilities as ut, FighterUtil as fu

if __name__ == '__main__':
    battles = fu.run_fighter_battle(ut.get_training_dataset(), 100)
    print(battles.head())
    print(battles.describe())

