;; Common Lisp Script
;; Manoel Vilela

(format t "~a~%" (reduce #'lcm (loop for x from 1 to 20 collect x)))
