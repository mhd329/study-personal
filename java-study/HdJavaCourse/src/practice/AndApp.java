package practice;
public class AndApp {

	public static void main(String[] args) {

		// ==============================
		// # & &&
		//	동일 기능
		// ==============================
		boolean b1 = true;
		boolean b2 = false;

		if (b1 & b2) {
			System.out.println("b1 & b2=T");
		} else {
			System.out.println("b1 & b2=F");
		}

		if (b1 && b2) {
			System.out.println("b1 && b2=T");
		} else {
			System.out.println("b1 && b2=F");
		}

	}

}
