#lang racket

(define (mult3-5 x)
  (or (= (remainder x 3) 0)
      (= (remainder x 5) 0)))

(define (main)
  (let ((answer (apply + (filter mult3-5 (range 0 1000)))))
    (display (format "~a~%" answer))))

(main)
