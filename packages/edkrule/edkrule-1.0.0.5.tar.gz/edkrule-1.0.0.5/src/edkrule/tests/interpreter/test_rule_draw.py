from edkrule.edk_rule import EdkRule


def test_case1():
    rule_string = """a==1&&b==1?true:false"""
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule1.html")
    assert data == {'name': 'TernaryOperator', 'children': [{'name': 'Anonymous',
                                                             'children': [{'name': 'a', 'value': 'a'},
                                                                          {'name': '==', 'value': '=='},
                                                                          {'name': '1', 'value': '1'}],
                                                             'value': 'a==1'}, {'name': '&&', 'value': '&&'},
                                                            {'name': 'Anonymous',
                                                             'children': [{'name': 'b', 'value': 'b'},
                                                                          {'name': '==', 'value': '=='},
                                                                          {'name': '1', 'value': '1'}],
                                                             'value': 'b==1'}, {'name': '?', 'value': '?'},
                                                            {'name': 'true', 'value': 'true'},
                                                            {'name': ':', 'value': ':'},
                                                            {'name': 'false', 'value': 'false'}],
                    'value': 'a==1&&b==1?true:false'}



def test_case2():
    rule_string = """a&&b==1?x==1?true:false:false"""
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule2.html")
    assert data == {'name': 'TernaryOperator', 'children': [{'name': 'a', 'value': 'a'}, {'name': '&&', 'value': '&&'},
                                                            {'name': 'Anonymous',
                                                             'children': [{'name': 'b', 'value': 'b'},
                                                                          {'name': '==', 'value': '=='},
                                                                          {'name': '1', 'value': '1'}],
                                                             'value': 'b==1'}, {'name': '?', 'value': '?'},
                                                            {'name': 'TernaryOperator', 'children': [
                                                                {'name': 'Anonymous',
                                                                 'children': [{'name': 'x', 'value': 'x'},
                                                                              {'name': '==', 'value': '=='},
                                                                              {'name': '1', 'value': '1'}],
                                                                 'value': 'x==1'}, {'name': '?', 'value': '?'},
                                                                {'name': 'true', 'value': 'true'},
                                                                {'name': ':', 'value': ':'},
                                                                {'name': 'false', 'value': 'false'}],
                                                             'value': 'x==1?true:false'}, {'name': ':', 'value': ':'},
                                                            {'name': 'false', 'value': 'false'}],
                    'value': 'a&&b==1?x==1?true:false:false'}



def test_case3():
    rule_string = """a&&b==1?x==1?true:false:y==1?true:false"""
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule3.html")
    assert data == {'name': 'TernaryOperator', 'children': [{'name': 'a', 'value': 'a'}, {'name': '&&', 'value': '&&'},
                                                            {'name': 'Anonymous',
                                                             'children': [{'name': 'b', 'value': 'b'},
                                                                          {'name': '==', 'value': '=='},
                                                                          {'name': '1', 'value': '1'}],
                                                             'value': 'b==1'}, {'name': '?', 'value': '?'},
                                                            {'name': 'TernaryOperator', 'children': [
                                                                {'name': 'Anonymous',
                                                                 'children': [{'name': 'x', 'value': 'x'},
                                                                              {'name': '==', 'value': '=='},
                                                                              {'name': '1', 'value': '1'}],
                                                                 'value': 'x==1'}, {'name': '?', 'value': '?'},
                                                                {'name': 'true', 'value': 'true'},
                                                                {'name': ':', 'value': ':'},
                                                                {'name': 'false', 'value': 'false'}],
                                                             'value': 'x==1?true:false'}, {'name': ':', 'value': ':'},
                                                            {'name': 'TernaryOperator', 'children': [
                                                                {'name': 'Anonymous',
                                                                 'children': [{'name': 'y', 'value': 'y'},
                                                                              {'name': '==', 'value': '=='},
                                                                              {'name': '1', 'value': '1'}],
                                                                 'value': 'y==1'}, {'name': '?', 'value': '?'},
                                                                {'name': 'true', 'value': 'true'},
                                                                {'name': ':', 'value': ':'},
                                                                {'name': 'false', 'value': 'false'}],
                                                             'value': 'y==1?true:false'}],
                    'value': 'a&&b==1?x==1?true:false:y==1?true:false'}



