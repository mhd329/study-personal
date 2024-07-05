package ch12.sec04;

public class MeasureRunTimeExample {

	public static void main(String[] args) {
		long t1 = System.nanoTime();
		int sum = 0;
		for (int i = 0; i <= 1000000; i ++) {
			sum += i;
		}
		long t2 = System.nanoTime();
		
		System.out.println(sum);
		System.out.println(t2 - t1);
	}

}
