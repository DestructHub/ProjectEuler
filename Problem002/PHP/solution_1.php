<?php

    $fibonacci = array(1, 2);

    array_walk($fibonacci, function($x) use (&$fibonacci){
        if($x * 2.6180 <= 4000000) // lim Φ²n, n -> ∞
            array_push( $fibonacci, array_sum(array_slice($fibonacci, -2, 2)));
    });

    echo array_reduce($fibonacci, function($carry, $x) use (&$fibonacci){
        return $carry += ($x%2 == 0) * $x;
    });

?>

