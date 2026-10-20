from MisesMaterial import MisesMaterial

class MaterialSet:

    # コンストラクタ
    # name     : 名前
    # young    : ヤング率
    # poisson  : ポアソン比
    # density  : 密度
    # material : 材料の構成則
    def __init__(self, name, young, poisson=0.3, density=None, material = None):
        self.name = name
        self.young = young
        self.poisson = poisson
        self.density = density
        self.material = MisesMaterial(young, poisson)
        if not material is None:
            self.material = material