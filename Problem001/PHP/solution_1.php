<?php
              
$sum = 0;

foreach(range(1, 999) as $i)
{
    if ($i % 5 == 0 || $i % 3 == 0)
        $sum += $i;
}

echo $sum;

?>
