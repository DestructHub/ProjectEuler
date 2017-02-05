;; Common Lisp Script
;; Manoel Vilela


;; next lexicographical permutation of a vector
;; borrowed from http://rosettacode.org/wiki/Permutations#Common_Lisp
;; (next-perm #(9 8 7 6 5 4 3 2 1)) => #(9 8 7 6 5 4 3 1 2)
(defun next-perm (vec &optional (cmp '>))  ; modify vector
  (declare (type (simple-array * (*)) vec))
  (macrolet ((el (i) `(aref vec ,i))
             (cmp (i j) `(funcall cmp (el ,i) (el ,j))))
    (loop with len = (1- (length vec))
          for i from (1- len) downto 0
          when (cmp i (1+ i)) do
            (loop for k from len downto i
                  when (cmp i k) do
                    (rotatef (el i) (el k))
                    (setf k (1+ len))
                    (loop while (< (incf i) (decf k)) do
                      (rotatef (el i) (el k)))
                    (return-from next-perm vec)))))

;; check if n is prime
(defun primep (n)
  (loop for d from 2 to (1+ (isqrt n))
        never (and (= (mod n d) 0)
                   (/= n d))))

;; vector of digits => integer
;; (vec->int #(9 8 7 6 5 4 3 2 1)) => 987654321
(defun vec->int (vec)
  (loop for d across vec
        for pos from (1- (length vec)) downto -1
        sum (* (expt 10 pos)
               d)))

;; loop from the biggest to small pandigital,
;; get the first pandigital prime
(defun solution (vec)
  (loop for pandigital = (vec->int vec)
        when (primep pandigital)
          return pandigital
        when (null (next-perm vec))
          return (if (< (length vec) 2) ;; if is only #(1), calling solution again will make a infinity loop
                     nil
                     (solution (subseq (reverse vec) 1)))))


(format t "~a~%" (solution #(9 8 7 6 5 4 3 2 1)))
