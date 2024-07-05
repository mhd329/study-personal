package classtest.biz;

public class Biz {
	private int age;
	private int height;
	private int month;
	
	int getAge() {
		return this.age;
	}

	void setAge(int age) {
		if (age > 0) {			
			this.age = age;
		} else {
			System.out.println("나이는 0보다 커야합니다.");
		}
	}
	
	int getHeight() {
		return this.height;
	}
	
	void setHeight(int height) {
		if (height > 0) {			
			this.height = height;
		} else {
			System.out.println("키는 0보다 커야합니다.");
		}
	}
	
	int getMonth() {
		return this.month;
	}
	
	void setMonth(int month) {
		if (month > 0 && month < 13) {			
			this.month = month;
		} else {
			System.out.println("달의 범위는 1부터 12여야 합니다.");
		}
		
	}
	
}
