#!/usr/bin/python

import operator

class TablePrinter(object):
    "Print a list of dicts as a table"
    def __init__(self, fmt, sep='', ul=None, tl=None, bl=None):
        """
        @param fmt: list of tuple(heading, key, width)
                        heading: str, column label
                        key: dictionary key to value to print
                        width: int, column width in chars
        @param sep: string, separation between columns
        @param ul: string, character to underline column label, or None for no underlining
        @param tl: string, character to draw as top line over table, or None
        @param bl: string, character to draw as bottom line under table, or None
        """
        super(TablePrinter,self).__init__()
        fmt = map(lambda x: x + tuple(['left']) if len(x) < 4 else x, fmt)
        self.fmt   = str(sep).join('{lb}{0}:{align}{1}{rb}'.format(key, width, lb='{', rb='}', align='<' if alignment == 'left' else '>') for heading,key,width,alignment in fmt)
        self.head  = {key:heading for heading,key,width,alignment in fmt}
        self.ul    = {key:str(ul)*width for heading,key,width,alignment in fmt} if ul else None
        self.width = {key:width for heading,key,width,alignment in fmt}
        self.tl    = {key:str(tl)*width for heading,key,width,alignment in fmt} if tl else None
        self.bl    = {key:str(bl)*width for heading,key,width,alignment in fmt} if bl else None

    def row(self, data, separation_character=False):
        if separation_character:
            return self.fmt.format(**{ k:str(data.get(k,''))[:w] for k,w in self.width.iteritems() })
        else:
            return self.fmt.format(**{ k:str(data.get(k,'')) if len(str(data.get(k,''))) <= w else '%s...' %str(data.get(k,''))[:(w-3)] for k,w in self.width.iteritems() })

    def __call__(self, data_list, totals=None):
        _r = self.row
        res = [_r(data) for data in data_list]
        res.insert(0, _r(self.head))
        if self.ul:
            res.insert(1, _r(self.ul, True))
        if self.tl:
            res.insert(0, _r(self.tl, True))
        if totals:
            if self.ul:
                res.insert(len(res), _r(self.ul, True))
            res.insert(len(res), _r(totals))
        if self.bl:
            res.insert(len(res), _r(self.bl, True))
        return '\n'.join(res)
