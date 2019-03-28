# coding: utf-8

import operator
import copy
# import gc

basename = "./"

number = 9
offset_dis = [[0, 1, 2, 1, 2, 3, 2, 3, 4],
              [1, 0, 1, 2, 1, 2, 3, 2, 3],
              [2, 1, 0, 3, 2, 1, 4, 3, 2],
              [1, 2, 3, 0, 1, 2, 1, 2, 3],
              [2, 1, 2, 1, 0, 1, 2, 1, 2],
              [3, 2, 1, 2, 1, 0, 3, 2, 1],
              [2, 3, 4, 1, 2, 3, 0, 1, 2],
              [3, 2, 3, 2, 1, 2, 1, 0, 1],
              [4, 3, 2, 3, 2, 1, 2, 1, 0]]


# checkerboard class is to describe the status of this time
class checkerboard:
    # initial status, final status,and the index of space in the checkerboard
    status, final_status, space = list(), list(), 0
    parent = -1
    # the distance of index when space moved ,consider the 3*3 checkerboard as a linear list  from [0-8]
    steps = [-1, -3, 1, 3]

    def __init__(self):
        pass

    def init(self, filename):
        with open(basename + filename, 'r') as f:
            raw_datas = f.read().splitlines()
            for i, line in enumerate(raw_datas):
                if i == 0:
                    self.status = [int(x) for x in line.split(" ")]
                elif i == 1:
                    self.space = int(line.split(" ")[0])
                else:
                    self.final_status = [int(x) for x in line.split(" ")]
        self.parent = -1

    def check_move_action(self, i):
        next = self.space + self.steps[i]
        if next < 0 or next > 8:  # out of range
            return False
        else:
            return True


open_list = []
close_list = []
hold_list = []


class A_star:

    def __init__(self):
        pass

    def init(self, filename):
        self.board = checkerboard()
        self.board.init(filename)
        self.cur_nums_pos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.goal_nums_pos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(number):
            self.cur_nums_pos[self.board.status[i]] = i
            self.goal_nums_pos[self.board.final_status[i]] = i
        self.f, self.g, self.h = 0, 0, 0

    def whether_expend_available(self, i):
        if (self.board.check_move_action(i)):  # means still in the checkerboard (move action is legal)
            # change the status memory in the data structure,the status list and the digital position list
            next = self.board.space + self.board.steps[i]
            self.board.status[self.board.space] = self.board.status[next]
            self.board.status[next] = 0
            self.board.space += self.board.steps[i]
            return True
        else:
            return False

    def calculate_f(self):
        self.h =0
        # calculate the offset loss of status change
        for i in range(number):
            self.h += offset_dis[self.cur_nums_pos[i]][self.goal_nums_pos[i]]
        # the true loss of the move
        self.g += 1
        return self.g + self.h


def repeat_id(cur_status):
    for i in range(len(hold_list)):
        if operator.eq(cur_status.board.status, hold_list[i].board.status):
            return i
    return len(hold_list)


def search(start_status):
    head, tail = 0, 0
    hold_list.append(start_status) # insert to the hold list
    flag = False
    # from head to tail holds a non-decrease list of open_list,the close_list is from 0 to head-1
    while head <= tail:
        for i in range(4):
            cur = copy.deepcopy(hold_list[head])  # get the head value of hold_list
            if cur.h == 0:
                flag = True
                # the route is gotten!!!
                res = []

                while cur.board.parent != -1: # the end is the root node
                    res.append(cur.board.status)
                    cur = hold_list[cur.board.parent]
                # add the goal node status to the route
                res.append(cur.board.status)
                res.reverse()


                route ={}
                for i,node_status in enumerate(res):
                    print(str(i) + "th :")
                    print(node_status)
                    route[i] = node_status
                print(route)
                import json
                import os
                if os.path.exists(basename+"route_result.json"):
                    os.remove(basename+"route_result.json")
                with open(basename+"route_result.json","w") as json_f:
                    json.dump(route,json_f)
                    print("store the optimal route (dic) to the json file!")

                # print("finish !!!")
                return
            if cur.whether_expend_available(i):
                s_temp = cur.cur_nums_pos[cur.board.status[cur.cur_nums_pos[0]]]
                cur.cur_nums_pos[cur.board.status[cur.cur_nums_pos[0]]] = cur.cur_nums_pos[0]
                cur.cur_nums_pos[0] = s_temp
                #print(cur.cur_nums_pos)

                insert_index = repeat_id(cur)
                if insert_index < head:  # the status is in the close list
                    continue

                cur.board.parent = head  # record the parent of this node
                cur.f = cur.calculate_f()  # calculate it's f,g,h value at the same time

                if insert_index <= tail:  # the node is repeat with a existed node in the open_list
                    # keep the min g in the node
                    temp = hold_list[insert_index]
                    if cur.g < temp.g:
                        # hold_list[insert_index] = cur
                        hold_list[insert_index].f,hold_list[insert_index].g,hold_list[insert_index].h = cur.f,cur.g,cur.h
                        hold_list[insert_index].board.parent = cur.board.parent
                else: # add a new node in its position
                    j = head + 1
                    while j < len(hold_list):
                        if hold_list[j].f >= cur.f:
                            break
                        j += 1
                    # print("%d - %d - %d" %(cur.f,cur.g,cur.h))
                    hold_list.insert(j, cur)  # join the cur node to the hold list
                    tail += 1
        head += 1
    if not flag:
        print("the original status can't achieve the final status!")


def main():
    filename = "eight.txt"
    a = A_star()
    a.init(filename)
    a.f = a.calculate_f()
    search(a)


if __name__ == '__main__':
    main()
