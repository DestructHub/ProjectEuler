(defun range (n)
  (loop for x from 1 to n collect x))

(defun ilength (n)
  (length (write-to-string n)))

(defun solution()
  (loop
     for a in (range 9)
     for tries = (loop
                    for n in (range 21)
                    for x = (expt a n)
                    when (= (ilength x) n)
                      collect x)
     sum (length tries)))


(princ (solution))
