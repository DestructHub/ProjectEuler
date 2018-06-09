(define divmod
  (lambda (n d)
    (let ((q (floor (/ n d)))
          (r (remainder n d)))
      (cons q r))))

(define factor
  (lambda (n)
    (factor-iter 2 n '())))

(define factor-iter
  (lambda (p n L)
    (let ((dm (divmod n p)))
      (cond
       ((= n 1) L)
       ((> p (car dm)) (factor-iter p 1 (append L (list n))))
       ((= 0 (cdr dm)) (factor-iter p (car dm) (append L (list p))))
       (else (factor-iter (next p) n L))))))

(define next
  (lambda (p)
    (cond
     ((= p 2) 3)
     ((= p 3) 5)
     ((= (remainder p 6) 1) (+ p 4))
     ((= (remainder p 6) 5) (+ p 2)))))

(define biggest-prime-factor
  (lambda (n)
    (car (reverse (factor n)))))

(define solve
  (let ((input 600851475143))
    (biggest-prime-factor input)))

(display solve)
(newline)
