import copy
original_list = [1,2,3,4,5,6,7,8,9,10]

try :
    extract_list = original_list[0:5:1]
    reverse_list = copy.deepcopy(extract_list)
    reverse_list.reverse()

    print(f"\nOriginal list: {original_list}")
    print(f"\nExtracted first five element list: {extract_list}")
    print(f"\nReversed extracted elements: {reverse_list}")
except Exception as e :
    print(f"\nError: {e}")
finally : 
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") 