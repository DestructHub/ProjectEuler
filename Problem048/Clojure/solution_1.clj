;; Clojure version of problem048
;; Manoel Vilela

(defn exp [x n]
   (reduce *' (repeat n x)))


(defn series [x]
   (reduce +' (map (fn [x]  (exp x x)) (range 1 (+ x 1)) )))


(defn answer []
  (let [x (str (series 1000))
        y (count x)]
    (subs x (- y 10) y)))

(println (answer))
