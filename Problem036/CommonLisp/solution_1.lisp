;; Common Lisp Script
;; Manoel Vilela

(defun palindromep (s)
  (equal s
         (reverse s)))

(defun bin (n)
  (format nil "~b" n))

(defun solution (n)
  (loop for x from 0 below n
        when (and (palindromep (write-to-string x))
                  (palindromep (bin x)))
          sum x))

(format t "~a~%" (solution 1000000))
