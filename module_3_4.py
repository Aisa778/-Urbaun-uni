def single_root_words(*other_words, root_word='На'):
    same_words = []
    for i in other_words:
        z=root_word.lower()
        k=str(i)
        low_k=k.lower()
        if z in low_k:
            same_words.append(i)
        # else:
        #     i+=1
    print(same_words)

single_root_words('На','налим','настроение', 'наушники', 'кружка','стол')
