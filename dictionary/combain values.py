from collections import Counter
list_dic = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
c = Counter()
for d in list_dic:
    c[d['item']] =c[d['item']] + d['amount']
print(c)