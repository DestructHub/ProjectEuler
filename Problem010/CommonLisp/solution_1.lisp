;; Common Lisp Script
;; Manoel Vilela

(defun primep (n)
  (let ((divisors (loop for x from 2 to (floor (1+ (sqrt n)))
                        collect x)))
    (loop for d in divisors
          never (and (= (mod n d) 0)
                     (not (= n d))))))


(defun solution (limit)
  (loop for x from 2
        for prime? = (primep x)
        count prime? into primes
        while (< x limit)
        when prime? sum x))


(format t "~a~%" (solution 2000000))
