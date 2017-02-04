;;; Common Lisp version
;;; Manoel Vilela

;; ProjectEuler Problem045 solution


(defun quadratic (a b c)
  (/ ( + (- b) (sqrt (coerce (- (* b b) (* 4 a c))
                             'long-float))) (* 2 a)))

;; x² + x => x * (x + 1)
(defun triangle (x)
  (/ (* (+ x 1) x) 2))

(defun hexagonalp (x)
  (quadratic 2 -1 (* -1 x)))

(defun pentagonalp (x)
  (quadratic 3 -1 (* -2 x)))

(defun solution ()
  (loop for last from 286
        for tr = (triangle last)
        for hp = (hexagonalp tr)
        for tp = (pentagonalp tr)
        when (and (equalp (floor hp) hp)
                  (equalp (floor tp) tp))
          return tr))

(format t "~a" (solution))
