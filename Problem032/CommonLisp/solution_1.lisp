;; Common Lisp Script
;; Manoel Vilela


(defun cat (&rest strings)
  (apply #'concatenate (cons 'string strings)))

(defun string-to-list (string)
  (loop for c across string collect (parse-integer (string c))))


(defun nums-to-string (&rest x)
  (apply #'cat (mapcar #'write-to-string x)))


(defun ordered-digits (&rest x)
  (apply #'nums-to-string (sort (string-to-list (apply #'nums-to-string x)) #'<)))


(defun solution ()
  (loop with pandigitals-table = (make-hash-table)
        with pandigitals = 0
        for x from 1 to 9999
        do (loop for y from 1 to 99
                 for xy = (* x y)
                 unless (nth-value 1 (gethash xy pandigitals-table))
                   when (equalp "123456789" (ordered-digits x y xy))
                     do (progn (setf pandigitals (+ xy pandigitals))
                               (setf (gethash xy pandigitals-table) t)))
        finally (return pandigitals)))

(prin1 (solution))
