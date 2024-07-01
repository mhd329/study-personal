package ch04.sec02;
import java.util.LinkedHashMap;

public class IfElseIfElseExample {

	public static boolean printGrade(int score) {
		LinkedHashMap<Integer, String> hashMap = new LinkedHashMap<>();
		hashMap.put(90, "A");
		hashMap.put(80, "B");
		hashMap.put(70, "C");
		
		for (int key: hashMap.keySet()) {
			if (score >= key) {
				System.out.println("점수가 " + key + "이상 " + (key + 10) + "미만 입니다.");
				System.out.println("등급은 " + hashMap.get(key) + "입니다.");
				return true;
			}
		}
		System.out.println("점수가 70 미만입니다.");
		System.out.println("등급은 D입니다.");
		return false;
	}
	
	public static void main(String[] args) {
		
		int score = 90;
		printGrade(score);

	}

}
