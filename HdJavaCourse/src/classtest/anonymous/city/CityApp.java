package classtest.anonymous.city;

public class CityApp {

	public static void main(String[] args) {
		System.out.println("===== Variable =====");
		System.out.println("\n----- extends Class -----");
		City seoul = new Seoul();
		seoul.printInfo();
		
		City busan = new Busan();
		busan.printInfo();
		
		System.out.println("\n----- Anonymous -----");
		
		City jeju = new City() {
			@Override
			public void printInfo() {
				System.out.println("제주");
			}
		};
		
		jeju.printInfo();
		
		City naju = new City() {
			@Override
			public void printInfo() {
				System.out.println("나주");
			}
		};
		
		naju.printInfo();
		
		System.out.println("\n===== Method =====");
		System.out.println("\n----- extends Class -----");
		Biz b = new Biz();
		b.biz(seoul);
		b.biz(jeju);
		
		System.out.println("\n----- Anonymous -----");
		b.biz(new City() {
			@Override
			public void printInfo() {
				System.out.println("전주");
			}
		});
		
	}

}
