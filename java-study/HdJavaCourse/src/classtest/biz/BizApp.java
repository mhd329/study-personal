package classtest.biz;

public class BizApp {

    public static void main(String[] args) {

        Biz biz = new Biz();

        System.out.println("===== age =====");
        biz.setAge(10);
        System.out.println(biz.getAge());

        biz.setAge(-20);
        System.out.println(biz.getAge());

        System.out.println("\n===== height =====");
        biz.setHeight(-5);
        System.out.println(biz.getHeight());

        System.out.println("\n===== month =====");
        biz.setMonth(3);
        System.out.println(biz.getMonth());

        biz.setMonth(0);
        System.out.println(biz.getMonth());

        biz.setMonth(-2);
        System.out.println(biz.getMonth());

        biz.setMonth(15);
        System.out.println(biz.getMonth());

    }

}