def test_case4():
    rule_string = """a==1||b==2||c==3"""
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule4.html")
    assert data == {'name': 'Anonymous', 'children': [{'name': 'Anonymous', 'children': [{'name': 'Anonymous',
                                                                                          'children': [{'name': 'a',
                                                                                                        'value': 'a'},
                                                                                                       {'name': '==',
                                                                                                        'value': '=='},
                                                                                                       {'name': '1',
                                                                                                        'value': '1'}],
                                                                                          'value': 'a==1'},
                                                                                         {'name': '||', 'value': '||'},
                                                                                         {'name': 'Anonymous',
                                                                                          'children': [{'name': 'b',
                                                                                                        'value': 'b'},
                                                                                                       {'name': '==',
                                                                                                        'value': '=='},
                                                                                                       {'name': '2',
                                                                                                        'value': '2'}],
                                                                                          'value': 'b==2'}],
                                                       'value': 'a==1||b==2'}, {'name': '||', 'value': '||'},
                                                      {'name': 'Anonymous', 'children': [{'name': 'c', 'value': 'c'},
                                                                                         {'name': '==', 'value': '=='},
                                                                                         {'name': '3', 'value': '3'}],
                                                       'value': 'c==3'}], 'value': 'a==1||b==2||c==3'}



def test_case5():
    rule_string = """a==1||b==2||c"""
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule5.html")
    assert data == {'name': 'Anonymous', 'children': [{'name': 'Anonymous', 'children': [{'name': 'Anonymous',
                                                                                          'children': [{'name': 'a',
                                                                                                        'value': 'a'},
                                                                                                       {'name': '==',
                                                                                                        'value': '=='},
                                                                                                       {'name': '1',
                                                                                                        'value': '1'}],
                                                                                          'value': 'a==1'},
                                                                                         {'name': '||', 'value': '||'},
                                                                                         {'name': 'Anonymous',
                                                                                          'children': [{'name': 'b',
                                                                                                        'value': 'b'},
                                                                                                       {'name': '==',
                                                                                                        'value': '=='},
                                                                                                       {'name': '2',
                                                                                                        'value': '2'}],
                                                                                          'value': 'b==2'}],
                                                       'value': 'a==1||b==2'}, {'name': '||', 'value': '||'},
                                                      {'name': 'c', 'value': 'c'}], 'value': 'a==1||b==2||c'}



def test_case6():
    rule_string = """a||b==2||c==2"""
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule6.html")
    assert data == {'name': 'Anonymous', 'children': [{'name': 'Anonymous', 'children': [{'name': 'a', 'value': 'a'},
                                                                                         {'name': '||', 'value': '||'},
                                                                                         {'name': 'Anonymous',
                                                                                          'children': [{'name': 'b',
                                                                                                        'value': 'b'},
                                                                                                       {'name': '==',
                                                                                                        'value': '=='},
                                                                                                       {'name': '2',
                                                                                                        'value': '2'}],
                                                                                          'value': 'b==2'}],
                                                       'value': 'a||b==2'}, {'name': '||', 'value': '||'},
                                                      {'name': 'Anonymous', 'children': [{'name': 'c', 'value': 'c'},
                                                                                         {'name': '==', 'value': '=='},
                                                                                         {'name': '2', 'value': '2'}],
                                                       'value': 'c==2'}], 'value': 'a||b==2||c==2'}



def test_case7():
    rule_string = """a||(b==2||c==2)"""
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule7.html")
    assert data == {'name': 'Anonymous', 'children': [{'name': 'a', 'value': 'a'}, {'name': '||', 'value': '||'},
                                                      {'name': 'Anonymous', 'children': [{'name': 'Anonymous',
                                                                                          'children': [
                                                                                              {'name': 'Anonymous',
                                                                                               'children': [
                                                                                                   {'name': 'b',
                                                                                                    'value': 'b'},
                                                                                                   {'name': '==',
                                                                                                    'value': '=='},
                                                                                                   {'name': '2',
                                                                                                    'value': '2'}],
                                                                                               'value': 'b==2'},
                                                                                              {'name': '||',
                                                                                               'value': '||'},
                                                                                              {'name': 'Anonymous',
                                                                                               'children': [
                                                                                                   {'name': 'c',
                                                                                                    'value': 'c'},
                                                                                                   {'name': '==',
                                                                                                    'value': '=='},
                                                                                                   {'name': '2',
                                                                                                    'value': '2'}],
                                                                                               'value': 'c==2'}],
                                                                                          'value': 'b==2||c==2'}],
                                                       'value': 'b==2||c==2'}], 'value': 'a||(b==2||c==2)'}



