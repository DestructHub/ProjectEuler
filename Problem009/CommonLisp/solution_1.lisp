;; Common Lisp Script
;; Manoel Vilela

(defun pythagorean (a b c)
  (= (+ (* a a)
        (* b b))
     (* c c)))

(defun solution()
  (loop for a from 1 to 998 do
    (loop for b from a to 998 do
      (loop for c from b to 998
            when (and (= 1000 (+ a b c))
                      (pythagorean a b c))
                 do (return-from solution (* a b c))))))

(format t "~a~%" (solution))
