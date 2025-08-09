import re

# frase1 = "(32)98858-2438"
# print(re.findall("\(\d{2}\)\d{4,5}-\d{4}",frase1))

# frase2 = "128.006.313-92"
# print(re.findall('\d{3}\.\d{3}\.\d{3}-\d{2}', frase2))

frase3 = "www.youtube.com"
print(re.findall('\w+\.\w+\.\w*', frase3))