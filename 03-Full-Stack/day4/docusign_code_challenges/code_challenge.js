function areEqual(obj1,obj2) {
    forEach(key in obj1) {
        if (obj1[key] !== obj2[key]) {
            return false
        }
    }
    return true;
}

function areArraysEqual(arr1,arr2) {
    for (int i = 0; i++; i < arr1.length) {
        if (arr1[i] !== arr2[i]) {
            return false
        }
    }
    return true
}

//Testing is key
//How to make the reference work
obj1 = {
    name: 'Inigo Montoya',
    skills: ['fencing','revenge']
}

obj2 = {
    name: 'Inigo Montoya',
    skills: ['fencing','revenge']
}