from ipynb_strip_copy import *

def test_search_act():
    file_test = 'test_case_in.ipynb'
    file_expect = 'test_case_out.ipynb'

    target_act_list = [('CLEARME', ACTION_CLEAR_CELL),
                       ('DELETEME', ACTION_RM_CELL)]

    json_dict_in = json_from_ipynb(file_test)
    json_dict_exp = json_from_ipynb(file_expect)

    json_dict_obs = search_act(json_dict_in, target_act_list)

    assert json_dict_in == json_dict_obs
