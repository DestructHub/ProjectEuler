;; Common Lisp Script
;; Manoel Vilela


(defun integer-to-list (x)
  (if (< x 10)
      (cons x nil)
      (cons (mod x 10) 
            (integer-to-list (floor (/ x 10))))))

(defun sum (the-list)
  (reduce '+ the-list))

(defun solution ()
  (sum (integer-to-list (expt 2 1000))))


(princ (solution))