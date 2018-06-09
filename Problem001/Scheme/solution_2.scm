(define triangular
  (lambda (n)
    (/ (* (+ n 1) n) 2)))

(define sum-multiples-less-than
  (lambda (n k)
    (* k (triangular (floor (/ (- n 1) k))))))

(define sum-multiples-of-3-or-5-less-than
  (lambda (n)
    (- (+ (sum-multiples-less-than n 3)
          (sum-multiples-less-than n 5))
       (sum-multiples-less-than n 15))))

(define solve
  (let ((input 1000))
    (sum-multiples-of-3-or-5-less-than input)))

(display solve)
(newline)
