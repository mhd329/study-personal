package classtest.pay;

public class Pay2App {

	public static void main(String[] args) {
		int hP = 9860;
		Pay2 p = new Pay2(hP);

		System.out.println("일급");
		int dPay = p.getDPay();
		System.out.println(dPay);
		System.out.println("주급");
		int wPay = p.getWPay();
		System.out.println(wPay);
		System.out.println("연봉");
		int yPay = p.getYPay();
		System.out.println(yPay);
		
	}

}
