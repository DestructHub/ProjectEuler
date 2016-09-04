(defn prime? [n]
  (= 1 (->> (range 1 (inc (Math/sqrt n)))
            (map (partial rem n))
            (filter (partial = 0))
            (count))))

(defn next-prime
  [n]
  (loop [candidate n]
    (if (prime? candidate)
      candidate
      (recur (+ candidate 1)))))

(defn prime-seq
  ([] (prime-seq 2))
  ([n] (cons n (lazy-seq (prime-seq (next-prime (+' 1 n )))))))

(str (last (take 10001 (prime-seq))))


