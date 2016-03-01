;; Common Lisp Script
;; Manoel Vilela


(defun sum-digits (x)
  (if (< x 10)
      x
      (+ (mod x 10) (sum-digits (floor (/ x 10))))))

(format t "~d ~%" (sum-digits (expt 2 1000)))