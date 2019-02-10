
values = {'Two':2, 'Three':3, 'Four':4}

class Add:
    def __init__(self):
        self.hand=(['Two of ace','Three of sam'],['Three of jan','Four of Dec'])
        self.hand_com=self.hand[0]
        self.hand_playr=self.hand[1]
        self.value=0
        self.value1=0
        
    def add(self):
        
        val_comp=(' '.join(val.split()[0] for val in self.hand_com))
        val_player=(' '.join(val.split()[0] for val in self.hand_playr))
        val_comp=val_comp.split()
        val_player=val_player.split()
        print(val_comp)
        print(val_player)
        
        for val in val_comp:
            self.value += values[val]
        for val in val_player:
            self.value1 += values[val]  
           
        print(self.value)
        print(self.value1)

x=Add()
x.add()







# =============================================================================
# class A:
#     def __init__(self):
#         self.x=('qazwsx','kolpm')
#         
#     def x(self):
#         self.y=self.x
#         return self.y
# 
#     def __str__(self):
#         return self.y
# 
# x=A()
# x.x()
# print(x)
# =============================================================================











