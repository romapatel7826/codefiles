import re
# str = " i am a blogger at https://github.com/romapatel7826/workflows "

str = " i am a blogger at https://github.com/romapatel7826/workflowsand my blog https://www.instagram.com/coding_21_/"



url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
print(url)