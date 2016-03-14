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
  (let ((pandigitals))
    (loop for x from 1 to 9999 do 
      (loop for y from 1 to 99
            for xy = (* x y)
            when (equalp "123456789" (ordered-digits x y xy))
            do (push xy pandigitals)))
   (reduce #'+ (delete-duplicates pandigitals))))
  
(princ (solution))