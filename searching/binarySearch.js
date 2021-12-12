function binarySearchRecursively(array, target) {
  /* It's impossible to find index without helper function */
  return binarySearchHelper(array, target, 0, array.length - 1);
}

function binarySearchRecursivelyHelper(array, target, left, right) {
  if (left > right) return -1;
  const middle = Math.floor((left + right) / 2);
  const potentialMatch = array[middle];

  if (potentialMatch === target) {
    return middle;
  } else if (target < potentialMatch) {
    return binarySearchHelper(array, target, left, middle - 1);
  } else {
    return binarySearchHelper(array, target, middle + 1, right);
  }
}

function binarySearchIteratively(array, target) {
  let left = array[0];
  let right = array[array.length - 1];

  while (left <= right) {
    let middle = Math.floor((left + right) / 2);

    if (array[middle] == target) {
      console.log('Done', middle);
    }

    if (array[middle] < target) {
      left = middle + 1;
    } else {
      right = middle - 1;
    }
  }

  return null;
}
