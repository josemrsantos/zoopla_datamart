from ..datamart import *

def test_create_fact_with_2_dimensions_insert_line():
    ''' with 2 identical lines, both get stored
    '''
    dimension1 = Dimension("dimension1")
    dimension2 = Dimension("dimension2")
    fact = Fact("test_fact")
    fact.addDimension(dimension1)
    fact.addDimension(dimension2)
    fact.addFactLine(('test1', 'test2'))
    assert fact.id_value == 2
    assert len(fact.values) == 1
    assert len(fact.dimensions[0].values) == 1
    assert len(fact.dimensions[1].values) == 1

