#!/usr/bin/bash
seq -f '%.0f' 3 2 8000000 | factor | gawk '/ .* /{next} BEGIN{f=0;t=1;fifo[0]=2} {while(fifo[f]<$2){print fifo[f];fifo[t]=fifo[f]**2;f+=1;t+=1}} {print $2; fifo[t]=$2*$2;t+=1}' | head -500500 | gawk 'BEGIN{s=1}{s=(s*$1)%500500507}END{print s}'
