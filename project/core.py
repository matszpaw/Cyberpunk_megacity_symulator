class thing_in_itself:

    def __init__(self,name:str,list_of_features:list,feature): #za każdym razem jak tworzę obiekt
        self.name = name
        self.list_of_features = list_of_features
        self.feature = feature #do wywoływania poszczególnych funkcji

    #methods
    def check_features(self):
        if len(list_of_features) != 0:
            print('incoming')
            #for i in list_of_features:
            #return #wywołuje główną metodę funkcji która zmienia coś w world class
        else:
            print('no features')

    def add_feature(self,name_of_feature):
        list_of_fetures.append(name_of_feature)
        print(f'the feature {name_of_feature} has been added, beware of the consequences...')


aaa='Droid Sans Mono'

    #space for storing all the features methods in form of functions