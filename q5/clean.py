#!/usr/bin/env python
import sys
for line in sys.stdin:
	values=line.strip('\t').strip('\n').split(',')
	for item in values:
		item=item.strip('\t').strip('\n')
	print ','.join(values)