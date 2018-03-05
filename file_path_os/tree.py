#!/usr/bin/env python3
"""
This script prints a directory hierarchy (optionally including files)

Examples:
    tree.py test_hierarchy
        prints test_hierarchy excluding files

    tree.py test_hierarchy -f
        prints test_hierarchy including files
"""
import os
import sys


def gen_paths(spath: str, inc_files: bool=False) -> list:
    """
    Generate a list of all of the paths under a specified directory

    Args:
        spath: the path where to start the walk
        inc_files: true to include files / false only include directories

    Returns:
        Sorted list of all of the paths under the starting directory.
        This includes files if inc_files == True.

    Examples:
        >>> from pprint import pprint
        >>> pprint(gen_paths('test_hierarchy', True)) #*nix
        ['test_hierarchy',
         'test_hierarchy/f1.txt',
         'test_hierarchy/f2.txt',
         'test_hierarchy/sd1',
         'test_hierarchy/sd1/sd1_f1.txt',
         'test_hierarchy/sd1/sd1_f2.txt',
         'test_hierarchy/sd1/sd1_sd1',
         'test_hierarchy/sd1/sd1_sd1/sd1_sd1_f1.txt',
         'test_hierarchy/sd1/sd1_sd1/sd1_sd1_f2.txt',
         'test_hierarchy/sd1/sd1_sd2',
         'test_hierarchy/sd1/sd1_sd2/sd1_sd2_f1.txt',
         'test_hierarchy/sd1/sd1_sd3',
         'test_hierarchy/sd1/sd1_sd3/sd1_sd3_f1.txt',
         'test_hierarchy/sd2',
         'test_hierarchy/sd2/sd2_f1.txt',
         'test_hierarchy/sd2/sd2_sd1',
         'test_hierarchy/sd2/sd2_sd1/sd2_sd1_f1.txt',
         'test_hierarchy/sd3',
         'test_hierarchy/sd3/sd3_f1.txt']

        >>> pprint(gen_paths('test_hierarchy', True)) #Windows
        ['test_hierarchy',
         'test_hierarchy\\\\f1.txt',
         'test_hierarchy\\\\f2.txt',
         'test_hierarchy\\\\sd1',
         'test_hierarchy\\\\sd1\\\\sd1_f1.txt',
         'test_hierarchy\\\\sd1\\\\sd1_f2.txt',
         'test_hierarchy\\\\sd1\\\\sd1_sd1',
         'test_hierarchy\\\\sd1\\\\sd1_sd1\\\\sd1_sd1_f1.txt',
         'test_hierarchy\\\\sd1\\\\sd1_sd1\\\\sd1_sd1_f2.txt',
         'test_hierarchy\\\\sd1\\\\sd1_sd2',
         'test_hierarchy\\\\sd1\\\\sd1_sd2\\\\sd1_sd2_f1.txt',
         'test_hierarchy\\\\sd1\\\\sd1_sd3',
         'test_hierarchy\\\\sd1\\\\sd1_sd3\\\\sd1_sd3_f1.txt',
         'test_hierarchy\\\\sd2',
         'test_hierarchy\\\\sd2\\\\sd2_f1.txt',
         'test_hierarchy\\\\sd2\\\\sd2_sd1',
         'test_hierarchy\\\\sd2\\\\sd2_sd1\\\\sd2_sd1_f1.txt',
         'test_hierarchy\\\\sd3',
         'test_hierarchy\\\\sd3\\\\sd3_f1.txt']

        >>> pprint(gen_paths('test_hierarchy', False)) #*nix
        ['test_hierarchy',
         'test_hierarchy/sd1',
         'test_hierarchy/sd1/sd1_sd1',
         'test_hierarchy/sd1/sd1_sd2',
         'test_hierarchy/sd1/sd1_sd3',
         'test_hierarchy/sd2',
         'test_hierarchy/sd2/sd2_sd1',
         'test_hierarchy/sd3']

        >>> pprint(gen_paths('test_hierarchy', False)) # Windows
        ['test_hierarchy',
         'test_hierarchy\\\\sd1',
         'test_hierarchy\\\\sd1\\\\sd1_sd1',
         'test_hierarchy\\\\sd1\\\\sd1_sd2',
         'test_hierarchy\\\\sd1\\\\sd1_sd3',
         'test_hierarchy\\\\sd2',
         'test_hierarchy\\\\sd2\\\\sd2_sd1',
         'test_hierarchy\\\\sd3']


    """
    paths = set()
    for root, dir_names, files in os.walk(spath):
        paths.add(root)
        for directory in dir_names:
            paths.add(os.path.join(root, directory))
        if inc_files:
            for file in files:
                paths.add(os.path.join(root, file))
    return sorted(paths)


