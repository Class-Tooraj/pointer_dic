#!user/bin/env python3

__author__ = "tooraj_jahangiri"
__email__ = "toorajjahangiri@gmail.com"


class PointerDic:
    ASCII: dict = lambda x: {n: chr(n) for n in range(0, 128)}
    
    def __init__(self, intro: list[any] or dict[int: any] = None, focus: int = 0) -> None:
        """
        Create Dic use PointerDic Protocol
        :param intro: if dict must be start from '0' example: {0: 'A', 1: 'B', ...} or ['A', 'B']
        :type intro: -list-, -dict-
        :default intro: ASCII -> idx 0, idx 127
        :param focus: choice index for focusing value
        :default focus: 0
        :type focus: -int-
        """

        if isinstance(intro, list):
            idx = self.indexer(intro)
            intro = idx
            del idx

        self.intro = self.ASCII() if intro is None else intro  # 'ASCII' table
        self.focus = focus
        self.skeleton = self.new_skeleton(len(self.intro), self.focus)
        self.map = {
            'A': {self.intro[key]: self.intro[value] for key, value in self.skeleton.items()},  # Alpha map
            'B': {self.intro[value]: self.intro[key] for key, value in self.skeleton.items()},  # Beta map
            'G': {self.intro[value]: key for key, value in self.skeleton.items()}  # Skeleton Graph
        }

    def update_map(self, focus: int = 0) -> None:
        """
        Update Map to New Point
        :param focus: choice index for focusing value
        :default focus: 0
        :type focus: -int-
        """

        self.focus = focus
        self.skeleton = self.new_skeleton(len(self.intro), self.focus)
        self.map = {
            'A': {self.intro[key]: self.intro[value] for key, value in self.skeleton.items()},  # Alpha map
            'B': {self.intro[value]: self.intro[key] for key, value in self.skeleton.items()},  # Beta map
            'G': {self.intro[value]: key for key, value in self.skeleton.items()}  # Skeleton Graph
        }

    def change_intro(self, intro: list[any] or dict[int: any] = None, focus: int = 0) -> bool:
        """
        Change intro value
        :param intro: if dict must be start from '0' example: {0: 'A', 1: 'B', ...}
        :type intro: -list-, -dict-
        :default intro: ASCII -> idx 0, idx 127
        :param focus: choice index for focusing value
        :default focus: 0
        :type focus: -int-
        :return : 'True' if is Not Problem
        :rtype : -bool-
        """

        try:
            self.intro = self.ASCII() if intro is None else intro
            self.focus = focus
            self.update_map(focus)
            return True
        except BaseException:
            raise

    def __rshift__(self, other: int = 1) -> None:
        """
        Shift to right '>>'
        :param other: shift value [ 'value > 0' ]
        :default other: 1
        :type other: -int-
        """

        if other < 1:
            raise ValueError["Value Must > 0"]

        x = (self.focus + other)
        while True:
            if x <= len(self.skeleton):
                self.update_map(x)
                break
            else:
                b = (self.focus - other)
                x = abs(b)

    def __lshift__(self, other: int = 1) -> None:
        """
        Shift to left '<<'
        :param other: shift value [ 'value > 0' ]
        :default other: 1
        :type other: -int-
        """

        if other < 1:
            raise ValueError["Value Must > 0"]

        x = (self.focus - other)
        while True:
            if x >= 0:
                self.update_map(x)
                break
            else:
                b = (len(self.skeleton) - other)
                x = abs(b)

    def __reversed__(self, focus: int = None) -> None:
        """
        Reverse intro
        :param focus: choice index for focusing value
        :default focus: None -> if None use global focus
        :type focus: -int-
        """

        re_key: list[int] = reversed(self.skeleton.keys())
        new: dict[int: int] = {next(re_key): self.skeleton[k] for k in range(0, len(self.skeleton))}
        try:
            self.skeleton = new
            self.update_map(self.focus if focus is None else focus)
        except Exception:
            raise
        del new, re_key

    def __add__(self, other: list[any]) -> None:
        """
        Add value to intro '+'
        :param other: value to add intro
        :type other: -list-
        """

        get_max = max(self.intro.keys())
        new_map = {}
        counter = 1
        for i in range(0, len(other)):
            new_map[(get_max + counter)] = other[i]
            counter += 1
        self.intro.update(new_map)
        self.update_map(self.focus)
        del get_max, new_map, counter, other, i

    def __sub__(self, other: list[any]) -> None:
        """
        Remove value from intro '-'
        :param other: value remove from intro
        :type other: -list-
        """
        re_value = list(self.intro.values())
        for i in other:
            re_value.remove(i)
        re_idx = self.indexer(re_value)
        self.change_intro(re_idx, self.focus)
        del re_value, re_idx, other, i

    def reset(self) -> bool:
        """
        Reset class
        :return: 'True' if reset is done else raise
        :rtype: -bool-
        """

        try:
            self.skeleton = self.new_skeleton(len(self.intro))
            self.update_map()
            return True
        except BaseException:
            raise

    @staticmethod
    def new_skeleton(length: len, point: int = 0) -> dict[int: int]:
        """
        [staticmethod] -> make new skeleton 
        :param length: length skeleton you need
        :type length: -int- | (len)
        :param point: choice index for focusing value point
        :type point: -int-
        :default point: 0
        :return: new skeleton created
        :rtype: -dict-
        """
        new_dic: dict[int: int] = {}
        record = 0
        _mines = length - point

        for num in range(point, length):
            new_dic[num - point] = num

        for num in range(_mines, length):
            new_dic[num] = record
            record += 1

        return new_dic

    @staticmethod
    def indexer(value: list[any]) -> dict[int: any]:
        """
        [staticmethod] -> list value to map value
        :param value: list from any value
        :type value: -any-
        :return: key, value -> idx: value
        :rtype: -dict-
        """
        idx = {i: value[i] for i in range(0, len(value))}
        return idx
