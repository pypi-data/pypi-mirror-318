# PyCrawlBot
A simple web crawler

## Usage
install:
```shell
pip install PyCrawlBot
```
code:
```python
import PyCrawlBot

bot = PyCrawlBot.crawl('url')

bot.set_charset('utf-8')

# get text from html
text = bot.get('type(like a h1, h2, h3, p, div, span, a, img, ...)')
```