class root:
    @staticmethod
    def root(degree,radicand):
        return radicand ** degree(1/float(radicand))
