package classtest.movie3;

public class MovieApp {

	public static void main(String[] args) {
		System.out.println("m1");
		Movie m1 = new Movie();
		m1.setTitle("탑건:매버릭");
		m1.setCategory("액션");
		m1.setDirector("조셉 코신스키");
		m1.setRunningTime(110);
		m1.printInfo();
		
		System.out.println("m2");
		Movie m2 = new Movie("아바타 물의길", "SF");
		m2.setDirector("제임스 카메론");
		m2.setRunningTime(192);
		m2.printInfo();
		
		System.out.println("m3");
		Movie m3 = new Movie("인사이드아웃", "애니메이션", "켈시 맨", 96);
		m3.printInfo();
		
	}

}
