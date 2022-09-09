def reverse_words(s):
    list_ = s.split(' ')
    list_.reverse()
    v = ' '.join(list_)
    print(v)
reverse_words('4 3 2 1')