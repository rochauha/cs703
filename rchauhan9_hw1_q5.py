from cvc5.pythonic import *

# upper and lower bounds for intervals represented by nodes a, b, c, d
la = Real("la")
lb = Real("lb")
lc = Real("lc")
ld = Real("ld")

ha = Real("ha")
hb = Real("hb")
hc = Real("hc")
hd = Real("hd")


node_f = And( Lt(la, ha), Lt(lb, hb), Lt(lc, hc), Lt(ld, hd) )

edge_f = And( Lt(la, hb), Lt(lb, ha),
              Lt(la, hc), Lt(lc, ha),
              Lt(lb, hd), Lt(ld, hb),
              Lt(lc, hd), Lt(ld, hc) )

noedge_f = And(Not(And(Lt(la, hd), Lt(ld, ha))),
               Not(And( Lt(lb, hc), Lt(lc, hb))))

final_formula = And(node_f, edge_f, noedge_f)

solver = Solver("ALL")
#  solver.add(Exists([la, lb, lc, ld, ha, hb, hc, hd], final_formula))
solver.add(Not(final_formula))

result = solver.check()

if result == sat:
    print("sat")

    model = solver.model()
    print(model)

else:
    print("unsat")
