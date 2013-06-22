#coding=utf-8
#version = v0.1
#售货机程序，测试分析示例经常遇到自己写个
#实现业务逻辑判断
import vemdb

class vemrule(object):
    """
    售货机运算规则
    BuyRule 计算投币额是否大于单价，是否为接受的币种，计算找零
    Change 计算找零：每种币种需要找回多少
    EnoughSales 判断库存是否足够（现在不能输入数量 后面优化）
    AllCalc 对计算的数据进行处理
    """
    InitChange = 0

    def __init__(self, inmoney,Objid):
        self.vemdb_rule = vemdb.vemdb()
        self.inmoney = inmoney
        self.Objid = Objid
        self.Objpri = self.vemdb_rule.select_price(Objid)
        #单价
        self.Objsum = self.vemdb_rule.select_subinventory(Objid)
        #库存
        self.summoney = self.vemdb_rule.select_submoney()
        #面额总额



    def BuyRule(self):
        Objpri = self.Objpri
        inmoney = self.inmoney
        Objid = self.Objid
        summoney = self.summoney
        """if inmoney>=Objpri and inmoney in summoney.keys():
            rule.InitChange=inmoney-Objpri
            return True
        else:
            print "have no enough money or money error"
            return False"""
        if inmoney>=Objpri: 
            if inmoney in summoney.keys():
                vemrule.InitChange=inmoney-Objpri
                return True
            else:
                print "Currency amount can not identify"
                return False
        else:
            print "have no enough money"
            return False

    
    def Change(self):
        """获取找零 从第二大币额开始；依次扫描，优先找零大币额"""
        summoney = self.summoney
        InitChange = vemrule.InitChange
        numkeymoney = {}
        keymoneys = sorted(summoney.keys(),reverse = True)

        for keymoney in keymoneys[1:]:
            calc = divmod(InitChange,keymoney)
            if calc[0]>summoney[keymoney] and keymoney==keymoneys[-1]:
                #如果有主键与最后一个主键相同，则有bug；后续数据库设计时唯一主键设为key值
                print "Not change"
                return False            
            elif calc[0]<=summoney[keymoney] and calc[0]!=0:
                #所需币种大于0 且余额充足
                #numkeymoney.append(keymoney,divmod(InitChange,keymoney)[0])
                numkeymoney[keymoney]=calc[0]
                InitChange = InitChange-numkeymoney[keymoney]*keymoney
                summoney[keymoney] -= numkeymoney[keymoney]
            else:
                pass
        return True
        #for nummoney in numkeymoney.keys():
        #    summoney[nummoney] = summoney[nummoney]-numkeymoney[nummoney]
        #print summoney         
        #print numkeymoney[1][0]

    def EnoughSales(self):
        Objsum = self.Objsum
        Objid = self.Objid
        if Objsum>0:
            return True
        else:
            print "Inventory is not enough"
            return False    



    def AllCalc(self):
        vemdb_rule = self.vemdb_rule
        summoney = self.summoney
        inmoney = self.inmoney
        Objsum = self.Objsum
        Objid = self.Objid
        if x.BuyRule()and x.Change() and x.EnoughSales():
            summoney[inmoney] += 1
            Objsum -= 1
            for key in summoney.keys():
                vemdb_rule.update_submoney(key,summoney[key])
            vemdb_rule.update_subinventory(Objid,Objsum)
            vemdb_rule.conn_vemdb.commit()
            vemdb_rule.cursor_vemdb.close()
            vemdb_rule.conn_vemdb.close()
                #print key
            print 'pass'
        else:
            pass

        

        



if __name__ == '__main__':
    x = vemrule(5,1)
    #x.AllCalc()
    x.BuyRule()
    x.Change()