def test_case8():
    rule_string = """max=a>b?a:b"""
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule8.html")
    assert data == {'name': 'Anonymous', 'children': [{'name': 'max', 'value': 'max'}, {'name': '=', 'value': '='},
                                                      {'name': 'TernaryOperator', 'children': [{'name': 'Anonymous',
                                                                                                'children': [
                                                                                                    {'name': 'a',
                                                                                                     'value': 'a'},
                                                                                                    {'name': '>',
                                                                                                     'value': '>'},
                                                                                                    {'name': 'b',
                                                                                                     'value': 'b'}],
                                                                                                'value': 'a>b'},
                                                                                               {'name': '?',
                                                                                                'value': '?'},
                                                                                               {'name': 'a',
                                                                                                'value': 'a'},
                                                                                               {'name': ':',
                                                                                                'value': ':'},
                                                                                               {'name': 'b',
                                                                                                'value': 'b'}],
                                                       'value': 'a>b?a:b'}], 'value': 'max=a>b?a:b'}



def test_case9():
    rule_string = """
    getSubjectArmCode=="Arm A: ONC-392 + LU 177 VIPIVOTIDE" || getSubjectArmCode=="Arm 1: ONC-392 LOW DOSE + LU 177 VIPIVOTIDE" || getSubjectArmCode=="Arm 2: ONC-392 HIGH DOSE + LU 177 VIPIVOTIDE"
    """
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule9.html")
    assert data == {'name': 'Anonymous', 'children': [{'name': 'Anonymous', 'children': [{'name': 'Anonymous',
                                                                                          'children': [{
                                                                                                           'name': 'getSubjectArmCode',
                                                                                                           'value': 'getSubjectArmCode'},
                                                                                                       {'name': '==',
                                                                                                        'value': '=='},
                                                                                                       {
                                                                                                           'name': '"Arm A: ONC-392 + LU 177 VIPIVOTIDE"',
                                                                                                           'value': '"Arm A: ONC-392 + LU 177 VIPIVOTIDE"'}],
                                                                                          'value': 'getSubjectArmCode=="Arm A: ONC-392 + LU 177 VIPIVOTIDE"'},
                                                                                         {'name': '||', 'value': '||'},
                                                                                         {'name': 'Anonymous',
                                                                                          'children': [{
                                                                                                           'name': 'getSubjectArmCode',
                                                                                                           'value': 'getSubjectArmCode'},
                                                                                                       {'name': '==',
                                                                                                        'value': '=='},
                                                                                                       {
                                                                                                           'name': '"Arm 1: ONC-392 LOW DOSE + LU 177 VIPIVOTIDE"',
                                                                                                           'value': '"Arm 1: ONC-392 LOW DOSE + LU 177 VIPIVOTIDE"'}],
                                                                                          'value': 'getSubjectArmCode=="Arm 1: ONC-392 LOW DOSE + LU 177 VIPIVOTIDE"'}],
                                                       'value': 'getSubjectArmCode=="Arm A: ONC-392 + LU 177 VIPIVOTIDE"||getSubjectArmCode=="Arm 1: ONC-392 LOW DOSE + LU 177 VIPIVOTIDE"'},
                                                      {'name': '||', 'value': '||'}, {'name': 'Anonymous', 'children': [
            {'name': 'getSubjectArmCode', 'value': 'getSubjectArmCode'}, {'name': '==', 'value': '=='},
            {'name': '"Arm 2: ONC-392 HIGH DOSE + LU 177 VIPIVOTIDE"',
             'value': '"Arm 2: ONC-392 HIGH DOSE + LU 177 VIPIVOTIDE"'}],
                                                                                      'value': 'getSubjectArmCode=="Arm 2: ONC-392 HIGH DOSE + LU 177 VIPIVOTIDE"'}],
                    'value': '\n    getSubjectArmCode=="Arm A: ONC-392 + LU 177 VIPIVOTIDE" || getSubjectArmCode=="Arm 1: ONC-392 LOW DOSE + LU 177 VIPIVOTIDE" || getSubjectArmCode=="Arm 2: ONC-392 HIGH DOSE + LU 177 VIPIVOTIDE"\n    '}



