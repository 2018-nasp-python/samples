#! /usr/bin/env python3

def func_w_keywords(p1='default_p1', p2='default_p2'):
    print('P1: {}  P2: {}'.format(p1, p2))


def main():
    func_w_keywords()
    func_w_keywords(1, 2)
    func_w_keywords(1)
    func_w_keywords(p2="p2 argument")
    func_w_keywords(p2="p2 argument", p1="p1 argument")


if __name__ == '__main__':
    main()