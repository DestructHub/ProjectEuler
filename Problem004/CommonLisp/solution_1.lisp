;; Common Lisp Script
;; Manoel Vilela

(defun reverse-digits (n)
  (labels ((next (n v)
             (if (zerop n)
                 v
                 (multiple-value-bind (q r)
                     (truncate n 10)
                   (next q (+ (* v 10) r))))))
    (next n 0)))

(defun palindromep (n)
  (= n (reverse-digits n)))

(defun solution()
  (loop for x from 100 to 999
        for m = (loop for y from 100 to 999
                      for p = (* x y)
                      when (palindromep p) maximize p)
        when (numberp m) maximize m))

(format t "~a ~%"(solution))

