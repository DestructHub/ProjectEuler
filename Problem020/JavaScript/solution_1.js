console.log(digitsum(findex('100')));
function findex(num){
  var result = num;
  for(p = 1; p < num; p++){
    toadd = '' + p;
    result = multiply(result, toadd);
  }
  return result;
}
function digitsum(target){
  var result = 0;
  for(l = 0; l < target.length; l++){
    var toadd = parseInt(target[l]);
    result += toadd;
  }
  return result;
}
function square(stringnumber, number){
  var result = 1;
  var power = parseInt(number);
  for(o = 0; o < power; o++){
    result = multiply(result, stringnumber);
  }
  return result;
}
function multiply(a, b){
  var longstring = long(a, b);
  var result = long(a, b);
  var multiplier = parseInt(short(a, b));
  for(u = 1; u < multiplier; u++){
    result = add(result, longstring);
  }
  return result;
}
function add(a, b){
  var ar = [];
  var br = [];
  var rr = [];
  arrify(a, ar);
  arrify(b, br);
  var big = long(ar, br);
  var smol = short(ar, br);
  var pointer = 0;
  var lendiff = big.length - smol.length;
  var carry = 0;

  for(i = 0; i < big.length; i++){
    if(i >= lendiff){
      rr.push(parseInt(big[i]) + parseInt(smol[i - lendiff]));
    }else{
      rr.push(big[i]);
    }
  }
  for(i = 0; i < rr.length; i++){
    rr[i] = parseInt(rr[i]);
  }
  for(g = 0; g < big.length; g++){
    for(i = 0; i < rr.length; i++){
      if(i != 0){
        if(rr[i] >= 10){
          rr[i] = rr[i] - 10;
          rr[i - 1] += 1;
        }
      }else{
        if(rr[0] >= 10){
          rr[0] = rr[0] - 10;
          rr.push(rr[rr.length - 1]);
          for(h = rr.length - 1; h > 0; h--){
            rr[h] = rr[h - 1];
          }
          rr[0] = 1;
        }
      }
    }
  }
  var result = '';
  for(i = 0; i < rr.length; i++){
    result += rr[i];
  }
  return result;
}
function arrify(string, array){
  for(i = 0; i < string.length; i++){
    var char = string.charAt(i);
    array.push(char);
  }
}
function long(x,y){if(x.length > y.length){return x;}else{return y;}}
function short(x,y){if(x.length > y.length){return y;}else{return x;}}
function max(x,y){if(x > y){return x;}else{return y;}}
function min(x,y){if(x > y){return y;}else{return x;}}
