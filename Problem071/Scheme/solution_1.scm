;; -*- mode: scheme; coding: utf-8-unix -*-

#|
An implementation of Farey Sequence(s)

References:
- Cut the Knot article: https://www.cut-the-knot.org/blue/Farey.shtml
- Stern-Brocott Tree: https://www.cut-the-knot.org/blue/Stern.shtml
- Ivan Niven, Herbert S. Zuckerman, Hugh L. Montgomery,
              "An introduction to the theory of numbers", 5th Edition, Wiley, NY

TODO:
- Documentation
|#

(require srfi/9)

(define gcd
  (lambda (m n)
    (cond
     ((= n 0) m)
     ((= n 1) 1)
     ((< m n) (gcd n m))
     (else (gcd n (remainder m n))))))

(define-record-type :fraction
  (fraction numerator denominator)
  fraction?
  (numerator numerator set-numerator!)
  (denominator denominator set-denominator!))

(define pretty-print-fraction
  (lambda (header f)
    (display "Fraction: ")
    (display header)
    (newline)
    (display "Numerator: ")
    (display (numerator f))
    (newline)
    (display "Denominator: ")
    (display (denominator f))
    (newline)))

(define simplify
  (lambda (f)
    (let ((num (numerator f))
	  (den (denominator f))
	  (g (gcd num den)))
      (fraction (/ num g) (/ den g)))))

(define smaller?
  (lambda (f1 f2)
    (< (* (numerator f1) (denominator f2))
       (* (numerator f2) (denominator f1)))))

(define bigger?
  (lambda (f1 f2)
    (smaller? f2 f1)))

(define equals?
  (lambda (f1 f2)
    (not (or (smaller? f1 f2) (bigger? f1 f2)))))

(define zero
  (fraction 0 1))
(define one
  (fraction 1 1))

(define-record-type :interval
  (interval lower upper)
  interval?
  (lower lower set-lower!)
  (upper upper set-upper!))

(define canonical-order
  (lambda (i)
    (let ((low (lower i))
	  (upp (upper i)))
      (if (bigger? low upp)
	  (interval upp low)
	  (interval low upp)))))

(define pretty-print-interval
  (lambda (header i)
    (display "Interval: ")
    (display header)
    (newline)
    (pretty-print-fraction "Lower" (lower i))
    (pretty-print-fraction "Upper" (upper i))))

(define mediant
  (lambda (i)
    (let* ((f1 (lower i))
	   (f2 (upper i))
	   (n (+ (numerator f1) (numerator f2)))
	   (d (+ (denominator f1) (denominator f2))))
      (fraction n d))))

(define lower-mediant-split
  (lambda (i)
    (interval (lower i) (mediant i))))

(define upper-mediant-split
  (lambda (i)
    (interval (mediant i) (upper i))))

(define zero-one
  (interval zero one))

(define first-interval-mediant
  (lambda (f)
    (define first-interval-mediant-acc
      (lambda (f acc)
	(let* ((med (mediant acc))
	       (lower (lower-mediant-split acc))
	       (upper (upper-mediant-split acc)))
	  (cond
	   ((bigger? f med) (first-interval-mediant-acc f upper))
	   ((smaller? f med) (first-interval-mediant-acc f lower))
	   (else acc)))))
    (first-interval-mediant-acc f zero-one)))

(define first-interval-upper
  (lambda (f)
    (lower-mediant-split (first-interval-mediant f))))

(define first-interval-lower
  (lambda (f)
    (upper-mediant-split (first-interval-mediant f))))

(define largest-fraction-inside-with-denominator-below
  (lambda (i limit)
    (let ((med (mediant i))
	  (up (upper-mediant-split i)))
      (cond
       ((> (denominator (lower i)) limit) (lower i))
       ((> (denominator med) limit) (lower i))
       (else (largest-fraction-inside-with-denominator-below up limit))))))

(define solve
  (let ((input1 (fraction 3 7))
        (input2 1000000))
    (numerator (largest-fraction-inside-with-denominator-below
		(first-interval-upper input1) input2))))

(display solve)
(newline)
