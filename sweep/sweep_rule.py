#coding=utf-8
#version = 0.1
#author = test_lins
#简单的扫雷游戏
#主要练习广度优先 和二维数组的处理
import random

class sweep_rule(object):
    
    def __init__(self,area,sweep_num):
        self.area = area #盘的大小
        self.sweep_num = sweep_num #雷的数量
    '''    
    def _init_arealist(self):
        area = self.area
        arealist = [[0 for col in xrange(area)]for row in xrange(area)]
        return arealist
    '''
    
    def _init_sweep(self):
        area =  self.area
        sweep_num = self.sweep_num
        area_point = []
        random_point = []
        arealist = [[0 for col in xrange(area)]for row in xrange(area)]#初始化列表
        for col in xrange(area):
            for row in xrange(area):
                area_point.append([col,row])#创建坐标列表
        while sweep_num>0:
            point = random.randint(0,(len(area_point)-1))
            if point in random_point:
                sweep_num +=1 #处理重复随机数
            else:
                random_point.append(point)
                arealist[area_point[point][0]][area_point[point][1]] = -1#初始化雷区
            sweep_num -= 1
            #print sweep_num
        #print random_point
        for point in random_point:
            #计算周围雷的个数
            for col in [area_point[point][0]-1,area_point[point][0],area_point[point][0]+1]:
                if col<0 or col> area-1:
                    pass
                else:
                    for row in [area_point[point][1]-1,area_point[point][1],area_point[point][1]+1]:
                        if row<0 or row> area-1:
                            pass
                        else:
                            if arealist[col][row] != -1:
                               arealist[col][row] += 1 
       # for x in arealist:
       #     print x
        return arealist       
                            
    def chick(self):
        
        
        #return arealist
    
    
            

if __name__ == '__main__':
    x = sweep_rule(10,10)
    x._init_sweep()
        
        
        