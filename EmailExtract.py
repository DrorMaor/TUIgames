import re
text = open('emails', 'r').read()
matches = re.findall(r'[\w\.-]+@[\w\.-]+', text)

results = open('results', 'w')
results.write('\r\n'.join(matches))
results.close()
