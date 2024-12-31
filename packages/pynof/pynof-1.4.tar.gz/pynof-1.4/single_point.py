import pynof

mol = pynof.molecule("""
0 1
  O   -0.0000000   -0.5695024    0.0000000
  F    0.0000000    0.2398016   -1.0454190
  F   -0.0000000    0.2398016    1.0454190
""")

p = pynof.param(mol,"cc-pvdz")

p.ipnof = 4
p.occ_method = "EBI"

p.RI = True

E,C,n,fmiug0 = pynof.compute_energy(mol,p)
