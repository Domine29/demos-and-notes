class HashTable{
    constructor(){
        this.table = new Array(64).fill(0)
        this.table = this.table.map((el) => {
            return []
        })
    }

    printArray = () =>{
        console.log(this.table)
    }

    set(key, value){
        const index = this._hash(key)
        console.log('index = ' + index)
        // this.table[index] = value
        this.table[index].push([key, value])
    }

    get(key){
        const index = this._hash(key)
        for (let data of this.table[index]){
            if (data[0] == key){
                return data[1]
            }
        }
        // return this.table[index]
    }

    _hash(key){
        let hash = 0
        for ( let i = 0; i < key.length; i++){
            hash += key.charCodeAt(i)
        }
        return hash % this.table.length
    }

}

myHashtable = new HashTable()

myHashtable.printArray()

myHashtable.set('fruit', 'apple')

myHashtable.printArray()

myHashtable.set('name', 'kia')
myHashtable.set('name', 'bob')

myHashtable.set('mane', 'lion')

myHashtable.set('manename', 'lion')



myHashtable.printArray()

// console.log(myHashtable.get('cars'))

console.log(myHashtable.get('name'))
