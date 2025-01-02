import json
from pathlib import Path

from edkrule.edk_rule import EdkRule

# expression = EdkRule().expression("condition(mustAnswer(toNum($*.*.*)), isRange($*.*.*, 40,160))")
# expression = EdkRule().expression("toDate($*.*.*)!=\"\"&&toDate(getMinByLog($*.Informed Consent.DSSTDAT))!=\"\"?dateDiff(getMinByLog($*.Informed Consent.DSSTDAT),$*.*.*, \"D\")>0:true")
# expression = EdkRule().expression("""autoValue(RoundN(sum(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG, $*.Target Lesions Assessment (Details) (Screening).TLLOC != 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU == "CM") , multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG, $*.Target Lesions Assessment (Details) (Screening).TLLOC != 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU == "MM"),1/10) , getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT, $*.Target Lesions Assessment (Details) (Screening).TLLOC == 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU== "CM") , multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT, $*.Target Lesions Assessment (Details) (Screening).TLLOC == 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU== "MM"),1/10)), 0.01), true)""")
expression = EdkRule().draw("""autoValue(RoundN(sum(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG, $*.Target Lesions Assessment (Details) (Screening).TLLOC != 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU == "CM") , multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG, $*.Target Lesions Assessment (Details) (Screening).TLLOC != 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU == "MM"),1/10) , getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT, $*.Target Lesions Assessment (Details) (Screening).TLLOC == 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU== "CM") , multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT, $*.Target Lesions Assessment (Details) (Screening).TLLOC == 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU== "MM"),1/10)), 0.01), true)""", Path("test.html"))
# data = expression.tree_data()
# print(data)
# with open("tree.json", 'w') as f:
#     json.dump(data, f)
