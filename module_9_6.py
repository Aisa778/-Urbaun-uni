# def all_variants(text):
#     for z in range(len(text)):
#         yield text[z]
#         z+=1
#
#     for z in range(len(text)):
#         for g in range(z, len(text)):
#             yield text[z:g+1]
#
#         z+=1

def all_variants(text):
    for z in range(len(text)):
        yield text[z]
        z+=1

    for z in range(len(text)):
        for g in range(z+1, len(text)):
            yield text[z:g+1]
            g+=1

            z+=1





a = all_variants("abc")
for i in a:
    print(i)
