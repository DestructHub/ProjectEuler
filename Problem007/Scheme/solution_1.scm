(require srfi/9) ;; Records

;; begin record :listcount

(define-record-type :listcount
  (listcount lst cnt)
  listcount?
  (lst lst set-lst!)
  (cnt cnt set-cnt!))

(define listcount-car
  (lambda (lc)
    (car (lst lc))))

(define listcount-cdr
  (lambda (lc)
    (let ((new-lc-lst (cdr (lst lc)))
          (new-lc-cnt (- (cnt lc) 1)))
      (listcount new-lc-lst new-lc-cnt))))       

(define listcount-null?
  (lambda (lc)
    (= (cnt lc) 0)))

(define listcount-init
  (listcount '() 0))

(define append-into-listcount
  (lambda (n lc)
    (let ((new-lc-lst (append (lst lc) (list n)))
          (new-lc-cnt (+ 1 (cnt lc))))
      (listcount new-lc-lst new-lc-cnt))))

;; end record :listcount

(define square
  (lambda (n) (* n n)))

(define listcount-has-useful-divisor?
  (lambda (n lc)
    (cond
     ((listcount-null? lc) #f)
     ((< n (square (listcount-car lc))) #f)
     ((= (remainder n (listcount-car lc)) 0) #t)
     (else (listcount-has-useful-divisor? n (listcount-cdr lc))))))

;; begin record :sieve

(define-record-type :sieve
  (sieve last-unchecked primes)
  sieve?
  (last-unchecked last-unchecked set-last-unchecked!)
  (primes primes set-primes!)) ;; primes is a listcount

(define sieve-init
  (sieve 5
   (listcount '(2 3) 2)))

;; end record :sieve

(define next-sieve
  (lambda (S)
    (let* ((n (last-unchecked S))
           (old-primes (primes S))
           (test-lc (listcount-cdr old-primes)))
      (if (listcount-has-useful-divisor? n test-lc)
          (sieve (+ n 2) old-primes)
          (sieve (+ n 2) (append-into-listcount n old-primes))))))

(define next-sieve-prime
  (lambda (S)
    (let ((next-S (next-sieve S)))
      (cond
       ((= (cnt (primes S)) (cnt (primes next-S)))
        (next-sieve-prime next-S))
       (else next-S)))))

(define collect-primes-acc
  (lambda (S-acc limit)
    (cond
     ((not (> limit (cnt (primes S-acc)))) S-acc)
     (else (collect-primes-acc (next-sieve-prime S-acc) limit)))))

(define collect-primes
  (lambda (n)
    (collect-primes-acc sieve-init n)))

(define solve
  (let ((input 10001))
    (- (last-unchecked (collect-primes input)) 2)))

(display solve)
(newline)
