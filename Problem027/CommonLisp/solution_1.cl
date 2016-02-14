;; Common Lisp version


(setf limit 1000)

(defun forall(L P)
   (if (null L) 
       T 
       (and (FUNCALL P (cAR L)) (forall (CDR L) P) )
   )
)

(defun nums(start stop)
    (setf L nil)
    (loop ( when(> start stop) (return (reverse L)) )
         (setf L (cons start L) )
         (incf start)
    ) 
)


(defun prime(N)
   (forall (nums 2 (floor (sqrt N)) )  
       #'(lambda (d) (not (= (MOD N d) 0)))
   )
)

(defun evalfunc (a b) 
    (setf n 0)
    (loop (when (prime (+ (* n n) (* a n) b))) (setf n (+ n 1)))
    (n)
)

(defun main () 
    (setf primes 0)
    (setf a 0)
    (setf b 0)
    (loop for i from -limit to limit)
        (loop for i from -limit to limit))
            (setf n (evalfunc (i j)))
            (if (> primes n)
                (setf primes n)
                (setf a i)
                (setf b j)
            )
            (setf j (+ j 1))
        )
        (setf i (+ i 1))
    )

    (primes a b)
)

(main)