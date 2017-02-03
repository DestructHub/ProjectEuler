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
  (let ((nums (loop for x from 100 to 999
                    appending (loop for y from 100 to 999
                                    collect (* x y)))))
    (loop for x in (sort nums #'>)
          when (palindromep x) return x)))

(format t "~a ~%"(solution))

