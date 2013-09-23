#coding=utf-8
class rena(object):
    """
    人狼羊菜 过河问题 这里用错算法，此代码中用宽度遍历 和一些控制语句完成判断；
    造成程序过于复杂 臃肿 逻辑不清楚，且不能判断所有过河情况；后面用回朔算法重写
    """
    def __init__(self):
        super(rena, self).__init__()
        self.start = {'ren':1,'lang':1,'yang':1,'cai':1}
        self.end = {'ren':0,'lang':0,'yang':0,'cai':0}
        self.cross = ['ren']#初始化 便于crossback 方法调用
        self.crossback = ['ren']#初始化 便于cross 方法调用
        

    def liverule(self,adict):
        if adict['ren']==0:
            if adict['lang']==adict['yang']==1 or adict['yang']==adict['cai']==1  or adict['lang']==adict['yang']==adict['cai']==1:
                return False
            else:
                return True
        else:
            return True

    def cross1(self):
        '''到b岸'''
        start = self.start
        end = self.end
        self.cross = ['ren']#重新赋值
        crossback = self.crossback
        cross = self.cross
        startkey = []
        [startkey.append(item) for item in start if start[item]==1 and item!='ren']

        while  True:#应该用startkey长度判断……
            crosskey = startkey.pop()
            cross.append(crosskey)
            for item in cross:
                start[item] -= 1

            if self.liverule(start):
                if len(crossback)>1 and crossback[-1] not in cross:#多人回a岸的情况
                    
                    for item in cross:
                        end[item] += 1
                    break
                elif len(crossback)<=1:#单人回a岸的情况
                    for item in cross:
                        end[item] += 1
                    break
                    
                else:
                    for item in cross:
                        start[item] += 1
                    cross = ['ren']
                    
                    
            else:
                for item in cross:
                    start[item] += 1
                cross = ['ren']


    def crossback1(self):
        '''回a岸'''
        start = self.start
        end = self.end
        cross = self.cross
        self.crossback  = ['ren']      
        crossback = self.crossback
        endkey = []
        [endkey.append(item) for item in end if end[item]==1 and item!='ren']
        if len(endkey)==1  :#除人外 只剩一个
            for item in crossback:
                end[item] -=1
                start[item] +=1
            return crossback
        else:
            end[crossback[0]] -= 1
            if self.liverule(end):#除人外剩余的可以共处
                for item in crossback:
                    start[item] +=1
                return crossback
            else:
                end[crossback[0]] += 1
                while  True:            
                    crossbackkey = endkey.pop()
                    crossback.append(crossbackkey)
                    for item in crossback:
                        end[item] -= 1
                
                    if self.liverule(end) and cross[-1] not in crossback:#避免死循环
                        for item in crossback:
                            start[item] +=1
                        
                        return crossback
                    else:
                        for item in crossback:
                            end[item] += 1
                        crossback = ['ren']
            
    def output(self):
        result =  {'ren':1,'lang':1,'yang':1,'cai':1}

        while True:
            self.cross1() 
            print 'start is %s'%self.start
            if self.end == result:
                print 'good'
                return True
            else:
                self.crossback1()
                print 'end is   %s'%self.end

yang = rena()
yang.output()

        
