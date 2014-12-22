from ..datamart import *

def test_create_dimension():
    dimension = Dimension("test_dimension")
    assert dimension.is_degenerate == False

def test_create_dimension_insert_2_identical_lines():
    ''' with 2 identical lines, only one gets stored
    '''
    dimension = Dimension("test_dimension")
    dimension.addDimensionLine('test')
    dimension.addDimensionLine('test')
    assert dimension.id_value == 1
    assert len(list(dimension.values)) == 1

def test_create_dimension_insert_2_identical_lines_and_1_different():
    ''' with 2 identical lines and one different, only 2 get stored
    '''
    dimension = Dimension("test_dimension")
    dimension.addDimensionLine('test')
    dimension.addDimensionLine('test2')
    dimension.addDimensionLine('test')
    assert dimension.id_value == 2
    assert len(list(dimension.values)) == 2
