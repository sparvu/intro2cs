# importing module 
import collections 
  
# initialising a deque() of arbitrary length 
linked_list = collections.deque() 
  
# filling deque() with elements 
linked_list.append('subaru') 
linked_list.append('toyota') 
linked_list.append('mercedes') 
  
print("Elements in the linked list:") 
print(linked_list) 
  
# adding element at an arbitrary position 
linked_list.insert(2, 'bmw') 
  
print("Elements in the linked list:") 
print(linked_list) 
  
# deleting the last element 
linked_list.pop() 
  
print("Elements in the linked list:") 
print(linked_list) 
  
# removing a specific element 
linked_list.remove('bmw') 
  
print("Elements in the linked list:") 
print(linked_list)
