export function isEmpty(obj) {
  for (const prop in obj) {
    if (obj.hasOwnProperty(prop)) return false;
  }

  return true;
}

export function capitalize(string) {
  if (typeof string === 'object') {
    return string.map(str => `${str.charAt(0).toUpperCase() + str.slice(1)} `);
  }
  const stringArray = string.indexOf('-') > -1 ? string.split('-') : string.split(' ' || '');
  return stringArray.map(arr => `${arr.charAt(0).toUpperCase() + arr.slice(1)} `);
  // return string.charAt(0).toUpperCase() + string.slice(1);
}

export function sizeOfAnObject(obj) {
  let size = 0,
    key;
  for (key in obj) {
    if (obj.hasOwnProperty(key)) size++;
  }
  return size;
}

export function isNegative(number) {
  if (number && typeof number === 'number') {
    return number < 0;
  }
}

export function objectify(key, value) {
  if (key && value)
    return {
      [key]: value
    };
}
