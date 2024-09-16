# Dy regjistra kubitë
qreg1 = cirq.LineQubit.range(2)
qreg2 = cirq.LineQubit.range(2, 4)

# Definimi i një porte Adder me input 2D 
adder = Adder(input_register=[2, 2], target_register=[2, 2])

# Definimi i qarkut
circ = cirq.Circuit(
    cirq.X.on(qreg1[0]),
    cirq.X.on(qreg2[1]),
    adder.on(*qreg1, *qreg2),
    cirq.measure_each(*qreg1),
    cirq.measure_each(*qreg2)
)

# Paraqitja e qarkut
print("Qarku:\n")
print(circ)

# Paraqitja e rezultateve
print("\n\nRezultatet:\n")
print(cirq.sample(circ, repetitions=5).data)
