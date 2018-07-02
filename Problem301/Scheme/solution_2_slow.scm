;; -*- mode: scheme; coding: utf-8-unix -*-

;; Racket doesn't define SRFI-151 (Bitwise Operations) - yet
;; (require srfi/151)

(define loser?
  (lambda (n)
    (= (bitwise-xor n (* 2 n) (* 3 n)) 0)))

(define list-losers-not-greater-than
  (lambda (n)
    (define list-losers-not-greater-than-acc
      (lambda (n acc)
	(cond
	 ((= n 0) acc)
	 ((loser? n) (list-losers-not-greater-than-acc (- n 1) (append (list n) acc)))
	 (else (list-losers-not-greater-than-acc (- n 1) acc)))))
    (list-losers-not-greater-than-acc n '())))

(define count-losers-not-greater-than
  (lambda (n)
    (define count-losers-not-greater-than-acc
      (lambda (n acc)
	(cond
	 ((= n 0) acc)
	 ((loser? n) (count-losers-not-greater-than-acc (- n 1) (+ acc 1)))
	 (else (count-losers-not-greater-than-acc (- n 1) acc)))))
    (count-losers-not-greater-than-acc n 0)))

(define power
  (lambda (base exp)
    (define power-acc
      (lambda (base exp acc)
	(cond
	 ((= exp 0) acc)
	 (else (power-acc base (- exp 1) (* base acc))))))
    (power-acc base exp 1)))

(define solve
  (let ((input 30))
    (count-losers-not-greater-than (power 2 input))))

(display solve)
(newline)
