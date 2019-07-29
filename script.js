// square root of  a^2 + b^2

let a = 10;
let b = 15;

console.log(Math.sqrt(a*a + b*b));




let a_limit = 90;
let b_limit = 80;
let c_limit = 70;
let d_limit = 60;

let score = 82;

// and
// or
// not


if (score > c_limit) {
  console.log("You Passed!");
  if (score > a_limit){
    console.log("with a A");

  }
  else if (score > b_limit) {
      console.log("with a B");
  }
  else if (score > c_limit){
    console.log("With a C");
  }
  else {
    console.log("You Failed");
  }

  if (score > 95) {
    console.log("You get an A+");
  }
}

// New block starts with if,
// Else and else if are optional