def print_paths(paths):
    """
    Prints a sorted listed of nested paths as an indented hierarchy
    Args:
        paths: a sorted list of paths to print

    Returns:
        None

    Examples:
        >>> path_list = ['test_hierarchy',
        ... 'test_hierarchy/sd1',
        ... 'test_hierarchy/sd1/sd1_sd1',
        ... 'test_hierarchy/sd1/sd1_sd2',
        ... 'test_hierarchy/sd1/sd1_sd3',
        ... 'test_hierarchy/sd2',
        ... 'test_hierarchy/sd2/sd2_sd1',
        ... 'test_hierarchy/sd3']
        >>> print_paths(path_list)
        test_hierarchy
            sd1
                sd1_sd1
                sd1_sd2
                sd1_sd3
            sd2
                sd2_sd1
            sd3

        >>> path_list = ['test_hierarchy',
        ... 'test_hierarchy/f1.txt',
        ... 'test_hierarchy/f2.txt',
        ... 'test_hierarchy/sd1',
        ... 'test_hierarchy/sd1/sd1_f1.txt',
        ... 'test_hierarchy/sd1/sd1_f2.txt',
        ... 'test_hierarchy/sd1/sd1_sd1',
        ... 'test_hierarchy/sd1/sd1_sd1/sd1_sd1_f1.txt',
        ... 'test_hierarchy/sd1/sd1_sd1/sd1_sd1_f2.txt',
        ... 'test_hierarchy/sd1/sd1_sd2',
        ... 'test_hierarchy/sd1/sd1_sd2/sd1_sd2_f1.txt',
        ... 'test_hierarchy/sd1/sd1_sd3',
        ... 'test_hierarchy/sd1/sd1_sd3/sd1_sd3_f1.txt',
        ... 'test_hierarchy/sd2',
        ... 'test_hierarchy/sd2/sd2_f1.txt',
        ... 'test_hierarchy/sd2/sd2_sd1',
        ... 'test_hierarchy/sd2/sd2_sd1/sd2_sd1_f1.txt',
        ... 'test_hierarchy/sd3',
        ... 'test_hierarchy/sd3/sd3_f1.txt']
        >>> print_paths(path_list)
        test_hierarchy
            f1.txt
            f2.txt
            sd1
                sd1_f1.txt
                sd1_f2.txt
                sd1_sd1
                    sd1_sd1_f1.txt
                    sd1_sd1_f2.txt
                sd1_sd2
                    sd1_sd2_f1.txt
                sd1_sd3
                    sd1_sd3_f1.txt
            sd2
                sd2_f1.txt
                sd2_sd1
                    sd2_sd1_f1.txt
            sd3
                sd3_f1.txt


    """
    for path in paths:
        rel_path = os.path.relpath(path, paths[0])
        path_parts = rel_path.split(os.sep)
        depth = len(path_parts)
        if path == paths[0]:
            print(path)
        else:
            if depth == 1:
                print('    {output}'.format(output=path_parts[depth - 1]))
            else:
                print('    {fill}{output}'.format(fill="".join("    " * (depth - 1)),
                                                  output=path_parts[depth - 1]))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print_paths(gen_paths(sys.argv[1], False))
    elif len(sys.argv) == 3 and sys.argv[2] == '-f':
        print_paths(gen_paths(sys.argv[1], True))
    else:
        print(__doc__)
