;; Common Lisp Script
;; Manoel Vilela


(defun integer-to-list (x)
  (if (< x 10)
      (cons x nil)
      (cons (mod x 10) 
            (integer-to-list (floor (/ x 10))))))

(defun sum (the-list)
  (reduce '+ the-list))

(defun fat (x)
  (if (<= x 2)
      x
      (* x (fat (1- x)))))

(defun solution ()
  (sum (integer-to-list (fat 100))))


(princ (solution))