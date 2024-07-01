package classtest.array;

public class StringArray {

	public static void main(String[] args) {
		String[] strArr;
		strArr = new String[3];
		
		strArr[0] = new String("Hello");
		strArr[1] = new String("World");
		strArr[2] = new String("Welcome");
		
		System.out.println(strArr[0]);
		System.out.println(strArr[1]);
		System.out.println(strArr[2]);
		
		for (int i = 0; i < strArr.length; i ++) {
			System.out.printf("strArr[%s] : %s\n", i, strArr[i]);
		}

	}

}
