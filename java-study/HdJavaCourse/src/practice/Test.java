package practice;
import java.util.LinkedHashMap;

public class Test {

	public static boolean printGrade(int score) {
		LinkedHashMap<Integer, String> hashMap = new LinkedHashMap<>();
		hashMap.put(90, "A");
		hashMap.put(80, "B");
		hashMap.put(70, "C");
		
		for (int key: hashMap.keySet()) {
			if (score >= key) {
				System.out.println("학점="+hashMap.get(key));
				return true;
			}
		}
		System.out.println("학점=D");
		return false;
	}
	
	public static void main(String[] args) {
		int k = 88;
		int e = 92;
		int m = 100;
		int sum = (k + e + m);
		int avg = sum / 3;
		System.out.println("국어="+k);
		System.out.println("영어="+e);
		System.out.println("수학="+m);
		System.out.println("총점="+sum);
		System.out.println("평균="+avg);
		printGrade(avg);

	}

}
