;; Author: G4BB3R

(defn fat [n]
    (if (<= n 1)
        1
        (* n (fat (- n 1)))))

(defn fatorial [n]
  (fat (bigint n)))


;; (print (/ (fat 40) (Math/pow (fat 20) 2) )) overflow man
(println (str(bigint (/ (fatorial (bigint 40)) (Math/pow (fat (bigint 20)) 2) ))))

;; print(fat(40) / fat(20) ^ 2)
