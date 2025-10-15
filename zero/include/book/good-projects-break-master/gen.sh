#!/usr/bin/env bash

for f in *.png; do
    date=$(grep -Po '\d+' <<< "$f" | sed -r 's@(....)(..)(..)@\1-\2-\3@g')
    echo "$date"
    echo -e '![['$f']]\n\n'
done
