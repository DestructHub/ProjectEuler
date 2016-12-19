<?php

	echo array_sum(array_filter(range(1, 999), function($x){
		return !($x % 3 && $x % 5);	//Morgan's laws
	}));

?>
