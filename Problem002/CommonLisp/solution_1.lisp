;; Common Lisp Script
;; Manoel Vilela

(defun fib (n)
  (labels ((tail-fib (n a b)
             (if (= n 0)
                 a
                 (tail-fib (1- n)
                           b
                           (+ a b)))))
    (tail-fib n 0 1)))

(defun solution ()
  (format t "~a~%" (loop for x from 0
                          for fib-x = (fib x)
                          while (< fib-x 4000000)
                          when (evenp fib-x) sum fib-x)))

(solution)
