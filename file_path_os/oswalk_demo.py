"""
Simple script that demonstrates the os.walk function

See the following links for more background:
    1. https://docs.python.org/3/library/os.html#os.walk
    1. https://docs.python.org/3/library/sys.html#sys.argv

Args:
    sys.argv[1] - this should be the starting path to "walk"
"""
import sys
import os


def follow_oswalk(spath):
    """
    Function invokes os.walk printing the output of all each iteration


    Args:
        spath: the starting path to "walk"

    Returns:
        None

    Examples:
        >>> follow_oswalk('test_hierarchy')
        Root: test_hierarchy
        Dirs: ['sd1', 'sd2', 'sd3']
        Files: ['f1.txt', 'f2.txt']
        <BLANKLINE>
        Root: test_hierarchy/sd1
        Dirs: ['sd1_sd1', 'sd1_sd2', 'sd1_sd3']
        Files: ['sd1_f1.txt', 'sd1_f2.txt']
        <BLANKLINE>
        Root: test_hierarchy/sd1/sd1_sd1
        Dirs: []
        Files: ['sd1_sd1_f1.txt', 'sd1_sd1_f2.txt']
        <BLANKLINE>
        Root: test_hierarchy/sd1/sd1_sd2
        Dirs: []
        Files: ['sd1_sd2_f1.txt']
        <BLANKLINE>
        Root: test_hierarchy/sd1/sd1_sd3
        Dirs: []
        Files: ['sd1_sd3_f1.txt']
        <BLANKLINE>
        Root: test_hierarchy/sd2
        Dirs: ['sd2_sd1']
        Files: ['sd2_f1.txt']
        <BLANKLINE>
        Root: test_hierarchy/sd2/sd2_sd1
        Dirs: []
        Files: ['sd2_sd1_f1.txt']
        <BLANKLINE>
        Root: test_hierarchy/sd3
        Dirs: []
        Files: ['sd3_f1.txt']
        <BLANKLINE>
    """
    for dir_path, sub_dirs, files in os.walk(spath):
        # dir_path -> is the current directory in the walk
        # sub_dirs -> are all the sub directories in that directory
        # files -> are all the files in the current directory
        # os.walk starts at the starting path and uses that as the dir_path
        # on subsequent iterations it uses the first sub directory as the
        # current directory (by default - i.e. top down)

        if '.git' in sub_dirs:
            sub_dirs.remove('.git')

        print("Root: {}".format(dir_path))
        print("Dirs: {}".format(sub_dirs))
        print("Files: {}\n".format(files))


if __name__ == '__main__':
    follow_oswalk(sys.argv[1])
