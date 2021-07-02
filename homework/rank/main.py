import csv

# if reverse=True, higher score get better rank
def get_rank(filename, name, item, reverse):
  datas = []
  with open(filename, 'r') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
      datas.append(row)

  datas.sort(key=lambda data: float(data[item]))
  if reverse:
    datas.reverse()
  for idx, data in enumerate(datas):
    if data['username'] == name:
      print(f'score: {data[item]}, ({idx+1} / {len(datas)-1})')
      return

if __name__ == '__main__':
  queries = [
    {
      'filename': 'hw5_grade.csv',
      'name': 'chuuuuu',
      'item': 'public',
      'reverse': True,
    },
    {
      'filename': 'hw5_grade.csv',
      'name': 'chuuuuu',
      'item': 'private',
      'reverse': True,
    },
    {
      'filename': 'hw6_grade.csv',
      'name': 'chuuuuu',
      'item': 'FID',
      'reverse': True,
    },
    {
      'filename': 'hw6_grade.csv',
      'name': 'chuuuuu',
      'item': 'AFD',
      'reverse': False,
    },
    {
      'filename': 'hw10_grade.csv',
      'name': 'chuuuuu',
      'item': 'public',
      'reverse': False,
    },
    {
      'filename': 'hw10_grade.csv',
      'name': 'chuuuuu',
      'item': 'private',
      'reverse': False,
    },
    {
      'filename': 'hw12_grade.csv',
      'name': 'chuuuuu',
      'item': 'reward',
      'reverse': True,
    },
  ]

  for query in queries:
    print(f'{query}')
    filename = query['filename']
    name = query['name']
    item = query['item']
    reverse = query['reverse']
    get_rank(filename, name, item, reverse)