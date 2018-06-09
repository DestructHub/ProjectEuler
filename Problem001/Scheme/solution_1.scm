(define (range a b)
  (if (>= a b)
      '()
      (cons a (range (+ a 1) b))))

(define (filter f l)
  (cond ((null? l) '())
        ((f (car l)) (cons (car l) (filter f (cdr l))))
        (#t (filter f (cdr l)))))

(define (mult3-5 x)
  (or (= (remainder x 3) 0)
      (= (remainder x 5) 0)))

(define (sum l)
  (apply + l))

(define (main)
  (let ((answer (sum (filter mult3-5 (range 0 1000)))))
    (display answer)
    (newline)))

(main)

