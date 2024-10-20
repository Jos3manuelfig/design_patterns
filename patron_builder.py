# Producto: La clase que queremos construir
class Pizza:
    def __init__(self):
        self.masa = None
        self.salsa = None
        self.ingrediente = None

    def __str__(self):
        return f"Pizza con masa {self.masa}, salsa {self.salsa} y {self.ingrediente} como ingrediente."


# Builder: Clase abstracta que define la interfaz para crear los diferentes componentes de un producto
class PizzaBuilder:
    def definir_masa(self, masa):
        raise NotImplementedError

    def definir_salsa(self, salsa):
        raise NotImplementedError

    def definir_ingrediente(self, ingrediente):
        raise NotImplementedError

    def obtener_pizza(self):
        raise NotImplementedError


# ConcreteBuilder: Implementa la interfaz del Builder y crea el producto paso a paso
class MargheritaPizzaBuilder(PizzaBuilder):
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


# Director: Controla el proceso de construcción utilizando un Builder específico
class DirectorPizza:
    def __init__(self, builder):
        self.builder = builder

    def hacer_pizza(self):
        return (self.builder
                .definir_masa("delgada")
                .definir_salsa("tomate")
                .definir_ingrediente("mozzarella")
                .obtener_pizza())


# Uso del patrón Builder
if __name__ == "__main__":
    # Elegimos un builder específico para una pizza Margherita
    constructor = MargheritaPizzaBuilder()
    director = DirectorPizza(constructor)

    # El director construye la pizza paso a paso
    pizza = director.hacer_pizza()

    print(pizza)  # Output: Pizza con masa delgada, salsa tomate y mozzarella como ingrediente.
