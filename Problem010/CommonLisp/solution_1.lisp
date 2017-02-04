;; Common Lisp Script
;; Manoel Vilela

(defun primep (n)
  (loop for d from 2 to (floor (1+ (sqrt n)))
        never (and (= (mod n d) 0)
                   (not (= n d)))))


(defun solution (limit)
  (+ 2 (loop for x from 3 by 2
             for prime? = (primep x)
             count prime? into primes
             while (< x limit)
             when prime? sum x)))


(format t "~a~%" (solution 2000000))
