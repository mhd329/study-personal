public class Hash {
    public class Slot {
        String value;

        Slot(String value) {
            this.value = value;
        }
    }
    public Slot[] hashTable;

    public Hash(Integer size) {
        this.hashTable = new Slot[size];
    }

    // SDBM 해시 함수
    public int hashFunction(String key) {
        int hash = 0;
        for (int i = 0; i < key.length(); i++) {
            hash = key.charAt(i) + (hash << 6) + (hash << 16) - hash;
        }
        return hash;
    }

    public boolean saveData(String key, String value) {
        Integer hashAddress = this.hashFunction(key);
        if (hashTable[hashAddress] != null) {

            return false;
        }
        else {
            this.hashTable[hashAddress].value = value;
            return true;
        }
    }

    public String getData(String key) {
        Integer hashAddress = this.hashFunction(key);
        if (hashTable[hashAddress] != null) {
            return this.hashTable[hashAddress].value;
        }
        else {
            System.out.println("테이블에 없는 키");
            return "";
        }
    }
}
