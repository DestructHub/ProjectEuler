<?php

    $fibonacci = array( 1, 2);

    array_walk( $fibonacci, function($num) use (&$fibonacci)
    {
        if (4000000 / $num > 2.6244){ // Will never be smaller then Φ²
            array_push( $fibonacci, $num + next($fibonacci));
            prev($fibonacci);
        }
    });
    
    echo array_sum($fibonacci);
    
?>

