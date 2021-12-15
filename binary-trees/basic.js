// const tree = {
//   nodes: [
//     { id: "10", left: "5", right: "15", value: 10 },
//     { id: "15", left: "13", right: "22", value: 15 },
//     { id: "22", left: null, right: null, value: 22 },
//     { id: "13", left: null, right: "14", value: 13 },
//     { id: "14", left: null, right: null, value: 14 },
//     { id: "5", left: "2", right: "5-2", value: 5 },
//     { id: "5-2", left: null, right: null, value: 5 },
//     { id: "2", left: "1", right: null, value: 2 },
//     { id: "1", left: null, right: null, value: 1 },
//   ],
//   root: "10",
// };

// function getNthFib(n) {
//   if (n == 1) return 0;

//   let base = 0;
//   let next = 1;

//   for (let i = 2; i < n; i++) {
//     let temp = base;

//     base = next;
//     next = temp + next;
//   }

//   return next;
// }

function getNthFib(n, memo) {
  memo = memo || {};

  if (memo[n]) return memo[n];
  if (n <= 1) return 1;

  return (memo[n] = getNthFib(n - 1, memo) + getNthFib(n - 2, memo));
}

function selectionSort(array) {
  for (let i = 0; i < array.length; i++) {
    let minIndex = i + 1;

    for (let j = i + 1; j < array.length; j++) {
      if (array[j + 1] < array[minIndex]) minIndex = j;
    }

    array[i] = array[minIndex];
    array[minIndex] = array[i];
  }

  console.log(array);
}

const arr = [14, 33, 27, 10, 35, 19, 42, 44];

selectionSort(arr);
