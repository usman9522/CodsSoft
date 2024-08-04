
x = 'AI is important for its potential to change how we live, work and play. It has been effectively used in business to automate tasks done by humans, including customer service work, lead generation, fraud detection and quality control. In a number of areas, AI can perform tasks much better than humans. Particularly when it comes to repetitive, detail-oriented tasks, such as analyzing large numbers of legal documents to ensure relevant fields are filled in properly, AI tools often complete jobs quickly and with relatively few errors. Because of the massive data sets it can process, AI can also give enterprises insights into their operations they might not have been aware of. The rapidly expanding population of generative AI tools will be important in fields ranging from education and marketing to product design.'
count = 1
for i in range (len(x)):
    if x[i] == ' ':
        count += 1
print(count)
total = 0
for i in range (65, 91):
    cap = chr(i)
    small = chr(i+32)
    count = 0
    for j in range (len(x)):
        if j == 0:
            if x[j] == cap or x[j] == small:
                count += 1
        if x[j] == ' ' or x[j] == ' (':
            if x[j+1] == cap or x[j+1] == small:
                count += 1
    total += count
    if count != 0:
        print(f'Words started from {cap} are: {count}')
print(f'Total Words : {total}')

