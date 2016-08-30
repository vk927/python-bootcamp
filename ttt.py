import re
pattern = r"(123)"
string = "123zzb"

match = re.match(pattern, string)
print(match.groups(0))
# Out: '123'

sentence = "This is a phone number 672-123-456-9910"
print(re.match(r'.*(phone).*?([\d-]+)', sentence).group(0))
# Out: ('phone', '672-123-456-9910')