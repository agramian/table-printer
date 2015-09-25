# table-printer

### Description
Print a list of python dicts as an organized table.

### Installation
`pip install git+git://github.com/agramian/table-printer.git`

### Usage
```
from table_printer import TablePrinter

fmt = [
  ('Title',         'title',        50, 'left'),
  ('Description',   'description',  50, 'right'),
]
data = [{'title': 'Hello', 'description': 'World'}]
print TablePrinter(fmt, sep='|', ul='=', tl='-', bl='_')(data)
```

##### Output
```
--------------------------------------------------|--------------------------------------------------
Title                                             |                                       Description
==================================================|==================================================
Hello                                             |                                             World
__________________________________________________|__________________________________________________
```

*See table_printer/table_printer.py for additional arguments and details.*
