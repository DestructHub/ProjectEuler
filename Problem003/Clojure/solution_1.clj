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

(defn solution
  [n]
  (loop [remaining n prime 1 factors '()]
    (def p (last (take prime (prime-seq))))
    (def x (/ remaining p))
    (cond
      (= 1 x) (cons p factors)
      (ratio? x) (recur remaining (+' prime 1) factors)
      :else (recur x 1 (cons p factors)))))

(str (first (solution 600851475143)))
