# Description
The purpose of this problem is to [find the longest word in a provided sequence](https://techdevguide.withgoogle.com/resources/former-interview-question-find-longest-word/#!). There are plenty of ways to do this problem such as brute force, character eliminiation, various greedy algorithms etc, but I settled on a suitable solution for the given problem context using regexes that searches like:
```python
import re
search_string = 'abppplee'
re.search('a[a-z]*l[a-z]*e[a-z]*', search_string)
```
where I've very specifically enforced the structure of the worth through the regex. For me this seemed a lot more natural than the proposed alternatives for the particular alphabet size we're working on. If we need to shift to a bigger alphabet in production, then I would agree that we take the appropriate tool for the job. Forcing a more generalized algorithm in this specific instance is the equivalent of driving a tank to the grocery store for milk as I've heard it. It's a reasonable solution, but know we could do better for production.
