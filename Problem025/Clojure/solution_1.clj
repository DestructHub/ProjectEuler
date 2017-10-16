(defn fib-seq
  ([] (fib-seq (bigint 0) (bigint 1)))
  ([a b] (lazy-seq (cons b (fib-seq b (+ a b))))))

(defn solution
  []
  (->> (fib-seq)
       (take-while #(< (count (str %)) 1000))
       (count)
       (+ 1)))

(println (solution))
