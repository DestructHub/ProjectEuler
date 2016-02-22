;; Problem 048
;; Common Lisp


#| The series, 1¹ + 2¹ + 3³ + ... + 10^10 = 10405071317.
   Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000^1000.
 |#


(defun series (x)
  (reduce '+ (loop for x from 1 to x collect (expt x x))))

(defun solution ()
  (let (answer)
    (setf answer (series 1000))
    (mod answer (expt 10 10))))


(format t "~d" (solution))