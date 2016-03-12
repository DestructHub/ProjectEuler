;Author: tkovs

(defn exp [x n]
   (reduce *' (repeat n x)))

(defn sum [x]
    (apply + (map #(Integer. (str %)) (str x))))

(defn solve []
    (let [list (range 1 100)
          numbers (mapcat (fn [x] (map (fn [y] (exp x y)) list)) list)
          sumDigits (map sum numbers)]
            (apply max sumDigits) ))

(println (solve))