def soma(x: int | float, y: int | float) -> int | float:
    return x + y

def multiplica(
        x: int | float,
        y: int | float,
        z: int | float | None = None

) -> int | float:
    if z is None:
        return x * y 
    return x * y * z

variavel_2 = 2
variavel_3 = 3
variavel_4 = 4