def test_case10():
    rule_string = """toDate($C1D1.ONC-392 Administration.ECSTDAT)!=""&& toDate($*.*.LBDAT)!=""&& toDate("2015-1-12 "+$C1D1.ONC-392 Administration.ECSTTIM+":00")!="" &&toDate("2015-1-12 "+$*.*.*+":00")!=""?dateDiff($C1D1.ONC-392 Administration.ECSTDAT+" "+$C1D1.ONC-392 Administration.ECSTTIM+":00",$*.*.LBDAT+" "+$*.*.*+":00","m")>0:true"""
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule10.html")
    assert data == {'name': 'TernaryOperator', 'children': [{'name': 'Anonymous', 'children': [{'name': 'toDate',
                                                                                                'children': [{
                                                                                                                 'name': '$C1D1.ONC-392 Administration.ECSTDAT',
                                                                                                                 'value': '$C1D1.ONC-392 Administration.ECSTDAT'}],
                                                                                                'value': 'toDate($C1D1.ONC-392 Administration.ECSTDAT)'},
                                                                                               {'name': '!=',
                                                                                                'value': '!='},
                                                                                               {'name': '""',
                                                                                                'value': '""'}],
                                                             'value': 'toDate($C1D1.ONC-392 Administration.ECSTDAT)!=""'},
                                                            {'name': '&&', 'value': '&&'}, {'name': 'Anonymous',
                                                                                            'children': [
                                                                                                {'name': 'toDate',
                                                                                                 'children': [{
                                                                                                                  'name': '$*.*.LBDAT',
                                                                                                                  'value': '$*.*.LBDAT'}],
                                                                                                 'value': 'toDate($*.*.LBDAT)'},
                                                                                                {'name': '!=',
                                                                                                 'value': '!='},
                                                                                                {'name': '""',
                                                                                                 'value': '""'}],
                                                                                            'value': 'toDate($*.*.LBDAT)!=""'},
                                                            {'name': '&&', 'value': '&&'}, {'name': 'Anonymous',
                                                                                            'children': [
                                                                                                {'name': 'toDate',
                                                                                                 'children': [{
                                                                                                                  'name': 'Anonymous',
                                                                                                                  'children': [
                                                                                                                      {
                                                                                                                          'name': 'Anonymous',
                                                                                                                          'children': [
                                                                                                                              {
                                                                                                                                  'name': '"2015-1-12 "',
                                                                                                                                  'value': '"2015-1-12 "'},
                                                                                                                              {
                                                                                                                                  'name': '+',
                                                                                                                                  'value': '+'},
                                                                                                                              {
                                                                                                                                  'name': '$C1D1.ONC-392 Administration.ECSTTIM',
                                                                                                                                  'value': '$C1D1.ONC-392 Administration.ECSTTIM'}],
                                                                                                                          'value': '"2015-1-12 "+$C1D1.ONC-392 Administration.ECSTTIM'},
                                                                                                                      {
                                                                                                                          'name': '+',
                                                                                                                          'value': '+'},
                                                                                                                      {
                                                                                                                          'name': '":00"',
                                                                                                                          'value': '":00"'}],
                                                                                                                  'value': '"2015-1-12 "+$C1D1.ONC-392 Administration.ECSTTIM+":00"'}],
                                                                                                 'value': 'toDate("2015-1-12 "+$C1D1.ONC-392 Administration.ECSTTIM+":00")'},
                                                                                                {'name': '!=',
                                                                                                 'value': '!='},
                                                                                                {'name': '""',
                                                                                                 'value': '""'}],
                                                                                            'value': 'toDate("2015-1-12 "+$C1D1.ONC-392 Administration.ECSTTIM+":00")!=""'},
                                                            {'name': '&&', 'value': '&&'}, {'name': 'Anonymous',
                                                                                            'children': [
                                                                                                {'name': 'toDate',
                                                                                                 'children': [{
                                                                                                                  'name': 'Anonymous',
                                                                                                                  'children': [
                                                                                                                      {
                                                                                                                          'name': 'Anonymous',
                                                                                                                          'children': [
                                                                                                                              {
                                                                                                                                  'name': '"2015-1-12 "',
                                                                                                                                  'value': '"2015-1-12 "'},
                                                                                                                              {
                                                                                                                                  'name': '+',
                                                                                                                                  'value': '+'},
                                                                                                                              {
                                                                                                                                  'name': '$*.*.*',
                                                                                                                                  'value': '$*.*.*'}],
                                                                                                                          'value': '"2015-1-12 "+$*.*.*'},
                                                                                                                      {
                                                                                                                          'name': '+',
                                                                                                                          'value': '+'},
                                                                                                                      {
                                                                                                                          'name': '":00"',
                                                                                                                          'value': '":00"'}],
                                                                                                                  'value': '"2015-1-12 "+$*.*.*+":00"'}],
                                                                                                 'value': 'toDate("2015-1-12 "+$*.*.*+":00")'},
                                                                                                {'name': '!=',
                                                                                                 'value': '!='},
                                                                                                {'name': '""',
                                                                                                 'value': '""'}],
                                                                                            'value': 'toDate("2015-1-12 "+$*.*.*+":00")!=""'},
                                                            {'name': '?', 'value': '?'}, {'name': 'Anonymous',
                                                                                          'children': [
                                                                                              {'name': 'dateDiff',
                                                                                               'children': [
                                                                                                   {'name': 'Anonymous',
                                                                                                    'children': [{
                                                                                                                     'name': 'Anonymous',
                                                                                                                     'children': [
                                                                                                                         {
                                                                                                                             'name': 'Anonymous',
                                                                                                                             'children': [
                                                                                                                                 {
                                                                                                                                     'name': '$C1D1.ONC-392 Administration.ECSTDAT',
                                                                                                                                     'value': '$C1D1.ONC-392 Administration.ECSTDAT'},
                                                                                                                                 {
                                                                                                                                     'name': '+',
                                                                                                                                     'value': '+'},
                                                                                                                                 {
                                                                                                                                     'name': '" "',
                                                                                                                                     'value': '" "'}],
                                                                                                                             'value': '$C1D1.ONC-392 Administration.ECSTDAT+" "'},
                                                                                                                         {
                                                                                                                             'name': '+',
                                                                                                                             'value': '+'},
                                                                                                                         {
                                                                                                                             'name': '$C1D1.ONC-392 Administration.ECSTTIM',
                                                                                                                             'value': '$C1D1.ONC-392 Administration.ECSTTIM'}],
                                                                                                                     'value': '$C1D1.ONC-392 Administration.ECSTDAT+" "+$C1D1.ONC-392 Administration.ECSTTIM'},
                                                                                                                 {
                                                                                                                     'name': '+',
                                                                                                                     'value': '+'},
                                                                                                                 {
                                                                                                                     'name': '":00"',
                                                                                                                     'value': '":00"'}],
                                                                                                    'value': '$C1D1.ONC-392 Administration.ECSTDAT+" "+$C1D1.ONC-392 Administration.ECSTTIM+":00"'},
                                                                                                   {'name': 'Anonymous',
                                                                                                    'children': [{
                                                                                                                     'name': 'Anonymous',
                                                                                                                     'children': [
                                                                                                                         {
                                                                                                                             'name': 'Anonymous',
                                                                                                                             'children': [
                                                                                                                                 {
                                                                                                                                     'name': '$*.*.LBDAT',
                                                                                                                                     'value': '$*.*.LBDAT'},
                                                                                                                                 {
                                                                                                                                     'name': '+',
                                                                                                                                     'value': '+'},
                                                                                                                                 {
                                                                                                                                     'name': '" "',
                                                                                                                                     'value': '" "'}],
                                                                                                                             'value': '$*.*.LBDAT+" "'},
                                                                                                                         {
                                                                                                                             'name': '+',
                                                                                                                             'value': '+'},
                                                                                                                         {
                                                                                                                             'name': '$*.*.*',
                                                                                                                             'value': '$*.*.*'}],
                                                                                                                     'value': '$*.*.LBDAT+" "+$*.*.*'},
                                                                                                                 {
                                                                                                                     'name': '+',
                                                                                                                     'value': '+'},
                                                                                                                 {
                                                                                                                     'name': '":00"',
                                                                                                                     'value': '":00"'}],
                                                                                                    'value': '$*.*.LBDAT+" "+$*.*.*+":00"'},
                                                                                                   {'name': '"m"',
                                                                                                    'value': '"m"'}],
                                                                                               'value': 'dateDiff($C1D1.ONC-392 Administration.ECSTDAT+" "+$C1D1.ONC-392 Administration.ECSTTIM+":00",$*.*.LBDAT+" "+$*.*.*+":00","m")'},
                                                                                              {'name': '>',
                                                                                               'value': '>'},
                                                                                              {'name': '0',
                                                                                               'value': '0'}],
                                                                                          'value': 'dateDiff($C1D1.ONC-392 Administration.ECSTDAT+" "+$C1D1.ONC-392 Administration.ECSTTIM+":00",$*.*.LBDAT+" "+$*.*.*+":00","m")>0'},
                                                            {'name': ':', 'value': ':'},
                                                            {'name': 'true', 'value': 'true'}],
                    'value': 'toDate($C1D1.ONC-392 Administration.ECSTDAT)!=""&& toDate($*.*.LBDAT)!=""&& toDate("2015-1-12 "+$C1D1.ONC-392 Administration.ECSTTIM+":00")!="" &&toDate("2015-1-12 "+$*.*.*+":00")!=""?dateDiff($C1D1.ONC-392 Administration.ECSTDAT+" "+$C1D1.ONC-392 Administration.ECSTTIM+":00",$*.*.LBDAT+" "+$*.*.*+":00","m")>0:true'}



