from cvc5.pythonic import *

# Boolean variables r, g, b for each node in graph H
r0 = Bool("r0")
g0 = Bool("g0")
b0 = Bool("b0")

r1 = Bool("r1")
g1 = Bool("g1")
b1 = Bool("b1")

r2 = Bool("r2")
g2 = Bool("g2")
b2 = Bool("b2")

r3 = Bool("r3")
g3 = Bool("g3")
b3 = Bool("b3")

r4 = Bool("r4")
g4 = Bool("g4")
b4 = Bool("b4")

node0_f = Or(r0, g0, b0)
node1_f = Or(r1, g1, b1)
node2_f = Or(r2, g2, b2)
node3_f = Or(r3, g3, b3)
node4_f = Or(r4, g4, b4)

edge01_f = And( Or(Not(r0), Not(r1)), Or(Not(g0), Not(g1)), Or(Not(b0), Not(b1)) )
edge02_f = And( Or(Not(r0), Not(r2)), Or(Not(g0), Not(g2)), Or(Not(b0), Not(b2)) )
edge12_f = And( Or(Not(r1), Not(r2)), Or(Not(g1), Not(g2)), Or(Not(b1), Not(b2)) )
edge13_f = And( Or(Not(r1), Not(r3)), Or(Not(g1), Not(g3)), Or(Not(b1), Not(b3)) )
edge14_f = And( Or(Not(r1), Not(r4)), Or(Not(g1), Not(g4)), Or(Not(b1), Not(b4)) )
edge23_f = And( Or(Not(r2), Not(r3)), Or(Not(g2), Not(g3)), Or(Not(b2), Not(b3)) )
edge24_f = And( Or(Not(r2), Not(r4)), Or(Not(g2), Not(g4)), Or(Not(b2), Not(b4)) )


final_formula = And(node0_f, node1_f, node2_f, node3_f, node4_f,
                    edge01_f, edge02_f, edge12_f,
                    edge13_f, edge14_f, edge23_f, edge24_f)

solver = Solver("ALL")
solver.add(final_formula)

result = solver.check()

print("For graph H :")
if result == sat:
    print("sat i.e 3 colorable")
    model = solver.model()
    if (model[r0]): print("node 0 : red")
    if (model[g0]): print("node 0 : green")
    if (model[b0]): print("node 0 : blue")

    if (model[r1]): print("node 1 : red")
    if (model[g1]): print("node 1 : green")
    if (model[b1]): print("node 1 : blue")

    if (model[r2]): print("node 2 : red")
    if (model[g2]): print("node 2 : green")
    if (model[b2]): print("node 2 : blue")

    if (model[r3]): print("node 3 : red")
    if (model[g3]): print("node 3 : green")
    if (model[b3]): print("node 3 : blue")

    if (model[r4]): print("node 4 : red")
    if (model[g4]): print("node 4 : green")
    if (model[b4]): print("node 4 : blue")

else:
    print("unsat i.e not 3 colorable")


