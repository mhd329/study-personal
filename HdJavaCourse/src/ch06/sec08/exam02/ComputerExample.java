package ch06.sec08.exam02;

public class ComputerExample {

	public static void main(String[] args) {
		Computer c = new Computer();
		int res1 = c.sum(1, 2, 3);
		int res2 = c.sum(1, 2, 3, 4, 5);
		
		int[] v = {1, 2, 3, 4, 5};
		int res3 = c.sum(v);
		
		int res4 = c.sum(new int[] {1, 2, 3, 4, 5});

		System.out.println(res1);
		System.out.println(res2);
		System.out.println(res3);
		System.out.println(res4);
	}

}
