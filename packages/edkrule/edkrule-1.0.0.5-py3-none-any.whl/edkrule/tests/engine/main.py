from edkrule.edk_rule import EdkRule







if __name__ == '__main__':
    rule_string = """autoValue(RoundN(sum(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG, $*.Target Lesions Assessment (Details) (Screening).TLLOC != 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU == "CM") , multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG, $*.Target Lesions Assessment (Details) (Screening).TLLOC != 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU == "MM"),1/10) , getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT, $*.Target Lesions Assessment (Details) (Screening).TLLOC == 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU== "CM") , multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT, $*.Target Lesions Assessment (Details) (Screening).TLLOC == 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU== "MM"),1/10)), 0.01), true)"""
    rule_string = """' '+b==1?2+3:4+1+2"""
    expression = EdkRule.expression(rule_string)
    r = EdkRule.run("1/1", none_default=True)
    print(r)

    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule1999.html")