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