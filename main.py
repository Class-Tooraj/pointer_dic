#!user/bin/env python3

__author__ = "tooraj_jahangiri"
__email__ = "toorajjahangiri@gmail.com"

from base64 import b64encode, b64decode
from pointerdic import PointerDic
from time import perf_counter
from random import choice


def main() -> int:
    """
    PointerDic Main prg: [check(class): ./pointerdic.py]
    I did not use argparse or sys.argv
    ALL INPUT CMD SUPPORT:
        /I: change intro [list]
        /F: update focus [int]
        /R: reversed map [int]
        >>: focus up [int] , default= 1
        <<: focus down [int] , default= 1
        +: add items to map [list]
        -: sub items from map [list]
        /reset: reset to default
        ----
        en: encrypt data
        de: decrypt data

    pattern:/support command/
        /All command support/-> [cmd][value]
        /Only 'en' & 'de'/-> [cmd]

    example:/use command/
       All available -> '/F 3' |mean update focus to 3
       en & de -> 'en' |mean set to encrypt mode for one[1] period encrypt
    """

    # set PointerDic class

    print("/...STARTING.../\t[W&8]")

    remap = [chr(i) for i in range(33, 127)]    # make list value   ASCII 33-127
    print("@/>:[MAKE INTRO]", end="\n")

    foc = choice([num for num in range(0, len(remap))])     # chose focus
    print(f"@/>:[CHOSE FOCUS]=[{foc}]", end="\n")

    cls_active = PointerDic(remap, focus=foc)   # init class
    print("@/>:[POINTER DIC]", end="\n")

    trc_e = str.maketrans(cls_active.map['A'])  # make encrypt translator  'Alpha'
    trc_d = str.maketrans(cls_active.map['B'])  # make decrypt translator  'Beta'
    print("@/>:[STRING TRANSLATOR]", end="\n")
    # remove used value
    del remap, foc

    print("*Hint: if u need Help type ['help'] or ['/?'].\tQuit is ['exit'] or ['/*'].", end="\n")

    order = {
        "/I": ('cls_active.change_intro', list, 'change intro char list. type[list]'),  # intro
        "/F": ('cls_active.update_map', int, 'change focus. type[int]'),  # focus
        "/R": ('cls_active.__reversed__', int, 'reversed skeleton. optional focus type[int]'),  # reverse
        ">>": ('cls_active.__rshift__', int, 'rshift focus default(focus + 1). type[int]'),  # rshift
        "<<": ('cls_active.__lshift__', int, 'lshift focus default(focus - 1). type[int]'),  # lshift
        "+": ('cls_active.__add__', list, 'add new val in intro. type[list]'),  # add
        "-": ('cls_active.__sub__', list, 'sub val from intro. type[list]'),  # sub
        "/reset": ('cls_active.reset', lambda x: None, 'reset class.'),  # reset
    }
    cmd = {
        # encrypt   use base64 > translate pointerdic > encrypted value
        "en": (lambda x: x.encode('utf-8'), b64encode, lambda x: x.decode('ASCII').translate(trc_e), 'encrypt data.'),
        # decrypt   translate pointerdic > base64 > source
        "de": (lambda x: x.translate(trc_d), b64decode, lambda x: x.decode('utf-8'), 'decrypt data'),
    }

    d_inp: [int, str] = lambda x: 1 if x == " " or x == [] else x   # input check if need: set
    while True:
        icm, *inp = str(input("/... >: ")).split(" ")   # get command and value
        inp = inp[0] if len(inp) == 1 else inp  # if 1 value get value else all value

        t0 = perf_counter     # add time 0
        if icm in ("exit", "/*"):
            break

        elif icm in ("help", "/?"):
            t0 = t0()
            new = {}
            new.update(order)
            new.update(cmd)
            print("Command\t\tAction")
            for k, v in new.items():
                print(f"[key]=[{k}]\t[Hint]=[{v[-1]}]", end='\n')
                print("Help: ['help'] or ['/?'].\nExit: ['exit'] or ['/*']")
            del new, k, v

        elif icm in order:
            t0 = t0()  # add time 0
            print(f"order [ {icm} ]\t{inp}")
            get_order = f"{order[icm][0]}({order[icm][1](d_inp(inp))})"
            exec(get_order)
            print(f"result:\n[{order[icm][2]}]\t->G_Hash:[{hash(''.join(cls_active.map['G'].keys()))}]<-")
            del get_order, inp

        elif icm in cmd:
            t0 = t0()  # add time 0
            print(f"command [ {icm} ]")
            check = (1, [], " ", "")
            val = str(input('??>: ')) if inp in check else ''.join(inp)
            get_cmd = cmd[icm][0](val)
            mk_cm = cmd[icm][1](get_cmd)
            result = cmd[icm][2](mk_cm)
            print(f"result:\n\n->[{result}]<-", end='\n\n')
            del val, inp, get_cmd, mk_cm, result

        else:
            print(ValueError(f"command [ {icm} ] is not exist !"))

        total_time = perf_counter() - t0
        print(f"!!PROSES TIME: [{total_time:.5f}]\n-->> Pointer_Focus: / {cls_active.focus} /")
    return 0


if __name__ == '__main__':
    exit(main())
