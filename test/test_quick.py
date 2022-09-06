from ipynb_strip_copy import *

def test_quick():
    file_in = 'test_case.ipynb'
    file_out0 = 'test_case0.ipynb'
    file_out1 = 'test_case1.ipynb'

    json_in = json_from_ipynb(file_in)
    json_out0 = json_from_ipynb(file_out0)
    json_out1 = json_from_ipynb(file_out1)

    suffix_json_dict = search_apply_json(json_in)

    assert suffix_json_dict['0'] == json_out0
    assert suffix_json_dict['1'] == json_out1