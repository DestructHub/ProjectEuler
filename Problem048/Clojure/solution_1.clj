;; Clojure version of problem048
;; Manoel Vilela

(defn exp [x n]
   (reduce *' (repeat n x)))

(defn series [x]
   (reduce +' (map (fn [x]  (exp x x)) (range 1 (+ x 1)) )))

(defn answer []
  (let [x (series 1000)]
    (mod x (exp 10 10))))

(println (str (answer)))
