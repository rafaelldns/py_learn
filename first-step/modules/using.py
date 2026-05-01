import modules.op_math as op_math
import modules.utilities as utilities

su = op_math.suma(2, 5)
print(su)
suub = op_math.suba(2, 5)
print(suub)
mt = op_math.mult(2, 5)
print(mt)

ms = input("What message do you want to insert? ")
utilities.msg(ms)

cit = utilities.city()
utilities.print_ct(f"Your city is {cit} !")
