package practice;
public class AndShortCircuitApp {

	public static void main(String[] args) {

		System.out.println("===== Short-Circuit Operation =====");
		System.out.println("----- & -----");
		// & 연산자
		// - 모든 비교 요소 연산
		int i1 = 1;
		int i2 = 2;
		int i3 = 3;
		if (i1 < 10 & i2 < 10 & i3 < 10) {
			System.out.println("T");
		} else {
			System.out.print("F");
		}

		System.out.println("\n----- && -----");
		// && 연산자
		// - 첫번째 비교가 만족하면 이후 비교는 진행하지 않음
		int i4 = 1;
		int i5 = 2;
		int i6 = 3;
		if (i4 < 10 && i5 < 10 && i6 < 10) {
			System.out.println("T");
		} else {
			System.out.print("F");
		}

	}

}
