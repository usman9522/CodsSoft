x = 'Firms exporting products from the Pakistan are often asked by foreign customers or foreign governments to supply a written export certification for products regulated by the Pakistan Food and Drug Administration (FDA and PEMRA). For food products, FDA provides written certifications for exports in the form of certificates and lists of eligible exporters for specific products and destinations.'

#Task 1

def words(x):
    count = 1
    for i in range (len(x)):
        if x[i] == ' ':
            count += 1
    print(f'Number of Words: {count}')
words(x)


#Task 2

def max_len_word(x):
    maxi = 0
    x = x.split()
    for i in range (len(x)):
        a = len(x[i])
        if maxi < a:
            maxi = a
    print(f'Max Length of word is: {maxi}')

max_len_word(x)

#Task 3

def sentence(x):
    count = 0
    for i in range (len(x)):
        if x[i] == '.':
            count += 1
    print(f'Number of Sentences: {count}')
    for i in range (len(x)):
        if x[i] != '.':
            print(x[i],end='')
        else:
            print()

sentence(x)

