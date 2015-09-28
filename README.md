# table-printer

### Description
Print a list of python dicts as an organized table.

The code is mostly copied from [this](http://stackoverflow.com/a/5087336) Stack Overflow comment with the following additions:
- customization of the top and bottom line characters
- customization of the alignment ('left' or 'right')
- automatic truncation of text that is longer than the column width with ellipses ('...')
- ability to receive a separate data set that will be printed as a totals row at the bottom of the table by passing optional argument

### Installation
`pip install table_printer`

### Usage
```
from table_printer import TablePrinter

fmt = [
  ('Title',         'title',        50, 'left'),
  ('Description',   'description',  50, 'right'),
]
data = [{'title': 'Hello', 'description': 'World'}]
totals = {'title': 'TOTAL', '1 title'}
print TablePrinter(fmt, sep='|', ul='=', tl='-', bl='_')(data, totals)
```

##### Output
```
--------------------------------------------------|--------------------------------------------------
Title                                             |                                       Description
==================================================|==================================================
Hello                                             |                                             World
==================================================|==================================================
TOTAL                                             |                                           1 title
__________________________________________________|__________________________________________________
```

*See table_printer/table_printer.py for additional arguments and details.*
