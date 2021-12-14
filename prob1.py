class Factory:
    name = None

    def engine(self):
        return "Двигатель создан"

    def bridge(self):
        return "Ходовая часть создана"

honda = Factory()
honda.name = "Honda Accord"
print(honda.name, honda.engine(), honda.bridge())

class Toyota(Factory):
    def wheels(self):
        return "Колеса готовы"

    def windows(self):
        return "Стекла готовы"

fit = Toyota()
fit.name = "Fit"
lst = [fit.name, fit.wheels(), fit.windows(), fit.bridge(), fit.engine()]
print(lst)