"use strict";

function smallest_multiple() {
  let i = 1;
  for (let k = 1; k < 21; k++) {
    if (i % k > 0) {
      for (let j = 1; j < 21; j++) {
        if ((i * j) % k == 0) {
          i *= j;
          break;
        }
      }
    }
  }
  return i;
}

console.log(smallest_multiple());
