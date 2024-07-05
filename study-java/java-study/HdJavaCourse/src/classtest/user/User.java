package classtest.user;

public class User {
	private String name;
	private char sex;
	private int age;
	private double height;
	private boolean marriageYn;
	
	public String getName() {
		return this.name;
	}
	
	public char getSex() {
		return this.sex;
	}
	
	public int getAge() {
		return this.age;
	}
	
	public double getHeight() {
		return this.height;
	}
	
	public boolean isMarriageYn() {
		return this.marriageYn;
	}

	public void printInfo() {
		System.out.println(this.getName());
		
		if (this.getSex() == 'M') {
			System.out.println("남");
		} else {
			System.out.println("여");
		}
		
		System.out.println(this.getAge());
		System.out.println(this.getHeight());
		
		if (this.isMarriageYn()) {
			System.out.println("기혼");
		} else {
			System.out.println("미혼");
		}
		
	}
	
	public void setName(String name) {
		this.name = name;
	}
	public void setSex(char sex) {
		switch (sex) {
			case 'w', 'f', 'W', 'F' -> {
				this.sex = sex;
			}
			case 'm', 'M' -> {
				this.sex = sex;
			}
			default -> {
				System.out.println("올바른 성별을 입력해주세요.");
			}
		}
	}
	public void setHeight(double height) {
		if (height < 0) {
			System.out.println("키는 0보다 작을 수 없습니다.");
			return;
		}
		this.height = height;
	}
	public void setAge(int age) {
		if (age < 0) {
			System.out.println("나이는 0보다 작을 수 없습니다.");
			return;
		}
		this.age = age;
	}
	public void setMarriageYn(boolean marriageYn) {
		this.marriageYn = marriageYn;
	}
	
	public User() {
		this("", 0, 'M', 0, false);
	}
	
	public User(String name, int age, char sex) {
		this(name, age, sex, 0, false);
	}
	
	public User(String name, int age, char sex, double height, boolean marriageYn) {
		this.setName(name);
		this.setAge(age);
		this.setSex(sex);
		this.setHeight(height);
		this.setMarriageYn(marriageYn);
	}
	
}
