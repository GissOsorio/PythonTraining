def my_function(texts):
  naughty = 0
  nice = 0
  for text in texts:
    letrainicial = text[0]
    if letrainicial == 'b' or letrainicial == 'f' or letrainicial == 'k':
      naughty += 1
    elif letrainicial == 'g' or letrainicial == 's' or letrainicial == 'n':
      nice += 1
  return 'naughty' if naughty>nice else 'nice' if nice>naughty else 'naughty'