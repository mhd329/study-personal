public class Array {
    public static void main(String[] args) {
        int [] array1;
        array1 = new int[5];
        array1[0] = 10;
        array1[1] = 10;
        array1[2] = 10;
        array1[3] = 10;
        array1[4] = 10;
        // 파이썬처럼 아래와 같이 하면 해시코드가 나옴.
        // System.out.println(array1);

        String [] array2 = {"a", "b", "c", "d", "e"};
        for (int i = 0; i < array1.length; i ++) {
            System.out.println(array1[i]);
            System.out.println(array2[i]);
        }
    }
}
