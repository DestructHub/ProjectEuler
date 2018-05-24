;; Common Lisp Script
;; Manoel Vilela

(defun factors (n)
  "Return a list of '(prime factor) for n
   (factors 100) => ((2 2) (5 2))
  "
  (loop for x from 2
        while (> n 1)
        when (= 0 (mod n x))
          collect (loop for c from 0
                        while (= 0 (mod n x))
                        do (setq n (/ n x))
                        finally (return (list x c)))))

(defun solution ()
  (caar (last (factors 600851475143))))

(format t "~a~%"(solution))
