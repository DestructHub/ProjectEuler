<?php

    	echo array_reduce(range(1, 999), function($carry, $x){
		return $carry += (!($x % 3 && $x % 5)) * $x; //Morgan's laws
    	});


?>
