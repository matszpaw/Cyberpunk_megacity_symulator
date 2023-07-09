class thing_in_itself:

    def __init__(self,list_of_features:list):
        self.list_of_features = list_of_features
    
    def add_feature(self,name_of_feature:str):
        self.list_of_features.append(name_of_feature)
        print('new amulet has enter the world of Ulram, beware of the consequences...')
    
    def activate_features(self):
        #add activation on tick
        if len(self.list_of_features) != 0:
            print('features has been activated')
        else:
            print('no features to activate')



thing1 = thing_in_itself([])


print(thing1.list_of_features)
thing1.activate_features()
thing1.add_feature('strong')
print(thing1.list_of_features)
thing1.activate_features()