def test_case11():
    rule_string = """autoValue(RoundN(sum(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG, $*.Target Lesions Assessment (Details) (Screening).TLLOC != 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU == "CM") , multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG, $*.Target Lesions Assessment (Details) (Screening).TLLOC != 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU == "MM"),1/10) , getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT, $*.Target Lesions Assessment (Details) (Screening).TLLOC == 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU== "CM") , multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT, $*.Target Lesions Assessment (Details) (Screening).TLLOC == 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU== "MM"),1/10)), 0.01), true)"""
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule11.html")
    assert data == {'name': 'autoValue', 'children': [{'name': 'RoundN', 'children': [{'name': 'sum', 'children': [
        {'name': 'getSumOfItemInLog', 'children': [{'name': '$*.Target Lesions Assessment (Details) (Screening).TLLONG',
                                                    'value': '$*.Target Lesions Assessment (Details) (Screening).TLLONG'},
                                                   {'name': 'Anonymous', 'children': [{'name': 'Anonymous',
                                                                                       'children': [{
                                                                                                        'name': '$*.Target Lesions Assessment (Details) (Screening).TLLOC ',
                                                                                                        'value': '$*.Target Lesions Assessment (Details) (Screening).TLLOC '},
                                                                                                    {'name': '!=',
                                                                                                     'value': '!='},
                                                                                                    {'name': '11',
                                                                                                     'value': '11'}],
                                                                                       'value': '$*.Target Lesions Assessment (Details) (Screening).TLLOC !=11'},
                                                                                      {'name': '&&', 'value': '&&'},
                                                                                      {'name': 'Anonymous',
                                                                                       'children': [{
                                                                                                        'name': '$*.Target Lesions Assessment (Details) (Screening).TLDIAU ',
                                                                                                        'value': '$*.Target Lesions Assessment (Details) (Screening).TLDIAU '},
                                                                                                    {'name': '==',
                                                                                                     'value': '=='},
                                                                                                    {'name': '"CM"',
                                                                                                     'value': '"CM"'}],
                                                                                       'value': '$*.Target Lesions Assessment (Details) (Screening).TLDIAU =="CM"'}],
                                                    'value': '$*.Target Lesions Assessment (Details) (Screening).TLLOC !=11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU =="CM"'}],
         'value': 'getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG,$*.Target Lesions Assessment (Details) (Screening).TLLOC !=11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU =="CM")'},
        {'name': 'multiply', 'children': [{'name': 'getSumOfItemInLog', 'children': [
            {'name': '$*.Target Lesions Assessment (Details) (Screening).TLLONG',
             'value': '$*.Target Lesions Assessment (Details) (Screening).TLLONG'}, {'name': 'Anonymous', 'children': [
                {'name': 'Anonymous', 'children': [{'name': '$*.Target Lesions Assessment (Details) (Screening).TLLOC ',
                                                    'value': '$*.Target Lesions Assessment (Details) (Screening).TLLOC '},
                                                   {'name': '!=', 'value': '!='}, {'name': '11', 'value': '11'}],
                 'value': '$*.Target Lesions Assessment (Details) (Screening).TLLOC !=11'},
                {'name': '&&', 'value': '&&'}, {'name': 'Anonymous', 'children': [
                    {'name': '$*.Target Lesions Assessment (Details) (Screening).TLDIAU ',
                     'value': '$*.Target Lesions Assessment (Details) (Screening).TLDIAU '},
                    {'name': '==', 'value': '=='}, {'name': '"MM"', 'value': '"MM"'}],
                                                'value': '$*.Target Lesions Assessment (Details) (Screening).TLDIAU =="MM"'}],
                                                                                     'value': '$*.Target Lesions Assessment (Details) (Screening).TLLOC !=11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU =="MM"'}],
                                           'value': 'getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG,$*.Target Lesions Assessment (Details) (Screening).TLLOC !=11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU =="MM")'},
                                          {'name': 'Anonymous',
                                           'children': [{'name': '1', 'value': '1'}, {'name': '/', 'value': '/'},
                                                        {'name': '10', 'value': '10'}], 'value': '1/10'}],
         'value': 'multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG,$*.Target Lesions Assessment (Details) (Screening).TLLOC !=11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU =="MM"),1/10)'},
        {'name': 'getSumOfItemInLog', 'children': [
            {'name': '$*.Target Lesions Assessment (Details) (Screening).TLSHORT',
             'value': '$*.Target Lesions Assessment (Details) (Screening).TLSHORT'}, {'name': 'Anonymous', 'children': [
                {'name': 'Anonymous', 'children': [{'name': '$*.Target Lesions Assessment (Details) (Screening).TLLOC ',
                                                    'value': '$*.Target Lesions Assessment (Details) (Screening).TLLOC '},
                                                   {'name': '==', 'value': '=='}, {'name': '11', 'value': '11'}],
                 'value': '$*.Target Lesions Assessment (Details) (Screening).TLLOC ==11'},
                {'name': '&&', 'value': '&&'}, {'name': 'Anonymous', 'children': [
                    {'name': '$*.Target Lesions Assessment (Details) (Screening).TLDIAU',
                     'value': '$*.Target Lesions Assessment (Details) (Screening).TLDIAU'},
                    {'name': '==', 'value': '=='}, {'name': '"CM"', 'value': '"CM"'}],
                                                'value': '$*.Target Lesions Assessment (Details) (Screening).TLDIAU=="CM"'}],
                                                                                      'value': '$*.Target Lesions Assessment (Details) (Screening).TLLOC ==11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU=="CM"'}],
         'value': 'getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT,$*.Target Lesions Assessment (Details) (Screening).TLLOC ==11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU=="CM")'},
        {'name': 'multiply', 'children': [{'name': 'getSumOfItemInLog', 'children': [
            {'name': '$*.Target Lesions Assessment (Details) (Screening).TLSHORT',
             'value': '$*.Target Lesions Assessment (Details) (Screening).TLSHORT'}, {'name': 'Anonymous', 'children': [
                {'name': 'Anonymous', 'children': [{'name': '$*.Target Lesions Assessment (Details) (Screening).TLLOC ',
                                                    'value': '$*.Target Lesions Assessment (Details) (Screening).TLLOC '},
                                                   {'name': '==', 'value': '=='}, {'name': '11', 'value': '11'}],
                 'value': '$*.Target Lesions Assessment (Details) (Screening).TLLOC ==11'},
                {'name': '&&', 'value': '&&'}, {'name': 'Anonymous', 'children': [
                    {'name': '$*.Target Lesions Assessment (Details) (Screening).TLDIAU',
                     'value': '$*.Target Lesions Assessment (Details) (Screening).TLDIAU'},
                    {'name': '==', 'value': '=='}, {'name': '"MM"', 'value': '"MM"'}],
                                                'value': '$*.Target Lesions Assessment (Details) (Screening).TLDIAU=="MM"'}],
                                                                                      'value': '$*.Target Lesions Assessment (Details) (Screening).TLLOC ==11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU=="MM"'}],
                                           'value': 'getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT,$*.Target Lesions Assessment (Details) (Screening).TLLOC ==11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU=="MM")'},
                                          {'name': 'Anonymous',
                                           'children': [{'name': '1', 'value': '1'}, {'name': '/', 'value': '/'},
                                                        {'name': '10', 'value': '10'}], 'value': '1/10'}],
         'value': 'multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT,$*.Target Lesions Assessment (Details) (Screening).TLLOC ==11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU=="MM"),1/10)'}],
                                                                                       'value': 'sum(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG,$*.Target Lesions Assessment (Details) (Screening).TLLOC !=11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU =="CM"),multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG,$*.Target Lesions Assessment (Details) (Screening).TLLOC !=11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU =="MM"),1/10),getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT,$*.Target Lesions Assessment (Details) (Screening).TLLOC ==11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU=="CM"),multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT,$*.Target Lesions Assessment (Details) (Screening).TLLOC ==11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU=="MM"),1/10))'},
                                                                                      {'name': '0.01',
                                                                                       'value': '0.01'}],
                                                       'value': 'RoundN(sum(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG,$*.Target Lesions Assessment (Details) (Screening).TLLOC !=11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU =="CM"),multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG,$*.Target Lesions Assessment (Details) (Screening).TLLOC !=11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU =="MM"),1/10),getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT,$*.Target Lesions Assessment (Details) (Screening).TLLOC ==11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU=="CM"),multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT,$*.Target Lesions Assessment (Details) (Screening).TLLOC ==11&&$*.Target Lesions Assessment (Details) (Screening).TLDIAU=="MM"),1/10)),0.01)'},
                                                      {'name': 'true', 'value': 'true'}],
                    'value': 'autoValue(RoundN(sum(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG, $*.Target Lesions Assessment (Details) (Screening).TLLOC != 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU == "CM") , multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLLONG, $*.Target Lesions Assessment (Details) (Screening).TLLOC != 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU == "MM"),1/10) , getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT, $*.Target Lesions Assessment (Details) (Screening).TLLOC == 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU== "CM") , multiply(getSumOfItemInLog($*.Target Lesions Assessment (Details) (Screening).TLSHORT, $*.Target Lesions Assessment (Details) (Screening).TLLOC == 11 && $*.Target Lesions Assessment (Details) (Screening).TLDIAU== "MM"),1/10)), 0.01), true)'}



