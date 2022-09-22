list_of_strings=["i'm a ", 'list of ', 'strings ', 'can you ', 'find me', 'queue me up']

for string in list_of_strings:
    print(string)


def string_input(string_1):
    for string in list_of_strings:
        print(string, string_1)
    

string_input('i was given this string')



def find_q(string_2):
    for string in list_of_strings:
        if(string.startswith('q')):
            print('q found', string)
    print(string_2)


find_q('was given this')

list_of_dict = [{'username': 'alpha', 'is_subscribed': False, 'age': 22},
{'username': 'alpha2', 'is_subscribed': False, 'age': 22},
{'username': 'alph3', 'is_subscribed': False, 'age': 23},
{'username': 'alph4', 'is_subscribed': True, 'age': 24},
{'username': 'alph5', 'is_subscribed': False, 'age': 52},
{'username': 'alph6', 'is_subscribed': True, 'age': 26},]

def dictionary_input(add_more):
    new_list = []
    for dict in add_more:
        if(dict['is_subscribed'] == True):
            new_list.append(dict)
    print(new_list)
    return new_list




dictionary_input(list_of_dict)

        


