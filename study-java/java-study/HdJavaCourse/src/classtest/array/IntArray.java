package classtest.array;

public class IntArray {

	public static void main(String[] args) {
		int[] arr;
		arr = new int[2];

		arr[0] = 1;
		arr[1] = 2;
		
		System.out.println(arr[0]);
		System.out.println(arr[1]);
		
		int arrLen = arr.length;
		System.out.printf("길이 : %d\n", arrLen);
		
		for (int i = 0; i < arrLen; i ++) {
			System.out.printf("i : %d | 원소 : %d\n", i, arr[i]);
		}
		
	}

}
