(defn is-prime
  [n]
  (if (or (= n 1) (= n 4))
    false
    (loop [candidates (range 2 (+ 1 (Math/sqrt n)))]
      (cond
        (empty? candidates) true
        (= 0 (rem n (first candidates))) false
        :else (recur (next candidates))))))

(defn next-prime
  [n]
  (loop [candidate n]
    (if (is-prime candidate)
      candidate
      (recur (+ candidate 1)))))

(defn prime-seq
  ([] (prime-seq 2))
  ([n] (cons n (lazy-seq (prime-seq (next-prime (+' 1 n )))))))

(println (str (last (take 10001 (prime-seq)))))
