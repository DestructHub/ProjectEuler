(define gcd
  (lambda (m n)
    (cond
     ((= n 0) m)
     ((= n 1) 1)
     ((< m n) (gcd n m))
     (else (gcd n (remainder m n))))))

(define fraction
  (lambda (num den)
    (let ((g (gcd num den)))
      (cons (/ num g) (/ den g)))))

(define num
  (lambda (f)
    (car f)))

(define den
  (lambda (f)
    (cdr f)))

(define smaller?
  (lambda (f1 f2)
    (< (* (num f1) (den f2)) (* (num f2) (den f1)))))

(define bigger?
  (lambda (f1 f2)
    (smaller? f2 f1)))

(define equals?
  (lambda (f1 f2)
    (and (= (num f1) (num f2)) (= (den f1) (den f2)))))

(define interval
  (lambda (f1 f2)
    (if (smaller? f1 f2)
        (cons f1 f2)
        (cons f2 f1))))

(define lower
  (lambda (i)
    (car i)))

(define upper
  (lambda (i)
    (cdr i)))

(define mediant
  (lambda (i)
    (let* ((f1 (lower i))
           (f2 (upper i))
           (n (+ (num f1) (num f2)))
           (d (+ (den f1) (den f2))))
      (fraction n d))))

(define left-mediant-split
  (lambda (i)
    (let ((med (mediant i)))
      (interval (lower i) med))))

(define right-mediant-split
  (lambda (i)
    (let ((med (mediant i)))
      (interval med (upper i)))))

(define first-interval-with-mediant-acc
  (lambda (f acc)
    (let* ((med (mediant acc))
           (left (left-mediant-split acc))
           (right (right-mediant-split acc)))
      (cond
       ((equals? f med) acc)
       ((bigger? f med) (first-interval-with-mediant-acc f right))
       ((smaller? f med) (first-interval-with-mediant-acc f left))))))

(define first-interval-with-mediant
  (lambda (f)
    (let ((initial-interval (interval (fraction 0 1) (fraction 1 1))))
      (first-interval-with-mediant-acc f initial-interval))))

(define first-interval-with-upper
  (lambda (f)
    (left-mediant-split (first-interval-with-mediant f))))

(define target
  (lambda (i limit)
    (let ((med (mediant i)))
      (cond
       ((> (den (lower i)) limit) (lower i))
       ((> (den med) limit) (lower i))
       (else (target (right-mediant-split i) limit))))))

(define solve
  (let ((input1 (fraction 3 7))
        (input2 1000000))
    (num(target (first-interval-with-upper input1) input2))))

(display solve)
(newline)
