;; My first code in Clojure
;; Manoel Vilela

;; solution of problem001
(defn solution [x]
    (reduce + (filter (fn [n] (or (= (mod n 5) 0) (= (mod n 3) 0))) (range 1 x)))
)

(println (solution 1000))
