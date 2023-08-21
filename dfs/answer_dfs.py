# -*-coding:utf-8-*-
from common.common_interface import CommonInterface


class AnswerDfs(CommonInterface):
    def __init__(self):
        CommonInterface.__init__(self)

    def calculate_res(self):
        return "ahaha"


if __name__ == "__main__":
    answer = AnswerDfs()
    print answer.calculate_res()
