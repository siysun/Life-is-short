# -*- coding:utf-8 -*-
import random
import os


class LifeChoiceMaker():
    def __init__(self):
        pass

    def input_plan(self, available_hours, plan_names_list=[], end_flag=False):
        input_plan_names_str = str(raw_input('请输入活动名称:'))
        if str(input_plan_names_str).strip() == "":
            print "输入为空!"
        else:
            this_plan_names_list = input_plan_names_str.split(',')
            for plan_name in this_plan_names_list:
                plan_names_list.append(plan_name)
            print '现在的活动列表:%s' % plan_names_list
        if available_hours > len(this_plan_names_list):
            left_hours = int(available_hours) - len(this_plan_names_list)
            print '最少还需要输入%s项活动' % left_hours
            plan_names_list, end_flag = self.input_plan(left_hours, plan_names_list)
        else:
            end_input = str(raw_input('是否结束活动名称输入？'))
            if end_input.lower() == 'yes' or end_input.lower() == 'y':
                end_flag = True
            else:
                plan_names_list, end_flag = self.input_plan(0, plan_names_list)
        return plan_names_list, end_flag

    def random_pick_plans(self, availalbe_hours, plan_names_list):
        print '决定是你了!'
        picked_plan_names_list = []
        for elect_turn in range(0, availalbe_hours):
            elected_plan_num = random.randint(1, len(plan_names_list))
            print plan_names_list[elected_plan_num - 1]
            picked_plan_names_list.append(plan_names_list[elected_plan_num - 1])
            plan_names_list.pop(elected_plan_num - 1)
        return picked_plan_names_list

    def load_plans_from_text(self):
        plan_save_path = os.path.abspath("./myplans.txt")
        try:
            with open(plan_save_path, 'r') as myplans_file:
                input_plan_names_str = myplans_file.read()
        except IOError:
            input_plan_names_str = ""
        return input_plan_names_str

    def __save_plans_to_text(self):
        plan_save_path = os.path.abspath("./myplans.txt")
        with open(plan_save_path, 'a') as myplans_file:
            myplans_file.write()

    def __get_distinct_plan_names_list(self, plan_names_list):
        pass


if __name__ == '__main__':
    availalbe_hours = int(raw_input('请输入可用小时数:'))
    my_choice_maker_instance = LifeChoiceMaker()
    # saved_plan_names_str = my_choice_maker_instance.load_plans_from_text()
    plan_names_list, end_flag = my_choice_maker_instance.input_plan(availalbe_hours)
    distinct_plan_names_list = list(set(plan_names_list))
    my_choice_maker_instance.random_pick_plans(availalbe_hours, distinct_plan_names_list)