def test_case12():
    rule_string = """mustAnswer($*.*.CRONGO)&&$*.*.CRONGO=='N'?$*.*.*!='':true"""
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    EdkRule.draw(rule_string, "rule12.html")
    assert data == {'name': 'TernaryOperator', 'children': [
        {'name': 'mustAnswer', 'children': [{'name': '$*.*.CRONGO', 'value': '$*.*.CRONGO'}],
         'value': 'mustAnswer($*.*.CRONGO)'}, {'name': '&&', 'value': '&&'}, {'name': 'Anonymous', 'children': [
            {'name': '$*.*.CRONGO', 'value': '$*.*.CRONGO'}, {'name': '==', 'value': '=='},
            {'name': "'N'", 'value': "'N'"}], 'value': "$*.*.CRONGO=='N'"}, {'name': '?', 'value': '?'},
        {'name': 'Anonymous', 'children': [{'name': '$*.*.*', 'value': '$*.*.*'}, {'name': '!=', 'value': '!='},
                                           {'name': "''", 'value': "''"}], 'value': "$*.*.*!=''"},
        {'name': ':', 'value': ':'}, {'name': 'true', 'value': 'true'}],
                    'value': "mustAnswer($*.*.CRONGO)&&$*.*.CRONGO=='N'?$*.*.*!='':true"}


def test_case13():
    rule_string = """a==1&&b==2||c"""
    expression = EdkRule.expression(rule_string)
    data = expression.tree_data()
    assert data == {'name': 'Anonymous', 'children': [{'name': 'Anonymous', 'children': [{'name': 'Anonymous', 'children': [{'name': 'a', 'value': 'a'}, {'name': '==', 'value': '=='}, {'name': '1', 'value': '1'}], 'value': 'a==1'}, {'name': '&&', 'value': '&&'}, {'name': 'Anonymous', 'children': [{'name': 'b', 'value': 'b'}, {'name': '==', 'value': '=='}, {'name': '2', 'value': '2'}], 'value': 'b==2'}], 'value': 'a==1&&b==2'}, {'name': '||', 'value': '||'}, {'name': 'c', 'value': 'c'}], 'value': 'a==1&&b==2||c'}
    EdkRule.draw(rule_string, "rule13.html")


def test_rule_draw():
    test_case1()
    test_case2()
    test_case3()
    test_case4()
    test_case5()
    test_case6()
    test_case7()
    test_case8()
    test_case9()
    test_case10()
    test_case11()
    test_case12()
    test_case13()






