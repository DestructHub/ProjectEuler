;; Common Lisp Script
;; Manoel Vilela

(defun square (x)
  (* x x))

;; (1 2 3) => 1² + 2² + 3² => 14
(defun square-sum (list)
  (reduce #'+ (mapcar #'square
                      list)))

;; (1 2 3) => (1 + 2 + 3)² => 6² => 36
(defun sum-square (list)
  (square (reduce #'+ list)))

(defun solution(n)
  (let ((numbers (loop for x from 1 to n collect x)))
    (- (sum-square numbers)
       (square-sum numbers))))


(format t "~a~%" (solution 100))
