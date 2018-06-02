
(define square-of-sum
  (lambda (n)
    (/ (* n n (+ n 1) (+ n 1)) 4)))

(define sum-of-squares
  (lambda (n)
    (/ (* n (+ n 1) (+ (* 2 n) 1)) 6)))

(define solve
  (let ((input 100))
    (- (square-of-sum input) (sum-of-squares input))))

(display solve)
(newline)
