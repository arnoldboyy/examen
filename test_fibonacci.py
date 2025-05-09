import timeit
from fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    print("¡Pruebas pasadas! Código de Kevin Arnold Cortes Pacheco")

if __name__ == "__main__":
    test_fibonacci()
    time = timeit.timeit("fibonacci(20)", setup="from fibonacci import fibonacci", number=100)
    print(f"Tiempo de ejecución (100 iteraciones de fibonacci(20)): {time:.4f} segundos")
