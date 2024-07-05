package classtest.inheritance.animal;

public class Animal {
	private String type;
	private String name;
	private int age;
	private char sex;
	
	public String getType() {
		return type;
	}
	public void setType(String type) {
		this.type = type;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		if (age < 0) {
			System.out.println("나이는 0보다 작을 수 없습니다.");
			this.age = 0;
			return;
		}
		this.age = age;
	}
	public char getSex() {
		return sex;
	}
	public void setSex(char sex) {
		switch (sex) {
		case 'm', 'M':
			this.sex = 'M';
			break;
		case 'f', 'F':
			this.sex = 'F';
			break;
		default:
			System.out.println("성별은 M 혹은 F 만 입력할 수 있습니다.");
			this.sex = 'X';
		}
	}

	public Animal(String type, String name, int age, char sex) {
		this.type = type;
		this.name = name;
		this.setAge(age);
		this.setSex(sex);
	}
	
	public void printInfo() {
		System.out.printf("동물=%-4s\t| 이름=%-4s\t| 나이=%-3d\t", this.type, this.name, this.age);
		if (this.getSex() == 'M') {
			System.out.printf("| 성별=%-6s\t", "남");
		} else if (this.getSex() == 'F') {
			System.out.printf("| 성별=%-6s\t", "여");
		} else {
			System.out.printf("| 성별=%-6s\t", "알 수 없음");
		}
	}
	
}
