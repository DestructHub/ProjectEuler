;; Common Lisp version
;; Manoel Vilela

;;; Veeery slow, take some about 2m30s to finish

(defun forall(L P)
   (if (null L)
       t
       (and (funcall P (car L)) (forall (cdr L) P))))


(defun range(start stop)
  (setf L nil)
  (loop (when (> start stop) (return (reverse L)))
    (setf L (cons start L))
    (incf start)))


(defun primep (N)
  (forall (range 2 (floor (sqrt N)) )
    #'(lambda (d) (not (= (mod N d) 0)))))


(defun funcprimes (a b)
  (do* ((n 0 (+ n 1)))
        ((if (not (primep (abs (+ (* n n) ( * a n ) b)))) 
             (return n)))))


(defun solution ()
  (let (a b primes)
    (setf primes 0)
    (do ((x -1000 (1+ x))) ((= x 1000))
      (do ((y -1000 (1+ y))) ((= y 1000))
        (setf n (funcprimes x y))
        (when (> n primes)
          (setf a x
                b y
                primes n)))) (* a b)))
  
(format t "~d" (solution))
