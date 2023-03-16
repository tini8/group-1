def backwards(text):
  
  text = text.split()
  backwards_text = []
  for i in text:
    backwards_text.append(i[::-1])
  print(''.join(backwards_text))
  
backwards("world")

