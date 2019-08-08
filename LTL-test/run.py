from impo import *
from paths import *
from main_to_do import *
imp = impo()
lst = paths(imp[0], imp[1])
for formula in imp[2]:
    print(LTL_check(lst, formula))