;; Common Lisp version
;; Manoel Vilela


(defun div (x d)
  (= (mod x d) 0))

(defun special-sum (n)
  (reduce '+ (loop for x from 1 to n when (or (div x 5) (div x 3)) collect x)))

(format t "~d" (special-sum 1000))
