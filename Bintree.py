#root.search(x): ◯.data == x のものが存在するある場合それを出力、ない場合Noneを出力
#root.insert(x): ◯.data == xが存在する場合Falseを出力、ない場合◯.data == x なる頂点を作る
#y.to_s(): 頂点yのdataを出力
#y.left_s(): 頂点yのleftを出力(ない場合はNone)
####################################################
class Bintree:
    def __init__(self,data=None): # デフォルト値を使うのはrootのみ
        self.data = data
        self.left = None
        self.right = None
    def search(self,data):
        if self.data == None:
            return None
        if data < self.data:
            if self.left == None:
                return None # 左の子がなければない
            else:
                return self.left.search(data) # 左の子があれば左の子(の下を)再帰的に検索
        elif data > self.data:
            if self.right == None:
                return None
            else:
                return self.right.search(data)
        else: # data == self.dataなら発見
            return self
    
    def insert(self,data):
        if self.data == None:
            self.data = data
            return self
        if data < self.data:
            if self.left == None:
                self.left = Bintree(data) # 左の子がなければ、そこに頂点を作って登録
                return True
            else:
                return self.left.insert(data)
        elif data > self.data:
            if self.right == None:
                self.right = Bintree(data)
                return True
            else:
                return self.right.insert(data)
        else: # data == self.data:
            return False
    def to_s(self):
        return self.data
    def left_s(self):
        if self.left==None:
            return None
        return (self.left).data
    def right_s(self):
        if self.right == None:
            return None
        return (self.right).data
    

#########################################

#test
root = Bintree()

#5,3,6,4,2,7を加える

root.insert(5)
root.insert(3)
root.insert(6)
root.insert(4)
root.insert(2)
root.insert(7)

#1,3,4,0,6,7があるかの判定

for i in [1,3,4,0,6,7]:
    s = root.search(i)
    if s == None:
        print(None)
    else:
        print(s.to_s())

#5の左側は何か
s = root.search(5)
if s == None:
    print(None)
else:
    print(s.left_s())

#6の右側は何か
s = root.search(6)
if s == None:
    print(None)
else:
    print(s.right_s())

#7の右側は何か(ないね)
s = root.search(7)
if s == None:
    print(None)
else:
    print(s.right_s())