package classtest.shirt;

public class ShirtClass {

	public static void main(String[] args) {
		System.out.println("s1");
		Shirt s1 = new Shirt();
		s1.setName("코튼/린넨 버튼 다운 셔츠");
		s1.setColor("White");
		s1.setCompany("Wow");
		s1.setSize('L');
		s1.setPrice(35000);
		s1.printInfo();
		
		System.out.println("s2");
		Shirt s2 = new Shirt("린넨 밴드칼라 하프 플라캣 셔츠", "black", 25000);
		s2.setCompany("Wow");
		s2.setSize('L');
		s2.printInfo();
		
		System.out.println("s3");
		Shirt s3 = new Shirt("코튼/린넨 버튼 다운 셔츠", "blue", "Wow", 'M', 30000);
		s3.printInfo();

	}

}
