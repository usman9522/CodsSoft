x = 'AI is important for its potential to change how we live, work and play. It has been effectively used in business to automate tasks done by humans, including customer service work, lead generation, fraud detection and quality control. In a number of areas, AI can perform tasks much better than humans. Particularly when it comes to repetitive, detail-oriented tasks, such as analyzing large numbers of legal documents to ensure relevant fields are filled in properly, AI tools often complete jobs quickly and with relatively few errors. Because of the massive data sets it can process, AI can also give enterprises insights into their operations they might not have been aware of. The rapidly expanding population of generative AI tools will be important in fields ranging from education and marketing to product design.'
total_alp = 0
total_char = 0

for i in range (65, 91):
    cap = chr(i)
    small = chr(i+32)
    count = 0
    for j in range (len(x)):

        if x[j] == cap or x[j] == small:
            count += 1
            total_alp += 1

    print(f'Word {cap} appears {count} times.')
print(f'Total Alphabets: {total_alp}')
print(f'Total Characters: {len(x)}')


