;; Common Lisp Script
;; Manoel Vilela

(defmacro memoize (func)
  `(let ((table (make-hash-table :size 10000))
         (old-function (symbol-function ',func)))
     (defun ,func (x &rest tail)
       (multiple-value-bind
             (value exists)
           (gethash x table)
         (if exists
             value
             (setf (gethash x table) (apply old-function (cons x tail))))))))


(defun reverse-integer (n)
  (labels ((next (n v)
             (if (zerop n)
                 v
                 (multiple-value-bind (q r)
                     (truncate n 10)
                   (next q (+ (* v 10) r))))))
    (next n 0)))

(defun palindromep (n)
  (= (reverse-integer n) n))


(defun iterative-palindromep (n &optional (depth 50))
  (unless (= depth 0)
    (let ((next (+ n (reverse-integer n))))
      (if (palindromep next)
          t
          (iterative-palindromep next (1- depth))))))

(defun lychrelp (x)
  (not (iterative-palindromep x)))


(defun solution()
  (memoize palindromep)
  (memoize iterative-palindromep)
  (memoize reverse-integer)
  (loop for x from 1 below 10000
        when (lychrelp x)
          count x ))

(princ (solution))
