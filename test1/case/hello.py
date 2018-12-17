import sys
def test():
    argv=sys.argv
    if len(argv)==1:
        print("one argv!")
    elif len(argv)==2:
        print("two argvs!")
    else:
        print("too many argvs!")
if __name__ == '__main__':
    test()