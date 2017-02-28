import Game.Utilities as ut


class PlayerClass(object):

    def get_hit_roll(self)->float:
        pass

    def get_saving_throw(self, versus_attack: ut.ATTACK_TYPES)->list[:bool, :float]:
        return -1
