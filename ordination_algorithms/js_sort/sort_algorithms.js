import Chance from "chance";

const chance = new Chance();
///const chance = require("chance");

//Bogo Sort
function bogoSort(arr) {
  while (!sorted(arr)) {
    arr = shuffle(arr);
  }

  return arr;
}

function shuffle(arr) {
  let m = arr.length,
    t,
    i;

  while (m) {
    i = Math.floor(Math.random() * m--);

    t = arr[m];
    arr[m] = arr[i];
    arr[i] = t;
  }

  return arr;
}

function sorted(arr) {
  let sorted = true;

  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i + 1] < arr[i]) {
      sorted = false;
    }
  }

  return sorted;
}

//Bubble Sort
function bubbleSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}

// cocktail shaker sort
function cocktailShakerSort(arr) {
  let isSorted = true;
  while (isSorted) {
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        isSorted = true;
      }
    }

    if (!isSorted) break;

    isSorted = false;

    for (let j = arr.length - 1; j > 0; j--) {
      if (arr[j - 1] > arr[j]) {
        let temp = arr[j];
        arr[j] = arr[j - 1];
        arr[j - 1] = temp;
        isSorted = true;
      }
    }
  }

  return arr;
}

//Gnome sort
function gnomeSort(arr) {
  let i = 1; // start at 1 because we're comparing i-1 to i
  let j = 2; // start at 2 because we're comparing i-1 to i
  while (i < arr.length) {
    if (arr[i - 1] <= arr[i]) {
      i = j;
      j++;
    } else {
      [arr[i - 1], arr[i]] = [arr[i], arr[i - 1]]; // swap
      i--;
      if (i === 0) {
        i = j;
        j++;
      }
    }
  }
  return arr;
}

// heap sort
function heapSort(arr) {
  let len = arr.length;
  let end = len - 1;
  heapify(arr, len);
  while (end > 0) {
    swap_(arr, end--, 0);
    siftDown(arr, 0, end);
  }
  return arr;
}

function heapify(arr, len) {
  let mid = Math.floor((len - 2) / 2);
  while (mid >= 0) {
    siftDown(arr, mid--, len - 1);
  }
}

function siftDown(arr, start, end) {
  let root = start,
    child,
    toSwap;
  while (root * 2 + 1 <= end) {
    child = root * 2 + 1;
    toSwap = root;
    if (arr[toSwap] < arr[child]) {
      toSwap = child;
    }
    if (child + 1 <= end && arr[toSwap] < arr[child + 1]) {
      toSwap = child + 1;
    }
    if (toSwap === root) {
      return;
    } else {
      swap_(arr, root, toSwap);
      root = toSwap;
    }
  }
}

function swap_(arr, i, j) {
  [arr[i], arr[j]] = [arr[j], arr[i]];
}

//Insertion Sort
function insertionSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    let current = arr[i];

    let j = i - 1;

    while (j > -1 && current < arr[j]) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = current;
  }
  return arr;
}

//JS sort
function jsSort(arr) {
  return arr.sort((a, b) => a - b);
}

//merge sort
function mergeSort(arr) {
  const mid = arr.length / 2;

  if (arr.length < 2) {
    return arr;
  }

  const left = arr.splice(0, mid);
  return merge(mergeSort(left), mergeSort(arr));
}

function merge(left, right) {
  let arr = [];
  while (left.length && right.length) {
    if (left[0] < right[0]) {
      arr.push(left.shift());
    } else {
      arr.push(right.shift());
    }
  }

  return [...arr, ...left, ...right];
}

//Quick Sort
function quickSort(arr, left = 0, right = arr.length - 1) {
  if (left >= right) {
    return;
  }

  let pivotIndex = partition(arr, left, right);
  quickSort(arr, left, pivotIndex - 1);
  quickSort(arr, pivotIndex + 1, right);

  return arr;
}

