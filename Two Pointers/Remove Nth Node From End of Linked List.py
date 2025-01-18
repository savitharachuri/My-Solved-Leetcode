# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

def remove_node_from_end(head, n):
  right = head
  left = head

  for i in range(n):
    right = right.next

  if not right: # it means if right == None
    return head.next 

  while right.next != None: # aligning left so that the difference between last node, i.e, right and left is n
    right = right.next 
    left = left.next

  left.next = left.next.next

  return head
  

  
