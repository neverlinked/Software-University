article_title = input()
article_content = input()
comments = []

while True:
    comment = input()

    if comment == 'end of comments':
        break

    comments.append(comment)

print('<h1>')
print(article_title)
print('</h1>')
print('<article>')
print(article_content)
print('</article>')

for comment in comments:
    print('<div>')
    print(comment)
    print('</div>')