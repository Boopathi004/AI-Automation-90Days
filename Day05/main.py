# it belongs to (module) packeges_demo

from packeges_demo.calculator import add
from packeges_demo.converter import cm_to_meter
from packeges_demo.valitator import is_adult

print("Addition:", add(10, 20))
print("Meters:", cm_to_meter(250))
print("Is Adult:", is_adult(22))