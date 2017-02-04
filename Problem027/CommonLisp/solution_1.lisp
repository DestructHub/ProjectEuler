;; Common Lisp version
;; Manoel Vilela


(defun primep (n)
  (loop for d from 2 to (1+ (isqrt N))
        never (and (= (mod n d) 0)
                   (/= n d))))


(defun funcprimes (a b)
  (do* ((n 0 (+ n 1)))
       ((if (not (primep (abs (+ (* n n) ( * a n) b))))
             (return n)))))

(defun solution ()
  (let (a b n (primes 0))
    (do ((x -1000 (1+ x))) ((= x 1000))
      (do ((y -1000 (1+ y))) ((= y 1000))
        (setf n (funcprimes x y))
        (when (> n primes)
          (setf a x
                b y
                primes n)))) (* a b)))

(format t "~d~%" (solution))
