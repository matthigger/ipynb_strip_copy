if __name__ == '__main__':
    from ipynb_strip_copy.file_ipynb import json_from_ipynb, json_to_ipynb, \
        search_apply_json
    import argparse

    # parse arguments
    description = \
        """ modifies jupyter cells per commands. see 
        https://github.com/matthigger/ipynb_strip_copy for details """
    parser = argparse.ArgumentParser(description)
    parser.add_argument('file', type=str, nargs=1, help='input ipynb')
    parser.add_argument('--suffix-sep', dest='sep', type=str, default='_',
                        help='character which separates suffix from stem')
    args = parser.parse_args()

    # apply commans
    json_in = json_from_ipynb(args.file[0])
    suffix_json_dict = search_apply_json(json_in)

    # build file out template
    file_out = args.file[0].split('.')
    file_out[-2] = args.sep.join(file_out[-2].split(args.sep)[:-1])
    file_out = '.'.join(file_out)

    # output ipynb
    for suffix, json_dict in suffix_json_dict.items():
        _file_out = file_out.replace('.ipynb', args.sep + suffix + '.ipynb')
        json_to_ipynb(json_dict, _file_out)
