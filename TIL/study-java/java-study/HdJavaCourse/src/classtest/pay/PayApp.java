package classtest.pay;

public class PayApp {

	public static void main(String[] args) {
		int hP = 9860;
		Pay p = new Pay();

		System.out.println("일급");
		int dPay = p.getDPay(hP);
		System.out.println(dPay);
		System.out.println("주급");
		int wPay = p.getWPay(hP);
		System.out.println(wPay);
		System.out.println("연봉");
		int yPay = p.getYPay(hP);
		System.out.println(yPay);
		
	}

}
