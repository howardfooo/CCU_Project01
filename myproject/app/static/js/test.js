console.log("123456")
function varTest() {
    var x = 1;
    if (true) {
      x = 2; // 同一作用域內重複聲明
      console.log(x); // 2
    }
    console.log(x); // 2
  }
varTest();