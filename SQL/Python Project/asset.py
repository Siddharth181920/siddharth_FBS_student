class AssetD:

    def __init__(self,id,name,type,status,quantity):

        self.aid = id
        self.aname = name
        self.atype = type
        self.astatus = status
        self.aquantity = quantity
        


    def __str__(self):
        return f'{self.aid}, {self.aname}, {self.atype}, {self.astatus},{self.aquantity}'

# if(__name__ == '__main__'):
#     s1 = asset('M-1', 'Mouse', 'Accessory', 'Assigned', 7)
#     print(s1)