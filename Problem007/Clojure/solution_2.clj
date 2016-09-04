(defn prime? [n]
  (= 2 (reduce +
               (for [i (range 1 (inc n))]
                 (if (= 0 (rem n i)) 1 0)))))

(defn next-prime
  [n]
  (loop [candidate n]
    (if (is-prime candidate)
      candidate
      (recur (+ candidate 1)))))

(defn prime-seq
  ([] (prime-seq 2))
  ([n] (cons n (lazy-seq (prime-seq (next-prime (+' 1 n )))))))

(str (last (take 10001 (prime-seq))))
