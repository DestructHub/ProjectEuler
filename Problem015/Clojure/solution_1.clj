;; Author: G4BB3R


(defn fatorial [n]
	(fat (bigint n)))

(defn fat [n]
	(if (<= n 1)
		1
		(* n (fat (- n 1)))))

(print (/ (fat 40) (Math/pow (fat 20) 2) ))
(bigint (/ (fatorial (bigint 40)) (Math/pow (fat (bigint 20)) 2) ))

;; print(fat(40) / fat(20) ^ 2)

