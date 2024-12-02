
def all_variants(text):
    for k in range(0, len(text)):
        i = 0
        while i != len(text) - k:
            yield text[i:i + k + 1]
            i += 1


a = all_variants("abc")
for i in a:
    print(i)





