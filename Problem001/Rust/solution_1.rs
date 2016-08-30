fn sum_all_multiples(limit: i32) -> i32 {
    let mut sum = 0;

    for i in 0..limit {
    	if i % 3 == 0 || i % 5 == 0 {
    	    sum += i;
    	}
    }

    return sum;
}

fn main() {
	println!("{:?}", sum_all_multiples(1000));
}