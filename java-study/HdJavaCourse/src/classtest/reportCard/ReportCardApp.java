package classtest.reportCard;

public class ReportCardApp {

	public static void main(String[] args) {
		System.out.println("s1");
		int k1 = 96;
		int e1 = 82;
		int m1 = 78;
		ReportCard rc1 = new ReportCard("Victoria", k1, e1, m1);
		
		int sum1 = rc1.sum();
		System.out.println(sum1);
		int average1 = rc1.average();
		System.out.println(average1);
		int hakjum1 = rc1.hakjum();
		System.out.println(hakjum1);
		
		rc1.printInfo();
		
		int k2 = 88;
		int e2 = 100;
		int m2 = 92;
		System.out.println("s2");
		ReportCard rc2 = new ReportCard("Paige");
		
		rc2.setKorean(k2);
		rc2.setEnglish(e2);
		rc2.setMath(m2);
		
		int sum2 = rc2.sum();
		System.out.println(sum2);
		int average2 = rc2.average();
		System.out.println(average2);
		int hakjum2 = rc2.hakjum();
		System.out.println(hakjum2);
		
		rc2.printInfo();

	}

}
