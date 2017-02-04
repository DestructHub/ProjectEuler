;; Common Lisp Script
;; Manoel Vilela

(defun sum-digits (number &optional (base 10))
  (loop for n = number then q
        for (q r) = (multiple-value-list (truncate n base))
        sum r until (zerop q)))

(defun solution ()
  (loop for a from 1 to 100
        maximize (loop for b from 1 to 100
                       maximize (sum-digits (expt a b)))))

(format t "~a~%" (solution))
