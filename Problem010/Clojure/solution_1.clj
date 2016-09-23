(defn prime? [n]
  (.isProbablePrime (BigInteger/valueOf n) 10))

(defn next-prime
  [n]
  (loop [candidate n]
    (if (prime? candidate)
      candidate
      (recur (+ candidate 1)))))

(defn prime-seq
  ([] (prime-seq 2))
  ([n] (cons n (lazy-seq (prime-seq (next-prime (+' 1 n )))))))

(->> (prime-seq)
     (take-while (partial > 2000000))
     (reduce +)
     (println))
