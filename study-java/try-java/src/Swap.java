public class Swap {
    public static void main(String[] args) {
        int a;
        int b;
        int temp;
        a = 10;
        b = 20;
        System.out.println("a is " + a);
        System.out.println("b is " + b);

        temp = a;
        a = b;
        b = temp;
        System.out.println("a is " + a);
        System.out.println("b is " + b);
    }
}
