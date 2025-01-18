def remove_node_from_end(head, n):
  right = head
  left = head

  for i in range(n):
    right = right.next

  if not right: # it means if right == None
    return head.next 

  while right.next != None:
    right = right.next
    left = left.next

  left.next = left.next.next

  return head
  

  
