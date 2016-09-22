(def fib
  (->> [0 1]
       (iterate (fn [[x y]] [y (+' x y)]))
       (map first)))

(defn solution []
  (->> fib
       (take-while #(< % 4000000))
       (filter even?)
       (reduce +')
       (println)))

(solution)
