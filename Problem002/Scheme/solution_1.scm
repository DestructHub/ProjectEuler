;;
;; The even Fibonacci numbers satisfy the recurrence
;;
;; A(n+2) = 4*A(n+1) + A(n) if n>0
;; A(1) = 2, A(2) = 8
;;

(define next-term
  (lambda (a1 a2)
    (+ a1 (* 4 a2))))

(define sum-terms-smaller-than
  (lambda (acc1 acc2 max sum)
    (cond
     ((> acc1 max) sum)
     (else (sum-terms-smaller-than acc2 (next-term acc1 acc2) max (+ acc1 sum))))))

(define solve
  (let ((input 4000000))
    (sum-terms-smaller-than 2 8 input 0)))

(display solve)
(newline)
