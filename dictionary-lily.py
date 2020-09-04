# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}


libarry_dict = { 'shelf1': {'category': 'science', 'layer1': 'bilogy', 'layer2': 'energy'},
                  'shelf2': {'category': 'computer', 'layer1': 'python', 'layer2': 'hardware'}}
print(libarry_dict['shelf1']['category'])