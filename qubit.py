from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
from qiskit.primitives import Sampler

# Crear un circuito cuántico con 1 qubit y 1 bit clásico
circuit = QuantumCircuit(1, 1)

# Aplicar una puerta de Hadamard al qubit
circuit.h(0)

# Medir el qubit
circuit.measure(0, 0)

# Dibujar el circuito
print(circuit.draw())

# Simular el circuito
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(circuit, simulator)

# Usamos el sampler para ejecutar el circuito
sampler = Sampler()
result = sampler.run(compiled_circuit).result()

# Obtener y mostrar los resultados
counts = result.quasi_dists[0].binary_probabilities()
print("\nResultados del experimento:", counts)
print("\nResultados del experimento:", counts)
print("\nResultados del experimento:", counts)
