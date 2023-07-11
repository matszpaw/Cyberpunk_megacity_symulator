class thing_in_itself:

    def __init__(self,list_of_features:list):
        self.list_of_features = list_of_features

    def add_feature(self,name_of_feature:str):
        self.list_of_features.append(name_of_feature)
        print('new feature added, beware of consequences...')
    
    def activate_features(self):
        if len(self.list_of_features) != 0:
            for x in range(len(self.list_of_features)):
                print(f'feature {self.list_of_features[x]} has been activated')
        else:
            print('no features to activate')

#every subclass has its own set of features in form of function
#they are activated by passing their names into that function
#add logic in which parameters of simillar/neighbur objects change
#on activation

#list_of_stuff = []
#for x in range(2):
#    list_of_stuff.append(thing_in_itself([]))
#list_of_stuff[1].add_feature('strong')
#print(list_of_stuff[1])
#thing1 = thing_in_itself([])
#thing1.add_feature('strong')
#print(thing1.list_of_features)
#thing1.activate_features()