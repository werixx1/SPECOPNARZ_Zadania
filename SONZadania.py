# ZADANIE 1
def is_criticality_balanced(temp, neutrons):
  if temp > 800:
     return False
  if neutrons < 500:
    return False
  if (temp*neutrons) > 500000:
    return False
  return True

print(is_criticality_balanced(750, 600), is_criticality_balanced(100,200))
