;; -*- mode: scheme; coding: utf-8-unix -*-

#|
A somewhat easy to demonstrate theorem:
the desired number is a Fibonacci one!
|#

(define fibonacci
  (lambda (n)
    (define fibonacci-acc
      (lambda (n acc1 acc2)
	(cond
	 ((= n 0) acc1)
	 ((= n 1) acc2)
	 (else (fibonacci-acc (- n 1) acc2 (+ acc2 acc1))))))
    (fibonacci-acc n 0 1)))

(define solve
  (let ((input 30))
    (fibonacci (+ input 2))))

(display solve)
(newline)
