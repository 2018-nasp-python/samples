
def func_w_args(arg1, arg2, arg3):
    print('arg1: {:20} arg2: {:20} arg3: {:20}'.format(arg1, arg2, arg3))

def func_w_kwargs(arg1="default", arg2="default"):
    print('arg1: {:20} arg2: {:20}'.format(arg1, arg2))

if __name__ == '__main__':
    list_of_names = ["Tom", "Fred", "Paul"]
    func_w_args(*list_of_names)
    dict_of_names = {'arg1' : "Tom", 'arg2' : "Fred"}
    func_w_kwargs(**dict_of_names)
