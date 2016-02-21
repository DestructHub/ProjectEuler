;;; Common Lisp version
;;; Manoel Vilela

;; ProjectEuler Problem045 solution

 
(defun quadratic (a b c)
  (/ ( + (- b) (sqrt (- (* b b) (* 4 a c)))) (* 2 a)))
 
;; x² + x => x * (x + 1)
(defun triangle (x)
  (/ (* (+ x 1) x) 2))

(defun hexagonalp (x) 
  (quadratic 2 -1 (* -1 x)))

(defun pentagonalp (x) 
  (quadratic 3 -1 (* -2 x)))
 
(defun solution ()
  (do* ((last 286 (+ 1 last))
         (tr (triangle last) (triangle last))
           (hp (hexagonalp tr) (hexagonalp tr))
             (tp (pentagonalp tr) (pentagonalp tr)))
        ((and (integerp hp)
              (integerp tp))
         tr)))

(format t "~d" (solution))