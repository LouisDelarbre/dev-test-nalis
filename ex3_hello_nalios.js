function hellonalios() {
    // all the code from the carachters
    const charachterArray = [72, 101, 108, 108, 111, 44, 32, 78, 97, 108, 105, 111, 115, 32, 33];
    return String.fromCharCode(...charachterArray);
  }

console.log(hellonalios())