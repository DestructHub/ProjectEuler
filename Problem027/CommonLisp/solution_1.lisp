q;; Common Lisp version
;; Manoel Vilela

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

(defun solution ()
    (setf limit 1000)
    (setf -limit -1000)
    (setf primes 0)
    (setf a 0)
    (setf b 0)
    (loop for i from -limit to limit
        do (loop for j from -limit to limit
                do (setf n (evalfunc i j))

                    ; (when (> primes n)
                    ;     (setf primes n)
                    ;     (setf a i)
                    ;     (setf b j)
                    ; )
                ;)
            ;)
        )
    )
    (* a b)
)

(format t "~d" (eval (solution)))
