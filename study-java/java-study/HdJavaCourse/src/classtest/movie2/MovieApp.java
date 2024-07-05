package classtest.movie2;

public class MovieApp {

    public static void main(String[] args) {

        Movie m1 = new Movie();

        m1.setTitle("탑건:매버릭");
        System.out.println(m1.getTitle());

        m1.setCategory("액션");
        System.out.println(m1.getCategory());

        m1.setDirector("조셉 코신스키");
        System.out.println(m1.getDirector());

        m1.setRunningTime(132);
        System.out.println(m1.getRunningTime());

        System.out.println("\n----- printInfo() -----");
        m1.printInfo();

    }

}
