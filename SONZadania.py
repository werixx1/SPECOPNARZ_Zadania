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

# ZADANIE 2
def reactor_efficiency(voltage, current, theoretical_max_power):
  generated_power = voltage*current
  spr = (generated_power/theoretical_max_power)*100
  if spr >= 80:
    return 'zielony'
  elif spr < 80 and spr >= 60:
    return 'pomaranczowy'
  elif spr < 60 and spr >= 30:
    return 'czerwony'
  else:
    return 'czarny'
print(reactor_efficiency(1,2,32))

# ZADANIE 3
def fail_safe(kelwiny, neutrony_produkowane_na_sekunde, prog):
  stan = kelwiny*neutrony_produkowane_na_sekunde
  if stan < (0.9*prog):
    return 'LOW'
  elif stan < (prog*0.9) or stan > (prog*1.1):
    return 'NORMAL'
print(fail_safe(2,2,2))
