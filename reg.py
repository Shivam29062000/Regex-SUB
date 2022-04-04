import sys
import re

with open(sys.argv[1],'r') as f:
  f_con=f.read()
  
  pattern='[$₹£]'
  print(re.findall(pattern,f_con))
  
  datematch=re.findall(r'\d{2,4}/\d{2}/\d{2,4}',f_con) 
  print(datematch)
  
  cardth=re.findall(r'[a-zA-Z]{3,}th\b',f_con)
  cardnumth=re.findall(r'[0-9]{1,}th\b',f_con)
  cardnd=re.findall(r'second|third|first|1st|2nd',f_con)
  print(cardth,cardnumth,cardnd)
  
  vow=re.findall(r'\b[AEIOUaeiou]\w{3}\b',f_con)
  print(vow)