function partition(arr, left, right) {
  let pivotValue = arr[right];
  let partitionIndex = left;

  for (let i = left; i < right; i++) {
    if (arr[i] < pivotValue) {
      swap(arr, i, partitionIndex);
      partitionIndex++;
    }
  }

  swap(arr, right, partitionIndex);
  return partitionIndex;
}

function swap(arr, firstIndex, secondIndex) {
  let temp = arr[firstIndex];
  arr[firstIndex] = arr[secondIndex];
  arr[secondIndex] = temp;
}

function quickSortCheatMode(arr) {
  if (arr.length <= 1) return arr;
  let pivot = arr[0];
  let left = arr.filter((x) => x < pivot);
  let right = arr.filter((x) => x > pivot);
  return [...quickSort(left), pivot, ...quickSort(right)];
}

function quickSort2(arr) {
  if (arr.length < 2) {
    return arr;
  }
  const pivotIndex = Math.floor(arr.length / 2);
  const pivot = arr.splice(pivotIndex, 1)[0];
  const left = [];
  const right = [];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }

  return [...quickSort(left), pivot, ...quickSort(right)];
}

//Radix Sort
function radixSort(arr) {
  let maxDigits = 0;

  for (let i = 0; i < arr.length; i++) {
    maxDigits = Math.max(maxDigits, getNumberOfDigits(arr[i]));
  }

  for (let i = 0; i < maxDigits; i++) {
    let buckets = Array.from({ length: 10 }, () => []);

    for (let j = 0; j < arr.length; j++) {
      let digit = getDigit(arr[j], i);
      buckets[digit].push(arr[j]);
    }

    arr = [].concat(...buckets);
  }

  return arr;
}

function getDigit(num, place) {
  return Math.floor(Math.abs(num) / Math.pow(10, place)) % 10;
}

function getNumberOfDigits(num) {
  return Math.floor(Math.log10(Math.abs(num))) + 1;
}

//Selection Sort
function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let min = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[min]) {
        min = j;
      }
    }
    if (min !== i) {
      [arr[i], arr[min]] = [arr[min], arr[i]];
    }
  }
  return arr;
}

// shell sort
function shellSort(arr) {
  const len = arr.length;
  let gap = Math.floor(len / 2);

  while (gap > 0) {
    for (let i = gap; i < len; i++) {
      let j = i;
      let current = arr[i];
      while (j - gap >= 0 && current < arr[j - gap]) {
        arr[j] = arr[j - gap];
        j = j - gap;
      }
      arr[j] = current;
    }
    gap = Math.floor(gap / 2);
  }
  return arr;
}

// Helper Functions

function makeShuffledRange(len) {
  const arr = [];
  for (let i = 0; i <= len; i++) {
    arr.push(i);
  }
  return arr.sort(() => Math.random() - 0.5);
}

function isSorted(arr) {
  let sorted = true;
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      sorted = false;
      break;
    }
  }
  return sorted;
}

function runIt(algo) {
  const cp = [...testData];
  const start = performance.now();
  const result = algo(cp);
  results.push({ name: algo.name, time: performance.now() - start });
  !isSorted(result) && console.log(algo.name, "sorting failed!");
  result.length !== testData.length &&
    console.log(algo.name, "length mismatch!");
}

// Main Testing

// const testData = makeShuffledRange(10000);
// const testData = makeRandomArrayOfChars(10000);
// const testData = chance.n(chance.character, 10000);
const testData = chance.n(chance.hammertime, 10000);
const results = [];

runIt(selectionSort);
runIt(bubbleSort);
runIt(quickSort);
runIt(quickSort2);
runIt(insertionSort);
runIt(mergeSort);
runIt(heapSort);
runIt(cocktailShakerSort);
runIt(shellSort);
runIt(gnomeSort);
runIt(radixSort); // only works on ints
runIt(jsSort);
// runIt(bogoSort); // careful now

console.table(results.sort((a, b) => a.time - b.time));
