# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/description/

def reverse_words_in_a_string(sentence):
  sent = trim_spaces(sentence)
  reverse(sent, 0, len(sent)-1)
  reverse_each_word(sent)
  return " ".join(sent)

def trim_spaces(s):
  left = 0
  right = len(s)-1
  while s[left] <= s[right] and s[left] == " ":
    left += 1
  while s[left] <= s[right] and s[right] == " ":
    right -= 1
  output = []
  while left < right:
    if s[left] != " ":
      output.append(s[left])
    elif output[-1] != " ":
      output.append(s[left])
    else:
      left += 1
  return output

def reverse(l, left, right):
  while left < right:
    l[left], l[right] = l[right], l[left]
    left += 1
    right -= 1

def reverse_each_word(l):
  n = len(l)
  start, end = 0, 0
  while start < n:
    while end < n and l[end] != " ":
        end += 1
    reverse(l, start, end-1)
    start = end+1
    end += 1
  return l
    
  

