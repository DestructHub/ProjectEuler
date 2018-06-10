;;

(define makelist
  (lambda (f min max L)
    (cond
     ((> min max) L)
     (else (makelist f (+ min 1) max (append L (list (f min))))))))

(define aggregate
  (lambda (f n L)
    (cond
     ((null? L) n)
     (else (aggregate f (f n (car L)) (cdr L))))))

(define gcd
  (lambda (m n)
    (cond
     ((= n 0) m)
     ((= n 1) 1)
     ((< m n) (gcd n m))
     (else (gcd n (remainder m n))))))

(define lcm
 (lambda (m n)
   (cond
    ((= n 1) m)
    ((= n 0) 0)
    (else (/ (* m n) (gcd m n))))))

(define solve
  (let ((input 20))
    (aggregate lcm 1 (makelist (lambda (x) x) 2 input '()))))

(display solve)
(newline)
