import java.lang.Math;
class Node {
    String key;
    String value;
    Node next;

    public Node(String key, String value) {
        this.key = key;
        this.value = value;
        // next에는 다음 Node가 들어감.
        this.next = null;
    }
}

public class Hash {
    private Node[] hashTable;

    public Hash(Integer size) {
        /*
        * 부하 계수는 `0.75`.
        * 테이블 사이즈를 구하는 과정은 다음과 같다.
        * 1. 임의로 주어진 사이즈를 부하 계수로 나눈 값을 구함.
        * 2. `1`에서 구한 값에서 소수점 이하 버림.
        * 3. `2`에서 구한 값과 같거나 큰 소수를 찾는다.
        * 4. `3`의 값을 테이블 사이즈로 함.
        */
        double load = 0.75;
        // 소수점 이하 버림.
        int tableSize = (int)((size / load) + 0.5);
        int sqrt = (int)(Math.sqrt(tableSize));
        boolean flag = true;
        while (flag) {
            for (int i = 2; i <= sqrt; i++) {
                if (tableSize % i == 0) {
                    ++tableSize;
                    sqrt = (int)(Math.sqrt(tableSize));
                    break;
                }
                flag = false;
            }
        }
        this.hashTable = new Node[tableSize];
    }

    // SDBM 해시 함수
    private int hashFunction(String key) {
        // 오버플로우 일어나기 때문에 long 사용.
        long hashFactor = 0;
        for (int i = 0; i < key.length(); i++) {
            hashFactor = key.charAt(i) + (hashFactor << 6) + (hashFactor << 16) - hashFactor;
        }
        return (int)(hashFactor % this.hashTable.length);
    }

    public void setData(String key, String value) {
        int hashAddress = this.hashFunction(key);
        Node newNode = new Node(key, value);
        if (hashTable[hashAddress] == null) {
            this.hashTable[hashAddress] = newNode;
        } else {
            Node currentNode = this.hashTable[hashAddress];
            boolean flag = true;
            while (flag) {
                // 새로 들어온 key가 현재 노드의 key와 중복된다면,
                if (currentNode.key.equals(key)) {
                    // 새 값으로 덮어씌우고 탐색 종료.
                    currentNode.value = value;
                    flag = false;
                // 새로운 key일 경우,
                } else {
                    // 다음 노드가 비어있을 경우,
                    if (currentNode.next == null) {
                        // 새로운 값을 할당하고 탐색 종료.
                        currentNode.next = newNode;
                        flag = false;
                    // 다음 노드가 비어있지 않을 경우,
                    } else {
                        // 다음 노드부터 다시 탐색.
                        currentNode = currentNode.next;
                    }
                }
            }
        }
    }

    public String getData(String key) {
        int hashAddress = this.hashFunction(key);
        if (hashTable[hashAddress] == null) {
            return "일치하는 데이터가 없습니다.";
        }
        else {
            Node node = this.hashTable[hashAddress];
            if (node.next != null) {
                while (!node.key.equals(key)) {
                    node = node.next;
                }
            }
            return node.value;
        }
    }

    public static void main(String[] args) {
        Hash hashTable = new Hash(10);
        hashTable.setData("a", "안녕");
        hashTable.setData("a", "하세요");
        hashTable.setData("a", "Hello");
        hashTable.setData("ab", "안녕하세요");
        hashTable.setData("abc", "안녕하십니까");
        hashTable.setData("abcd", "안녕히가세요");

        // 키 확인
        System.out.println("a : " + hashTable.getData("a"));
        System.out.println("ab : " + hashTable.getData("ab"));
        System.out.println("abc : " + hashTable.getData("abc"));
        System.out.println("abcd : " + hashTable.getData("abcd"));
        System.out.println("abcde : " + hashTable.getData("abcde"));
    }
}
