class Pizza:
    def __init__(self):
        self.masa = None
        self.salsa = None
        self.ingrediente = None

    def __str__(self):
        return f"Pizza con masa {self.masa}, salsa {self.salsa} y {self.ingrediente} como ingrediente"


class PizzaBase:
    def definir_masa(self, masa):
        raise NotImplementedError

    def definir_salsa(self, salsa):
        raise NotImplementedError

    def definir_ingrediente(self, ingrediente):
        raise NotImplementedError

    def obtener_pizza(self):
        raise NotImplementedError


class PizzaMargarita(PizzaBase):
    def __init__(self):
        self.pizza = Pizza()

    def definir_masa(self, masa):
        self.pizza.masa = masa
        return self

    def definir_salsa(self, salsa):
        self.pizza.salsa = salsa
        return self

    def definir_ingrediente(self, ingrediente):
        self.pizza.ingrediente = ingrediente
        return self

    def obtener_pizza(self):
        return self.pizza


class CocineroPizza:
    def __init__(self, builder):
        self.builder = builder

    def preparar_pizza(self):
        return (self.builder
                .definir_masa("delgada")
                .definir_salsa("tomate")
                .definir_ingrediente("Tocineta")
                .obtener_pizza()
        )


tipo_pizza = PizzaMargarita()
cocinar_pizza = CocineroPizza(tipo_pizza)

pizza = cocinar_pizza.preparar_pizza()
print(pizza)
