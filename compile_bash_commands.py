# write these strings in to bash scripts

out_name = 'welcome.sh'
in_name = 'test_01.txt'

with open(out_name, 'w') as fp:
    fp.write(r'#!/bin/sh')
    fp.write('\n')

with open(in_name, 'r') as fp:
    lines = fp.readlines()

for line in lines:
    to_write = line.strip()
    if to_write:
        with open(out_name, 'a') as fp:
            fp.write("echo \"     %s\""%to_write)
            fp.write('\n')
