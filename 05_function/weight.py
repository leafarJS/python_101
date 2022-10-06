"""
Gravity works differently in Zortan, use the following formula
to see how much you weight on Zortan.
Zortan Weight = (Earth Weight + 32) / 8
"""
""" 
La gravedad funciona de manera diferente en Zortan, usa la siguiente fórmula para ver cuánto pesas en Zortan.
Peso de Zortan = (Peso de la Tierra + 32) / 8
"""
def calc_weight(weight: float) -> float:
  return (weight + 32) / 8


print(f"You weight {calc_weight(72)} kgs. on Zortan")

print(f"You weight {calc_weight(120):.2f} kgs. on Zortan")