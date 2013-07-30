#coding=utf-8
#version = 0.1
#author = test_lins
#简单的扫雷游戏，不做界面
#主要练习广度优先 和二维数组的处理
import random

class minesweep_rule(object):
    
    def __init__(self,area,mine_num):
        self.area = area #盘的大小
        self.mine_num = mine_num #雷的数量
        self.statuslist = [['' for col in xrange(area)]for row in xrange(area)]
        self.arealist = [[0 for col in xrange(area)]for row in xrange(area)]
        self.donepoint = []
    def _init_list(self):
        area = self.area
        arealist = [[0 for col in xrange(area)]for row in xrange(area)] #布雷表
        statuslist = [['' for col in xrange(area)]for row in xrange(area)] #状态表
        area_point = []
        for col in xrange(area):
            for row in xrange(area):
                area_point.append([col,row]) #坐标表      
        return arealist,statuslist,area_point

    
    def _init_mine(self):
        area = self.area
        mine_num = self.mine_num
        random_point = []
        #arealist = (minesweep_rule._init_list(self))[0]
        arealist = self.arealist
        area_point = (minesweep_rule._init_list(self))[2]

        while mine_num>0:
            point = random.randint(0,(len(area_point)-1))
            if point in random_point:
                mine_num +=1 #处理重复随机数
            else:
                random_point.append(point)
                arealist[area_point[point][0]][area_point[point][1]] = -1#初始化雷区
            mine_num -= 1

        for point in random_point:
            #计算周围雷的个数
            point_value = area_point[point]
            for item in self.Sudoku_rule(point_value):
                if  arealist[item[0]][item[1]]!= -1:
                    arealist[item[0]][item[1]] += 1 #计算周围地雷个数

        print "################################"
        for x in arealist:#命令行显示雷区
            print x
        print "################################"
        #print arealist
        return arealist

    def Sudoku_rule(self,point_value):
        Sudokulist = []  #计算九宫格
        area = self.area
        for col in [point_value[0]-1,point_value[0],point_value[0]+1]:
            if col<0 or col> area-1:
                pass
            else:
                for row in [point_value[1]-1,point_value[1],point_value[1]+1]:
                    if row<0 or row> area-1:
                        pass
                    else:
                        Sudokulist.append([col,row])
        return Sudokulist

    def chick(self,point,arealist):
        donepoint = self.donepoint
        todopoint = []
        #arealist = self._init_mine()
        #arealist = [[0, 0, 1, -1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, -1, 1, 0], [0, 0, 0, 0, 1, 2, 2, 1, 0], [1, 1, 0, 0, 1, -1, 2, 1, 1], [-1, 2, 1, 1, 3, 3, 3, -1, 1], [3, -1, 1, 1, -1, -1, 2, 1, 1], [-1, 2, 1, 1, 2, 2, 2, 1, 1], [1, 1, 0, 0, 0, 0, 1, -1, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1]]
        statuslist = self.statuslist
        area_point = (minesweep_rule._init_list(self))[2]
        todopoint.append(point)
        while  len(todopoint)>0:
            point_value = todopoint.pop(0)
            #广度优先计算打开区域
            if arealist[point_value[0]][point_value[1]]==0:
                #donepoint.append(point_value)
                for item in self.Sudoku_rule(point_value):#计算九宫格
                    if item in donepoint:#跳过重复坐标
                        pass
                    else:
                        if arealist[item[0]][item[1]] != 0:
                            statuslist[item[0]][item[1]] = arealist[item[0]][item[1]]
                            donepoint.append(item)
                        elif arealist[item[0]][item[1]] == 0:
                            statuslist[item[0]][item[1]] = arealist[item[0]][item[1]]
                            donepoint.append(item)
                            todopoint.append(item)
            elif arealist[point_value[0]][point_value[1]]== -1:
                statuslist[point_value[0]][point_value[1]] = 'X'
                return False
            else:
                statuslist[point_value[0]][point_value[1]] = arealist[point_value[0]][point_value[1]]
                if point_value not in donepoint:
                    donepoint.append(point_value)
                #donepoint.append(point_value)
        print "*********************************"
        for x in statuslist:#命令行显示雷区
            print x
        print "*********************************"
        #print len(donepoint)
        #print donepoint








if __name__ == '__main__':
    x = minesweep_rule(9,10)
    #print x._init_list()[1]
    a = x._init_mine()
    #print x.Sudoku_rule([1,2])
    x.chick([1,1],a)
    x.chick([0,2],a)
    x.chick([0,4],a)
    x.chick([0,5],a)
    x.chick([8,0],a)
        
    