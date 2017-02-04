;; Common Lisp Script
;; Manoel Vilela


(defparameter *max-perimeter* 1000)
(defparameter *perimeter-solutions* (make-array (1+ *max-perimeter*) :initial-element 0))
;; (1+ *max-perimeter*) is just to avoid decrement later to access the index by perimeter-solution

(defun pythagoreanp (a b c)
  (= (* a a)
     (+ (* b b)
        (* c c))))

(defun <=-perimeter (a b c)
  (<= (+ a b c) *max-perimeter*))

(defun solution ()
  (loop for c from 1 to *max-perimeter*
        do (loop for b from c to *max-perimeter*
                 for a = (loop for x from b
                               while (< (* x x) (+ (* b b)
                                                   (* c c)))
                               finally (return x))
                 when (and (pythagoreanp a b c)
                           (<=-perimeter a b c))
                   do (setf (aref *perimeter-solutions* (+ a b c))
                            (1+ (aref *perimeter-solutions* (+ a b c))))))
  (loop with max-perimeter = 0
        for i from 1 to *max-perimeter*
        when (> (aref *perimeter-solutions* i)
                (aref *perimeter-solutions* max-perimeter))
             do (setf max-perimeter i)
        finally (return max-perimeter)))


(format t "~a~%" (solution))
