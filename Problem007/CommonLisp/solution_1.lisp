;; Common Lisp Script
;; Manoel Vilela


(defun primep (n)
  (let ((divisors (loop for x from 2 to (floor (1+ (sqrt n)))
                        collect x)))
    (loop for d in divisors
          never (and (= (mod n d) 0)
                     (not (= n d))))))

(defun solution (n)
  (loop for x from 2
        count (primep x) into primes
        while (< primes n)
        finally (return x)))

(format t "~a~%" (solution 10001))
